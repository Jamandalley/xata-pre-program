from fastapi import APIRouter

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    save_directory = "pdf_files"
    os.makedirs(save_directory, exist_ok=True)
    file_path = os.path.join(save_directory, pdf_file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await pdf_file.read())
    return {"message": "PDF file uploaded successfully", "file_name": pdf_file.filename}
