# Adaptation & Synthetic Dataset Generation

This directory contains scripts to generate v1 adaptation & v3 synthetic ID-SU CSQA dataset.

## Installation

You need to install some dependencies required to run the generation script. The `requirements.txt` is placed in the root directory.

1. Create an isolated virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup Google Cloud Project and OpenAI API Key

The generation process use the Google Translation API. So you need to setup the Google Cloud by following this guide [here](https://cloud.google.com/translate/docs/setup?_ga=2.228297949.-1989954949.1697698668).

You also need to prepare your OpenAI API Key to run the generation script, which you can put in the environment variables explained next.

## Setup Environment Variables

Create a `.env` file based on the provided example, containing OpenAI API key and Google Cloud Project:

- Copy `.env.example` to `.env`:
  ```bash
  cp .env.example .env
  ```
- Edit the `.env` file and set the required environment variables according to your configuration.

## Generate v1 Adaptation Dataset

Run the generation script with some arguments. The required arguments are `--output_path` and `--raw_data_path`, others are optional which you can find by running `--help`.

```bash
python generate_v1.py --output_path path/to/output_dir --raw_data_path path/to/raw_data
```

## Generate v3 Synthetic Dataset

Run the generation script with some arguments. No required arguments, only optional which you can find by running `--help`.

```bash
python generate_v3.py
```
