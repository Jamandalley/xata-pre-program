from fastapi import FastAPI
from .getpdf import router as name_router

app = FastAPI()

app.include_router(name_router)
