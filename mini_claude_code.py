from openai import OpenAI
from pathlib import Path
import json 
from dotenv import load_dotenv 
import os

#Read .env manually
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

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"File {path} not found"
TOOL_SCHEMAS = [
        {
            "type": "function",
            "function": {
                "name": "read_file",
                "description": "Read a text file and return its contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "path of the file to read"},
                        },
                        "required": ["path"],
                    },
                },
            },
        ]

messages = [
        {"role": "user", "content": "what is inside notes.text? summarize it in one line"},
        ]

while True:
    response = client.chat.completions.create(
        model="nvidia/nemotron-3.5-lightning:free",
        messages=messages,
        tools=TOOL_SCHEMAS,
    )
    
    message = response.choices[0].message
    messages.append(message)
    
    # NO tool call means the model is done 

    if not message.tool_calls:
        print(message.content)
        break

    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)
        print(f"Model wants to run: read_file({args})")

        result = read_file(**args)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
            })

