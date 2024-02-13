import streamlit as sl
from openai import OpenAI
import os

sl.title("API Tester")
sl.header("Check different LLM API calls") 

sl.write("Select a LLM (only gpt-3.5-turbo-0125 is available for now):")

selectbox = sl.selectbox("Select a LLM",
                        options=["GPT-4", "GPT-4 Turbo", "GPT-3.5 Turbo", "CohereNow", "BedrockAWS", "AnthropicSimple", "Other"],
                        key="llm_selectbox",
                        on_change=None)

if selectbox == "GPT-3.5 Turbo":
    client = OpenAI()

    user_message = sl.text_input(f"Ask something to {selectbox}")


    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": user_message}
    ]
    )

    sl.write(f"""The response is:
             
             {response.choices[0].message.content}""")
    sl.write(f"Tokens used: {response.usage.total_tokens}")
    sl.write(f"Price of this call: ${(response.usage.prompt_tokens * 0.0000005) + (response.usage.completion_tokens * 0.0000015)}")

## Upload file
