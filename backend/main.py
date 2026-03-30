import sys
import os

from fastapi import FastAPI, HTTPException , Depends
from sqlalchemy.orm import Session 
from fastapi.middleware.cors import CORSMiddleware
from models import CatalogRequest, StoryRequest, PricingRequest
from desc import gen_desc
from details import gen_details
from pricing import gen_pricing

app = FastAPI()

#Database creation part 
import database 
from database import SessionLocal,engine 
import database_models 
from database_models import ProductContent

from database import Base
Base.metadata.create_all(bind=engine)

# This get_db func is used to create a new database session for each request & 
# closes it automatically after the request is done.
# This helps us to avoid manually creating new db session and close it every time.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.post("/generate")
def generate_all(data: CatalogRequest, db: Session = Depends(get_db)):
    try:
        # Check cache
        existing = db.query(ProductContent).filter_by(
            product=data.product,
            material=data.material,
            craft_type=data.craft_type,
            region=data.region
        ).first()

        # If found, return cached data
        if existing:
            print("CACHE HIT")
            return {
                "source": "cache",
                "description": existing.description,
                "details": existing.details,
                "pricing": existing.pricing
            }

        # If not, Generate from LLM
        desc = gen_desc(data.product, data.material, data.region)
        print("DESC:", desc)

        details = gen_details(data.product, data.craft_type, data.region)
        print("DETAILS:", details)

        pricing = gen_pricing(data.product, data.material, data.craft_type, data.region)
        print("PRICING:", pricing)

        #  If any module returns empty content, then raise error
        if not desc or not details or not pricing:
            raise ValueError("LLM returned empty response")

        # Store the generated content in DB
        new_record = ProductContent(
            product=data.product,
            material=data.material,
            craft_type=data.craft_type,
            region=data.region,
            description=str(desc),
            details=str(details),
            pricing=str(pricing)
        )

        db.add(new_record)
        db.commit()
        db.refresh(new_record)

        return {
            "source": "llm",
            "description": desc,
            "details": details,
            "pricing": pricing
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "error": str(e)
        }

@app.get("/")
def root():
    return {"message": "Artisans Marketplace AI API is running"}


@app.get("/previous_data")
def get_previous_data(db: Session = Depends(get_db)):
    data = db.query(ProductContent).all()
    return {"History of datas": data}

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