from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from engines.attack_runner import AttackRunner

from providers.provider_factory import (
    get_provider
)

from engines.comparison_engine import (
    ComparisonEngine
)

app = FastAPI(
    title="AI Red Team Platform",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


@app.post("/assess/{provider}/{target}")
def assess_provider_target(
    provider: str,
    target: str
):

    try:

        runner = AttackRunner(
            get_provider(provider)
        )

        return (
            runner
            .assess_target_by_name(
                target
            )
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.post(
    "/compare/{provider1}/{provider2}/{target}"
)
def compare_models(
    provider1: str,
    provider2: str,
    target: str
):

    try:

        runner1 = AttackRunner(
            get_provider(provider1)
        )

        runner2 = AttackRunner(
            get_provider(provider2)
        )

        result1 = (
            runner1
            .assess_target_by_name(
                target
            )
        )

        result2 = (
            runner2
            .assess_target_by_name(
                target
            )
        )

        comparison_engine = (
            ComparisonEngine()
        )

        return comparison_engine.compare(
            result1,
            result2,
            provider1,
            provider2
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )