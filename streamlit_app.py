import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me!",
    icon="🥼",
    default=True
)

project_1_page = st.Page(
    "views/stats_chatbot.py",
    title="Stats Chatbot",
    icon="🧮"
)

project_2_page = st.Page(
    "views/testimonial_generator.py",
    title="Testimonial Generator",
    icon="📝"
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Personal Projects": [project_1_page],
        "School Tools" : [project_2_page]
    }
)

# --- SHARED ON ALL PAGES ---
#st.success("Personal Profile and Porfolio!")
st.sidebar.text("Made with ❤️ by Clarence Wong")

# --- RUN NAVIGATION ---
pg.run()