from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()



data = {
    "email": "PaulDurov@gmail.com",
    "bio": "govnoel",
    "age": 40,
}

data_not_age = {
    "email": "PaulDurov@gmail.com",
    "bio": "govnoel",
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra="forbid")
 

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "Юзер добавлен"}

@app.get("/users")
def get_user() -> list[UserSchema]:
    return users 




#class UserAgeSchema(UserSchema):
#    age: int = Field(ge=0, le=130)


