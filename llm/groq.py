from groq import Groq
from llm.system import newsSystemInstruction
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)


def callLLM(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": newsSystemInstruction},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_completion_tokens=6000,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content
