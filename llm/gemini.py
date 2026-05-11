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
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
    )

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            # This is how you pass your system instruction in the new SDK
            system_instruction=systemInstruction,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
        ),
    )

    return response.text
