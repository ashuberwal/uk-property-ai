[![CI Pipeline](https://github.com/ashuberwal/uk-property-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/ashuberwal/uk-property-ai/actions/workflows/ci.yml)

# 🏡 UK Property AI Engine

An end-to-end machine learning pipeline and RESTful API that predicts UK real estate prices using historical HM Land Registry data. 

This project demonstrates a complete AI Engineering workflow, moving from raw data processing and feature engineering to model training and production-ready containerized deployment.

## 🚀 Key Features
* **Data Pipeline:** Processes raw CSV data, handles missing values, and extracts temporal features (Year, Month).
* **Feature Engineering:** Implements Target Encoding to translate complex geographical text data (Town/City) into mathematical signals.
* **Machine Learning:** Evaluates multiple algorithms. Selected a highly optimized Linear Regression model over Random Forest to prevent overfitting and ensure lightning-fast API response times.
* **REST API:** Serves predictions in real-time using FastAPI and Uvicorn.
* **Containerization:** Fully dockerized environment ensuring consistent, OS-agnostic deployment.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **API Framework:** FastAPI, Pydantic
* **Deployment:** Docker

## 🐳 How to Run Locally (Docker)

You don't need Python installed to run this AI, just Docker.

1. Clone the repository:
   git clone [https://github.com/ashuberwal/uk-property-ai.git](https://github.com/ashuberwal/uk-property-ai.git)
   cd uk-property-ai

2. Build the Docker image:
    docker build -t uk-property-api .
3. Run the container:
    docker run -p 8000:8000 uk-property-api
4. Access the interactive API documentation at: http://localhost:8000/docs

API Usage Example:
    Send a POST request to /predict with the following JSON payload:
    {
    "year": 2026,
    "month": 2,
    "property_type": 3,
    "old_new": 1,
    "town_city": "LONDON"
    }

    Response:
    {
    "town_city": "LONDON",
    "estimated_price": 97120.34,
    "currency": "GBP"
    }

Author:
    Ashu Berwal - AI Engineer
