# OCR + Gemini Headline & Byline Detector

Automatically detect and label headlines and bylines in newspaper and magazine images using EasyOCR and Google Gemini AI. This tool generates annotated images and structured JSON outputs for further processing.

## Features

- **Automated text detection** using EasyOCR
- **AI-powered classification** with Google Gemini (headlines vs. bylines)
- **Annotated image output** with labeled text regions
- **Structured JSON export** with detected text and classifications
- **Jupyter notebook interface** for easy experimentation

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Newspaper or magazine images (PNG, JPG, etc.)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Funelas/Article-Extractor.git
cd ocr-gemini-detector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Quick Start

### 1. Prepare Your Image
Place your newspaper/magazine image in the project directory or update the path in the notebook.

### 2. Run the Notebook
```bash
jupyter notebook ocr_gemini_detector.ipynb
```

### 3. Configure the Image Path
In the notebook, update this line with your image file:
```python
image_path = "./path/to/your/image.png"
```

### 4. Execute All Cells
Run all cells in sequence to process your image.

## Output

The tool generates outputs in dedicated folders:

| Output | Location | Description |
|--------|----------|-------------|
| **Annotated Image** | `ocr_annotated/` | Image with labeled text boxes and classifications |
| **JSON Data** | `ocr_output/` | Structured text detections with metadata |

Example JSON structure:
```json
{
  "values": [
    {
      "headline": "PH share prices dip; peso climbs to 56.65 a dollar",
      "byline": "Jennifer B. Austria with AFP",
      "headline_coord": [98, 671, 1148, 967],
      "byline_coord": [698, 3377, 1231, 3420]
    },
    {
      "headline": "Metro Pacific unit acquires coconut processor for P1b",
      "byline": "By Jennifer B. Austria",
      "headline_coord": [1287, 1871, 3644, 2423],
      "byline_coord": [1313, 2420, 1813, 2488]
    }
  ]
}
```

**JSON Fields:**
- `headline` - The detected headline text
- `byline` - The detected byline/author text
- `headline_coord` - Bounding box coordinates [x1, y1, x2, y2] for the headline
- `byline_coord` - Bounding box coordinates [x1, y1, x2, y2] for the byline

## Configuration

### Adjusting OCR Settings
Modify these parameters in the notebook to fine-tune detection:
- `lang`: Language codes (e.g., `['en']` for English)
- `gpu`: Set to `True` for GPU acceleration

### Gemini Model Parameters
Customize the AI classification by adjusting:
- Temperature (creativity level)
- Max tokens (response length)

## Troubleshooting

**Issue: API key not found**
- Verify `.env` file is in the project root
- Ensure `GOOGLE_API_KEY=` is correctly formatted
- Restart the Jupyter kernel after creating/updating `.env`

**Issue: No text detected**
- Check image quality and resolution (higher is better)
- Ensure text is clearly visible
- Try adjusting OCR language settings

**Issue: Poor classification accuracy**
- Verify the text in your image is readable
- Consider preprocessing images (contrast, brightness)
- Test with different sample images

## Requirements

See `requirements.txt` for full dependencies:
- `easyocr` - Text detection and recognition
- `google-generativeai` - Gemini API client
- `python-dotenv` - Environment variable management
- `opencv-python` - Image processing
- `pillow` - Image manipulation
- `jupyter` - Interactive notebook environment

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the project.

## Support

For questions or issues, please open an issue on GitHub or contact the project maintainers.

---

**Last Updated:** October 2025