# agents/recommender_agent.py

import streamlit as st

class RecommenderAgent:
    def __init__(self, products_db):
        self.products = products_db

    def recommend(self, user_profile):
        # Dummy logic: recommend first 3 items
        return self.products[:3]

# Streamlit UI
st.title("🛒 Multi-Agent Smart Cart Recommender")
st.write("Enter your interests and get product recommendations:")

# Sample product database
products = ["Shoes", "Bag", "Watch", "Headphones", "Sunglasses", "Wallet", "Perfume"]

# User input
interests = st.text_input("What are your interests? (e.g., fashion, gadgets)")

if interests:
    user = {"interests": interests.split(",")}
    agent = RecommenderAgent(products)
    recommendations = agent.recommend(user)
    
    st.subheader("🔮 Recommended Products:")
    for item in recommendations:
        st.write(f"- {item}")
