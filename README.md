# 🛡️ AI Red Team Platform

> An AI security assessment platform that automatically evaluates Large Language Models (LLMs) against the **OWASP Top 10 for LLM Applications** using automated adversarial attacks, risk scoring, and security assessments.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue)
![OWASP](https://img.shields.io/badge/OWASP-LLM%20Top%2010-red)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## Overview

Large Language Models are increasingly integrated into enterprise applications, making them attractive targets for prompt injection, jailbreaks, role confusion, and other adversarial attacks.

The AI Red Team Platform provides an automated framework to evaluate AI assistants against common attack techniques aligned with the **OWASP Top 10 for LLM Applications**.

The platform allows security engineers to:

- Assess multiple AI assistants
- Benchmark different LLM providers
- Execute automated attack suites
- Calculate security risk scores
- Compare model resilience across attack categories

---

# Features

## Multi-Provider Support

- OpenAI
- Anthropic Claude
- Ollama

---

## AI Assistant Targets

The platform currently supports evaluating multiple AI assistants:

- Banking Assistant
- HR Assistant
- Customer Support Assistant

Each target has its own system prompt and is assessed independently.

---

## Automated Attack Categories

Current attack implementations include:

- Prompt Injection
- Advanced Prompt Injection
- Jailbreak
- Role Confusion

Future attack categories:

- Indirect Prompt Injection
- Sensitive Information Disclosure
- Data Exfiltration
- Tool Abuse
- Agent Manipulation

---


## Assessment Engine

The assessment engine automatically:

- Executes attack suites
- Evaluates attack success
- Calculates attack success rates
- Generates overall risk scores
- Maps findings to OWASP categories

---

# Model Comparison

The platform supports comparing different LLM providers using the same attack suite.

Current API:

```http
POST /compare/{provider1}/{provider2}/{target}
```

Example:

```text
OpenAI

vs

Ollama

↓

Overall Score
Category Breakdown
Winner
```

---

# Architecture

```text
                    React Dashboard
                           │
                           ▼
                    FastAPI REST API
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
 Assessment Engine                Comparison Engine
          │
          ▼
      Attack Runner
          │
 ┌────────┼───────────┬──────────────┐
 ▼        ▼           ▼              ▼
Prompt  Advanced   Jailbreak   Role Confusion
Injection Injection
          │
          ▼
   OpenAI / Ollama Providers
          │
          ▼
      Large Language Model
```

---

# Tech Stack

## Backend

- Python 3.12
- FastAPI
- Uvicorn
- OpenAI SDK
- Ollama SDK

## Frontend

- React
- TypeScript
- Vite
- Axios

## Security

- OWASP Top 10 for LLM Applications
- Prompt Injection Testing
- Jailbreak Testing
- Role Confusion Testing

---


# Frontend Dashboard

Current dashboard includes:

- Provider Selection
- Target Selection
- Run Assessment
- Overall Risk Score
- Risk Rating
- Attack Category Summary
- Model Comparison

---

# Example Workflow

```text
Select Provider
        │
        ▼
Select Target
        │
        ▼
Run Assessment
        │
        ▼
Execute Attack Categories
        │
        ▼
Calculate Risk Score
        │
        ▼
Display Security Assessment
```

---


# Author

**Samartha Suresh**

---

# License

This project is intended for educational, research, and defensive security purposes only.