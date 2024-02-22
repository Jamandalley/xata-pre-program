# Author Name: Abimbade Jamiu A., 
# email: jamiuabimbade@gmail.com
# API Documentation:  https://fastapi.tiangolo.com
import uvicorn
from fastapi import FastAPI
from router.getname import router as get_fullname
from router.getpdf import router as get_pdf

app = FastAPI()

app.include_router(get_fullname.router)
app.include_router(get_pdf.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
