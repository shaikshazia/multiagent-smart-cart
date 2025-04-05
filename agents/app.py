# app.py

import streamlit as st
from agents.recommender_agent import RecommenderAgent
from agents.review_agent import ReviewAgent

st.set_page_config(page_title="Multi-Agent Smart Cart", layout="wide")

st.title("🛒 Smart Shopping with Gen AI & Multi-Agent Architecture")

# Input for product
product = st.text_input("Enter a product name", "wireless earbuds")

# Recommender Agent
st.subheader("🔎 Recommendations")
rec_agent = RecommenderAgent()
recommendations = rec_agent.recommend(product)
st.write(recommendations)

# Input for reviews
st.subheader("📝 Review Sentiment Analysis")
user_reviews = st.text_area("Paste some customer reviews (one per line)", "Excellent battery life\nNot great sound quality")
review_list = user_reviews.split("\n")
review_agent = ReviewAgent(review_list)
sentiments = review_agent.analyze_sentiment()

for i, sentiment in enumerate(sentiments):
    st.write(f"**Review:** {review_list[i]}")
    st.write(f"Sentiment: *{sentiment}*")
    st.markdown("---")
