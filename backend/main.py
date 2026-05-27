from fastapi import FastAPI

from engines.attack_runner import AttackRunner

from targets.banking_assistant import BANKING_SYSTEM_PROMPT

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

@app.post("/run-advanced-prompt-injection-test")
def run_advanced_prompt_injection_test():

    return runner.run_advanced_prompt_injection_test()

@app.post("/run-jailbreak-test")
def run_jailbreak_test():

    return runner.run_jailbreak_test()

@app.post("/assess-banking-assistant")
def assess_banking_assistant():

    return runner.assess_banking_assistant()