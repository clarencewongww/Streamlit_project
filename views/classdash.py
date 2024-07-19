import pandas as pd
import numpy as np 
import streamlit as st 

st.header("Class Duty Dashboard")

col1, col2 = st.columns([4,2], gap = "small", vertical_alignment="center")

with col1:
    with st.expander("See roles for duty"):
        tab1, tab2, tab3 = st.tabs(["Wipe All Board", "Clear Bins", "Sweep Floor (Two Students)"])

    with tab1:
        st.write("Student will use duster to clean all non-pernanent writings on ALL board. Permanent writing includes detials on events and exams.")

    with tab2:
        st.write("Clear bins from the class by emptying into main bin outside of the classroom. Ensure that bins are clear during every class break (eg. recess & lunch)")

    with tab3:
        st.write("Use the broom and dustpan to sweep up any dirt on the floor and pick up all litter. Loose paper and other artifacts should be collected and placed on the shelving at the side of the classroom as well. ")

# function for updating daily rating 
def update_rating(floor_rate, board_rate, bin_rate):
    print(floor_rate,board_rate, bin_rate)

with col2: 
    with st.expander("View / Rate Duty"):
        tab4, tab5 = st.tabs(["View Duty", "Rate Duty"])
    with tab4:
        selected_filter = st.selectbox("Select Duty to Display:", ("Odd Monday", "Odd Tuesday", "Odd Wednesday", "Odd Thursday", "Odd Friday", "Even Monday", "Even Wednesday", "Even Thursday", "Even Friday"), index = 0)
    with tab5:
        floor_rating = st.number_input("Rating for Floor", 1, 5, 3)
        board_rating = st.number_input("Rating for Board", 1, 5, 3)
        bin_rating = st.number_input("Rating for Bin", 1, 5, 3)
        st.button("Submit Daily Rating", on_click=update_rating, args=(floor_rating, board_rating, bin_rating))


# display the filtered duty dataframe
c = st.empty()
duty_list = pd.read_csv("./assets/duty_list.csv")
filtered_list = duty_list[duty_list["duty_slot"] == selected_filter]
c.dataframe(filtered_list)

duty_rating = pd.read_excel("./assets/duty_rating.xlsx")

#print(duty_rating)