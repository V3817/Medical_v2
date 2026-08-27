# Product Requirements Document (PRD)

# 🧠 SafeSpace AI

AI-Powered Medical and Mental Health Assistant

---

# 1. Product Overview

SafeSpace AI is an AI-powered medical and mental health assistant designed to demonstrate modern AI agent workflows using:

* LLM orchestration
* Tool calling
* FastAPI backend services
* Streamlit frontend interfaces
* Emergency escalation systems
* Specialist recommendation tools

The system provides safe, supportive, and structured responses for medical and mental health related queries.

This project is intended for:

* Educational purposes
* AI engineering demonstrations
* Hackathons
* Portfolio projects
* Agent architecture experimentation

It is NOT intended to replace professional medical care.

---

# 2. Problem Statement

Users frequently seek immediate preliminary medical or mental health guidance online.

However, existing systems often:

* Fail to handle emergencies safely
* Provide unsafe or hallucinated advice
* Lack structured tool integration
* Do not support escalation workflows
* Are difficult to extend with external APIs

There is a need for a safe, modular, tool-augmented AI assistant architecture that demonstrates:

* LLM reasoning
* Tool orchestration
* Safety constraints
* Emergency workflows
* Full-stack AI application integration

---

# 3. Product Goals

The primary goals of SafeSpace AI are:

* Demonstrate AI agent architecture
* Showcase LLM tool-calling workflows
* Provide safe and structured AI responses
* Integrate external tools such as Twilio
* Build an end-to-end deployable AI system
* Maintain modular architecture for future scalability

---

# 4. Target Users

## Primary Users

* Students learning AI systems
* Developers learning LangChain/LangGraph
* Recruiters evaluating AI engineering skills
* Hackathon evaluators
* Open-source contributors

## Secondary Users

* Users exploring AI mental health assistants
* Developers experimenting with tool-based LLM workflows

---

# 5. Scope

## In Scope

### AI Chat Interface

* Conversational medical assistant
* Mental health support assistant
* Real-time chat interaction

### Tool-Augmented Workflows

* Emergency alert system
* Specialist finder system
* Tool usage parser

### Full-Stack Architecture

* Streamlit frontend
* FastAPI backend
* LLM orchestration layer
* API communication

### Safety Features

* Medical disclaimers
* Emergency detection
* Safe prompting
* Restricted harmful advice

---

## Out of Scope

* Real medical diagnosis
* HIPAA compliance
* Clinical-grade healthcare deployment
* Real hospital integrations
* Real-time GPS tracking
* Persistent patient records
* Insurance integration
* Real appointment booking

---

# 6. Functional Requirements

## F1 — Conversational AI Interface

Users must be able to:

* Input natural language queries
* Receive structured responses
* View tool usage indicators
* Maintain chat history during a session

---

## F2 — AI Medical Response Generation

The system must:

* Generate medical and mental health responses
* Avoid definitive diagnoses
* Encourage professional consultation
* Maintain supportive tone
* Apply safety constraints

---

## F3 — Tool Invocation System

The AI agent must determine whether to:

* Respond directly
* Invoke a specialist finder tool
* Trigger emergency escalation

Tool invocation should be visible in the frontend.

---

## F4 — Emergency Detection and Alerting

The system must detect emergency-related messages such as:

* Suicide ideation
* Self-harm
* Severe chest pain
* Breathing difficulty
* Danger-to-life scenarios

Upon detection:

* Emergency alert SMS is triggered
* User receives emergency guidance
* Emergency flow overrides normal response generation

---

## F5 — Specialist Recommendation Tool

The system must:

* Recommend doctors/specialists
* Support location-based lookup
* Return structured specialist information

Current implementation uses a demo database.

---

## F6 — Frontend Tool Visualization

The UI must display:

* AI responses
* Tool used badges
* Backend status
* Session conversation history

---

## F7 — Health Check Endpoint

Backend must expose:

```http
GET /health
```

for frontend availability checks.

---

# 7. Non-Functional Requirements

## Performance

* Average response latency under 5 seconds
* Graceful timeout handling
* Fast frontend rendering

---

## Reliability

* Backend should handle invalid requests gracefully
* External API failures should not crash the system
* Emergency flow should remain prioritized

---

## Scalability

Architecture should support:

* Additional tools
* Multiple LLM providers
* Future memory systems
* API integrations

---

## Security

* API keys stored separately in config
* No exposure of credentials in frontend
* Restricted unsafe outputs

---

## Maintainability

Codebase should remain modular with separation between:

* Tools
* Agent logic
* Backend APIs
* Frontend UI

---

# 8. System Architecture

## Frontend Layer

Technology:

* Streamlit

Responsibilities:

* User chat interface
* Session state management
* Display responses
* Display tool usage
* Health status monitoring

---

## Backend Layer

Technology:

* FastAPI
* Uvicorn

Responsibilities:

* API routing
* Request validation
* Agent invocation
* Response formatting
* Error handling

---

## AI Orchestration Layer

Technologies:

* LangChain
* LangGraph
* OpenRouter

