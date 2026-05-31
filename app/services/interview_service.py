import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

load_dotenv()

from app.services.vector_service import (
    load_vector_store
)


def generate_interview_question(
    domain: str,
    session_id: str
):

    vector_store = load_vector_store(
        session_id
    )

    docs = vector_store.similarity_search(
        f"{domain} skills and projects",
        k=5
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = f"""
You are a senior technical interviewer.

Candidate Resume:
{context}

Generate ONE interview question for:

{domain}

Requirements:
- Personalized to candidate resume
- Intermediate difficulty
- Related to projects or skills
- Suitable for a real interview
- Return ONLY the question
"""

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv(
            "OPENAI_API_KEY"
        )
    )

    response = llm.invoke(
        prompt
    )

    return response.content

def evaluate_answer(question: str, answer: str):

    prompt = f"""
You are a highly experienced Senior Software Engineer and Technical Interviewer.

Your task is to evaluate a candidate's answer exactly as you would in a real technical interview.

QUESTION:
{question}

CANDIDATE ANSWER:
{answer}

==========================
EVALUATION CRITERIA
==========================

1. Technical Accuracy (40%)
- Are the concepts correct?
- Any misconceptions?

2. Completeness (25%)
- Does the answer cover all major points?
- Are important details missing?

3. Depth of Understanding (20%)
- Does the candidate demonstrate real understanding?
- Or are they repeating buzzwords?

4. Communication & Clarity (15%)
- Is the explanation structured and easy to follow?

==========================
SCORING GUIDELINES
==========================

10/10
- Interview-ready answer
- Accurate, complete and deep
- Includes relevant examples
- Demonstrates expert understanding

8-9/10
- Strong answer
- Mostly complete
- Minor missing details

6-7/10
- Correct core idea
- Missing important concepts
- Limited depth

4-5/10
- Partial understanding
- Several gaps
- Weak explanation

2-3/10
- Significant misunderstandings
- Major concepts missing

0-1/10
- Completely incorrect
- Irrelevant answer

STRICT RULES:
- One sentence answer → maximum 4/10
- Two to three sentence answer → maximum 6/10 unless exceptionally detailed
- Vague statements should be penalized
- Mentioning keywords without explanation should not earn high marks
- Be stricter than a typical interviewer
- Do NOT inflate scores

==========================
OUTPUT FORMAT
==========================

Return ONLY valid JSON.

{{
    "score": 0,

    "technical_accuracy": 0,

    "completeness": 0,

    "depth_of_understanding": 0,

    "communication": 0,

    "strengths": [
        ""
    ],

    "weaknesses": [
        ""
    ],

    "missing_concepts": [
        ""
    ],

    "ideal_answer": "",

    "follow_up_questions": [
        "",
        "",
        ""
    ]
}}

Do not return markdown.
Do not return explanations.
Return JSON only.
"""

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    response = llm.invoke(prompt)

    return response.content