from fastapi import FastAPI
import os
from dotenv import load_dotenv
import openai
import json
from .product_service import get_recommended_products, get_all_product_data, create_product_reccomendation
from .customer_service import get_customer_profile, get_all_customer_data
from .llm_service import generate_customer_analysis, generate_product_recommendations, get_product_suggestions
from .transaction_service import getCustomerTransactionsInsight
from .model_service import predict_transaction
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(
    api_key=os.getenv("SAMBANOVA_API_KEY"),
    base_url="https://api.sambanova.ai/v1",
)

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/all_products_data")
async def get_allProductData():
    all_product_data = get_all_product_data()
    return all_product_data

@app.get("/product_data/{product_id}")
async def get_customer_data(product_id: str):

    all_product_data = get_all_product_data()

    for product in all_product_data:
        if product["product_id"] == product_id:
            return product

@app.get("/product_optimizations/{product_id}")
async def get_product_optimisation(product_id: str):
    prompt = create_product_reccomendation(product_id)
    suggestion =get_product_suggestions(client,prompt)
    return suggestion
    


@app.get("/all_customers_data")
async def get_allCustomerData():
    all_customer_data = get_all_customer_data()
    return all_customer_data

@app.get("/customer_transaction_insights/{customer_id}")
async def get_customer_transaction_insights(customer_id: str):
    
    predictions = predict_transaction(customer_id)
    customer_transaction_insight = getCustomerTransactionsInsight(customer_id)
    return {
           "prediction" : predictions,
           "transaction_insights":customer_transaction_insight
    }


@app.get("/customer_data/{customer_id}")
async def get_customer_data(customer_id: str):

    all_customer_data = get_all_customer_data()

    for profile in all_customer_data:
        if profile["CustomerID"] == customer_id:
            return profile



@app.get("/product_recommendations/{customer_id}")
async def get_product_recommendations(customer_id: str):
    """
    Endpoint to get personalized product recommendations for a customer
    """
    combined_profile = get_customer_profile(customer_id)
    
    # Generate customer analysis using LLM
    analysis_prompt = create_analysis_prompt(combined_profile)
    analysis_result = generate_customer_analysis(client, analysis_prompt)
    
    #Get customer profile
    profile_summary =  analysis_result.get("profile_summary", "")

    # Get product recommendations based on analysis
    product_offering = analysis_result.get("product_offering", "")
    product_insights = get_recommended_products(product_offering)
    

    
    # Generate detailed product recommendations using LLM
    detailed_recommendations = generate_product_recommendations(
        client, 
        analysis_result, 
        product_insights["top_recommendations"]
    )
    
    return {"profile": profile_summary, "recommended": product_insights["top_recommendations"], "products_sentiment":product_insights["product_sentiment"] ,"products": detailed_recommendations}


def create_analysis_prompt(customer_profile):
    """
    Create prompts for the LLM to analyze customer data
    """
    system_prompt = """You are a professional data analyst at a bank. You have been provided with detailed customer information.
    Analyze the following customer data and provide descriptive summary of customer profile and insights into their financial needs, opportunities for product offerings. Output should be a JSON in the below format:
    {
        "profile_summary": "summary of customer profile. Should be in one paragraph",
        "product_offering": "financial needs and product preferences. Should be in one paragraph"
    }
    Only give the json format only. Don't give any other response.
    """
    
    user_prompt = f"Customer Information: {customer_profile}"
    
    return {
        "system_prompt": system_prompt,
        "user_prompt": user_prompt
    }