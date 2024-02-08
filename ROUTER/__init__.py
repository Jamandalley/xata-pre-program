from fastapi import FastAPI
from .getpdf import router as pdf_router

app = FastAPI()

app.include_router(pdf_router)