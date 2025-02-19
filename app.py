# -*- coding: utf-8 -*-
"""Task Time-Traveler.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lXiRr_IBL9XObV-gOAi2kPjD1l-QsVbY
"""

--!pip install ag2[captainagent] -q



--!pip install streamlit openai

from google.colab import drive
drive.mount('/content/drive')

import streamlit as st
import openai
# Streamlit app layout
st.title("Task Time-Traveler")
# from config import OPENAI_API_KEY

import os



# User inputs
task_description = st.text_input("Enter the task description:")
due_date = st.date_input("Enter the due date:")
importance = st.selectbox("Select the importance level:", ["High", "Medium", "Low"])
visualization_style = st.selectbox("Select the visualization style:", ["Humorous", "Dramatic", "Realistic"])



from google.colab import userdata
# OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

--!pip install dask[dataframe] -q

from autogen.agentchat.contrib.captainagent import CaptainAgent
from autogen import UserProxyAgent

import os

config_list = [
    {
        "model": "gpt-4o-mini",
        "api_key": userdata.get('OPENAI_API_KEY')
    }
]

llm_config = {
    "temperature": 0,
    "config_list": config_list
}

from autogen.agentchat.contrib.captainagent import CaptainAgent

captain_agent = CaptainAgent(
    name="captain_agent",
    llm_config=llm_config,
    code_execution_config={"use_docker": False, "work_dir": "task_time_traveler"}
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER"
)

def task_time_traveler(task_description, due_date, importance, visualization_style):
    prompt = f"""
    Task: {task_description}
    Due Date: {due_date}
    Importance: {importance}

    Generate two scenarios:
    1. If the task is completed today.
    2. If the task is delayed or avoided.

    Visualization Style: {visualization_style}

    Provide vivid, personalized narratives for both scenarios.
    """

    result = user_proxy.initiate_chat(captain_agent, message=prompt)
    return result

# Generate scenarios on button click
if st.button("Generate Scenarios"):
        scenarios = task_time_traveler(task_description, due_date, importance, visualization_style)
        st.subheader("Generated Scenarios:")
        st.write(scenarios)

task_description = "Complete the project report"
due_date = "2024-12-31"
importance = "High"
visualization_style = "Humorous"

scenarios = task_time_traveler(task_description, due_date, importance, visualization_style)
print(scenarios)
