import gradio as gr

LIGHT_BLUE_GLASS_CSS = """
/* Background Gradient */
body, .gradio-container {
    background: linear-gradient(135deg, #e0f2f7 0%, #b3e5fc 100%) !important;
    color: #000000 !important;
}
/* Headings (Title) */
h1, h2, h3 {
    color: #0d47a1 !important;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    font-family: 'Segoe UI', Arial, sans-serif;
}
/* Glass effect for main blocks */
.block {
    background: rgba(255, 255, 255, 0.7) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(0, 150, 255, 0.3) !important;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1) !important;
    border-radius: 12px !important;
}
/* Buttons - Primary gradient bg with darkest blue text (overrides white) */
button.primary-btn {
    background: linear-gradient(135deg, #42a5f5 0%, #2196f3 100%) !important;
    border: none !important;
    color: #0d47a1 !important;  /* Darkest blue (changed from #ffffff) */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    border-radius: 8px !important;
}
/* ALL buttons (primary, secondary, etc.) - Darkest blue text */
button, button.primary-btn, button.secondary-btn, .gr-button {
    color: #0d47a1 !important;
}
/* Text Inputs, Textareas, and Dropdowns (The text inside them) */
textarea, input[type="text"], .gr-form-control, .gd-select-value {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #000000 !important;
    border: 1px solid #90caf9 !important;
    border-radius: 6px !important;
}
/* Dropdown options text */
.gd-select-option {
    color: #000000 !important;
    background-color: #ffffff !important;
}
/* Labels (e.g., "Target Source", "Analysis Result") - ALL darkest blue */
label span, span {
    color: #0d47a1 !important;  /* Darkest blue (was #1976d2) */
    font-weight: 600;
}
/* Radio buttons (for model selection) - Container */
.gr-radio {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #0d47a1 !important;  /* Darkest blue */
    border: 1px solid #90caf9 !important;
    border-radius: 6px !important;
}
/* Radio labels, options, and choices specifically (fixes "Select Model Protocol" + "google/gemini-2.5-flash-lite") */
.gr-radio label,
.gr-radio label span,
.gr-radio .gr-form-choice,
.gr-radio .gr-form-choice label,
.gr-radio input + label,
.gr-radio .gr-radio-item label {
    color: #0d47a1 !important;
    font-weight: 600 !important;
}
"""

GLASS_THEME = gr.themes.Glass(
    primary_hue="blue",
    secondary_hue="blue",
    neutral_hue="slate",
).set(
    body_background_fill="linear-gradient(135deg, #e0f2f7 0%, #b3e5fc 100%)",
    block_background_fill="rgba(255, 255, 255, 0.7)",
    block_border_color="rgba(0, 150, 255, 0.3)",
    input_background_fill="rgba(255, 255, 255, 0.9)",
    button_primary_background_fill="linear-gradient(135deg, #42a5f5 0%, #2196f3 100%)",
    body_text_color="#000000",
    block_label_text_color="#1976d2",
    button_primary_text_color="#0d47a1"
)
