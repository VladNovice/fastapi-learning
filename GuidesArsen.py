from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()




Guides = [
    {
        "theme": "Гормонально нейромедиаторная теория",
        "text": "none, null",
    },
    {
        "theme": "Гайд по тестостерону",
        "author": "none, null",
    },
]


class GuidesCL(BaseModel):
    theme: str | None = Field(max_length=60)
    text: str

@app.get("/guides")
def get_guides():
    return Guides


