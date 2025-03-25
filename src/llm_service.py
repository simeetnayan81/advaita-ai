import json

def generate_customer_analysis(client, prompts):
    """
    Generate customer analysis using LLM
    
    Args:
        client: The OpenAI client
        prompts: Dict containing system_prompt and user_prompt
        
    Returns:
        dict: Parsed JSON response
    """
    response = client.chat.completions.create(
        model="Meta-Llama-3.1-70B-Instruct",
        messages=[
            {"role": "system", "content": prompts["system_prompt"]},
            {"role": "user", "content": prompts["user_prompt"]}
        ],
        temperature=0.1,
        top_p=0.1
    )
    
    # Parse the response
    output = response.choices[0].message.content
    # Remove JSON code fence markers if present
    cleaned_output = output
    if output.startswith("```json"):
        cleaned_output = output[7:-3]  # Remove ```json and ``` 
    elif output.startswith("```"):
        cleaned_output = output[3:-3]  # Remove ``` and ```
        
    return json.loads(cleaned_output)
def get_product_suggestions(client,prompts):
    response = client.chat.completions.create(
        model="Meta-Llama-3.1-70B-Instruct",
        messages=[
            {"role": "system", "content": prompts["system_prompt"]},
            {"role": "user", "content": prompts["user_prompt"]}
        ],
        temperature=0.1,
        top_p=0.1
    )
    
    # Parse the response
    output = response.choices[0].message.content
    # Remove JSON code fence markers if present
    cleaned_output = output
    if output.startswith("```json"):
        cleaned_output = output[7:-3]  # Remove ```json and ``` 
    elif output.startswith("```"):
        cleaned_output = output[3:-3]  # Remove ``` and ```
        
    return json.loads(cleaned_output)

def generate_product_recommendations(client, analysis, recommended_products):
    """
    Generate detailed product recommendations using LLM
    
    Args:
        client: The OpenAI client
        analysis: Customer analysis result
        recommended_products: List of recommended products
        
    Returns:
        dict: Detailed product recommendations
    """
    prompt = f"""
    As a professional financial advisor at a bank, I have given these recommendation. 
    Your goal is to provide tailored reasons for why these products are best for the customer. 
    Output should be strictly a JSON only in the format:
    {{
      "Products": [{{
          "Product_Name": "product name",
          "Reason": "Reason"
      }}...]
    }}
    
    Customer Analysis: {analysis}
    Available Products: {recommended_products}
    """
    
    response = client.chat.completions.create(
        model="Meta-Llama-3.1-70B-Instruct",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        top_p=0.1
    )
    
    # Parse the response
    output = response.choices[0].message.content
    # Remove JSON code fence markers if present
    cleaned_output = output
    if output.startswith("```json"):
        cleaned_output = output[7:-3]  # Remove ```json and ```
    elif output.startswith("```"):
        cleaned_output = output[3:-3]  # Remove ``` and ```
        
    return json.loads(cleaned_output)
