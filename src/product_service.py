import json
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine


products=None

product_file_path="./data/products.json"
with open(product_file_path, "r") as file:
    products = json.load(file)
            

def get_all_product_data():
    return products


class ProductRecommender:
    """
    A class to handle product recommendations using vector similarity
    """
    def __init__(self, model_name='multi-qa-MiniLM-L6-cos-v1'):
        self.model = SentenceTransformer(model_name)
        self.product_vectors = []
        self.products_loaded = False
        
    def load_products(self, file_path="./data/products.json"):
        """
        Load and vectorize products from a JSON file
        
        Args:
            file_path: Path to the JSON file containing products
        """

        self.product_vectors = []
        for product in products:
            text = product["description"] + " #### " + product["features"]
            vector = self.model.encode(text)
            self.product_vectors.append({
                "Product_Name": product["name"],
                "Product_Category": product["category"],
                "Product_Vector": vector
            })
        
        self.products_loaded = True
        
    def get_recommendations(self, text, top_k=3):
        """
        Get product recommendations based on text similarity
        
        Args:
            text: Text to compare products against
            top_k: Number of top recommendations to return
            
        Returns:
            list: Top product recommendations
        """
        if not self.products_loaded:
            self.load_products()
            
        # Vectorize the input text
        text_vector = self.model.encode(text)
        
        # Calculate product_similarity
        product_similarity=[]
        
        for product in self.product_vectors:
            similarity = self._cosine_similarity(text_vector, product["Product_Vector"])
            similarity = (similarity+1)/2.0
            product_similarity.append({
                "Product_Name": product["Product_Name"],
                "Product_Category": product["Product_Category"],
                "Similarity": str(similarity)
            })
        
        # Sort by similarity and get top k
        top_recommendations = sorted(
            product_similarity, 
            key=lambda x: float(x["Similarity"]), 
            reverse=True
        )[:top_k]
        #products_sentiment = self.product_sentiment(product_similarity)
        top_5_recommendations = sorted(
            product_similarity, 
            key=lambda x: float(x["Similarity"]), 
            reverse=True
        )[:5]
        bottom_5_recommendations=sorted(
            product_similarity, 
            key=lambda x: float(x["Similarity"]), 
            reverse=False
        )[:5]
        
        return {"top_recommendations":top_recommendations,
                "product_sentiment":top_5_recommendations+bottom_5_recommendations
                }
                

    def _cosine_similarity(self, vec1, vec2):
        """
        Calculate cosine similarity between two vectors
        
        Args:
            vec1: First vector
            vec2: Second vector
            
        Returns:
            float: Similarity score (0-1)
        """
        return 1 - cosine(vec1, vec2)

# Create a singleton instance
_recommender = None

def get_recommended_products(text):
    """
    Get product recommendations based on text
    
    Args:
        text: Text describing customer needs
        
    Returns:
        list: Recommended products
    """
    global _recommender
    if _recommender is None:
        _recommender = ProductRecommender()
    
    return _recommender.get_recommendations(text)
