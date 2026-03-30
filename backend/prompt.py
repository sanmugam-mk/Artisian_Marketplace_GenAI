def description_prompt(product, material, craft_type, region):
    return f"""
You are an e-commerce product listing generator.

Generate a SHORT and CRISP product description.

Input:
Product: {product}
Material: {material}
Craft Type: {craft_type}
Region: {region}

Rules:
- Max 2 lines
- No storytelling
- No cultural essays
- Keep it marketplace-ready
- Use simple, clean English

Return ONLY valid JSON:

{{
  "title": "max 6 words product title",
  "description": "2 short lines only",
  "category": "single word category",
  "tags": ["3-4 short keywords"]
}}
"""

def details_prompt(product, craft_type, region):
    return f"""
You are generating product specifications for an online marketplace.

Input:
Product: {product}
Craft Type: {craft_type}
Region: {region}

Rules:
- No storytelling
- Use bullet-style short points
- Keep each point under 10 words

Return ONLY valid JSON:

{{
  "details": [
    "Point 1",
    "Point 2",
    "Point 3",
    "Point 4"
  ]
}}
"""

def pricing_prompt(product, material, craft_type, region):
    return f"""
You are a pricing assistant for handcrafted products.

Input:
Product: {product}
Material: {material}
Craft Type: {craft_type}
Region: {region}

Rules:
- Give realistic price range
- No long explanation
- Keep it short

Return ONLY valid JSON:

{{
  "price_range": "₹XXXX - ₹XXXX",
  "pricing_note": "1 short line justification"
}}
"""