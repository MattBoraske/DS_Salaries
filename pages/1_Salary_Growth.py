import pandas as pd
import streamlit as st
import plotly.express as px

def formatSalary(salary):
    return str(salary // 1000) + "k"

st.set_page_config(
    page_title="Salary Growth",
    page_icon="💵"
)

#page header
page_header = "Salary Growth"
st.write("<div align='center'><h1>" + page_header + "</h1></div>", unsafe_allow_html=True)

#read in data science salary data
df = pd.read_csv("data/ds_salaries.csv")

#remove outliers by dropping rows with salaries not in USD
df_filtered = df[df["salary_currency"] == "USD"]

#present average salary for each experience level
avg_salary = df_filtered.groupby("experience_level")["salary"].mean().reset_index()
avg_salary["salary"] = avg_salary["salary"].astype(int)
avgSalariesString = "$" + formatSalary(avg_salary["salary"][0]) + " 👉 $" + formatSalary(avg_salary["salary"][2]) + " 👉 $" + formatSalary(avg_salary["salary"][3]) + " 👉 $" + formatSalary(avg_salary["salary"][1])
styled_text = f"<div style='text-align: center; font-size: 24px; font-weight: bold;'>{avgSalariesString}</div>"
st.write(styled_text, unsafe_allow_html=True)

#box-and-whisker plot of salaries by experience level
experience_order = ["EN", "MI", "SE", "EX"]
experience_labels = ["Entry Level", "Mid-Career", "Senior", "Executive"]
fig = px.box(df_filtered, x="experience_level", y="salary", category_orders={"experience_level": experience_order}, labels={"experience_level": "Experience Level", "salary": "Salary (USD)"}, color_discrete_sequence=["#636EFA"])
fig.update_xaxes(
    categoryorder="array",
    categoryarray=experience_order,
    ticktext=experience_labels,
    tickvals=experience_order)
st.plotly_chart(fig)

#print max and min salary in filtered df for each experience level
st.write("Max and min salary in filtered dataframe for each experience level:")
st.write(df_filtered.groupby("experience_level")["salary"].agg(["max", "min"]))
