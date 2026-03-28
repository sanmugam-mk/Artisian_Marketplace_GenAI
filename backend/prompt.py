def description_prompt(product, material, region):
    return f"""You are an expert Indian handicraft cataloger.

Product: {product}
Material: {material}
Region: {region}

Return ONLY a valid JSON object, no extra text, no markdown, no code blocks:
{{
  "title": "short catchy marketplace title",
  "description": "2-3 lines describing the product and its cultural value",
  "category": "main craft category (e.g. Pottery, Textiles, Woodwork, Jewelry)",
  "tags": ["tag1", "tag2", "tag3", "tag4"]
}}"""


def details_prompt(artisan, craft, region):
    return f"""You are a cultural storyteller for Indian artisans.

Artisan: {artisan}
Craft: {craft}
Region: {region}

Return ONLY a valid JSON object, no extra text, no markdown, no code blocks:
{{
  "story": "3-4 lines that are emotional, culturally rich, and connect the buyer to the artisan heritage and tradition"
}}"""


def pricing_prompt(product, material, craft_type, region):
    return f"""You are a pricing expert for Indian handmade marketplace products.

Product: {product}
Material: {material}
Craft Type: {craft_type}
Region: {region}

Consider raw material cost, artisan labor, regional craft rarity, and fair trade pricing.

Return ONLY a valid JSON object, no extra text, no markdown, no code blocks:
{{
  "min_price": 500,
  "max_price": 1500,
  "recommended_price": 999,
  "reasoning": "2 lines explaining why this price range is fair and competitive"
}}"""