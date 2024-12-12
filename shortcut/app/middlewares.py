from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware as cors_middleware

from app.settings import Settings


def add_cors_middleware(app: FastAPI, settings: Settings):
    app.add_middleware(
        cors_middleware,
        allow_origins=settings.ALLOW_ORIGINS,
        allow_credentials=settings.ALLOW_CREDENTIALS,
        allow_methods=settings.ALLOW_METHODS,
        allow_headers=settings.ALLOW_HEADERS,
    )
