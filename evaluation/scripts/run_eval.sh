#!/bin/bash
CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "SeaLLMs/SeaLLM-7B-Chat" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "SeaLLMs/SeaLLM-7B-Chat" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "SeaLLMs/SeaLLM-7B-Chat" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "SeaLLMs/SeaLLM-7B-Chat" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "bigscience/bloomz-7b1" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "DAMO-NLP-MT/polylm-chat-13b" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-13b-chat-hf" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v3_synthetic/ind/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1

CUDA_VISIBLE_DEVICES=0 python eval.py \
    --model_name "meta-llama/Llama-2-7b-chat-hf" \
    --dataset_path "../dataset/v3_synthetic/sun/filtered_test_clean.json" \
    --out_name "evaluation_metrics_clean_open.csv" \
    --gold_key "answer_creator" \
    --history_version "231205" \
    --batch_size 10 \
    --prompt_type 1