import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def call_llm(prompt: str, system: str = "You are a helpful assistant.") -> dict:
    response = client.chat.completions.create(
        model="google/gemini-2.0-flash-lite-001",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    )
    return {
        "text": response.choices[0].message.content,
        "model": response.model,
        "stop_reason": response.choices[0].finish_reason,
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens
    }

if __name__ == "__main__":
    response = call_llm("What is the capital of France?")
    print(response)