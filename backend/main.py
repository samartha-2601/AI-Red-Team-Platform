from fastapi import FastAPI

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