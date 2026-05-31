from app.utils.config import *

from fastapi import FastAPI

from app.routes.resume_routes import (
    router as resume_router
)

from app.routes.test_routes import (
    router as test_router
)

from app.routes.chat_routes import (
    router as chat_router
)

from app.routes.analysis_routes import (
    router as analysis_router
)

from app.routes.question_routes import (
    router as question_router
)

from app.routes.interview_routes import (
    router as interview_router
)

app = FastAPI(
    title="PrepPilot AI",
    description="AI-powered Interview Preparation Assistant",
    version="1.0.0"
)

# =====================================
# REGISTER ROUTERS
# =====================================

app.include_router(resume_router)

app.include_router(test_router)

app.include_router(chat_router)

app.include_router(analysis_router)

app.include_router(question_router)

app.include_router(interview_router)

# =====================================
# BASIC ENDPOINTS
# =====================================

@app.get("/")
def home():

    return {
        "message": "PrepPilot AI Running 🚀"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }