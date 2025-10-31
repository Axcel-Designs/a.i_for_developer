# Prompt Moderation and Response Generation using an AI Service API

📝 Task Description

First, create an account for yourself with OpenAI or any other AI API Service Provider

Then, build a small script or function (in Python, JavaScript, or any preferred language) that does the following:

    Accepts a user prompt from input (e.g., via command line, web form, or API endpoint).
    Sends this user prompt to an AI text generation API along with a system prompt that defines the AI’s behaviour.

Implements moderation checks on:

    The input (to block harmful or disallowed content before sending it to the AI).
    The output (to filter or flag unsafe responses before displaying them to the user).

⚙️ Functional Requirements

1. System Prompt: A system prompt that should guide the model’s behavior.

2. User Prompt: Collected dynamically from the user.

3. API Call: Make a POST request to an AI API service endpoint including

**Moderation Logic:**
```markdown
Simple input moderation: e.g. reject the prompt if it includes banned keywords (e.g., “kill”, “hack”, “bomb”).
Output moderation: check AI’s response for the same keywords and replace them with [REDACTED] if found.
Output: Display either the moderated AI response or a message saying: "Your input/output violated the moderation policy."
```
