from fastapi import FastAPI
from .getpdf import router as get_pdf

app = FastAPI()

app.include_router(get_pdf)