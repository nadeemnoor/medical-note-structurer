# Medical Note Structuring Assistant (LLaMA2)

This application converts unstructured doctor notes into structured medical data
for easier review, storage, and EMR integration.

## Features
- Extract symptoms, diagnosis, medications, and follow-up
- Batch CSV uploads
- Structured JSON and CSV export
- FastAPI backend + Streamlit frontend

## How to Run
1. Pull model:
   ollama pull llama2
2. Start backend:
   uvicorn backend.main:app --reload
3. Start frontend:
   streamlit run frontend/app.py
4. Upload clinical notes and extract structured data
