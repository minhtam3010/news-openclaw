import os
from google import genai
from google.genai import types


client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)


def callLLM(prompt, systemInstruction):
    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        system_instruction=systemInstruction,
    )
    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )

        return response.text
    except Exception:
        return "Server is in high demand, please try it again"