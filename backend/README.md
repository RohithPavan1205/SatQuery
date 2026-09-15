# SatQuery AI - Backend Foundation

## 1. Backend Purpose
This directory contains the foundational backend service for Team 2 of the SatQuery AI project. The backend will eventually serve as the main controller, API layer, and orchestration service for the vision-language models, geospatial queries, and agentic workflows.

## 2. Technology Stack
- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Testing:** pytest

## 3. Directory Structure
```
backend/
├── app/                  # Application code
│   ├── __init__.py
│   └── main.py           # FastAPI main application
├── tests/                # Test suite
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable placeholders
└── README.md             # This document
```

## 4. Development Environment Setup
The backend uses a standard Python virtual environment.
1. Navigate to the backend directory: `cd backend`
2. Create a virtual environment: `python3 -m venv .venv`
3. Activate the virtual environment:
   - On Mac/Linux: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`

## 5. Installing Dependencies
With the virtual environment activated, install the required packages:
```bash
pip install -r requirements.txt
```

## 6. Starting the Development Server
To start the FastAPI development server, run:
```bash
uvicorn app.main:app --reload
```
The API will be accessible at `http://127.0.0.1:8000`. You can check the health endpoint at `http://127.0.0.1:8000/health`.

## 7. Running Tests
Tests are located in the `tests/` directory. Run the test suite using pytest:
```bash
pytest
```

## 8. Current Development Status
This is purely a **development foundation**. It contains a minimal FastAPI setup to verify the environment works (via the `/health` endpoint). **No core application logic is implemented yet.** It does not connect to a database, no models are integrated, and no fake functionalities or mock data are used.

## 9. Planned Future Modules
The following modules are planned and are **NOT implemented yet**:
- **API routes**: Endpoints for queries, dataset ingestion, and GIS operations.
- **Input validation**: Schema definitions and validation logic.
- **Agent/controller integration**: Orchestration of workflows.
- **Task queue**: Background processing for long-running model and spatial tasks.
- **Storage**: Database connections and raw data storage.
- **Model service integration**: Interfacing with vision-language models and ML services.
- **Evaluation**: Metrics and reporting logic.
