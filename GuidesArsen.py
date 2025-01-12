from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()




Guides = [
    {
        "theme": "Гормонально нейромедиаторная теория",
        "text": "текст гайда",
    },
    {
        "theme": "Гайд по тестостерону",
        "author": "текст гайда",
    },
]

@app.get("/guidesGEt/{guide_theme}",
        tags=["Гайды"],
        summary="Получить конкретный гайд")
def get_book(theme: str):
    for guide in Guides:
        if guide["theme"] == theme:
            return guide
    raise HTTPException(status_code=404, detail="Гайд не найдена")

class GuidesCL(BaseModel):
    theme: str | None = Field(max_length=60)
    text: str

@app.get("/guides")
def get_guides():
    return Guides


