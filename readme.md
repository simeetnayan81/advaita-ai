# Product Recommendation API Documentation

## Overview
This API provides personalized financial product recommendations based on customer profiles and their financial needs using natural language processing and vector similarity.

## API Endpoints

### GET `/product_recommendations`
Returns personalized product recommendations for a customer with detailed reasons why each product is suitable.

**Parameters:**
- customerId

**Response:**
```json
{
  "Products": [
    {
      "Product_Name": "product name",
      "Reason": "Detailed reason why this product is suitable for the customer"
    },
    ...
  ]
}
```

## Modules

### Main Module (`main.py`)
This module contains the FastAPI application and endpoint definitions.

#### Functions

##### `get_product_recommendations()`
Endpoint to get personalized product recommendations for a customer.

**Returns:**
- JSON object containing product recommendations with reasons

##### `create_analysis_prompt(customer_profile)`
Create prompts for the LLM to analyze customer data.

**Parameters:**
- `customer_profile` (dict): The customer profile data

**Returns:**
- dict: Contains system_prompt and user_prompt for the LLM

### Customer Service (`customer_service.py`)
This module handles customer profile retrieval and processing.

#### Functions

##### `get_customer_profile(customer_id)`
Retrieve and combine customer profile with social media data.

**Parameters:**
- `customer_id` (str): The ID of the customer to retrieve

**Returns:**
- dict: Combined customer profile with personal and social media data

### LLM Service (`llm_service.py`)
This module manages interactions with the AI model.

#### Functions

##### `generate_customer_analysis(client, prompts)`
Generate customer analysis using the LLM.

**Parameters:**
- `client` (OpenAI): The OpenAI client
- `prompts` (dict): Dict containing system_prompt and user_prompt

**Returns:**
- dict: Parsed JSON response with customer analysis

##### `generate_product_recommendations(client, analysis, recommended_products)`
Generate detailed product recommendations using the LLM.

**Parameters:**
- `client` (OpenAI): The OpenAI client
- `analysis` (dict): Customer analysis result
- `recommended_products` (list): List of recommended products

**Returns:**
- dict: Detailed product recommendations with reasons

### Product Service (`product_service.py`)
This module encapsulates product recommendation logic.

#### Classes

##### `ProductRecommender`
A class to handle product recommendations using vector similarity.

###### Methods

###### `__init__(model_name='multi-qa-MiniLM-L6-cos-v1')`
Initialize the ProductRecommender with a sentence transformer model.

**Parameters:**
- `model_name` (str): Name of the sentence transformer model to use

###### `load_products(file_path="./data/products.json")`
Load and vectorize products from a JSON file.

**Parameters:**
- `file_path` (str): Path to the JSON file containing products

###### `get_recommendations(text, top_k=3)`
Get product recommendations based on text similarity.

**Parameters:**
- `text` (str): Text to compare products against
- `top_k` (int): Number of top recommendations to return

**Returns:**
- list: Top product recommendations

###### `_cosine_similarity(vec1, vec2)`
Calculate cosine similarity between two vectors.

**Parameters:**
- `vec1` (numpy.array): First vector
- `vec2` (numpy.array): Second vector

**Returns:**
- float: Similarity score (0-1)

#### Functions

##### `get_recommended_products(text)`
Get product recommendations based on text.

**Parameters:**
- `text` (str): Text describing customer needs

**Returns:**
- list: Recommended products

## Data Requirements

The application expects the following data files:
- `./data/updated_customer_profile.json`: Customer profile information
- `./data/non_contradictory_social_media_posts.json`: Social media posts linked to customers
- `./data/products.json`: Product catalog with descriptions and features

## Setup and Deployment

### Installing Dependencies
pip install -r requirements.txt

### Environment Variables
- `SAMBANOVA_API_KEY`: API key for accessing the SambaNova LLM service

### Starting the Server
```bash
uvicorn src.main:app --reload
```
