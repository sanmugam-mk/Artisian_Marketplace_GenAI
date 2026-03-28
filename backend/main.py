import sys
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import CatalogRequest, StoryRequest, PricingRequest
from desc import gen_desc
from details import gen_details
from pricing import gen_pricing

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Artisans Marketplace AI API is running"}

@app.post("/catalog")
def catalog(request: CatalogRequest):
    try:
        result = gen_desc(request.product, request.material, request.region)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/details")
def details(request: StoryRequest):
    try:
        result = gen_details(request.artisan, request.craft, request.region)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/pricing")
def pricing(request: PricingRequest):    
    try:
        result = gen_pricing(request.product, request.material, request.craft_type, request.region)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))