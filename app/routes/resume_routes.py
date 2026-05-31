from fastapi import APIRouter, UploadFile, File
import os
import uuid

from app.services.pdf_service import load_resume

from app.services.vector_service import (
    create_vector_store
)

router = APIRouter()

UPLOAD_DIR = "data"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    # =========================
    # Create Unique Session
    # =========================

    session_id = str(
        uuid.uuid4()
    )

    session_dir = os.path.join(
        "vectorstores",
        session_id
    )

    os.makedirs(
        session_dir,
        exist_ok=True
    )

    # =========================
    # Save Uploaded File
    # =========================

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{session_id}_{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    # =========================
    # Load PDF
    # =========================

    documents = load_resume(
        file_path
    )

    # =========================
    # Create Vector Store
    # =========================

    chunks = create_vector_store(
        documents,
        session_dir
    )

    return {
        "message":
        "Resume uploaded successfully",

        "session_id":
        session_id,

        "filename":
        file.filename,

        "chunks_created":
        chunks
    }