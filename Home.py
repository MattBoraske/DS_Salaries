import streamlit as st 
import pandas as pd

def run():
    st.set_page_config(
        page_title="2023 Data Science Salaries",
        page_icon=":bar_chart:"
    )

    st.write("# 2023 Data Science Salaries 📊")

    st.markdown(
        """
        This Streamlit app was built by Matt Boraske.
        """
    )

    #read in data
    df = pd.read_csv("data/ds_salaries.csv")
    st.dataframe(df)

if __name__ == "__main__":
    run()
