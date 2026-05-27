from fastapi import FastAPI

from engines.attack_runner import AttackRunner

app = FastAPI(
    title="AI Red Team Platform",
    version="0.1.0"
)

runner = AttackRunner()


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


@app.post("/run-prompt-injection-test")
def run_prompt_injection_test():

    return runner.run_prompt_injection_test()

@app.post("/run-all-targets")
def run_all_targets():

    return runner.run_all_targets()