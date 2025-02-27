import streamlit as st
from src.openai_models import *
from src.retriever import retrieve_info
import json

st.header("Staffwizzard employee chatbot")

def clear_text():
    st.session_state.user_input = ""

input = st.chat_input(
    "Ask something...", 
    key="user_input",
    on_submit=clear_text
)

if "info_embeddings" not in st.session_state:
    st.session_state.info_embeddings = np.load("data/info_embeddings.npy")
if "info_list" not in st.session_state:
    with open("data/info_list.json", "r") as f:
        st.session_state.info_list = json.load(f)
        
sensitive_word_list = ["401k", "PTO"]

if "input_memory" not in st.session_state:
  st.session_state.input_memory = ""

st.session_state.memory = []

if input and input != st.session_state.input_memory:
  st.session_state.input_memory = input
  st.session_state.memory.append({"role": "user", "content": input})

def contains_any(string, word_list):
  word_set = set(word_list)  # Convert list to set for O(1) membership tests
  return any(word in string for word in word_set)


sensitive = contains_any(input, sensitive_word_list)
if sensitive:
  info, sensitive_info = retrieve_info(input, st.session_state.info_embeddings, st.session_state.info_list)
  response = employee_sensitive_info_chatbot("gpt-4o-mini", st.session_state.memory, info)
  respons += "Here it is"
else:
  info, sensitive_info = retrieve_info(input, st.session_state.info_embeddings, st.session_state.info_list)
  response = employee_info_chatbot("gpt-4o-mini", st.session_state.memory, info)


response = model("gpt-4o-mini, st.session_state.memory, info)
st.session_state.memory.append({"role": "user", "assistant": response})
