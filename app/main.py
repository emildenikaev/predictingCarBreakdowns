from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.calculation import router as routes
from .routers.filters import router as filters

app = FastAPI(
    title="Aeroflot App"
)

app.include_router(routes)
app.include_router(filters)

# Разрешить все источники (для примера)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
