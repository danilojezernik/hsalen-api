from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse, FileResponse
import os

router = APIRouter()

# Folder to store uploaded files
PHOTO_FOLDER = "src/media/uploads/"

# TESTING ROUTE
@router.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        # Check if the uploads folder exists, and create it if not
        if not os.path.exists(PHOTO_FOLDER):
            os.makedirs(PHOTO_FOLDER)

        # Save the uploaded file to the uploads folder
        file_path = os.path.join(PHOTO_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        print(os.path.join(PHOTO_FOLDER, file.filename))

        return JSONResponse(content={"message": "File uploaded successfully", "path": os.path.join(PHOTO_FOLDER, file.filename)})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/photos/{photo_name}")
async def get_photo(photo_name: str):
    photo_path = os.path.join(PHOTO_FOLDER, photo_name)

    # Check if the photo exists
    if os.path.exists(photo_path):
        return FileResponse(photo_path, headers={"Content-Type": "image/jpeg"})  # Adjust the Content-Type based on your photo format
    else:
        return JSONResponse(content={"error": "Photo not found"}, status_code=404)
