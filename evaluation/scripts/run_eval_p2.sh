#!/bin/bash
CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2