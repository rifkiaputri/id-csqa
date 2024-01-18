#!/bin/bash
CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-3.5-turbo" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3