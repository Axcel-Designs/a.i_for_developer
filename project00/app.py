import os
import re
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("⚠️ Please add your OPENROUTER_API_KEY in the .env file.")

# Banned keywords for moderation
BANNED_KEYWORDS = ["kill", "hack", "bomb", "attack", "terror"]

def moderate_input(user_input):
    """Check if input contains any banned keyword."""
    text = user_input.lower()
    return any(word in text for word in BANNED_KEYWORDS)

def moderate_output(response_text):
    """Replace banned keywords with [REDACTED]"""
    moderated_text = response_text
    violated = False

    for word in BANNED_KEYWORDS:
        pattern = re.compile(word, re.IGNORECASE)
        if re.search(pattern, response_text):
            violated = True
            moderated_text = re.sub(pattern, "[REDACTED]", moderated_text)

    return violated, moderated_text

def call_openrouter_api(system_prompt, user_prompt):
    """Send the prompt to OpenRouter API and get AI response."""
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-4o-mini",  # Change model if needed
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]

def main():
    print("=== OpenRouter AI with Moderation (Python) ===\n")

    user_prompt = input("Enter your prompt: ")

    # 🔒 Input Moderation
    if moderate_input(user_prompt):
        print("❌ Your input violated the moderation policy.")
        return

    # 🧭 System Prompt (AI behavior)
    system_prompt = (
        "You are a helpful, polite AI assistant. "
        "Do not promote violence, hacking, or harmful activities. "
        "Respond briefly and kindly."
    )

    try:
        ai_response = call_openrouter_api(system_prompt, user_prompt)

        # 🧹 Output Moderation
        violated, moderated_text = moderate_output(ai_response)

        if violated:
            print("\n⚠️ Output contained restricted content. Showing moderated version:\n")
            print(moderated_text)
        else:
            print("\n✅ AI Response:\n")
            print(ai_response)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
