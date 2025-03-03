import streamlit as st
from src.openai_models import *
from src.retriever import retrieve_info
import json
import numpy as np
from dotenv import load_dotenv

load_dotenv()

st.header("Staffwizard employee chatbot")

reset = st.button("Reset")
if reset:
    st.session_state.memory = []
    st.session_state.input_memory = ""
    st.session_state.sensitive_memory = []
    
input = st.chat_input(
    "Ask something...", 
    key="user_input"
)

if "info_embeddings" not in st.session_state:
    st.session_state.info_embeddings = np.load("data/info_embeddings.npy")
if "info_list" not in st.session_state:
    with open("data/info_list.json", "r") as f:
        st.session_state.info_list = json.load(f)
        
sensitive_word_list = ["401k", "PTO"]

if "input_memory" not in st.session_state:
    st.session_state.input_memory = ""

if "memory" not in st.session_state:
    st.session_state.memory = []

if "sensitive_memory" not in st.session_state:
    st.session_state.sensitive_memory = []

def contains_any(string, word_list):
    word_set = set(word_list)  # Convert list to set for O(1) membership tests
    return any(word in string for word in word_set)
        
if input:
    st.session_state.input_memory = input    
    info, sensitive_info = retrieve_info(input, st.session_state.info_embeddings, st.session_state.info_list)
    prompt = f"You need to answer what the user asks based on the following information: {info} the user says: {input}"
    st.session_state.memory.append({"role": "user", "content": prompt})
    sensitive = contains_any(input, sensitive_word_list)
    
    if sensitive:
        response = employee_sensitive_info_chatbot("gpt-4o-mini", st.session_state.memory, info)
        st.session_state.memory.append({"role": "assistant", "content": response})
        response += " "
        response += sensitive_info
    else:
        response = employee_info_chatbot("gpt-4o-mini", st.session_state.memory, info)
        st.session_state.memory.append({"role": "assistant", "content": response})

    st.session_state.sensitive_memory.append("")
    st.session_state.sensitive_memory.append(sensitive_info)

#st.write(st.session_state.sensitive_memory)
#st.write(st.session_state.memory)
for i, message in enumerate(st.session_state.memory):
    with st.chat_message(message["role"]):
        content = message["content"]
        if message["role"] == "user":
            idx = content.index("says:")
            content = content[idx+6:]
        st.markdown(content + st.session_state.sensitive_memory[i])
        
