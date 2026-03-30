# Artisans Marketplace GenAI Backend

## Overview

This project is a backend system that generates structured marketplace content for handicraft products using a GenAI model (Groq LLM). It uses FastAPI for APIs and PostgreSQL for storing and caching generated results.

The system avoids repeated LLM calls by storing previously generated outputs in the database.

---

## Features

* Generate product description, details, and pricing using LLM
* Store generated results in PostgreSQL
* Cache results to avoid recomputation
* Clean FastAPI-based API endpoints

---

## Tech Stack

* FastAPI (Backend framework)
* PostgreSQL (Database)
* SQLAlchemy (ORM)
* Groq LLM (GenAI)
* Python

---

## Project Structure

```
backend/
│
├── main.py              # Main FastAPI app
├── database.py          # DB connection setup
├── database_models.py   # Table schema
├── models.py            # Request models
├── desc.py              # Description generation
├── details.py           # Details generation
├── pricing.py           # Pricing generation
├── prompt.py            # Prompt templates
├── config.py            # Config (API keys etc.)
└── test.py              # Testing (optional)
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd codechef_AI
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Database Setup (PostgreSQL)

1. Open pgAdmin
2. Create a database:

```
artisan_ai_db
```

3. Add `.env` file in root folder:

```
DATABASE_URL=postgresql://username:password@localhost:5432/artisan_ai_db
```

---

## Run the Server

```
cd backend
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /generate

#### Request Body

```
{
  "product": "saree",
  "material": "silk",
  "craft_type": "handloom weaving",
  "region": "kancheepuram"
}
```

#### Response

```
{
  "source": "llm" or "cache",
  "data": {
    "description": {...},
    "details": {...},
    "pricing": {...}
  }
}
```

---

## How It Works

1. User sends product input
2. Backend checks database for existing result
3. If found → return cached result
4. If not → call LLM
5. Store in PostgreSQL
6. Return structured response

---
