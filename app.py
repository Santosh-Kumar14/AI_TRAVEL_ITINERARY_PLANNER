import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon=":airplane:")
st.title("AI Travel Itinerary Planner")
st.write("Plan your day trip itinerary by entering a city and your interests.")

with st.form("planner_form"):
    city = st.text_input("Enter the city you want to visit:", placeholder="e.g., Paris")
    interests = st.text_input("Enter your interests (comma-separated):", placeholder="e.g., art, history, food")
    submitted= st.form_submit_button("Generate Itinerary")

    if submitted:
        if city and interests:
            planner=TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary=planner.generate_itinerary()
            st.subheader("Your Itinerary")
            st.markdown(itinerary)
        else:
            st.warning("Please enter both city and interests to generate an itinerary.")
        