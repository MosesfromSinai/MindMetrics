# MindMetrics

Full-stack emotional insight platform that tracks mood and attachment-related behaviors using psychology-based scoring.

## Tech Stack

- **Frontend:** Next.js, TypeScript, Chart.js
- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **Infrastructure:** Docker, AWS EC2, GitHub Actions CI/CD
- **Testing:** Pytest

## Project Structure

```
MindMetrics/
├── frontend/          # Next.js app
│   ├── src/
│   │   ├── app/              # Pages & layouts
│   │   ├── components/       # React components
│   │   ├── lib/              # API client & utilities
│   │   └── types/            # TypeScript types
│   └── Dockerfile
├── backend/           # FastAPI app
│   ├── app/
│   │   ├── api/routes/       # REST endpoints
│   │   ├── models/           # SQLAlchemy models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   └── db/               # Database config
│   ├── tests/                # Pytest tests
│   └── Dockerfile
├── docker-compose.yml
└── .github/workflows/ci.yml
```

## Getting Started

### With Docker (recommended)

```bash
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API docs: http://localhost:8000/docs

### Manual Setup

**Backend:**

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**

```bash
cd frontend
npm install
npm run dev
```

## Running Tests

```bash
cd backend
pytest
```
