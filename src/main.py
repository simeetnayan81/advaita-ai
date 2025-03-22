from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
import openai
import json
from vectorizing import getRecommendedProducts 


load_dotenv()

# client = openai.OpenAI(
#     api_key=os.environ.get("SAMBANOVA_API_KEY"),
#     base_url="https://api.sambanova.ai/v1",
# )

app = FastAPI()


with open("../data/updated_customer_profile.json", "r") as file:
    customer_profile = json.load(file)  # Load JSON content as a Python dictionary

with open("../data/non_contradictory_social_media_posts.json", "r") as file:
    social_media = json.load(file)  # Load JSON content as a Python dictionary

cus = "AlisonGaines78"

combined_profile = {}
for c in customer_profile:
    if c["CustomerID"] == cus:
        combined_profile = c

combined_profile["social_media"] = []

for sm in social_media:
    if sm["CustomerID"] == cus:
        combined_profile["social_media"].append("Platform: " + sm["Platform"] + " Post: "+sm["Post"])


prompt = f""" You are a professional data analyst at a bank. You have been provided with detailed customer information.
Analyze the following customer data and provide descriptive summary of customer profile and insights into their financial needs, opportunities for product offerings. Output should be a JSON in the below format:

    {{
        "profile_summary": "summary of customer profile. Should be in one paragraph",
        "product_offering": "financial needs and product preferences. Should be in one paragraph"
    }}
    Only give the json format only. Don't give any other response.
"""

user_prompt= f"""Customer Information: {combined_profile}"""


# @app.get("/")
# async def root():
    # response = client.chat.completions.create(
    # model="Meta-Llama-3.1-70B-Instruct",
    # messages=[{"role":"system","content":prompt},{"role":"user","content":user_prompt}],
    # temperature=0.1,
    # top_p=0.1)
    # #output ="**Customer Analysis: Alison Gaines**\n\n### Overview\n\nAlison Gaines is a 32-year-old female customer from Jacksonville, United States. She has an active account with a current balance of $36,867.07 and a low-risk profile.\n\n### Financial Needs\n\nBased on the data, Alison's financial needs can be summarized as follows:\n\n1. **Travel and Luxury**: Alison frequently uses her credit card for travel-related transactions and has expressed interest in luxury stays. She may be interested in premium travel credit cards or loyalty programs that offer exclusive benefits.\n2. **Digital Wallets**: Alison has mentioned using digital wallets for better deals on luxury stays, indicating a preference for convenient and cost-effective payment methods.\n3. **Investment and Retirement**: Alison's social media posts suggest that she is interested in investing in lifestyle and retiring comfortably. She may be a potential candidate for investment products or retirement planning services.\n4. **Travel Coverage**: Alison has emphasized the importance of travel coverage, indicating a need for insurance products that provide protection against unexpected events while traveling.\n\n### Potential Risks\n\n1. **Over-Reliance on Credit**: Alison's high average monthly spending and frequent use of credit cards may indicate a risk of over-reliance on credit. The bank may want to monitor her credit usage and offer guidance on responsible credit management.\n2. **International Transactions**: Alison has a high international transaction indicator, which may pose a risk of foreign exchange fluctuations or potential fraud. The bank may want to offer her foreign exchange services or monitor her international transactions closely.\n\n### Opportunities for Product Offerings\n\n1. **Premium Travel Credit Cards**: The bank may consider offering Alison a premium travel credit card with exclusive benefits, such as travel insurance, airport lounge access, or loyalty rewards.\n2. **Digital Wallet Solutions**: The bank may want to promote its digital wallet solutions to Alison, highlighting the convenience, security, and cost-effectiveness of these payment methods.\n3. **Investment and Retirement Products**: The bank may consider offering Alison investment products or retirement planning services that align with her interests and financial goals.\n4. **Travel Insurance**: The bank may want to offer Alison travel insurance products that provide protection against unexpected events while traveling, such as trip cancellations, medical emergencies, or luggage loss.\n\n### Recommendations\n\n1. **Personalized Marketing**: The bank may want to create personalized marketing campaigns that cater to Alison's interests and financial needs, such as offering premium travel credit cards or digital wallet solutions.\n2. **Financial Advisory Services**: The bank may consider offering Alison financial advisory services to help her manage her credit usage, invest in lifestyle, and plan for retirement.\n3. **Risk Management**: The bank may want to monitor Alison's credit usage and international transactions closely to mitigate potential risks and offer guidance on responsible credit management and foreign exchange services.\n\nBy analyzing Alison's customer data, the bank can gain valuable insights into her financial needs, potential risks, and opportunities for product offerings. By tailoring its services and marketing efforts to Alison's unique profile, the bank can strengthen its relationship with her and increase customer loyalty."
    # output = response.choices[0].message.content
    # print(output)
    # parsedOutput = json.loads(output)
    # print(parsedOutput)
    # reccomendedProducts = getRecommendedProducts(parsedOutput["product_offering"])
    # return reccomendedProducts
    # return {"message": json.dumps(response.choices[0].message.content)}



