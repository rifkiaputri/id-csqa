#!/bin/bash
CUDA_VISIBLE_DEVICES=6 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=6 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1