from fastapi import (
    FastAPI,
    Form
)

from fastapi.responses import (
    PlainTextResponse
)

from pydantic import BaseModel

from xml.etree.ElementTree import (
    Element,
    tostring
)

import uvicorn

from ai_agent import (
    agent,
    response_parser,
    trigger_emergency_alert,
    EMERGENCY_KEYWORDS
)

# ---------------- APP INIT ---------------- #

app = FastAPI(

    title="Medical AI Assistant API",

    version="2.0.0"
)

# ---------------- REQUEST SCHEMA ---------------- #

class ChatRequest(BaseModel):

    user_message: str

# ---------------- RESPONSE SCHEMA ---------------- #

class ChatResponse(BaseModel):

    response: str

    tool_used: str

# ---------------- TWILIO XML FORMATTER ---------------- #

def build_twiml_response(
    body: str
) -> PlainTextResponse:

    response_el = Element(
        "Response"
    )

    message_el = Element(
        "Message"
    )

    message_el.text = body

    response_el.append(
        message_el
    )

    xml_bytes = tostring(

        response_el,

        encoding="utf-8"
    )

    return PlainTextResponse(

        content=xml_bytes,

        media_type="application/xml"
    )

# ---------------- NORMAL CHAT ENDPOINT ---------------- #

@app.post(
    "/chat",
    response_model=ChatResponse
)

async def chat_endpoint(request: ChatRequest):

    user_message = request.user_message.strip()

    # ---------------- VALIDATION ---------------- #

    if not user_message:

        return {
            "response": "Message cannot be empty.",
            "tool_used": "none"
        }

    lower_input = user_message.lower()

    # ---------------- EMERGENCY OVERRIDE ---------------- #

    if any(
        keyword in lower_input
        for keyword in EMERGENCY_KEYWORDS
    ):

        trigger_emergency_alert.func(
            user_message
        )

        return {
            "response": (
                "Emergency support alert triggered. "
                "Please contact emergency services "
                "or a healthcare professional immediately."
            ),

            "tool_used": "trigger_emergency_alert"
        }

    # ---------------- NORMAL AGENT FLOW ---------------- #

    try:

        response = await agent.ainvoke({

            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        })

        parsed_response = response_parser(
            response
        )

        final_response = parsed_response.get(

            "final_response",

            ""
        )

        if not final_response:

            final_response = (
                "Response currently unavailable."
            )

        return {

            "response": final_response,

            "tool_used": parsed_response.get(

                "tool_used",

                "none"
            )
        }

    except Exception as e:

        return {
            "response": (
                f"Agent Error: {str(e)}"
            ),

            "tool_used": "none"
        }

# ---------------- WHATSAPP ENDPOINT ---------------- #

@app.post("/whatsapp")

async def whatsapp_webhook(

    Body: str = Form(...)
):

    try:

        print("\n====================")
        print("WHATSAPP REQUEST")
        print("====================")

        print(f"Incoming Body: {Body}")

        user_message = (
            Body.strip()
            if Body else ""
        )

        # ---------------- VALIDATION ---------------- #

        if not user_message:

            print("Empty WhatsApp message")

            return build_twiml_response(

                "Message cannot be empty."
            )

        lower_input = user_message.lower()

        # ---------------- EMERGENCY OVERRIDE ---------------- #

        if any(
            keyword in lower_input
            for keyword in EMERGENCY_KEYWORDS
        ):

            print("Emergency keyword detected")

            trigger_emergency_alert.func(
                user_message
            )

            return build_twiml_response(

                "Emergency support alert triggered. "
                "Please contact emergency services immediately."
            )

        # ---------------- NORMAL AGENT FLOW ---------------- #

        print("\nCalling AI Agent...\n")

        response = await agent.ainvoke({

            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        })

        print("\nRaw Agent Response:\n")

        print(response)

        parsed_response = response_parser(
            response
        )

        print("\nParsed Response:\n")

        print(parsed_response)

        final_response = parsed_response.get(

            "final_response",

            ""
        )

        # ---------------- FALLBACK ---------------- #

        if not final_response:

            print("No final response found")

            final_response = (
                "I'm here to support you, "
                "but I couldn't generate "
                "a response just now."
            )

        print("\nFinal Response:\n")

        print(final_response)

        # ---------------- XML RESPONSE ---------------- #

        return build_twiml_response(
            final_response
        )

    except Exception as e:

        print("\n====================")
        print("WHATSAPP ERROR")
        print("====================")

        print(str(e))

        return build_twiml_response(

            f"Internal Error: {str(e)}"
        )

# ---------------- HEALTH CHECK ---------------- #

@app.get("/health")

def health_check():

    return {
        "status": "healthy"
    }

# ---------------- MAIN ---------------- #

if __name__ == "__main__":

    uvicorn.run(

        "main:app",

        host="0.0.0.0",

        port=8000,

        reload=True
    )