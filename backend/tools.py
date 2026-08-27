from ollama import chat

SYSTEM_PROMPT = """
You are MedGemma, a safe and supportive AI medical assistant.

Rules:
- Do not provide dangerous medical advice
- Do not claim to be a licensed doctor
- Encourage professional medical help
- Give concise and safe responses
"""

# ---------------- QUERY FUNCTION ---------------- #

def query_medgemma(prompt: str) -> str:

    response = chat(

        model="nemotron-3-super:cloud",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        options={
            "temperature": 0.6,
            "top_p": 0.9,
            "num_predict": 350
        }
    )

    return response.message.content


from twilio.rest import Client

from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
    EMERGENCY_NUMBER
)

# ---------------- EMERGENCY TOOL ---------------- #

def emergency_alert(user_message: str) -> str:

    try:

        client = Client(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN
        )

        message = client.messages.create(

            body=(
                "🚨 SafeSpace Emergency Alert\n\n"
                f"Detected Message:\n{user_message}"
            ),

            from_=TWILIO_FROM_NUMBER,

            to=EMERGENCY_NUMBER
        )

        return (
            "Emergency alert sent successfully."
        )

    except Exception as e:

        return f"Twilio Error: {str(e)}"
    
# ---------------- EXPERT FINDER TOOL ---------------- #

def find_medical_expert(location: str) -> dict:

    demo_database = {

        "mumbai": {
            "doctor": "Dr. Ananya Sharma",
            "specialization": "Psychiatrist",
            "hospital": "Apollo Hospital Mumbai",
            "contact": "+91 9876543210"
        },

        "delhi": {
            "doctor": "Dr. Raj Mehta",
            "specialization": "Clinical Psychologist",
            "hospital": "AIIMS Delhi",
            "contact": "+91 9123456780"
        },

        "bangalore": {
            "doctor": "Dr. Priya Nair",
            "specialization": "Mental Health Specialist",
            "hospital": "Manipal Hospital",
            "contact": "+91 9988776655"
        }
    }

    location = location.lower().strip()

    if location in demo_database:

        expert = demo_database[location]

        return {
            "status": "success",
            "doctor": expert["doctor"],
            "specialization": expert["specialization"],
            "hospital": expert["hospital"],
            "contact": expert["contact"]
        }

    return {
        "status": "not_found",
        "message": f"No expert found for {location}"
    }

# ---------------- TEST ---------------- #
if __name__ == "__main__":

    response = emergency_alert(
        "I want to harm myself."
    )

    print(response)