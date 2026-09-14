from openai import OpenAI
from pathlib import Path
import os

from pydantic import with_config

# Read .env manually
env_file = Path(__file__).parent / ".env"
with open(env_file) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            key, _, value = line.partition("=")
            os.environ[key.strip()] = value.strip()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

messages = []

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_input})


    response = client.chat.completions.create(
        model="nvidia/nemotron-3.5-lightning:free",
        messages=messages, 
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("Bot:", reply)

