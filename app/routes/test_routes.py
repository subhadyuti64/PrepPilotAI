from fastapi import APIRouter

from app.services.pdf_service import load_resume

router = APIRouter()


@router.get("/test-pdf")
def test_pdf():

    docs = load_resume(
        "data/123BT0790_SubhadyutiDS.pdf"
    )

    return {
        "pages": len(docs),
        "preview": docs[0].page_content[:500]
    }