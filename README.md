# GenAI Artisan Product Generator

## 🚀 Overview

This project is a Generative AI-powered system that helps artisans and small sellers automatically generate:

* Product descriptions
* Detailed product information
* Pricing suggestions

based on simple inputs like product type, material, craft type, and region.

---

## 🎯 Problem Statement

Artisans often lack the time and expertise to write compelling product descriptions or decide optimal pricing. This system automates content generation and improves consistency using AI.

---

## 🤖 Why Generative AI?

This system uses a Large Language Model (LLM) to dynamically generate content. Unlike rule-based systems, the outputs are context-aware and generated in real time.

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Groq API
* **Language:** Python
* **API Testing:** Swagger UI (built-in FastAPI docs)

---

## 🧱 System Architecture

1. User inputs product details (product, material, craft_type, region)
2. FastAPI processes the request
3. Structured prompts are sent to the Groq LLM
4. LLM generates:

   * Description
   * Details
   * Pricing
5. Results are returned via API

---

## 📌 API Endpoints

### POST /desc

Generates product description

### POST /details

Generates detailed product insights

### POST /pricing

Generates pricing suggestions

---

## Run the server

```
inside the virtual environment,
cd backend
uvicorn main:app --reload
```

---

## 🔥 Features

* Modular API design
* Real-time AI-generated content
* Structured input handling
* Interactive API testing via Swagger

---

