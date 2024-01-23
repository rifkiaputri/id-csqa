#!/bin/bash
CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo-1106" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-0613" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human_gen/ind/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human_gen/sun/filtered_test.json" \
    --out_name "eval_0-shot_raw.csv" \
    --gold_key "answer_creator" \
    --history_version "240123" \
    --batch_size 10 \
    --prompt_type 3