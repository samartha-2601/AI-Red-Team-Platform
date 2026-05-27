from providers.openai_provider import (
    OpenAIProvider
)

from providers.ollama_provider import (
    OllamaProvider
)


def get_provider(
    provider_name
):

    if provider_name == "openai":
        return OpenAIProvider()

    if provider_name == "ollama":
        return OllamaProvider()

    raise ValueError(
        f"Unknown provider: {provider_name}"
    )