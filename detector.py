from PIL.ExifTags import TAGS
import pytesseract
import re

from patterns import SUSPICIOUS_PATTERNS

def extract_metadata(image):
    """Extract EXIF and metadata from image"""
    metadata_list = []
    try:
        exif_data = image.getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata_list.append(f"{tag}: {value}")
    except:
        pass
    
    # Check image info
    try:
        if hasattr(image, 'info') and image.info:
            for key, value in image.info.items():
                metadata_list.append(f"{key}: {value}")
    except:
        pass
    
    return "\n".join(metadata_list) if metadata_list else "No metadata found"

def extract_visible_text(image):
    """Extract visible text using OCR"""
    try:
        text = pytesseract.image_to_string(image)
        return text.strip() if text.strip() else "No visible text detected"
    except Exception as e:
        return f"OCR Error: {str(e)}"

def analyze_text_for_threats(text):
    """Check text for suspicious prompt injection patterns"""
    if not text or text == "No visible text detected" or "OCR Error" in text:
        return False, []
    
    detected_patterns = []
    text_lower = text.lower()
    
    for pattern in SUSPICIOUS_PATTERNS:
        matches = re.findall(pattern, text_lower, re.IGNORECASE)
        if matches:
            detected_patterns.append(f"Found: '{pattern}' (matched: {matches[0] if isinstance(matches[0], str) else 'pattern'})")
    
    return len(detected_patterns) > 0, detected_patterns

def detect_injection(image):
    """Main detection pipeline"""
    if image is None:
        return "⚠️ Please upload an image", "", "", "", 0
    
    # Extract metadata
    metadata = extract_metadata(image)
    print("Extracted Metadata:", metadata)
    # Extract visible text
    visible_text = extract_visible_text(image)
    print
    # Check metadata for threats
    metadata_threat, metadata_patterns = analyze_text_for_threats(metadata)
    print("Metadata Threat Detected:", metadata_threat)
    print("Metadata Patterns:", metadata_patterns)
    # Check visible text for threats
    text_threat, text_patterns = analyze_text_for_threats(visible_text)
    print("Visible Text Threat Detected:", text_threat)
    print("Visible Text Patterns:", text_patterns)
    # Combine results
    all_threats = metadata_patterns + text_patterns
    is_threat = metadata_threat or text_threat
    print("All Detected Threats:", all_threats)
    print("Overall Threat Detected:", is_threat)

    
    if is_threat:
        status = "🔴 ATTACK DETECTED"
        threat_score = min(len(all_threats) * 0.3, 1.0)  # Cap at 1.0
        details = "**Suspicious patterns found:**\n\n" + "\n".join([f"• {t}" for t in all_threats])
        recommendation = "⚠️ **DO NOT** pass this image to AI agents or LLMs"
    else:
        status = "🟢 SAFE"
        threat_score = 0.0
        details = "No suspicious patterns detected"
        recommendation = "✅ Image appears safe to process"
    
    return status, metadata, visible_text, details, threat_score, recommendation
