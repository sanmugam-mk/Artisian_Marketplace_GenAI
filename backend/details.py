import json
from config import client
from prompt import details_prompt


def clean_json(text):
    text = text.strip()
    if text.startswith("```"):
        parts = text.split("```")
        text = parts[1]
        if text.startswith("json"):
            text = text[4:]
    return text.strip()


def gen_details(artisan, craft, region):
    prompt = details_prompt(artisan, craft, region)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    text = clean_json(response.choices[0].message.content)
    result = json.loads(text)
    return result