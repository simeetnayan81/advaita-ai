from sentence_transformers import SentenceTransformer
import json
import numpy as np
from scipy.spatial.distance import cosine


model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')  
product_vector =[]
similarity =[]
   
def cosine_similarity(vec1, vec2):
    return 1 - cosine(vec1, vec2)


def vectoriseProductOfferings(product_offerings):
    return model.encode(product_offerings)

def createProductsVector():
    if(len(product_vector)==0):
        with open("../data/products.json", "r") as file:
            products = json.load(file) 
        for p in products:
            text = p["description"] + " #### " + p["features"]
            vectoriseProduct = model.encode(text)
            product_vector.append(
                {
                    "Product_Name" : p["name"],
                    "Product_Category" : p["category"],
                    "Product_Vector" : vectoriseProduct

                }
            )


def calculateSimilarity(productOfferingVector):
    for p in product_vector:
        s = cosine_similarity(productOfferingVector, p["Product_Vector"])
        similarity.append(
            {
            "Product_Name" : p["Product_Name"],
            "Product_Category" : p["Product_Category"],
            "Similarity" : str(s)
            }
        )    
    top_3_similar = sorted(similarity, key=lambda x: float(x["Similarity"]), reverse=True)[:3]    
    return top_3_similar


def getRecommendedProducts(paragraph):
    productOfferingVector = vectoriseProductOfferings(paragraph)

    if(len(product_vector)==0):
        createProductsVector()

    return calculateSimilarity(productOfferingVector)    