Responsibilities:

* LLM interaction
* Tool orchestration
* Response generation
* Agent workflows

---

## Tool Layer

### Emergency Alert Tool

Uses:

* Twilio SMS API

### Expert Finder Tool

Uses:

* Mock specialist database

### Medical Response Tool

Uses:

* OpenRouter free LLMs
* Ollama/Nemotron fallback architecture

---

# 9. Data Flow

```text
User Input
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
AI Agent Layer
    ↓
Tool Decision
    ↓
Tool Execution (optional)
    ↓
Response Parser
    ↓
Frontend Display
```

---

# 10. API Design

## Health Endpoint

### Request

```http
GET /health
```

### Response

```json
{
  "status": "healthy"
}
```

---

## Chat Endpoint

### Request

```http
POST /chat
```

### Request Body

```json
{
  "user_message": "I have anxiety"
}
```

---

### Response Body

```json
{
  "response": "Generated AI response",
  "tool_used": "ask_medgemma"
}
```

---

# 11. Agent Decision Logic

Current implementation uses hybrid routing:

## Emergency Override

Emergency keywords trigger:

```text
trigger_emergency_alert
```

Examples:

* suicide
* kill myself
* self harm
* chest pain
* breathing issues

---

## Specialist Queries

Location-related queries trigger:

```text
expert_finder
```

Examples:

* doctor in Mumbai
* psychiatrist nearby
* specialist recommendation

---

## General Medical Queries

General medical queries are handled using:

```text
OpenRouter LLM
```

with safe prompting.

---

# 12. Safety Constraints

The system must:

* Avoid medical diagnosis claims
* Avoid dangerous advice
* Encourage professional consultation
* Escalate emergencies immediately
* Avoid hallucinated claims
* Avoid harmful medication recommendations

All outputs must remain supportive and non-judgmental.

---

# 13. Tech Stack

| Layer             | Technology |
| ----------------- | ---------- |
| Frontend          | Streamlit  |
| Backend           | FastAPI    |
| Runtime           | Uvicorn    |
| Agent Framework   | LangGraph  |
| LLM Framework     | LangChain  |
| LLM Provider      | OpenRouter |
| Fallback Runtime  | Ollama     |
| Communication API | Twilio     |
| Package Manager   | uv         |

---

# 14. Current LLM Architecture

## Current Provider

OpenRouter free-tier models.

Example:

```text
openrouter/free
```

---

## Previous Experiments

The project experimented with:

* Gemini
* Groq
* Nemotron
* Ollama cloud models

Challenges observed:

* Tool-calling instability
* Free-tier rate limits
* Context explosion
* Provider outages

---

# 15. Milestones

## Phase 1 — Frontend & Backend Setup

* Streamlit UI
* FastAPI APIs
* Request/response flow

---

## Phase 2 — LLM Integration

* Ollama integration
* Nemotron/OpenRouter integration
* Prompt engineering

---

## Phase 3 — Tool Development

* Emergency SMS alerts
* Expert finder tool
* Medical response tool

---

## Phase 4 — Agent Workflow

* LangGraph ReAct agent
* Tool orchestration
* Response parser

---

## Phase 5 — UI Improvements

* Tool badges
* Session state
* Backend status
* Error handling

---

# 16. Risks and Limitations

## Technical Risks

* Free-tier LLM instability
* Rate limits
* Tool invocation failures
* External API downtime
* Long LLM latency

---

## AI Risks

* Hallucinated medical content
* Incorrect emergency classification
* Unsafe suggestions
* Context overflow

---

## Operational Risks

* Twilio delivery failures
* OpenRouter provider outages
* Backend timeout errors

---

# 17. Success Metrics

The project is considered successful if:

* Frontend and backend operate successfully
* Tool routing works correctly
* Emergency alerts trigger correctly
* Structured responses are returned
* Tool badges display properly
* Response latency remains acceptable
* Application remains stable during demos

---

# 18. Future Improvements

## AI Enhancements

* Conversational memory
* RAG pipelines
* Vector databases
* Fine-tuned medical models
* Emotion analysis

---

## Product Enhancements

* User authentication
* Real hospital APIs
* Appointment booking
* Voice interface
* Multi-language support
* Mobile app version
* PDF report generation

---

## Infrastructure Enhancements

* Docker deployment
* Kubernetes scaling
* CI/CD pipelines
* Monitoring dashboards
* Redis caching
* Database integration

---

# 19. Deployment Targets

## Frontend

* Streamlit Cloud
* Vercel
* Netlify

---

## Backend

* Render
* Railway
* AWS
* Azure
* GCP
* DigitalOcean

---

# 20. Conclusion

SafeSpace AI demonstrates a modern AI-agent architecture combining:

* LLM orchestration
* Tool integration
* Emergency escalation
* FastAPI backend systems
* Streamlit frontend interfaces
* Safe medical prompting

The project serves as a strong demonstration of:

* AI engineering workflows
* Tool-calling systems
* Full-stack AI applications
* Agent-based architectures

while maintaining safety-focused medical interaction constraints.
