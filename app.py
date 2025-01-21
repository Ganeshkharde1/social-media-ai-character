import streamlit as st
import os
from groq import Groq

# Initialize Groq API Client
client = Groq(api_key="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")  # Replace with your API key

# Fixed AI Character Profile
character_profile = {
    "name": "Ramesh",
    "age": 25,
    "location": "Mumbai, India",
    "profession": "AI Researcher & Digital Artist also a college student",
    "interests": ["Cyberpunk", "AI Ethics", "Gaming", "Photography", "food"],
    "personality": "Witty, Curious, Tech-Savvy",
    "posting_preferences": {
        "text": 40,
        "image": 30,
        "video": 20,
        "audio": 10
    }
}



left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("img.png",width=200)

st.title("AI Character Social Media Post Generator 🤖")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.write("Bhabha AI python ai intern task")

# User Inputs
st.sidebar.subheader("Stimulate the external parameters")
time_of_day = st.sidebar.text_input("Enter Time of Day (e.g., 08:00 AM)", "08:00 AM")
routine = st.sidebar.text_input("Enter Routine (e.g., Morning Coffee)", "Morning Coffee")
mood = st.sidebar.selectbox("Select Mood", ["Happy", "Motivated", "Thoughtful", "Excited", "Relaxed"])
weather = st.sidebar.text_input("Enter Weather Condition (e.g., Sunny)", "Sunny")
trending_topics = st.sidebar.text_area("Trending Topics (comma-separated)", "AI in Healthcare, SpaceX Mars Mission")
breaking_news = st.sidebar.text_input("Breaking News", "OpenAI launches new AI model")

# Button to Generate Post
if st.button("Generate Post"):
    # Prepare Prompt
    prompt = f"""
    Act as {character_profile['name']}, a {character_profile['age']}-year-old {character_profile['profession']} in {character_profile['location']}.
    You are {character_profile['personality']}. Your interests include {', '.join(character_profile['interests'])} .
    
    you have to behave like realistic human, who have your own characteristics. you are dynamic and as close to general human behaviour as possible i.e. 
    character would live in some part of the world, eat specific foods, have daily routines, maybe studying in college or doing some professional work, etc. 
    Right now, it is {time_of_day}, and you are engaged in {routine}. 
    Your mood is {mood}, and the weather outside is {weather}.

    Trending topics: {trending_topics}
    Breaking News: {breaking_news}

    Generate a social media post based on this context. Keep the tone engaging and aligned with your personality.
    """

    # Call LLM API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI character generating social media posts."},
            {
                "role": "user",
                "content": prompt}],

        model="llama3-70b-8192",
    )

    # Display Generated Post
    generated_post = chat_completion.choices[0].message.content
    st.subheader("Generated Post:")
    st.write(generated_post)

    platform = st.selectbox("Select platform", ["Instagram", "LinkedIn", "Twitter", "Whatsapp"])
    if st.button("Post on social Media"):
        st.write("Feature coming soon", icon="🚀")


