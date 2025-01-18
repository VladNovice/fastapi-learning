from fastapi import FastAPI, HTTPException, Response, Depends, BackgroundTasks
from authx import AuthX, AuthXConfig
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import asyncio

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_acces_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config = config)

text = """Сердце чемпиона


Теория:

Назначение практики - преодоление жалости к себе. Ты делаешь то, что думал сделать для тебя просто невозможно и фиксируешь состояние победителя.
“Сердце чемпиона” - уникальный инструмент перепрошивки психики на мыслеформы, которые ты выбрал. Прямейшая закалка духа.
“Сердце чемпиона” - не об оздоровлении, а о разъёбе физического здоровья для укрепления психического.
После систематического выполнения практики всё в жизни становится лёгким, будто ты выходишь в ринг против 5-летнего сразу после боя с Емельяненко.
Сердце чемпиона - абсолютная проекция всего, что ты делал и делаешь в жизни. Ты остаёшься один на один с собой и наконец направляешь свой взор внутрь, начиная видеть истинную суть.


Практика:

На ежедневной основе нужно выполнять такую нагрузку, которая для тебя будет выносимой, и ты сможешь её увеличивать без вреда для себя.
Минимальное время выполнения сердца чемпиона - 40 минут.
В сердце чемпиона ты выполняешь упражнения не на результат и не на скорость, а на время: главное - тренировка своей психики, ты держишься не смотря на боль чисто на менталке, продумывая все свои страхи, обиды, поражения, потери.
Можешь представлять всех своих хейтеров, стоящих рядом во время выполнения тобой практики, которые говорят “Мы же говорили, ты - никчёмен. Сдайся уже, прекрати строить из себя мужчину”. Норадреналин разорвёт твои жилы.


Задачи:
Прокачать сердце и тело кровью.
Выбить из тела всю дурь.
Впечатать в себя нужные прошивки.
Каждый раз фиксировать новые установки.
Запоминать и постепенно нормализовать для себя состояние победы, чемпиона.

План выполнения:
Составляешь план, который хочешь выполнить. Бросаешь себе вызов, чётко определяешь что тебе здесь нельзя, а что надо.
Прокачиваешь сердце кровью (статические упражнения для этого не подходят).
Тренируешь волю. С каждой минутой становится всё больнее и неприятнее, всё сильнее хочется сдаться и оставить начатое. Но ты не сдаёшься и прёшь как танк, ставя всё новые рекорды и фиксируя для себя всё бо́льшие грани возможностей."""






class UserLoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(creds: UserLoginSchema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"acces_token": token}
    raise HTTPException(status_code=401, detail="Incorrest username or password")

@app.get("/protected", dependencies=[Depends(security.access_token_required)])
async def protected():
    return {"data": "TOP SECRET"}


async def get_serchamp():
    return text

@app.get("/Гайд на сердце чемпиона")
async def some_serchamp(bg_tasks: BackgroundTasks):
    bg_tasks.add_task(get_serchamp)
    return {"message": await get_serchamp()}

    