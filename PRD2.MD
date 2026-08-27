# Product Requirements Document (PRD v2)

## Product Name  
SafeSpace AI — Version 2

---

# 1. Objective

Extend SafeSpace AI by adding:

- WhatsApp-based conversational interface
- Nearby psychiatrist/hospital finder using Google Maps APIs

without restructuring the Version 1 architecture.

---

# 2. Key Enhancements

## E1 — WhatsApp Integration

Users can interact with SafeSpace AI directly through WhatsApp using:

- Twilio WhatsApp Sandbox
- FastAPI webhook integration

The system should:

- Receive WhatsApp messages
- Route messages through existing AI agent
- Return AI-generated responses back to WhatsApp

---

## E2 — Google Maps Specialist Finder

Replace the demo expert database with dynamic specialist lookup using:

- Google Geocoding API
- Google Places API

The system should:

- Convert city/location into latitude & longitude
- Search nearby psychiatrists within ~5 km radius
- Return nearby specialists and hospitals

---

# 3. Existing Components Reused

Version 2 reuses the existing:

- FastAPI backend
- AI agent
- Tool routing logic
- Emergency alert system
- Response parser
- OpenRouter integration
- Streamlit frontend

No major restructuring should occur.

---

# 4. New Backend Endpoints

## POST `/whatsapp`

Purpose:

- Accept incoming Twilio WhatsApp webhook requests
- Parse Twilio form-data request format
- Invoke existing AI agent
- Return Twilio-compatible XML response

---

# 5. New Tools

## google_maps_tool.py

Responsibilities:

- Geocoding user location
- Finding nearby psychiatrists
- Returning structured hospital/specialist data

---

# 6. Architecture

```text
WhatsApp User
      ↓
Twilio Sandbox
      ↓
FastAPI /whatsapp Endpoint
      ↓
AI Agent
      ↓
Tool Invocation
 ├── Emergency Alerts
 ├── Google Maps Specialist Finder
 └── AI Response Generation
      ↓
Twilio XML Response
      ↓
WhatsApp User
```

---

# 7. Technical Requirements

## Twilio

- WhatsApp Sandbox enabled
- Webhook configured to deployed backend URL

## Google APIs

Required APIs:

- Geocoding API
- Places API

---

# 8. Constraints

- Maintain compatibility with Version 1
- Avoid major codebase restructuring
- Keep existing frontend operational
- Ensure safe AI responses
- Avoid storing sensitive medical data

---

# 9. Future Extensions

Potential future upgrades:

- Voice message support
- Speech-to-text
- Multi-language WhatsApp interaction
- Real-time appointment booking
- Live doctor availability
- Geo-location sharing support

---

# 10. Success Criteria

Version 2 is considered successful if:

- Users can chat with SafeSpace AI on WhatsApp
- AI responses are returned correctly through Twilio
- Nearby psychiatrists can be fetched dynamically
- Existing Version 1 system remains stable
- Emergency escalation continues functioning properly