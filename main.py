import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from helper import generate_content


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if (api_key == None) :
    raise RuntimeError("Invalid api key")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User Prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {
        "role": "user", "content": args.user_prompt,
    },
]

generate_content(client, messages, args)


