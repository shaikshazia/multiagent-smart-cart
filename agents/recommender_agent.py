# agents/recommender_agent.py
import streamlit as st

class RecommenderAgent:
    def __init__(self, products_db):
        self.products = products_db

    def recommend(self, user_profile):
        # Filter products based on user interests
        filtered_products = [product for product in self.products if any(interest.lower() in product.lower() for interest in user_profile['interests'])]
        
        # Dummy logic: recommend first 3 filtered products
        return filtered_products[:3]

# Streamlit UI
st.title("🛒 Multi-Agent Smart Cart Recommender")
st.write("Enter your interests and get product recommendations:")

# Sample product database
products = ["Shoes", "Bag", "Watch", "Headphones", "Sunglasses", "Wallet", "Perfume"]

# User input
interests = st.text_input("What are your interests? (e.g., fashion, gadgets)")

if not interests:
    st.write("Please enter your interests to get recommendations.")
else:
    user = {"interests": interests.split(",")}
    agent = RecommenderAgent(products)
    recommendations = agent.recommend(user)
    
    if recommendations:
        st.subheader("🔮 Recommended Products:")
        for item in recommendations:
            st.write(f"- {item}")
    else:
        st.write("Sorry, no products found based on your interests.")
    
    # Option to clear input
    if st.button("Clear"):
        interests = ""
