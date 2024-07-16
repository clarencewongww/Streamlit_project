import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me!",
    icon="🥼",
    default=True,
)

project_0_page = st.Page(
    "views/testing_page.py",
    title = "Project 0",
    icon="🧪"
)
project_1_page = st.Page(
    "views/stats_chatbot.py",
    title="Stats Chatbot",
    icon="🧮"
)
project_2_page = st.Page(
    "views/project_2.py",
    title="Project 2",
    icon="2️⃣"
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
        "Personal tools": [project_0_page]
    }
)


# --- SHARED ON ALL PAGES ---
#st.success("Personal Profile and Porfolio!")
st.sidebar.text("Made with ❤️ by Clarence Wong")


# --- RUN NAVIGATION ---
pg.run()