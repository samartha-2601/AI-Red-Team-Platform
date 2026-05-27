from enum import Enum


class OWASPLLMCategory(str, Enum):

    LLM01 = "Prompt Injection"

    LLM02 = "Sensitive Information Disclosure"

    LLM06 = "Excessive Agency"

    LLM07 = "System Prompt Leakage"