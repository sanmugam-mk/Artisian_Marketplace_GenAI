from desc import gen_desc
from details import gen_details
from pricing import gen_pricing

# Test Inputs 
product    = "Handwoven Cotton Scarf"
material   = "Cotton"
craft_type = "Handloom Weaving"
region     = "Varanasi"
artisan    = "Ravi Kumar"

print("\n" + "=" * 55)
print("  MODULE 1 — AUTO CATALOGING")
print("=" * 55)
catalog = gen_desc(product, material, region)
print(f"  Title       : {catalog['title']}")
print(f"  Description : {catalog['description']}")
print(f"  Category    : {catalog['category']}")
print(f"  Tags        : {', '.join(catalog['tags'])}")

print("\n" + "=" * 55)
print("  MODULE 2 — CULTURAL STORYTELLING")
print("=" * 55)
story = gen_details(artisan, craft_type, region)
print(f"  Story : {story['story']}")

print("\n" + "=" * 55)
print("  MODULE 3 — SMART PRICING")
print("=" * 55)
pricing = gen_pricing(product, material, craft_type, region)
print(f"  Price Range  : ₹{pricing['min_price']} — ₹{pricing['max_price']}")
print(f"  Recommended  : ₹{pricing['recommended_price']}")
print(f"  Reasoning    : {pricing['reasoning']}")

print("\n" + "=" * 55)
print("  ALL MODULES WORKING ✓")
print("=" * 55 + "\n")