# 🤖 AI Test Case Generator (FastAPI + OpenAI)

---

# 📌 What is this project?

This project is a **Backend AI Application** that automatically converts:

👉 Software Requirements / User Stories
into
👉 QA Test Cases

using **Python + FastAPI + OpenAI GPT**.

Instead of manually writing test cases, you send a requirement like:

> "User should login using email and password"

The system automatically generates:

* Test titles
* Steps
* Expected results
* Priority

---

# 🎯 Why this project?

Manual test case writing is:

* slow
* repetitive
* boring
* time consuming

Using AI:

* faster
* automated
* scalable
* smart suggestions

Also, this project helps you learn:

✅ Backend development
✅ API creation
✅ Python servers
✅ OpenAI integration
✅ Real-world AI engineering

This is NOT a toy script.
This is how **real AI features are built in production apps**.

---

# 🧠 Big Picture Architecture (How everything connects)

```
Browser / Swagger UI
        ↓
FastAPI Backend Server (main.py)
        ↓
Business Logic (service.py)
        ↓
OpenAI GPT API (AI brain)
        ↓
Generated Test Cases
```

Flow:

1. User sends requirement
2. Backend receives it
3. Backend calls OpenAI
4. OpenAI generates answer
5. Backend returns response

---

# 🧩 Concepts Explained (A → Z for beginners)

---

## 🔵 What is a Backend App?

A **backend app** is a server that:

* receives requests
* processes logic
* talks to databases/APIs
* sends responses back

Example:

Swiggy app:

```
Phone → Swiggy server → Restaurant
```

Your project:

```
Browser → Your backend → OpenAI
```

So you built the **middle brain**.

---

## 🔵 What is an API?

API = way for apps to talk to each other.

Example:

```
POST /generate-testcases
```

Means:
"Send me requirement → I'll return test cases"

Your project exposes this API.

So now:
👉 YOU are building services like real companies.

---

## 🔵 What is FastAPI?

FastAPI is:

👉 A Python framework to create backend APIs easily.

Without FastAPI:

* you must write raw HTTP code (hard)

With FastAPI:

* routing
* validation
* docs
* server
* JSON parsing

All automatic.

Example:

```python
@app.post("/generate-testcases")
```

Creates an API instantly.

---

## 🔵 What is Uvicorn?

Uvicorn = server engine.

Think:

FastAPI = car
Uvicorn = engine

Command:

```
uvicorn main:app --reload
```

Starts your server.

---

## 🔵 What is OpenAI API?

OpenAI API is:

👉 a cloud service that provides AI intelligence.

Instead of building your own AI model, you simply call:

```
"Generate test cases"
```

and it returns smart output.

Like:

* Stripe → payments
* Twilio → SMS
* OpenAI → AI brain

---

## 🔵 What is GPT?

GPT is the AI model that generates text.

We use:

```
gpt-4o-mini
```

Because:

* cheap
* fast
* good quality

Perfect for backend apps.

---

## 🔵 What is venv?

Virtual Environment.

Problem:
All projects share same packages → conflicts

Solution:
Each project gets its own isolated Python

```
venv/
```

Every professional Python project uses this.

---

## 🔵 What is requirements.txt?

List of dependencies.

Instead of:

```
pip install fastapi
pip install openai
```

You run:

```
pip install -r requirements.txt
```

Everything installs automatically.

---

## 🔵 What is .env?

Stores secrets like:

* API keys
* passwords

Example:

```
OPENAI_API_KEY=sk-xxxx
```

Never hardcode secrets.

---

# 📂 Project Structure

```
ai-testcase-generator/
│
├── main.py              → FastAPI server & routes
├── service.py           → AI logic (OpenAI call)
├── requirements.txt     → dependencies list
├── .env                 → API key
├── .gitignore           → ignores secrets/venv
├── README.md            → documentation
└── venv/                → virtual environment
```

---

# 📄 File-by-File Explanation

---

## main.py (Server Layer)

Responsibilities:

* start FastAPI
* create API endpoints
* accept request
* return response

Contains:

```
POST /generate-testcases
```

This is your public API.

---

## service.py (AI Brain Layer)

Responsibilities:

* load API key
* prepare prompt
* call OpenAI
* return AI response

This is where intelligence happens.

---

## requirements.txt

Dependencies:

```
fastapi
uvicorn
openai
python-dotenv
pydantic
```

---

## .env

Stores:

```
OPENAI_API_KEY=your_key_here
```

---

## .gitignore

Prevents pushing:

```
venv/
.env
__pycache__/
```

to GitHub.

---

# ⚙️ Installation Guide (Step-by-step)

---

## Step 1 — Install Python

Download:
https://python.org

Check:

```
python --version
```

---

## Step 2 — Create virtual environment

Inside project folder:

