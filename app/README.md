# Genlogs Backend API

REST API built with FastAPI that returns carriers operating between US cities.

**Live API:** https://genlogs-backend.onrender.com
**Docs (Swagger UI):** https://genlogs-backend.onrender.com/docs

---

## Tech Stack

- Python 3 + FastAPI
- Pydantic v2 — request/response validation
- Uvicorn — ASGI server
- Deployed on Render

---

## Endpoint

### POST /carriers

Returns the list of carriers operating between two cities.

**Request body:**

```json
{
  "from_city": "New York, NY, USA",
  "to_city": "Washington D.C., DC, USA"
}
```

**Response:**

```json
{
  "from_city": "New York, NY, USA",
  "to_city": "Washington D.C., DC, USA",
  "carriers": [
    { "name": "Knight-Swift Transport Services", "trucks_per_day": 10 },
    { "name": "J.B. Hunt Transport Services Inc", "trucks_per_day": 7 },
    { "name": "YRC Worldwide", "trucks_per_day": 5 }
  ]
}
```

**Supported routes:**

| From          | To             | Carriers                              |
|---------------|----------------|---------------------------------------|
| New York      | Washington DC  | Knight-Swift, J.B. Hunt, YRC Worldwide |
| San Francisco | Los Angeles    | XPO Logistics, Schneider, Landstar    |
| Any other     | Any other      | UPS Inc., FedEx Corp                  |

---

## Project Structure

```
app/
├── __init__.py
├── main.py       # FastAPI app setup + CORS
├── models.py     # Pydantic input/output models
└── routes.py     # Endpoint logic + carrier data
requirements.txt
```

---

## Local Setup

```bash
git clone https://github.com/cbastidas/genlogs-backend.git
cd genlogs-backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

API available at http://localhost:8000

Swagger UI at http://localhost:8000/docs

---

## Deployment

Deployed on Render. Every push to main triggers an automatic redeploy.

Note: Free tier instances spin down after inactivity. First request may take up to 50 seconds to wake up.