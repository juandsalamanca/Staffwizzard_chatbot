import streamlit as st
from src.openai_models import *


st.header("Staffwizzard employee chatbot")

input = st.text_input("What do you need")

sensitive_word_list = ["401k", "PTO"]

if "input_memory" not in st.session_state:
  st.session_state.input_memory = ""

st.session_state.memory = []

if input and input  != st.session_state.input_memory:
  st.session_state.input_memory = input
  st.session_state.memory.append({"role": "user", "content": input})

def contains_any(string, word_list):
  word_set = set(word_list)  # Convert list to set for O(1) membership tests
  return any(word in string for word in word_set)

if contains_any(input, sensitive_word_list):
  model = employee_sensitive_info_chatbot
else:
  model = employee_info_chatbot



