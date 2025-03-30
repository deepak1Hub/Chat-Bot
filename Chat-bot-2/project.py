import google.generativeai as genai


api_key = ""


if not api_key:
    raise ValueError("No API key")


genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-2.0-flash")

PROMPTS = {
    "movies": "You are an expert in recommending movies. Suggest some great {query} movies.",
    "education": "You are a knowledgeable tutor. Provide information on {query}.",
    "technology": "You are a tech expert. Explain {query} in detail.",
    "health": "You are a health and wellness advisor. Provide insights on {query}.",
    "business": "You are a business consultant. Share knowledge about {query}.",
    "sports": "You are a sports analyst. Discuss {query}.",
    "entertainment": "You are an entertainment expert. Talk about {query}.",
    "science": "You are a scientist. Explain {query}.",
    "travel": "You are a travel guide. Give recommendations for {query}.",
    "food": "You are a food expert. Suggest some great dishes related to {query}.",
    "society": "You are a social analyst. Provide insights on {query}.",
    "history": "You are a historian. Explain the significance of {query}.",
    "finance": "You are a finance expert. Provide tips on {query}.",
    "career": "You are a career counselor. Give guidance on {query}.",
    "AI": "You are an AI specialist. Explain {query} in simple terms.",
    "gaming": "You are a gaming expert. Recommend the best games for {query}.",
    "music": "You are a music expert. Suggest the best songs or artists for {query}.",
    "fashion": "You are a fashion stylist. Provide tips on {query}.",
    "general": "You are an AI assistant. Provide insights on {query}."
}


def get_category(query):
    keywords = {
        "movies": ["movie", "film", "cinema", "genre"],
        "education": ["study", "education", "learning", "course"],
        "technology": ["AI", "tech", "computer", "software", "hardware"],
        "health": ["health", "fitness", "diet", "medicine"],
        "business": ["business", "startup", "entrepreneur", "market"],
        "sports": ["sports", "football", "cricket", "NBA", "Olympics"],
        "entertainment": ["entertainment", "Hollywood", "Bollywood", "celebrity"],
        "science": ["science", "physics", "chemistry", "biology"],
        "travel": ["travel", "tourism", "vacation", "holiday"],
        "food": ["food", "cuisine", "recipe", "restaurant"],
        "society": ["society", "community", "social", "culture"],
        "history": ["history", "ancient", "past", "historical"],
        "finance": ["finance", "investment", "stock", "economy"],
        "career": ["career", "job", "profession", "resume"],
        "AI": ["artificial intelligence", "machine learning", "deep learning"],
        "gaming": ["game", "gaming", "video game", "eSports"],
        "music": ["music", "song", "artist", "album"],
        "fashion": ["fashion", "style", "clothing", "trends"]
    }
    
    for category, words in keywords.items():
        if any(word in query.lower() for word in words):
            return category
    return "general"


print("🤖 ChatBot: Hello! Ask me anything (Movies, Education, Tech, Health, etc.). Type 'exit' to stop.")

while True:
    user_input = input("💬 You: ").strip()

    if user_input.lower() == "exit":
        print("🤖 ChatBot: Goodbye! Have a great day! 🚀")
        break

    category = get_category(user_input)
    prompt = PROMPTS[category].format(query=user_input)

    response = model.generate_content(prompt)

    print(f"🤖 ChatBot ({category.capitalize()}): {response.text}\n")