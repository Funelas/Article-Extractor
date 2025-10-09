# 📰 OCR + Gemini Headline & Byline Detector

This project uses **EasyOCR** and **Google Gemini** to detect and label **headlines** and **bylines** in newspaper or magazine images. It outputs annotated images and structured JSON files.

---

## ⚙️ Setup & Usage

### 1. Install Requirements
Create and install from `requirements.txt`:
```bash
pip install -r requirements.txt

### 2. Add Your API Key
Create a `.env` file in the same folder:


### 3. Set Your Image Path
In the script, replace this line:
```python
image_path = "./imgs/page_56.png"

### 4. Run the Notebook
Open and run all cells in the Jupyter Notebook:
```bash
jupyter notebook ocr_gemini_detector.ipynb

### 5. View the Results
After running all cells, you’ll find the outputs automatically saved in a folder:

- **Annotated Image:**  
  Located in the `ocr_annotated/` folder (e.g., `ocr_annotated/page_56.png`)

- **Structured JSON:**  
  Contains text detections and classifications (headline/byline)

You can open the annotated image directly in the notebook or check the output folder.

