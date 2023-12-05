import csv
import os
import re
import string
import sys

script_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
from utils.api import get_openai_chat_completion

set_seed(42)


class ChatCompletionHistory:
    def __init__(self, model_name, version=None):
        self.model_name = model_name
        if version is None:
            self.history_file = f'eval_history/{model_name}_history.csv'
        else:
            self.history_file = f'eval_history/{model_name}_history_{version}.csv'
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
    
    def get_cleaned_response(self, response):
        """Clean model output."""
        response = response.choices[0].message.content.strip()
        first_sentence = response.split('. ')[0] if '. ' in response else response
        first_sentence = re.sub(r'(?i)answer:\s+', '', first_sentence)
        first_sentence = first_sentence.translate(self.translation_table).strip()
        
        if len(first_sentence) == 1:
            return first_sentence
        
        return response

    def query_model(self, prompt):
        """Query the GPT model, using history if available."""
        if prompt in self.history:
            return self.history[prompt]

        response = get_openai_chat_completion(prompt, self.model_name)
        answer_cleaned = self.get_cleaned_response(response)

        # Retry logic if answer length is greater than 1
        if len(answer_cleaned) > 1:
            print('Answer len > 1, retry...')
            print('Answer before:', answer_cleaned)
            response = get_openai_chat_completion(prompt, self.model_name)
            answer_cleaned = self.get_cleaned_response(response)
            print('Answer after:', answer_cleaned)

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
    def __init__(self, model_name, version=None):
        self.model_name = model_name
        model_filename = model_name.replace('/', '--')
        if version is None:
            self.history_file = f'eval_history/{model_filename}_history.csv'
        else:
            self.history_file = f'eval_history/{model_filename}_history_{version}.csv'
        self.history = self.load_history()
        self.model, self.tokenizer = self.load_models()
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
    
    def load_models(self):
        """Load HF model & tokenizer"""
        tokenizer = AutoTokenizer.from_pretrained(self.model_name, truncation_side="left")
        if tokenizer.pad_token is None:
            print('Setting pad_token...')
            tokenizer.pad_token = tokenizer.bos_token if tokenizer.bos_token is not None else tokenizer.eos_token
            print('pad_token:', tokenizer.pad_token)
        tokenizer.padding_side = "left"
        
        model = AutoModelForCausalLM.from_pretrained(
            self.model_name, 
            device_map="auto", 
            load_in_8bit=True, 
            resume_download=True
        )
        model = model.eval()
        
        return model, tokenizer
    
    def find_answer_key(self, prompt, resp):
        """Return answer key given the response string"""
        resp = resp.strip()
        lines = prompt.split("\n")
        for line in lines:
            line = line.strip()
            if resp in line:
                answer_key = line.strip().split('.')[0].strip()
                full_option = f"{answer_key}. {resp}"
                if full_option == line:
                    return answer_key

        return f"Answer key not found in the provided text: {resp}"
    
    def get_cleaned_response(self, prompt, response):
        """Clean model output."""
        response = response.replace(prompt, '').strip()
        if '\n' in response:
            response = response.split('\n')[0].strip()

        if '. ' in response:
            first_sentence = response.split('. ')[0]
        elif ' - ' in response:
            first_sentence = response.split(' - ')[0]
        else:
            raise NotImplementedError(f"Not implemented for response: {response}")

        first_sentence_cleaned = first_sentence.translate(self.translation_table).strip()

        if len(first_sentence_cleaned) != 1:
            first_sentence_cleaned = self.find_answer_key(prompt, response)
        
        if len(first_sentence_cleaned) == 1 or first_sentence_cleaned.startswith("Answer key not found"):
            return first_sentence_cleaned
        
        return response
    
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
            inputs = self.tokenizer(
                batch_prompts, padding=True, truncation=True, return_tensors="pt", max_length=1024
            ).to('cuda')
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    temperature=0.1,  # using the same temperature setting as closed model
                    do_sample=True,
                    min_new_tokens=1,
                    max_new_tokens=10
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
