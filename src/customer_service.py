import json


customer_profiles=None
social_media_posts=None

with open("./data/customer_profile.json", "r") as file:
    customer_profiles = json.load(file)
    
with open("./data/non_contradictory_social_media_posts.json", "r") as file:
    social_media_posts = json.load(file)


def get_all_customer_data():
    return customer_profiles

def get_customer_profile(customer_id):
    """
    Retrieve and combine customer profile with social media data
    
    Args:
        customer_id: The ID of the customer to retrieve
        
    Returns:
        dict: Combined customer profile
    """
    
    # Find customer profile
    combined_profile = {}
    for profile in customer_profiles:
        if profile["CustomerID"] == customer_id:
            combined_profile = profile
            break
    
    # Add social media posts
    combined_profile["social_media"] = []
    for post in social_media_posts:
        if post["CustomerID"] == customer_id:
            combined_profile["social_media"].append(
                f"Platform: {post['Platform']} Post: {post['Post']}"
            )
    
    return combined_profile