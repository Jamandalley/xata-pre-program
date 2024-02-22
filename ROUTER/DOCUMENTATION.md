"""
API Documentation: Upload PDF Endpoint

This endpoint allows users to upload PDF files to the server.

Endpoint:
    POST /upload_pdf/

Parameters:
    - pdf_file (UploadFile, required): The PDF file to be uploaded.

Returns:
    - JSON response containing:
        - message (str): A message indicating the status of the file upload.
        - file_name (str): The name of the uploaded PDF file.

Example Usage:
    ```python
    import requests

    url = "http://localhost:8000/upload_pdf/"
    files = {'pdf_file': open('example.pdf', 'rb')}
    response = requests.post(url, files=files)
    print(response.json())
    ```
"""

from fastapi import APIRouter, UploadFile, File
import os

# Initialize API router
router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    """
    Endpoint to upload PDF files.

    Parameters:
        pdf_file (UploadFile): The PDF file to be uploaded.

    Returns:
        dict: A JSON response indicating the status of the file upload.

    Raises:
        HTTPException: If the file upload fails.

    Example:
        $ curl -X 'POST' \
          'http://localhost:8000/upload_pdf/' \
          -H 'accept: application/json' \
          -H 'Content-Type: multipart/form-data' \
          -F 'pdf_file=@/path/to/your/file.pdf'
    """
    # Define directory to save the PDF files
    save_directory = "pdf_files"
    os.makedirs(save_directory, exist_ok=True)
    
    # Save the file to disk
    file_path = os.path.join(save_directory, pdf_file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await pdf_file.read())
    
    # Return success message
    return {"message": "PDF file uploaded successfully", "file_name": pdf_file.filename}
