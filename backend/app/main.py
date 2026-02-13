from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import mood, journal, health
from app.config import settings

app = FastAPI(
    title="MindMetrics API",
    description="Emotional insight platform API for tracking mood and attachment-related behaviors",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])
app.include_router(mood.router, prefix="/api/v1/moods", tags=["moods"])
app.include_router(journal.router, prefix="/api/v1/journals", tags=["journals"])
