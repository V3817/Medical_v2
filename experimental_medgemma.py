import os
import requests

# ---------------- CONFIG ---------------- #

HF_TOKEN = os.getenv(
    "HF_TOKEN"
)  # Set your Hugging Face API token here    

API_URL = (
    "https://router.huggingface.co/v1/"
    "chat/completions"
)

headers = {

    "Authorization": f"Bearer {HF_TOKEN}",

    "Content-Type": "application/json"
}

# ---------------- QUERY FUNCTION ---------------- #

def query_medgemma(prompt: str):

    payload = {

        "messages": [

            {
                "role": "system",

                "content": (
                    "You are MedGemma, "
                    "a safe medical AI assistant."
                )
            },

            {
                "role": "user",

                "content": prompt
            }
        ],

        "model": (
            "google/medgemma-27b-text-it:"
            "featherless-ai"
        )
    }

    response = requests.post(

        API_URL,

        headers=headers,

        json=payload,

        timeout=120
    )

    print("\nSTATUS CODE:\n")

    print(response.status_code)

    print("\nRAW RESPONSE:\n")

    print(response.text)

    # ---------- SAFE HANDLING ---------- #

    if response.status_code != 200:

        return (
            f"HF Error "
            f"{response.status_code}"
        )

    data = response.json()

    return (
        data["choices"][0]
        ["message"]["content"]
    )

# ---------------- TEST ---------------- #

if __name__ == "__main__":

    result = query_medgemma(

        "I have anxiety and cannot sleep."
    )

    print("\nAI RESPONSE:\n")

    print(result)