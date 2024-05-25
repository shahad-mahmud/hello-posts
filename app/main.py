from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs import app_configs, settings

app = FastAPI(**app_configs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

app.get("/")(lambda: {"message": "Hello World"})
