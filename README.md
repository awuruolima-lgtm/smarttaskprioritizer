# Smart Task Prioritizer

A Python FastAPI project that prioritizes tasks based on urgency, importance, complexity, and due dates.

## Features

- Add tasks with urgency, importance, complexity, and due date
- Prioritize tasks automatically
- REST API endpoints with FastAPI
- Uses SQLite as database (or any DB you configure)

## Requirements

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Installation

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn backend.app:app --reload
