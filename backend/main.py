from fastapi import FastAPI

from providers.openai_provider import test_connection

app = FastAPI(
    title="AI Red Team Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Red Team Platform API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/test-openai")
def test_openai():
    response = test_connection()

    return {
        "response": response
    }