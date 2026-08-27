# ---------------- IMPORTS ---------------- #

import streamlit as st
import requests

# ---------------- BACKEND CONFIG ---------------- #

BACKEND_URL = st.secrets["BACKEND_URL"]

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(

    page_title="AI Mental Health Therapist",

    page_icon="🧠",

    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

    .main {
        background-color: #0E1117;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: white;
    }

    .subtitle {
        color: #A0A0A0;
        margin-bottom: 2rem;
    }

    .footer-text {
        text-align: center;
        color: gray;
        margin-top: 2rem;
        font-size: 0.9rem;
    }

    .tool-badge {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        background-color: #262730;
        color: #D1D5DB;
        font-size: 0.8rem;
        margin-top: 0.5rem;
    }

    .emergency-badge {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        background-color: #7F1D1D;
        color: white;
        font-size: 0.8rem;
        margin-top: 0.5rem;
    }

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    """
    <div class="main-title">🧠 SafeSpace</div>

    <div class="subtitle">
        Your AI-powered mental health support companion
    </div>
    """,

    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("⚙️ Settings")

    # ---------------- BACKEND STATUS ---------------- #

    try:

        health_check = requests.get(
            f"{BACKEND_URL}/health",
            timeout=3
        )

        if health_check.status_code == 200:

            st.success("Backend Connected")

        else:

            st.warning("Backend Unreachable")

    except:

        st.error("Backend Offline")

    st.markdown("---")

    emergency_toggle = st.toggle(
        "Emergency Detection",
        value=True
    )

    st.markdown("---")

    # ---------------- CLEAR CHAT ---------------- #

    if st.button("Clear Chat"):

        st.session_state.chat_history = [

            {
                "role": "assistant",

                "content": (
                    "Hello 👋\n\n"
                    "I'm SafeSpace, your AI mental health assistant.\n\n"
                    "How are you feeling today?"
                ),

                "tool_used": "none"
            }
        ]

        st.rerun()

    st.markdown("---")

    st.info(
        "This is a demo AI therapist application.\n\n"
        "It does not replace professional medical advice."
    )

# ---------------- SESSION STATE ---------------- #

if "chat_history" not in st.session_state:

    st.session_state.chat_history = [

        {
            "role": "assistant",

            "content": (
                "Hello 👋\n\n"
                "I'm SafeSpace, your AI mental health assistant.\n\n"
                "How are you feeling today?"
            ),

            "tool_used": "none"
        }
    ]

# ---------------- DISPLAY CHAT HISTORY ---------------- #

for msg in st.session_state.chat_history:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])

        # Emergency badge
        if (
            msg.get("tool_used")
            == "trigger_emergency_alert"
        ):

            st.markdown(
                """
                <div class="emergency-badge">
                    Emergency Alert Triggered
                </div>
                """,

                unsafe_allow_html=True
            )

        # Normal tool badge
        elif msg.get("tool_used") != "none":

            st.markdown(
                f"""
                <div class="tool-badge">
                    Tool Used: {msg["tool_used"]}
                </div>
                """,

                unsafe_allow_html=True
            )

# ---------------- CHAT INPUT ---------------- #

user_input = st.chat_input(
    "What's on your mind today?"
)

# ---------------- HANDLE USER INPUT ---------------- #

if user_input:

    # Store user message
    st.session_state.chat_history.append({

        "role": "user",

        "content": user_input,

        "tool_used": "none"
    })

    # Show user message instantly
    with st.chat_message("user"):

        st.write(user_input)

    # ---------------- API CALL ---------------- #

    try:

        with st.spinner("Thinking..."):

            response = requests.post(

                f"{BACKEND_URL}/chat",

                json={
                    "user_message": user_input
                },

                timeout=180
            )

        data = response.json()

        assistant_response = data.get(
            "response",
            "No response received."
        )

        tool_used = data.get(
            "tool_used",
            "none"
        )

    except requests.exceptions.ConnectionError:

        assistant_response = (
            "Unable to connect to backend server.\n\n"
            "Make sure FastAPI is running on port 8000."
        )

        tool_used = "none"

    except Exception as e:

        assistant_response = f"Error: {str(e)}"

        tool_used = "none"

    # ---------------- STORE ASSISTANT RESPONSE ---------------- #

    st.session_state.chat_history.append({

        "role": "assistant",

        "content": assistant_response,

        "tool_used": tool_used
    })

    # ---------------- DISPLAY ASSISTANT RESPONSE ---------------- #

    with st.chat_message("assistant"):

        st.write(assistant_response)

        # Emergency badge
        if tool_used == "trigger_emergency_alert":

            st.markdown(
                """
                <div class="emergency-badge">
                    Emergency Alert Triggered
                </div>
                """,

                unsafe_allow_html=True
            )

        # Normal tool badge
        elif tool_used != "none":

            st.markdown(
                f"""
                <div class="tool-badge">
                    Tool Used: {tool_used}
                </div>
                """,

                unsafe_allow_html=True
            )

# ---------------- FOOTER ---------------- #

st.markdown(
    """
    <div class="footer-text">
        Built with Streamlit • AI Agent Demo System
    </div>
    """,

    unsafe_allow_html=True
)