# AI Request Validator API

A FastAPI project that validates AI model requests before they are sent to providers like Anthropic, OpenAI, and Groq. It checks that incoming requests are correctly structured, use supported models, and meet token constraints — returning a structured response with a unique ID on success, or a clear error on failure.

Built as a portfolio project to demonstrate clean API design, Pydantic v2 validation, and layered FastAPI architecture.

---

## Tech Stack

- **Python 3.11+**
- **FastAPI** — API framework
- **Pydantic v2** — request/response schema validation
- **UUID** — unique ID generation
- **Pytest** — testing

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/ai-request-validator.git
cd ai-request-validator
pip install fastapi uvicorn pydantic pytest httpx
```

---

## Running the App

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

Interactive docs (Swagger UI) are available at `http://localhost:8000/docs`.

---

## API Documentation

### `GET /models`

Returns a list of all supported AI model identifiers.

**Response**
```json
[
  "llama-3.1-8b-instant",
  "llama-3.3-70b-versatile",
  "claude-sonnet-4-6",
  "claude-opus-4-7",
  "gpt-4.1",
  "gpt-5.4"
]
```

---

### `POST /validate`

Validates an AI model request. Returns a structured response with a unique ID if valid, or a 422 error with details if invalid.

**Request Body**

| Field | Type | Required | Constraints |
|---|---|---|---|
| `messages` | `list[Message]` | Yes | Minimum 1 item |
| `model` | `string (enum)` | Yes | Must be a supported model name |
| `max_tokens` | `integer` | Yes | Between 5 and 500 |
| `system_prompt` | `string` | No | Defaults to null |

Each `Message` object:

| Field | Type | Constraints |
|---|---|---|
| `role` | `string (enum)` | `user`, `system`, or `assistant` |
| `content` | `string` | Cannot be empty or whitespace |

**Example Request**
```json
{
  "messages": [
    { "role": "user", "content": "How do I implement a binary search?" }
  ],
  "model": "claude-sonnet-4-6",
  "max_tokens": 200,
  "system_prompt": "You are a helpful coding assistant."
}
```

**Success Response (200)**
```json
{
  "id": "a3f1c2d4-...",
  "status": "success",
  "messages": [
    { "role": "user", "content": "How do I implement a binary search?" }
  ],
  "model": "claude-sonnet-4-6",
  "max_tokens": 200,
  "system_prompt": "You are a helpful coding assistant."
}
```

**Validation Error Response (422)**
```json
{
  "detail": [
    {
      "loc": ["body", "model"],
      "msg": "value is not a valid enumeration member",
      "type": "enum"
    }
  ]
}
```

---

## Project Structure

```
ai-request-validator/
├── main.py                  # App entry point
├── routers/
│   └── validation.py        # POST /validate and GET /models endpoints
├── models/
│   ├── request.py           # Role enum, ModelName enum, Message model, UserRequest schema
│   └── response.py          # UserResponse schema
├── services/
│   └── validator.py         # Validation logic and response construction
└── tests/
    └── test_validation.py   # Happy and unhappy path tests
```

---

## Running Tests

```bash
pytest tests/
```

---

## Design Decisions

- **Enums over free strings** — `model` and `role` fields use Python enums to prevent invalid values at the schema level, before any business logic runs.
- **Service layer separation** — validation logic lives in `services/validator.py`, not in the router, following the DRY principle and keeping endpoints thin.
- **Pydantic v2 field validators** — empty or whitespace-only message content is rejected at the model level, keeping that constraint close to the data.
- **UUID v4** — each successful validation response gets a unique identifier generated server-side.