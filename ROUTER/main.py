# Author Name: Abimbade Jamiu A., 
# email: jamiuabimbade@gmail.com
# API Documentation:  https://fastapi.tiangolo.com

from fastapi import FastAPI
from .getpdf import router as get_pdf

app = FastAPI()

app.include_router(get_pdf)
