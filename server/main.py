from fastapi import FastAPI, File, UploadFile
import cloudinary
import cloudinary.uploader
import cloudinary.api

app = FastAPI()

# Configure Cloudinary
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Upload file to Cloudinary
        result = cloudinary.uploader.upload(file.file)
        return {"url": result["secure_url"]}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
