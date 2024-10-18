# app.py

import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load the FLAN-T5 model and tokenizer
model_name = "google/flan-t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to generate a response from the model
def generate_response(prompt):
    # Encode the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate a response
    output = model.generate(input_ids, max_length=150, num_return_sequences=1, truncation=True)
    
    # Decode the generated response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Streamlit app
st.title("AI Chatbot")
st.subheader("Ask me anything about Artificial Intelligence!")

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Create the prompt for the model
    prompt = f"Explain the following: {user_input}"
    
    # Generate a response from the chatbot
    bot_response = generate_response(prompt)
    
    # Display the chatbot's response
    st.text_area("Chatbot:", bot_response, height=150)
