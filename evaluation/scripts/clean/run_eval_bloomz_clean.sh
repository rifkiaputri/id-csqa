#!/bin/bash
CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v1_ind" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v1_sun" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v1_ind" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v1_sun" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_llm_adapt/ind/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v1_ind" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_llm_adapt/sun/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v1_sun" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v3_ind" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v3_sun" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v3_ind" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v3_sun" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_llm_gen/ind/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v3_ind" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=2 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_llm_gen/sun/filtered_test_clean.json" \
    --out_name "eval_0-shot_clean.csv" \
    --gold_key "answer_creator" \
    --history_version "240124_v3_sun" \
    --batch_size 10 \
    --prompt_type 3