import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

# model = genai.GenerativeModel("models/gemini-pro")  # ✅ Must include "models/" prefix
# response = model.generate_content("Say hello!")
models = genai.list_models()
for m in models:
    print(m.name, "→", m.supported_generation_methods)
# print(response.text)