from fastapi import APIRouter

router = APIRouter()

@app.get("/")
async def root():
    return {"message": "Welcome to the myAPI. Use /user/{first_name}/{last_name} to get full name or /upload_pdf/ to upload a PDF."}

@router.get("/user/{first_name}/{last_name}")
async def get_full_name(first_name: str, last_name: str):
    full_name = f"{first_name} {last_name}"
    return {"full_name": full_name}
