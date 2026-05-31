import requests

BASE_URL = "https://preppilotai.onrender.com"

# =====================================
# UPLOAD RESUME
# =====================================

def upload_resume(file):

    files = {
        "file": (
            file.name,
            file,
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload-resume",
        files=files
    )

    return response.json()


# =====================================
# ANALYZE RESUME
# =====================================

def analyze_resume(session_id):

    response = requests.post(
        f"{BASE_URL}/analyze-resume",
        json={
            "session_id": session_id
        }
    )

    return response.json()


# =====================================
# RESUME CHAT
# =====================================

def ask_resume(
    question,
    session_id
):

    response = requests.post(
        f"{BASE_URL}/ask-resume",
        json={
            "session_id": session_id,
            "question": question
        }
    )

    return response.json()


# =====================================
# QUESTION GENERATOR
# =====================================

def generate_questions(
    domain,
    session_id
):

    response = requests.post(
        f"{BASE_URL}/generate-questions",
        json={
            "session_id": session_id,
            "domain": domain
        }
    )

    return response.json()


# =====================================
# MOCK INTERVIEW
# =====================================

def start_interview(
    domain,
    session_id
):

    response = requests.post(
        f"{BASE_URL}/start-mock-interview",
        json={
            "session_id": session_id,
            "domain": domain
        }
    )

    return response.json()


# =====================================
# ANSWER EVALUATION
# =====================================

def evaluate_answer(
    question,
    answer
):

    response = requests.post(
        f"{BASE_URL}/evaluate-answer",
        json={
            "question": question,
            "answer": answer
        }
    )

    return response.json()