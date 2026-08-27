# 🧠 SafeSpace AI v2

AI-powered mental health and medical support assistant with:

- FastAPI backend
- Streamlit frontend
- WhatsApp integration
- AI agent workflows
- Google Maps specialist finder
- Emergency escalation support

Built using:

- FastAPI
- Streamlit
- LangChain
- LangGraph
- OpenRouter
- Twilio
- Google Maps API

---

# 🚀 Version 2 Highlights

SafeSpace AI v2 introduces:

## ✅ WhatsApp AI Chatbot

Users can now interact with SafeSpace AI directly through WhatsApp using:

- Twilio WhatsApp Sandbox
- FastAPI webhook integration
- TwiML XML responses

---

## ✅ Google Maps Specialist Finder

The system can now:

- Convert city/location into coordinates
- Find nearby psychotherapists
- Return addresses and phone numbers
- Search within ~5km radius

Powered by:

- Google Geocoding API
- Google Places API

---

## ✅ Async AI Agent Architecture

Version 2 upgrades the backend to:

- Async FastAPI routes
- Async LangChain agent execution
- Improved scalability
- Better webhook compatibility

---

# ✨ Features

## 🧠 AI Medical Assistant

SafeSpace AI can:

- Answer general medical questions
- Provide mental health guidance
- Suggest safe self-care practices
- Encourage professional consultation
- Avoid unsafe or harmful responses

---

## 🚨 Emergency Detection

The system detects:

- Suicide ideation
- Self-harm intent
- Severe chest pain
- Dangerous symptoms
- Crisis situations

When detected:

- Emergency alert flow triggers
- Twilio SMS alerts can be sent
- User is encouraged to seek immediate help

---

## 🗺️ Therapist Finder

Users can ask:

```text
Find therapist in Mumbai
```

The system:

- Geocodes the location
- Finds nearby therapists
- Returns:
  - name
  - address
  - phone number

---

## 📱 WhatsApp Support

Users can interact with SafeSpace AI via:

- WhatsApp Sandbox
- Real-time AI responses
- Twilio webhook integration

---

# 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend API | FastAPI |
| AI Framework | LangChain |
| Agent Framework | LangGraph |
| LLM Provider | OpenRouter |
| Communication | Twilio |
| Maps Integration | Google Maps API |
| HTTP Server | Uvicorn |
| Environment Manager | uv |

---

# 📁 Project Structure

```bash
Medical_v2/
│
├── backend/
│   ├── ai_agent.py
│   ├── config.py
│   ├── google_map_tool.py
│   ├── main.py
│   ├── requirements.txt
│   └── tools.py
│
├── frontend.py
├── README.md
├── PRD2.md
│
└── .venv/
```

---

# ⚙️ Installation

# 1. Clone Repository

```bash
git clone https://github.com/your_username/Medical_v2.git
```

```bash
cd Medical_v2
```

---

# 2. Create Virtual Environment

Using uv:

```bash
uv venv
```

Activate:

## macOS/Linux

```bash
source .venv/bin/activate
```

## Windows

```bash
.venv\Scripts\activate
```

---

# 3. Install Dependencies

```bash
uv pip install -r backend/requirements.txt
```

---

# 🔑 Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_openrouter_key

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number

EMERGENCY_PHONE_NUMBER=your_phone

GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

---

# 🤖 OpenRouter Setup

Create API key:

[OpenRouter](https://openrouter.ai?utm_source=chatgpt.com)

Copy key into `.env`

---

# 📱 Twilio WhatsApp Setup

Open:

[Twilio WhatsApp Sandbox](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?utm_source=chatgpt.com)

## Configure Webhook

Webhook URL:

```text
https://your-render-url.onrender.com/whatsapp
```

Method:

```text
POST
```

---

# 🗺️ Google Maps API Setup

Open:

[Google Cloud Console](https://console.cloud.google.com?utm_source=chatgpt.com)

Enable:

- Geocoding API
- Places API

Generate API key and place into `.env`

---

# ▶️ Running Backend Locally

```bash
uv run backend/main.py
```

Backend:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

# ▶️ Running Frontend

```bash
uv run streamlit run frontend.py
```

Frontend:

```text
http://localhost:8501
```

---

# ☁️ Deployment

## Backend Deployment

Deployed using:

:contentReference[oaicite:3]{index=3}

### Build Command

```bash
pip install uv && uv pip install -r requirements.txt
```

### Start Command

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 10000
```

---

# 🧩 FastAPI Endpoints

# Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

# Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "user_message": "I feel anxious"
}
```

Response:

```json
{
  "response": "AI response here",
  "tool_used": "ask_medgemma"
}
```

---

# WhatsApp Endpoint

```http
POST /whatsapp
```

Receives:

- Twilio form-data request

Returns:

- TwiML XML response

Example:

```xml
<Response>
    <Message>
        AI response here
    </Message>
</Response>
```

---

# 🧠 AI Agent Flow

```text
User Input
    ↓
FastAPI Backend
    ↓
LangGraph Agent
    ↓
OpenRouter LLM
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
Response Parser
    ↓
Frontend / WhatsApp
```

---

# 🛠️ Tools

# 1. ask_medgemma

Purpose:

- AI medical assistance
- Mental health guidance

---

# 2. trigger_emergency_alert

Purpose:

- Emergency escalation
- SMS alerts

Uses:

- Twilio API

---

# 3. find_nearby_therapists_by_location

Purpose:

- Nearby therapist finder

Uses:

- Google Geocoding API
- Google Places API

Returns:

- Therapist name
- Address
- Phone number

---

# 🧪 Example Queries

## Mental Health

```text
I feel anxious and cannot sleep
```

---

## Medical

```text
I have headache from 3 days
```

---

## Emergency

```text
I want to harm myself
```

---

## Therapist Finder

```text
Find therapist in Mumbai
```

---

# 🔐 Safety Features

SafeSpace AI includes:

- Medical disclaimers
- Safe prompting
- Emergency escalation
- Harm prevention
- Professional help recommendations

---

# ⚠️ Limitations

This is a demo AI system.

Not intended for:

- Real diagnosis
- Clinical replacement
- Emergency healthcare replacement

Current limitations:

- Free-tier model limits
- Render cold starts
- No persistent database
- No authentication system

---

# 🔮 Future Improvements

Planned upgrades:

- Voice message support
- Speech-to-text
- Real-time appointment booking
- Authentication system
- Memory support
- RAG pipelines
- Multilingual support
- Geo-location sharing
- Vector databases
- Docker deployment
- Kubernetes scaling

---

# 🐳 Future Docker Support

```bash
docker build -t safespace-ai .
```

```bash
docker run -p 8000:8000 safespace-ai
```

---

# 🧑‍💻 Developer Notes

Important learnings during development:

- Async agents are required for webhook systems
- OpenRouter is OpenAI-compatible
- Free LLM providers may rate-limit requests
- Tool calling can increase latency
- Medical systems require deterministic safeguards
- Twilio requires XML/TwiML responses

---

# 📄 License

This project is intended for:

- Educational use
- AI experimentation
- Research
- Hackathons

Not intended for:

- Clinical diagnosis
- Production healthcare usage

---

# 🙌 Acknowledgements

Built using:

- FastAPI
- Streamlit
- LangChain
- LangGraph
- OpenRouter
- Twilio
- Google Maps API
- Render

---

# 📬 Contact

For collaboration, feedback, or contributions:

GitHub:
https://github.com/V3817
