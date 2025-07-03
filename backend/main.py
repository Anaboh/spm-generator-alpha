from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from agents import pdf_ingester, corap_creator, insight_generator, chat_agent, learning_agent
import os
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

documents_db = {}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = f"uploads/{file_id}.pdf"
    
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    text_content = pdf_ingester.ingest_pdf(file_path)
    corap = corap_creator.create_corap(text_content)
    
    documents_db[file_id] = {
        "text": text_content,
        "corap": corap
    }
    
    return {"file_id": file_id}

@app.post("/generate-spm")
async def generate_spm(
    file_id: str = Form(...),
    length: int = Form(3),
    model_name: str = Form("deepseek")
):
    corap = documents_db[file_id]["corap"]
    spm = insight_generator.generate_spm(corap, length, model_name)
    return {"spm": spm}

@app.post("/chat")
async def chat(
    file_id: str = Form(...),
    question: str = Form(...)
):
    text_content = documents_db[file_id]["text"]
    response, refs = chat_agent.chat_with_pdf(question, text_content)
    return {"response": response, "references": refs}

@app.get("/models")
async def get_models():
    return list(insight_generator.MODEL_MAP.keys())
