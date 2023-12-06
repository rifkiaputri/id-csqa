#!/bin/bash
CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2