# Prompt Chaining to Break Down A Complex Task

📝 Task Description
You have been tasked with building an intelligent customer support system for a bank that converses with customers and helps solve their problems.

The first stage of implementation is to design a prompt chain that processes a customer’s free-text query step by step to understand what the customer wants and how to respond.

Your prompt chain should have 5 clearly defined prompts that accomplish the following:

    Interpret the customer’s intent — Understand what the customer is asking or reporting.
    Map the query to possible categories — Suggest one or more categories that might apply.
    Choose the most appropriate category — Select the best matching category.
    Extract additional details — Identify any extra information needed to address the request (e.g., transaction date, amount, card type, etc.).
    Generate a short response — Produce a suitable reply to the customer based on the chosen category.

Each stage builds on the previous one, forming a logical reasoning chain from understanding → classification → response.

Available Categories

```markdown
All customer queries must be classified into one of these buckets:

- Account Opening
- Billing Issue
- Account Access
- Transaction Inquiry
- Card Services
- Account Statement
- Loan Inquiry
- General Information
```