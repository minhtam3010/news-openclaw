from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)


def callLLM(prompt, systemInstruction):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": systemInstruction},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_completion_tokens=1000,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content
