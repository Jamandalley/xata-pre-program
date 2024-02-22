# PDF File Upload API

This API endpoint allows users to upload PDF files to the server. The uploaded PDF files will be stored in a directory named "pdf_files".

## API Endpoint
The API endpoint for uploading PDF files is: `/upload_pdf/`

## Request
To upload a PDF file, make a POST request to the `/upload_pdf/` endpoint. The file should be sent as a multipart/form-data request.

### Request Body
| Parameter | Type | Description |
|-----------|------|-------------|
| pdf_file | File | The PDF file to be uploaded. |

## Response
The API
{
    "message": "PDF file uploaded successfully",
    "file_name": "example.pdf"}

## Installation

1. Clone the repository: 

```bash
git clone https://github.com/Jamandalley/xata-pre-program.git
