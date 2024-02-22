# Author Name: Abimbade Jamiu A., 
# email: jamiuabimbade@gmail.com
# API Documentation:  https://fastapi.tiangolo.com
import uvicorn
from fastapi import FastAPI
from routers import getname, getpdf

app = FastAPI()

app.include_router(getname.router)
app.include_router(getpdf.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
