from pydantic import BaseModel


class CatalogRequest(BaseModel):
    product: str
    material: str
    region: str


class StoryRequest(BaseModel):
    artisan: str
    craft: str
    region: str


class PricingRequest(BaseModel):
    product: str
    material: str
    craft_type: str
    region: str