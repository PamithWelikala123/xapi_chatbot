import openai
import streamlit as st
from dotenv import load_dotenv
import os
import shelve



load_dotenv()

st.title("Streamlit Chatbot Interface")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

st.write("""
# My first app
Hello *world!*
""")