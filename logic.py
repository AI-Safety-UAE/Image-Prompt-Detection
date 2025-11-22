import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openai import OpenAI
from config import OPENROUTER_API_KEY, PHOENIX_PROMPT, INJECTION_TEMPLATES

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def run_detector(image, model):
    if image is None:
        return "Upload an image."

    with open(image, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PHOENIX_PROMPT},
                    {"type": "text", "text": str(INJECTION_TEMPLATES)},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}
                ],
            }
        ],
    )
    return resp.choices[0].message.content.strip()

def test_injection(prompt, model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error with {model}: {e}"
    return f"=== {model} ===\n{reply}"

def render_dashboard(df_input):
    df = df_input.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['scan_id'] = range(1, len(df) + 1)
    df['risk_score'] = np.where(df['result'] == 'UNSAFE', 100, 0)

    unsafe_rate = df['risk_score'].mean()
    top_model = df['model_used'].mode().iloc[0] if not df['model_used'].mode().empty else 'N/A'

    kpi_html = f"""
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <div style="background: linear-gradient(135deg, #42a5f5, #2196f3); color: white; padding: 20px; border-radius: 12px; text-align: center; min-width: 150px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <h3>Risk Score</h3><h2>{unsafe_rate:.0f} / 100</h2>
        </div>
        <div style="background: linear-gradient(135deg, #ff9800, #f57c00); color: white; padding: 20px; border-radius: 12px; text-align: center; min-width: 150px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <h3>UNSAFE Rate</h3><h2>{unsafe_rate:.1f}%</h2>
        </div>
    </div>
    """

    fig_line = plt.figure(figsize=(8, 4), facecolor='white')
    plt.plot(df["scan_id"], df["risk_score"], color="black", marker="o", linewidth=2, markersize=6)

    plt.title("Threat Detection Trend  ", fontsize=14, fontweight='bold', color='skyblue')
    plt.xlabel("Scan Attempt #", color='skyblue')
    plt.ylabel("Risk Score", color='skyblue')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()


    result_counts = df["result"].value_counts()
    fig_bar = plt.figure(figsize=(8, 4), facecolor='white')
    plt.bar(result_counts.index, result_counts.values, color="black", alpha=0.7, edgecolor='white', linewidth=1.5)
    plt.title("Detection Result Frequency  ", fontsize=14, fontweight='bold', color='skyblue')
    plt.xlabel("Result Type", color='skyblue')
    plt.ylabel("Count", color='skyblue')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()

    return (
        kpi_html,
        ", ".join(df['result'].unique()),
        top_model,
        "Enhance guardrails for top model",
        df,
        fig_line,
        fig_bar
    )