### Windows

```
python -m venv venv
```

### Mac/Linux

```
python3 -m venv venv
```

---

## Step 3 — Activate

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

You should see:

```
(venv)
```

---

## Step 4 — Install dependencies

```
pip install -r requirements.txt
```

---

## Step 5 — Get OpenAI API key

Go:
https://platform.openai.com/api-keys

Create key → copy → add to `.env`

---

## Step 6 — Set spending limit (IMPORTANT)

Go:
https://platform.openai.com/settings/billing/limits

Set:

```
Hard limit = $3
```

Prevents extra charges.

---

# ▶️ How to Run

Start server:

```
uvicorn main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 How to Test

Open:

```
http://127.0.0.1:8000/docs
```

This opens Swagger UI.

Steps:

1. Click POST /generate-testcases
2. Try it out
3. Enter:

```
{
  "requirement": "User should login with email and password"
}
```

4. Execute

---

# ✅ Example Output

```
[
  {
    "title": "Valid login",
    "steps": "...",
    "expected_result": "...",
    "priority": "High"
  }
]
```

---

# 🚀 Future Improvements

You can extend this project by adding:

* structured JSON output
* save to Excel
* Jira integration
* Selenium auto test generation
* authentication
* Docker
* deploy to AWS
* UI frontend

---

# 🎯 Resume Line

Built an AI-powered test case generator using FastAPI and OpenAI GPT that converts requirements into structured QA test cases automatically.

---

# 🧠 Final Summary

This project teaches you:

👉 Backend engineering
👉 API design
👉 AI integration
👉 Production practices

Which is exactly what **AI Engineers do in real companies**.

---

Made while learning AI Engineering 🚀

----

sample prompt: {
  "requirement": "User should login using email and password. Show error if invalid credentials."
}

sample result: {
  "test_cases": "```json\n[\n    {\n        \"title\": \"Valid Login with Correct Email and Password\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Enter a valid email address in the email input field.\",\n            \"Enter the correct password in the password input field.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"User is successfully logged in and redirected to the dashboard.\",\n        \"priority\": \"High\"\n    },\n    {\n        \"title\": \"Invalid Login with Incorrect Email\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Enter an invalid email address in the email input field.\",\n            \"Enter a valid password in the password input field.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"An error message is displayed indicating invalid credentials.\",\n        \"priority\": \"High\"\n    },\n    {\n        \"title\": \"Invalid Login with Incorrect Password\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Enter a valid email address in the email input field.\",\n            \"Enter an incorrect password in the password input field.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"An error message is displayed indicating invalid credentials.\",\n        \"priority\": \"High\"\n    },\n    {\n        \"title\": \"Invalid Login with Both Email and Password Incorrect\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Enter an invalid email address in the email input field.\",\n            \"Enter an incorrect password in the password input field.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"An error message is displayed indicating invalid credentials.\",\n        \"priority\": \"High\"\n    },\n    {\n        \"title\": \"Login Attempt with Empty Email Field\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Leave the email input field empty.\",\n            \"Enter a valid password in the password input field.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"An error message is displayed indicating that the email field cannot be empty.\",\n        \"priority\": \"Medium\"\n    },\n    {\n        \"title\": \"Login Attempt with Empty Password Field\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Enter a valid email address in the email input field.\",\n            \"Leave the password input field empty.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"An error message is displayed indicating that the password field cannot be empty.\",\n        \"priority\": \"Medium\"\n    },\n    {\n        \"title\": \"Login Attempt with Both Email and Password Fields Empty\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Leave both the email and password input fields empty.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"An error message is displayed indicating that both fields cannot be empty.\",\n        \"priority\": \"Medium\"\n    },\n    {\n        \"title\": \"Login with Email Format Validation\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Enter an invalid email format (e.g., 'user@domain') in the email input field.\",\n            \"Enter a valid password in the password input field.\",\n            \"Click the 'Login' button.\"\n        ],\n        \"expected_result\": \"An error message is displayed indicating that the email format is invalid.\",\n        \"priority\": \"Medium\"\n    },\n    {\n        \"title\": \"Login Button Disabled When Fields Are Empty\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Leave both the email and password input fields empty.\"\n        ],\n        \"expected_result\": \"The 'Login' button is disabled.\",\n        \"priority\": \"Low\"\n    },\n    {\n        \"title\": \"Successful Logout After Login\",\n        \"steps\": [\n            \"Navigate to the login page.\",\n            \"Enter a valid email address in the email input field.\",\n            \"Enter the correct password in the password input field.\",\n            \"Click the 'Login' button.\",\n            \"Click the 'Logout' button.\"\n        ],\n        \"expected_result\": \"User is logged out and redirected to the login page.\",\n        \"priority\": \"Medium\"\n    }\n]\n```"
}