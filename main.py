import easyocr
from pdf2image import convert_from_path
import cv2
import numpy as np
import os
import re
from collections import defaultdict

# === Step 1: Convert PDF to Image (skip if input is already an image)
def pdf_to_image(pdf_path, output_folder="output_images"):
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path, dpi=300)
    image_paths = []
    for i, img in enumerate(images):
        path = os.path.join(output_folder, f"page_{i+1}.png")
        img.save(path, 'PNG')
        image_paths.append(path)
    return image_paths

# === Step 2: OCR using EasyOCR
def perform_ocr(image_path):
    # Read the image from file
    image = cv2.imread(image_path)

    # Perform OCR on the resized image
    reader = easyocr.Reader(['en'], gpu=True)
    results = reader.readtext(image, text_threshold= 0, width_ths= 1.0)


    return results  # list of (bbox, text, confidence)


# === Step 3: Group and rank by font size
def rank_by_font_size(ocr_results, tolerance=10):
    blocks = []
    for bbox, text, _ in ocr_results:
        y_top = bbox[0][1]
        y_bottom = bbox[2][1]
        height = abs(y_bottom - y_top)
        blocks.append({
            "text": text,
            "bbox": [[int(x), int(y)] for x, y in bbox],
            "height": height
        })

    # Get max height
    max_height = max(block["height"] for block in blocks)

    # Filter blocks within tolerance of max_height
    top_blocks = [
        block for block in blocks
        if abs(block["height"] - max_height) <= tolerance
    ]

    return top_blocks  # Only return the top-height group


# === Step 4: Draw Bounding Boxes with Font Size Labels
def annotate_image(image_path, annotations, output_path="annotated.png"):
    image = cv2.imread(image_path)

    if not annotations:
        print("⚠️ No annotations to draw.")
        return

    # Collect all x, y points from qualifying boxes
    all_points = [pt for ann in annotations for pt in ann["bbox"]]
    all_points_np = np.array(all_points)

    # Compute bounding rectangle
    x, y, w, h = cv2.boundingRect(all_points_np)

    # Draw bounding box in green
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Optionally label
    cv2.putText(image, "Headline", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imwrite(output_path, image)
    print(f"✅ Annotated image saved to: {output_path}")



# === Run Entire Flow
if __name__ == "__main__":
    image_path = "./img/Screenshot_21-7-2025_93757_mb.com.ph.jpeg"
    ocr_results = perform_ocr(image_path)
    ranked_blocks = rank_by_font_size(ocr_results)
    annotate_image(image_path, ranked_blocks, "annotated_result.png")
