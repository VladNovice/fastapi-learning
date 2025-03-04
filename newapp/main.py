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


@app.post("/multipe_files")
async def upload_files(uploaded_files: list[UploadFile]):
    for uploaded_file in uploaded_files:
        file = uploaded_file.file
        filename = uploaded_file.filename

        with open(f"1_{filename}", "wb") as f:
           f.write(file.read())