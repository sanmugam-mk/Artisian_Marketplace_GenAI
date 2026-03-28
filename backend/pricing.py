import json
from config import client
from prompt import pricing_prompt


def clean_json(text):
    text = text.strip()
    if text.startswith("```"):
        parts = text.split("```")
        text = parts[1]
        if text.startswith("json"):
            text = text[4:]
    return text.strip()


def gen_pricing(product, material, craft_type, region):
    prompt = pricing_prompt(product, material, craft_type, region)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    text = clean_json(response.choices[0].message.content)
    result = json.loads(text)
    return result