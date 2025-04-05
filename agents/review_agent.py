# agents/review_agent.py

class ReviewAgent:
    def __init__(self, reviews):
        self.reviews = reviews

    def analyze_sentiment(self):
        # Dummy logic: count positive words
        sentiments = []
        for review in self.reviews:
            if "good" in review.lower() or "excellent" in review.lower():
                sentiments.append("Positive")
            else:
                sentiments.append("Neutral/Negative")
        return sentiments

# Example usage
if __name__ == "__main__":
    reviews = ["Excellent quality!", "Not worth the price", "Good battery life"]
    agent = ReviewAgent(reviews)
    print("Sentiment:", agent.analyze_sentiment())
