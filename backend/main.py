from fastapi import FastAPI, Form
import requests

app = FastAPI()

def query_llama(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()

@app.post("/extract/")
def extract_medical_info(note: str = Form(...)):
    prompt = (
        "Extract the following from the doctor's note:\n"
        "- Symptoms\n"
        "- Diagnosis\n"
        "- Medications\n"
        "- Follow-up Instructions\n\n"
        "Return the output in valid JSON format.\n\n"
        f"Doctor's Note:\n{note}"
    )

    structured_data = query_llama(prompt)
    return {"structured": structured_data}