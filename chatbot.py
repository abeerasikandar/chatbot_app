import streamlit as st

# Function to generate responses based on user input
def get_heart_health_response(user_input):
    user_input = user_input.lower()
    
    if "symptoms" in user_input:
        return ("Common symptoms of heart problems include:\n"
                "- Chest pain or discomfort\n"
                "- Shortness of breath\n"
                "- Dizziness or lightheadedness\n"
                "- Fatigue\n"
                "If you experience these, please consult a healthcare professional immediately.")
    
    elif "treatment" in user_input:
        return ("Treatment options for heart problems may include:\n"
                "- Medications (e.g., beta-blockers, ACE inhibitors)\n"
                "- Lifestyle changes (diet, exercise)\n"
                "- Surgical procedures (e.g., angioplasty, bypass surgery)\n"
                "Consult your doctor for a personalized treatment plan.")
    
    elif "exercise" in user_input:
        return ("Recommended exercises for heart health include:\n"
                "- Walking: Aim for at least 30 minutes a day.\n"
                "- Cycling: A great way to improve cardiovascular fitness.\n"
                "- Swimming: Low-impact exercise that's easy on the joints.\n"
                "- Strength training: Incorporate this 2 days a week.\n"
                "Always consult with your healthcare provider before starting a new exercise program.")
    
    elif "diet" in user_input:
        return ("Heart-healthy dietary recommendations include:\n"
                "- Eat plenty of fruits and vegetables.\n"
                "- Choose whole grains over refined grains.\n"
                "- Limit saturated fats and trans fats.\n"
                "- Reduce sodium intake.\n"
                "- Include lean proteins such as fish and legumes.")
    
    elif "stress" in user_input:
        return ("Managing stress is crucial for heart health. Here are some tips:\n"
                "- Practice mindfulness or meditation.\n"
                "- Engage in physical activity.\n"
                "- Ensure adequate sleep.\n"
                "- Connect with friends and family for support.")
    
    elif "bye" in user_input:
        return "Goodbye! Stay healthy and take care of your heart."
    
    else:
        return "I'm not sure how to respond to that. Please ask about symptoms, treatment, exercise, or diet related to heart health."

# Streamlit app
st.title("❤️ Heart Health Chatbot")

# User input
user_input = st.text_input("You: ", "")

# Generate response
if user_input:
    response = get_heart_health_response(user_input)
    st.write(f"Chatbot: {response}")
