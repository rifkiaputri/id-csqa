# Synthetic Dataset Generation

This directory contains scripts to generate the synthetic ID & SU csqa dataset.

## Installation

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

Create a `.env` file based on the provided example:
- Copy `.env.example` to `.env`:
    ```bash
    cp .env.example .env
    ```
- Edit the `.env` file and set the required environment variables according to your configuration.

## Generating the Dataset

Run the generation script:
```bash
python generate.py
