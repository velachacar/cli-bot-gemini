# CLI Bot Gemini -- Full-Stack Project

FastAPI backend + React (Vite) frontend

## 📁 Project Structure

    cli-bot-gemini/
     ├── backend/         # FastAPI app (uv + virtual environment)
     └── frontend/        # React + Vite app

------------------------------------------------------------------------

## 🚀 Getting Started

This project contains two independent environments:

-   **Backend:** Python + FastAPI (managed with `uv`)
-   **Frontend:** React + Vite (managed with `npm`)

------------------------------------------------------------------------

# 🐍 Backend (FastAPI)

### Requirements

-   Python 3.10+
-   [`uv`](https://github.com/astral-sh/uv)

### Install dependencies

``` bash
cd backend
uv sync
```

### Run dev server

``` bash
uv run uvicorn app.api.main:app --host 127.0.0.1 --port 8000
```

FastAPI will run at:

http://127.0.0.1:8000

API docs:

-   Swagger → /docs
-   ReDoc → /redoc

------------------------------------------------------------------------

# ⚛️ Frontend (React + Vite)

### Requirements

-   Node.js 18+
-   npm

### Install dependencies

``` bash
cd frontend
npm install
```

### Run dev server

``` bash
npm run dev
```

Vite runs at:

http://localhost:5173

------------------------------------------------------------------------

# 🔗 Full-Stack Development

Run both servers in two terminals:

### Backend

``` bash
cd backend
source .venv/Scripts/activate.fish
uv run uvicorn app.api.main:app --host 127.0.0.1 --port 8000
```

If you want to deactivate the virtual environment, just use deactivate:

``` bash
deactivate
```

### Frontend

``` bash
cd frontend
npm run dev
```

------------------------------------------------------------------------

# 🔐 Environment Variables

This repo ignores environment files:

    .env
    .env.*

Backend secrets go in:

    backend/.env

Frontend secrets go in:

    frontend/.env

(Vite requires variables to start with `VITE_`.)

------------------------------------------------------------------------

## 🔐 Using the Gemini API Key

To enable the backend to use Google Gemini:

### 1. Create your API key in Google AI Studio

1.  Go to **Google AI Studio**:\
    https://aistudio.google.com

2.  Sign in with your Google account.

3.  In the left sidebar, click **"API keys"**.

4.  Click **"Create API key"**.

5.  Choose **"Create API key in new project"** or select an existing
    Google Cloud project.

6.  Copy your newly created **Gemini API key**.
    
### 2. Add your Gemini API key to `backend/.env`

Create the file if it doesn't exist:

    backend/.env

Insert your key:

    GEMINI_API_KEY=your_api_key_here

------------------------------------------------------------------------

# 📄 License

MIT License.