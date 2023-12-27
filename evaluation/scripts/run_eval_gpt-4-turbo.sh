#!/bin/bash
python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 3 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 3 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 2 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 2 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_adapt/ind/filtered_both_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 1 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v1_adapt/sun/filtered_both_test.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 1 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 3 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 3 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 2 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 2 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human/filtered_ind.json" \
    --gold_key "answer_majority" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 1 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v2_human/filtered_sun.json" \
    --gold_key "answer_majority" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 1 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 3 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 3 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 2 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 2 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_ind.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 1 \
    --few_shot

python eval.py \
    --model_name "gpt-4-1106-preview" \
    --dataset_path "../dataset/v3_synthetic/filtered_sun.json" \
    --gold_key "answer_creator" \
    --history_version "231205_few-shot" \
    --batch_size 10 \
    --prompt_type 1 \
    --few_shot