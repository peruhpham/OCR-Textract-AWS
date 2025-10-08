from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
import asyncio

from app.services import textract_service, ocr_store

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    """
    Nhận file từ frontend, gọi Textract (synchronous detect_document_text)
    Lưu kết quả vào MongoDB với job_id, trả về job_id cho frontend.
    """
    # đọc file bytes
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty file")

    job_id = str(uuid4())

    # Gọi Textract trong thread để tránh block event loop
    try:
        textract_response = await asyncio.to_thread(
            textract_service.detect_text, content
        )
    except Exception as e:
        # ghi log thật ở production
        raise HTTPException(status_code=500, detail=f"Textract error: {e}")

    # Lưu vào DB (async)
    await ocr_store.save_ocr_result(job_id, textract_response)

    return {"job_id": job_id}

@router.get("/status/{job_id}")
async def get_status(job_id: str):
    """
    Trả status: NOT_FOUND / PROCESSING / COMPLETED
    """
    return await ocr_store.get_status(job_id)

@router.get("/result/{job_id}")
async def get_result(job_id: str):
    """
    Trả raw JSON Textract (hoặc error)
    """
    return await ocr_store.get_result(job_id)
