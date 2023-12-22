#!/bin/bash
python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1