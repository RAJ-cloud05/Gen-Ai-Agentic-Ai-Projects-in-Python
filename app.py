# PERSONAL CHATBOT USING OLLAMA MODEL GEMMA4:LATEST 
# RUN BY cd ollama_streamlit
# streamlit run app.py



import streamlit as st
from ollama import Client 



client= Client(host="http://localhost:11434")

st.set_page_config(
    page_title="CUSTOM LLM MODEL BY RAJ VISHWAKARMA",
    layout="centered"

)
st.title("RAJ VISHWAKARMA - OLLAMA APP")

prompt = st.text_area("ENTER THE PROMPT:", height=200)

if st.button("GENERAE RESPOSNSE"):
    if  prompt.strip() == "gemma4:latest":
        st.warning("please enter a prompt")
    else:
        with st.spinner("THINKING..."):
            response= client.chat(
                model="gemma4:latest",
                messages=[{"role":"user",  "content":prompt}]

            )

            st.success("RESPONSE GENERATED!")
            st.write(response["message"]["content"])
            