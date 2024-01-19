#!/bin/bash
CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "Ichsan2895/Merak-7B-v4" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "Ichsan2895/Merak-7B-v4" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "Ichsan2895/Merak-7B-v4" \
    --dataset_path "../dataset/v2_human/ind/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "Ichsan2895/Merak-7B-v4" \
    --dataset_path "../dataset/v2_human/sun/filtered_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1