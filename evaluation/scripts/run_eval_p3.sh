#!/bin/bash
CUDA_VISIBLE_DEVICES=5 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=5 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3