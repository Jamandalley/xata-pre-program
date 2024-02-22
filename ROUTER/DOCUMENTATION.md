"""
## API Endpoint Documentation
# Description
This API provides functionality to retrieve full names based on given first and last names, as well as to upload PDF files.

# Endpoints
1. Root Endpoint
URL: /
Method: GET
Description: Returns a welcome message and instructions on how to use the API endpoints.
Response Body:

{
 `   "message": "Welcome to the myAPI. Use /user/{first_name}/{last_name} to get full name or /upload_pdf/ to upload a PDF." `
}

2. Get Full Name Endpoint
URL: /user/{first_name}/{last_name}
Method: GET
Description: Retrieves the full name by concatenating the first name and the last name provided in the URL parameters.
Parameters:
 `first_name: The first name of the user (string).`
 `last_name: The last name of the user (string).`
Response Body (Example):
{
   ` "full_name": "John Doe" `
}

3. Upload PDF Endpoint
URL: `/upload_pdf/`
Method: POST
Description: Allows users to upload a PDF file.
Request Body: The PDF file to be uploaded.
Parameters:
    `- pdf_file (UploadFile, required): The PDF file to be uploaded.`
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
Response Body (Example):
{
   ` "message": "PDF file uploaded successfully." `
}

## Response Status Codes
200 OK: Successful request.
400 Bad Request: Invalid request format or parameters.
404 Not Found: Endpoint not found.
500 Internal Server Error: Server encountered an unexpected condition.

## Usage
Send requests to the appropriate endpoint using the specified HTTP method.
Ensure correct formatting of request parameters and bodies.
Handle response status codes appropriately in your application.

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

This documentation provides an overview of the available endpoints, their descriptions, expected request parameters and bodies, and sample responses.