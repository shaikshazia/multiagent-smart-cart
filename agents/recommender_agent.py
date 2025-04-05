# agents/recommender_agent.py

class RecommenderAgent:
    def __init__(self, products_db):
        self.products = products_db

    def recommend(self, user_profile):
        # Dummy logic: recommend first 3 items
        return self.products[:3]

# Example usage
if __name__ == "__main__":
    products = ["Shoes", "Bag", "Watch", "Headphones"]
    user = {"interests": ["fashion", "gadgets"]}
    agent = RecommenderAgent(products)
    print("Recommended:", agent.recommend(user))
