# Product Recommendation API Documentation

## Overview
This API provides personalized financial product recommendations based on customer profiles and their financial needs using natural language processing and vector similarity.

# Bank Product Recommendation System

## Architecture Diagram

![System Architecture Diagram](res/arch.png)

## Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Future Improvements](#future-improvements)

## Introduction
This project is an innovative financial recommendation platform designed to provide personalized product suggestions and insights for bank customers. By leveraging advanced machine learning techniques, natural language processing, and comprehensive data analysis, the system aims to enhance customer experience and financial product matching.

## Demo
The system offers a web-based interface that allows users to:
- Retrieve detailed customer profiles
- Generate personalized product recommendations
- Analyze customer transaction insights
- Predict future transaction behaviors
- Optimize existing bank products

## Inspiration
The inspiration behind this project stems from the need to:
- Improve customer financial experiences
- Provide data-driven, personalized banking solutions
- Utilize advanced AI technologies to understand customer needs
- Create a more intelligent and responsive banking ecosystem

## What It Does
The Bank Product Recommendation System provides several key functionalities:

1. **Customer Profile Analysis**
   - Retrieves comprehensive customer information
   - Combines customer profiles with social media data
   - Generates detailed profile summaries using AI

2. **Product Recommendations**
   - Uses semantic similarity to match customer needs with bank products
   - Generates personalized product suggestions
   - Provides detailed reasoning for each recommendation

3. **Transaction Insights**
   - Analyzes customer transaction history
   - Predicts future transaction amounts
   - Generates transaction behavior insights

4. **Product Optimization**
   - Offers suggestions for improving existing bank products
   - Uses AI to generate specific, actionable recommendations

## How We Built It
The system was built using a modular, microservice-based architecture:

1. **Data Management**
   - Utilized JSON files for storing customer, product, and transaction data
   - Implemented services to load and process data dynamically

2. **Machine Learning Components**
   - Used SentenceTransformer for semantic product matching
   - Implemented a predictive transaction model using scikit-learn
   - Leveraged pre-trained machine learning models

3. **AI-Powered Analysis**
   - Integrated OpenAI-compatible LLM (Llama 3.1 70B) for natural language processing
   - Created sophisticated prompts for generating insights
   - Implemented robust JSON parsing and cleaning mechanisms

4. **API Development**
   - Used FastAPI for creating a robust, scalable web service
   - Implemented CORS middleware for cross-origin compatibility
   - Created endpoints for various functionalities

## Challenges We Faced
1. **Data Integration**
   - Combining multiple data sources with different structures
   - Ensuring data quality and consistency

2. **AI Prompt Engineering**
   - Designing prompts that generate precise, relevant outputs
   - Handling various edge cases in language model responses

3. **Performance Optimization**
   - Managing computational resources for ML models
   - Implementing efficient vector similarity calculations

4. **Model Interpretation**
   - Translating complex AI insights into understandable recommendations
   - Maintaining transparency in recommendation generation

## How to Run
To run the project:

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Tech Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Machine Learning**: 
  - SentenceTransformers
  - scikit-learn
  - NumPy
- **Natural Language Processing**: 
  - OpenAI/Llama 3.1 70B
- **Data Handling**: JSON
- **Libraries**: 
  - sentence-transformers
  - scipy
  - pickle
  - python-dotenv
- **Deployment**: Designed for containerization and cloud deployment

## Future Improvements
- Enhance model accuracy through continuous learning
- Expand data sources and integration
- Implement more advanced recommendation algorithms
- Add real-time transaction monitoring

# Project Documentation

## Project Structure

### Main Components
- `main.py`: FastAPI application serving the main endpoints
- `customer_service.py`: Customer data retrieval and processing
- `product_service.py`: Product recommendation logic
- `llm_service.py`: Large Language Model interactions
- `model_service.py`: Transaction prediction model
- `transaction_service.py`: Customer transaction insights retrieval

## Key Features

### 1. Product Recommendations
- Personalized product suggestions based on customer profile
- Uses sentence transformer for semantic similarity
- Generates detailed product recommendations with reasoning

### 2. Transaction Prediction
- Machine learning model predicts future transaction amounts
- Provides a normalized score for transaction prediction

### 3. Customer Analysis
- Combines customer profile with social media data
- Uses LLM to generate customer profile summaries
- Identifies potential financial needs and product offerings

## API Endpoints

### Customer-related Endpoints
- `/all_customers_data`: Retrieve all customer data
- `/customer_data/{customer_id}`: Get specific customer profile
- `/customer_transaction_insights/{customer_id}`: Get transaction insights and predictions

### Product-related Endpoints
- `/all_products_data`: Retrieve all product information
- `/product_data/{product_id}`: Get specific product details
- `/product_recommendations/{customer_id}`: Generate personalized product recommendations
- `/product_optimizations/{product_id}`: Get product improvement suggestions

## Technologies Used
- FastAPI
- OpenAI/SambaNova LLM
- Sentence Transformers
- Scikit-learn (for transaction prediction)
- NumPy
- Pickle (for model serialization)

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation Steps
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables (API keys, etc.)
5. Run the FastAPI application:
   ```
   uvicorn main:app --reload
   ```

## Data Sources
- `./data/customer_profile.json`
- `./data/products.json`
- `./data/customer_monthly_transaction_insights.json`
- `./models/TransactionModel.pkl`

## Customization
- Modify prompts in `llm_service.py` to adjust LLM behavior
- Update recommendation logic in `product_service.py`
- Retrain transaction prediction model in `model_service.py`

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
