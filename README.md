# 🛡️ Image Prompt Injection Detector

A proof-of-concept tool designed to act as a protective gateway, pre-scanning images for hidden threats before they are processed by multimodal LLMs or AI agents.

This project addresses the critical vulnerability of AI systems to prompt injection attacks by detecting two primary threat vectors:
1.  **Explicit Text-Based Injections:** Malicious commands hidden in image metadata (EXIF) or as visible text readable by OCR.
2.  **Implicit Adversarial Perturbations:** (Planned Feature) Pixel-level noise patterns designed to bypass an AI's safety alignment.

## ✨ Features

-   **Metadata Scanning:** Extracts and analyzes EXIF and other metadata.
-   **OCR Analysis:** Uses the Tesseract engine to read and analyze visible text.
-   **Pattern Matching:** Detects a wide range of suspicious patterns.
-   **Threat Scoring:** Provides an intuitive risk score for each image.
-   **Self-Contained & Portable:** Runs anywhere with Docker, with zero local dependencies.

## 🛠️ Tech Stack

-   **Backend:** Python
-   **UI:** Gradio
-   **Image Processing:** Pillow, Pytesseract, OpenCV, NumPy
-   **Containerization:** Docker & Docker Compose

---

### Installation & Running

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd ai-safety-detector
    ```

2.  **Build and Run the Docker Container**
    Use Docker Compose to build the image and start the application. This single command handles all dependencies and configurations.
    ```bash
    docker-compose up --build
    ```
    - The first time you run this, Docker will download the base image and install Tesseract, which may take a few minutes. Subsequent runs will be much faster.

3.  **Access the Application**
    Once the container is running, open your web browser and navigate to:
    [**http://localhost:7860**](http://localhost:7860)
