from langchain_openai import ChatOpenAI

from langgraph.prebuilt import create_react_agent

from langchain.tools import tool

from config import OPENROUTER_API_KEY

from tools import (
    query_medgemma,
    emergency_alert as send_emergency_alert
)

# ---------------- OPENROUTER LLM ---------------- #
llm = ChatOpenAI(

    model="openrouter/free",

    openai_api_key=OPENROUTER_API_KEY,

    openai_api_base="https://openrouter.ai/api/v1",

    temperature=0.6,

    max_tokens=1024
)

# ---------------- TOOL 1 ---------------- #

@tool
def ask_medgemma(user_message: str) -> str:
    """
    Query the MedGemma AI medical assistant.
    """

    return query_medgemma(user_message)

# ---------------- TOOL 2 ---------------- #

@tool
def trigger_emergency_alert(user_message: str) -> str:
    """
    Send emergency SMS alert.
    """

    return send_emergency_alert(user_message)

# ---------------- TOOL 3 ---------------- #

@tool
def expert_finder(location: str) -> dict:
    """
    Find nearby doctors and specialists.
    """

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

# ---------------- TOOLS ---------------- #

tools = [
    ask_medgemma,
    trigger_emergency_alert,
    expert_finder
]

# ---------------- SYSTEM PROMPT ---------------- #

SYSTEM_PROMPT = """
You are SafeSpace AI,
a safe and supportive medical AI assistant.

You have access to 3 tools:

1. ask_medgemma
- ALWAYS use this tool for
  medical or mental health questions

2. trigger_emergency_alert
- Use ONLY for emergencies
- Emergencies include:
    suicide
    self-harm
    chest pain
    breathing issues
    danger to life

3. expert_finder
- Use when user asks for:
    doctors
    hospitals
    specialists
    nearby experts

Rules:
- Never claim to be a real doctor
- Never provide dangerous advice
- Encourage professional help
- Be concise and supportive

Keep responses under 250 words.
"""

# ---------------- CREATE REACT AGENT ---------------- #

agent = create_react_agent(

    model=llm,

    tools=tools,

    prompt=SYSTEM_PROMPT
)

# ---------------- RESPONSE PARSER ---------------- #

def response_parser(agent_response: dict) -> dict:

    messages = agent_response.get(
        "messages",
        []
    )

    tool_name = "none"

    final_response = ""

    for message in messages:

        # Detect tool usage
        if hasattr(message, "name"):

            if message.name:

                tool_name = message.name

        # Extract final response
        if hasattr(message, "content"):

            if (
                isinstance(message.content, str)
                and message.content.strip()
            ):

                final_response = message.content

    return {
        "tool_used": tool_name,
        "final_response": final_response
    }

# ---------------- EMERGENCY KEYWORDS ---------------- #

EMERGENCY_KEYWORDS = [
    "die",
    "suicide",
    "kill myself",
    "self harm",
    "harm myself",
    "can't breathe",
    "chest pain",
    "heart attack",
    "severe bleeding"
]