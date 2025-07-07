from providers import mistral, gemini

PROVIDERS = {
    "mistral": mistral.completion,
    "gemini": gemini.completion,
}

def route(model_name: str):
    if model_name.lower() in PROVIDERS:
        return PROVIDERS[model_name.lower()]
    else:
        raise ValueError(f"Model '{model_name}' not supported.")

