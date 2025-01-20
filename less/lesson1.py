from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/', summary="Главная ручка", tags=["основные ручки"])
def home():
    return "hello, world!"



if __name__ == "__main__":
    uvicorn.run("lesson1:app", reload=True)
