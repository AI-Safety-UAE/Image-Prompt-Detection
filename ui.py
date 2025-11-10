import gradio as gr

from detector import detect_injection

def create_interface():
    with gr.Blocks(title="Image Prompt Injection Detector", theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # 🛡️ Image Prompt Injection Detector
        
        **Detect hidden prompt injection attacks in images before they reach AI agents.**
        
        This tool protects against attacks where malicious instructions are hidden in:
        - Image metadata (EXIF, comments)
        - Visible text overlays
        - OCR-readable content
        
        ### How it works:
        1. 📸 Upload an image
        2. 🔍 We extract all text (metadata + OCR)
        3. 🎯 Pattern matching detects injection attempts
        4. ✅ Get instant threat assessment
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                image_input = gr.Image(type="pil", label="📤 Upload Image to Scan")
                detect_btn = gr.Button("🔍 Scan for Threats", variant="primary", size="lg")
            
            with gr.Column(scale=1):
                status_output = gr.Textbox(label="🎯 Detection Status", lines=2, show_label=True)
                threat_score = gr.Slider(label="Threat Score", minimum=0, maximum=1, interactive=False)
                recommendation = gr.Textbox(label="💡 Recommendation", lines=2)
        
        threat_details = gr.Textbox(label="🔎 Detected Threats", lines=6)
        
        with gr.Accordion("📋 Extracted Data", open=False):
            with gr.Row():
                metadata_output = gr.Textbox(label="Image Metadata", lines=6)
                text_output = gr.Textbox(label="OCR Text", lines=6)
        
        # Example section
        gr.Markdown("""
        ---
        ## 🧪 Try These Examples
        Upload your own test images or use samples:
        """)
        
        detect_btn.click(
            fn=detect_injection,
            inputs=image_input,
            outputs=[
                status_output, 
                metadata_output, 
                text_output, 
                threat_details, 
                threat_score, 
                recommendation
            ]
        )
        
        gr.Markdown("""
        ---
        ### 📊 About This Project
        
        **Problem:** Agentic AI browsers can be hijacked by hidden text in images (prompt injection attacks)
        
        **Solution:** Pre-scan images before they reach AI agents
        
        **Detected Attack Types:**
        - Instruction overrides ("ignore previous instructions")
        - System prompt manipulation
        - Data exfiltration attempts
        - Jailbreak patterns
        """)
    return demo
