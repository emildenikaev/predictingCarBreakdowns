from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.calculation import router as routes

app = FastAPI(
    title="PGK"
)

app.include_router(routes)

# Разрешить все источники (для примера)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
