from fastapi import FastAPI,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from PIL import Image
import pytesseract
from ocr import extract_aadhaar_data

app=FastAPI()
Uploads_dir="uploads"
os.makedirs(Uploads_dir,exist_ok=True)
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.post("/upload-aadhaar") 
async def upload_aadhaar(file: UploadFile =File(...)):
    file_path = os.path.join(Uploads_dir,file.filename)

    with open (file_path,"wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
    image=Image.open(file_path)
    text = pytesseract.image_to_string(image)
    parsed = extract_aadhaar_data(text)
    return{
        "filename":file.filename,
        "extracted text":text,
        "parsed": parsed,
        "message":"File uploaded succesfully"
    }
