import google.generativeai as genai

genai.configure(api_key="your_api_key")  # Replace with actual Gemini API key

def completion(prompt: str):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
