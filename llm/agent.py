from llm.groq import callLLM as callGroq
from llm.gemini import callLLM as callGemini


def callLLM(prompt, systemInstruction, model="groq"):
    if model == "groq":
        return callGroq(prompt, systemInstruction)
    else:
        return callGemini(prompt, systemInstruction)
