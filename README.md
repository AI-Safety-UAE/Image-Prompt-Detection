---

# Image Prompt Injection Analyser

A security-focused application for detecting and analysing **prompt injection attacks** in both **image-based inputs** and **text prompts**, aligned with **OWASP LLM Top 10 (LLM01)**.

This tool is designed for AI security research, red teaming, and guardrail evaluation of modern language and vision models.

---

## Live Demo (Hugging Face Space)

[https://huggingface.co/spaces/Xhaheen/Phoenikzz_Apartsearch](https://huggingface.co/spaces/Xhaheen/Phoenikzz_Apartsearch)

---

## Overview

Prompt Injection Analyser identifies attempts to:

* Override system or developer instructions
* Bypass safety or moderation rules
* Inject hidden or indirect commands
* Manipulate model behaviour using novel or obfuscated techniques

The application supports both **image-based** and **text-based** prompt injection analysis.

---

## Features

### Image-Based Prompt Injection Detection

* Upload an image containing text
* Multimodal models analyse extracted content
* Compares against known injection templates
* Independently evaluates novel or disguised attacks
* Returns a strict binary verdict:

  * `SAFE`
  * `UNSAFE`

### Text Prompt Injection Testing

* Submit text prompts directly
* Test prompts against safety/guard models
* Observe how models respond to malicious instructions
* Useful for red teaming and guardrail validation

### Analytics Dashboard

* Load scan data from a CSV file
* Calculates:

  * Risk score
  * Unsafe detection rate
  * Detection trends
* Visualizations include:

  * Line chart for threat trends
  * Bar chart for result frequency
* Generates basic mitigation recommendations

### Learning Resources

* Curated references for:

  * Prompt injection techniques
  * LLM vulnerabilities
  * AI red teaming
  * OWASP GenAI security guidance

---

## Detection Logic

The analyser evaluates extracted text by:

* Comparing against known prompt injection templates
* Detecting instruction overrides and jailbreak attempts
* Flagging hidden, indirect, or obfuscated manipulation
* Treating humour, memes, or emoji-based attacks as valid threats

The system returns **only one word** as output:

```
SAFE
```

or

```
UNSAFE
```

---

## Technology Stack

| Component     | Technology                |
| ------------- | ------------------------- |
| UI            | Gradio                    |
| Language      | Python                    |
| Models        | OpenRouter-supported LLMs |
| Visualization | Pandas, Matplotlib        |
| Deployment    | Hugging Face Spaces       |

---

## Supported Models

### Vision / Multimodal

* google/gemini-2.5-flash-lite
* google/gemini-2.0-flash-lite-001
* google/gemma-3-27b-it
* microsoft/phi-4-multimodal-instruct
* openai/chatgpt-4o-latest
* mistralai/mistral-medium-3

### Text Guard

* meta-llama/llama-guard-4-12b

---

## Local Installation

Clone the repository:

```bash
git clone https://huggingface.co/spaces/Xhaheen/Phoenikzz_Apartsearch
cd Phoenikzz_Apartsearch
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your OpenRouter API key:

```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

Run the application:

```bash
python app.py
```

---

## Analytics Data

The analytics dashboard expects a CSV file (e.g., `analytics.csv`) with columns such as:

* `timestamp`
* `result` (SAFE or UNSAFE)
* `model_used`

The data can be edited directly in the interface and re-rendered to update metrics and charts.

---

## Intended Use

This project is intended for:

* AI security research
* Prompt injection red teaming
* Guardrail evaluation
* Defensive testing of LLM-based systems

Use responsibly and in accordance with applicable security and compliance policies.

---

## License

MIT License

---


