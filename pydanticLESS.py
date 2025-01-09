from pydantic import BaseModel, Field, EmailStr

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
 

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)


print(repr(UserAgeSchema(**data)))
print(repr(UserSchema(**data_not_age)))