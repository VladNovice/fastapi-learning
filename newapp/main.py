from fastapi import FastAPI, UploadFile

from pydantic import BaseModel, Field


app = FastAPI()

# ЗАГРУЗКА ДАННЫХ

@app.post("/files")
async def upload_file(uploaded_file: UploadFile):
    file = uploaded_file.file
    filename = uploaded_file.filename

    with open(f"1_{filename}", "wb") as f:
        f.write(file.read())