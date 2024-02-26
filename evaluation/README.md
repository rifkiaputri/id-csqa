# LLMs Evaluation

This folder contains the script to run evaluation of LLMs on our datasets.

## Environment Setup
We recommend creating a virtual environment using [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) by running this following script:
```bash
conda env create -f environment.yml
conda activate csqa
```

## Running the Evaluation
To run the evaluation, please execute this following script:
```
python eval.py \
    --model_name <huggingface or OpenAI model path> \
    --dataset_path <path to test set in json> \
    --out_name <output filename for storing the evaluation result> \
    --gold_key <gold annswer key in the json item, such as "answer_majority" or "answer_creator"> \
    --history_version <versioning in output filename> \
    --batch_size 10 \
    --prompt_type <input prompt type, can be 1, 2, or 3>
```

For example,
```bash
python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_ind" \
    --batch_size 10 \
    --prompt_type 1
```
the above script will run the evaluation of BLOOMZ (7b) model on the `LLM_Gen` test set.