import csv
import os
import re
import string
import sys
from collections import Counter

script_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
from utils.api import get_openai_chat_completion

set_seed(42)


class ChatCompletionHistory:
    def __init__(self, model_name, version=None, prompt_type=None):
        self.model_name = model_name
        history_filename = f'eval_history/{model_name}_history'
        if version is not None:
            history_filename += f'_{version}'
        if prompt_type is not None:
            history_filename += f'_{prompt_type}'
        self.history_file = history_filename + '.csv'
        self.history = self.load_history()
        self.translation_table = str.maketrans('', '', string.punctuation)

    def load_history(self):
        """Load history responses from a CSV file into memory, skipping the header."""
        history = {}
        if os.path.exists(self.history_file):
            print(f'History file found for {self.model_name}.')
            with open(self.history_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header row
                history = {row[0]: row[1] for row in reader}
        else:
            print(f'History file NOT found for {self.model_name}, creating a new one.')
        return history

    def extract_answer_from_explanation(self, resp):
        """Return answer key given the response string"""
        if "Answer: " in resp:
            resp_new = resp.split("Answer: ")[1]
            resp_new = resp_new.split('\n')[0]
            return resp_new.split('. ')[0] if '. ' in resp_new else resp_new
        
        if "\n" not in resp:
            answer_key = re.findall(r"The (correct )?answer is ([A-G]).", resp)
            match = [m[1] for m in answer_key]
        else:
            match = re.findall(r"\b([A-G]\..+?)\n", resp)
            
        if len(match) == 1:
            return match[0].split('. ')[0] if '. ' in match[0] else match[0]
        
        # If answer keys occurs more than two times, it could be the answer
        ans_keys = [m.split('. ')[0] for m in match]
        count = Counter(ans_keys)
        result = [el for el, occurrence in count.items() if occurrence >= 2]
        if len(result) == 1:
            return result[0]

        return resp
    
    def get_cleaned_response(self, response):
        """Clean model output."""
        response = response.choices[0].message.content.strip()

        # Handling answer with format "Answer: A"
        first_sentence = response.split('. ')[0] if '. ' in response else response
        first_sentence = re.sub(r'(?i)answer:\s+', '', first_sentence)
        first_sentence = first_sentence.translate(self.translation_table).strip()
        
        if len(first_sentence) == 1:
            return first_sentence
        
        # Check whether the model uses long explanation to provide answer
        return self.extract_answer_from_explanation(response)

    def query_model(self, prompt):
        """Query the GPT model, using history if available."""
        if prompt in self.history:
            return self.history[prompt]

        response = get_openai_chat_completion(prompt, self.model_name)
        answer_cleaned = self.get_cleaned_response(response)

        self.history[prompt] = answer_cleaned
        self.write_history_response(prompt, answer_cleaned)
        return answer_cleaned

    def write_history_response(self, prompt, response):
        """Write a new response to the history file, with a header if the file is new."""
        file_exists = os.path.exists(self.history_file)
        
        with open(self.history_file, mode='a', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # If the file didn't exist before, write a header
            if not file_exists:
                writer.writerow(['prompt', 'response'])

            writer.writerow([prompt, response])


class HfModelHistory:
    def __init__(self, model_name, version=None, prompt_type=None):
        self.model_name = model_name
        model_filename = model_name.replace('/', '--')
        history_filename = f'eval_history/{model_filename}_history'
        if version is not None:
            history_filename += f'_{version}'
        if prompt_type is not None:
            history_filename += f'_{prompt_type}'
        self.history_file = history_filename + '.csv'
        self.history = self.load_history()
        self.model, self.tokenizer = None, None
        self.translation_table = str.maketrans('', '', string.punctuation)
        self.translation_table_with_space = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    def load_history(self):
        """Load history responses from a CSV file into memory, skipping the header."""
        history = {}
        if os.path.exists(self.history_file):
            print(f'History file found for {self.model_name}.')
            with open(self.history_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header row
                history = {row[0]: row[1] for row in reader}
        else:
            print(f'History file NOT found for {self.model_name}, creating a new one.')
        return history
    
    def load_models(self):
        """Load HF model & tokenizer"""
        trust_remote_code = "sealion" in self.model_name
        
        if "polylm" in self.model_name:
            """
            Set legacy=False due to this warning:
            You are using the default legacy behaviour of the <class 'transformers.models.llama.tokenization_llama.LlamaTokenizer'>.
            This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. 
            If you want to use the new behaviour, set `legacy=False`. 
            This should only be set if you understand what it means, and thouroughly read the reason why this was added as explained 
            in https://github.com/huggingface/transformers/pull/24565
            """
            tokenizer = AutoTokenizer.from_pretrained(
                self.model_name,
                truncation_side="left",
                trust_remote_code=trust_remote_code,
                legacy=False
            )
        else:
            tokenizer = AutoTokenizer.from_pretrained(
                self.model_name,
                truncation_side="left",
                trust_remote_code=trust_remote_code
            )
        if tokenizer.pad_token is None or tokenizer.pad_token == "<unk>":
            print('Setting pad_token...')
            tokenizer.pad_token = tokenizer.bos_token if tokenizer.bos_token is not None else tokenizer.eos_token
            print('pad_token:', tokenizer.pad_token)
        tokenizer.padding_side = "left"
        
        model = AutoModelForCausalLM.from_pretrained(
            self.model_name, 
            device_map="auto", 
            load_in_8bit=True,
            resume_download=True,
            trust_remote_code=trust_remote_code
        )
        if any(model in self.model_name.lower() for model in ["seallm", "polylm", "llama"]):
            # quick fix for tensor error
            # https://github.com/facebookresearch/llama/issues/380
            model = model.bfloat16()
        model = model.eval()
        
        return model, tokenizer
    
    def find_answer_key(self, prompt, resp_orig):
        """Return answer key given the response string."""
        resp = resp_orig.lower().strip()
        if resp[-1] == ".":
            resp = resp[:-1]
        lines = prompt.lower().split("\n") 

        for line in lines:
            line = line.strip()
            answers = line.split('. ')

            if len(answers) <= 1:
                continue

            answer_key = answers[0].strip()
            answer_text = ' '.join(answers[1:])
            answer_text_no_punct = [a for a in answer_text.translate(self.translation_table_with_space).split() if a != ""]
            resp_no_punct = [r for r in resp.translate(self.translation_table_with_space).split() if r != ""]

            if resp_no_punct == answer_text_no_punct:
                return answer_key.upper()
            elif resp_no_punct == [answer_key] + answer_text_no_punct:
                return answer_key.upper()
            elif resp in line:
                if resp == line:
                    return answer_key.upper()
                full_option = f"{answer_key}. {resp}"    
                if full_option == line:
                    return answer_key.upper()
            elif resp.replace(' - ', '. ') == line or f"{resp[0]}.{resp[1:]}" == line:
                return answer_key.upper()
            elif resp[3:] in line:
                full_option = f"{answer_key}. {resp[3:]}"    
                if full_option == line:
                    return answer_key.upper()
        
        return f"Answer key not found in the provided text: {resp_orig}"
    
    def get_cleaned_response(self, prompt, response):
        """Clean model output."""
        response = response.replace(prompt, "").strip()
        unwanted_phrases = ["The correct answer is", "### USER:", "### USER", "### RESPONSE:", "### RESPONSE", "###"]
        for phrase in unwanted_phrases:
            response = response.replace(phrase, "").strip()

        response = response.split('\n', 1)[0].strip()  # Keep only the first line
        if response == "A, B, C, D, E":
            return response
        
        if response[0] == '(' and response [2] == ')':
            return response[1]
        
        resp_no_punct = response.translate(self.translation_table).strip()
        if len(resp_no_punct) == 1:
            return resp_no_punct

        return self.find_answer_key(prompt, response)

    def query_model(self, prompts):
        """Query the HF model, using history if available."""
        responses = {}
        batch_prompts = []
        for prompt in prompts:
            if prompt in self.history:
                responses[prompt] = self.history[prompt]
            else:
                batch_prompts.append(prompt)
        
        if batch_prompts:
            if self.model is None or self.tokenizer is None:
                self.model, self.tokenizer = self.load_models()

            inputs = self.tokenizer(
                batch_prompts,
                padding=True,
                truncation=True,
                return_tensors="pt",
                max_length=1024,
            ).to('cuda')
            
            if "sealion" in self.model_name:
                inputs.pop("token_type_ids", None)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    temperature=0.1,  # using the same temperature setting as closed model
                    do_sample=True,
                    min_new_tokens=1,
                    max_new_tokens=40
                )

            # for fairer comparison, using the same setting as closed model:
            # use decoded output rather than next token output probabilities
            batch_responses = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

            for prompt, resp in zip(batch_prompts, batch_responses):
                resp = self.get_cleaned_response(prompt, resp)
                responses[prompt] = resp
                self.history[prompt] = resp
            
            self.write_history_response(batch_prompts, [responses[prompt] for prompt in batch_prompts])

        return [responses[prompt] for prompt in prompts]

    def write_history_response(self, prompts, responses):
        """Write a new response to the history file, with a header if the file is new."""
        file_exists = os.path.exists(self.history_file)
        
        with open(self.history_file, mode='a', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # If the file didn't exist before, write a header
            if not file_exists:
                writer.writerow(['prompt', 'response'])

            for prompt, response in zip(prompts, responses):
                writer.writerow([prompt, response])
