#!/bin/bash
# CUDA_VISIBLE_DEVICES=4 python eval.py \
#     --model_name "DAMO-NLP-MT/polylm-chat-13b" \
#     --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.csv" \
#     --gold_key "answerKey" \
#     --history_version "231205" \
#     --batch_size 10 \
#     --prompt_type 3

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 3

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 2

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.csv" \
    --gold_key "answerKey" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=4 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1