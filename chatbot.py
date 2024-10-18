import streamlit as st

# Function to generate responses based on user input
def get_health_response(user_input):
    user_input = user_input.lower()
    
    if "symptoms" in user_input:
        return "Common symptoms include fever, cough, fatigue, and shortness of breath. Please consult a healthcare professional for more information."
    elif "headache" in user_input:
        return "Headaches can be caused by stress, dehydration, or tension. It's best to rest and stay hydrated. If it persists, see a doctor."
    elif "fever" in user_input:
        return "A fever is a common sign of infection. Monitor your temperature and consult a doctor if it exceeds 101°F (38.3°C) or lasts longer than three days."
    elif "cold" in user_input or "flu" in user_input:
        return "Rest, drink plenty of fluids, and consider over-the-counter medication. If symptoms worsen, seek medical advice."
    elif "exercise" in user_input:
        return "Regular exercise can improve your overall health. Aim for at least 150 minutes of moderate aerobic activity each week."
    elif "diet" in user_input:
        return "A balanced diet includes fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit processed foods and sugars."
    elif "mental health" in user_input:
        return "It's important to take care of your mental health. Consider talking to a mental health professional if you're feeling overwhelmed."
    elif "bye" in user_input:
        return "Goodbye! Stay healthy and take care."
    else:
        return "I'm not sure how to respond to that. Please ask about symptoms, exercise, diet, or mental health."

# Streamlit app
st.title("🏥 Healthcare Chatbot")

# User input
user_input = st.text_input("You: ", "")

# Generate response
if user_input:
    response = get_health_response(user_input)
    st.write(f"Chatbot: {response}")
