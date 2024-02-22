from fastapi import FastAPI
from .getpdf import router as full_name_router

app = FastAPI()

app.include_router(full_name_router)
