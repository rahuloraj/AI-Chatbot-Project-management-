from utils.db_utils import load_data
from utils.gpt_chain import get_gpt_response
import os
from dotenv import load_dotenv

load_dotenv()

def generate_summary():
    updates = load_data()
    if not updates:
        return "No tasks logged yet."

    text = "\n".join([u["update"] for u in updates])
    prompt = f"Summarize the following project updates into a weekly project report:\n{text}"
    return get_gpt_response(prompt, os.getenv("OPENAI_API_KEY"))