from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import requests

app = FastAPI()


BASE_URL = 'https://api.coingecko.com/api/v3'


class CryptoStandart(BaseModel):
    crypto: str = Field(max_length=30)
    price: float

@app.get("/crypto", response_model=CryptoStandart)
def crypto_price(crypto_name: str):
    response = requests.get(f"{BASE_URL}/simple/price?ids={crypto_name}&vs_currencies=usd")
    data = response.json()

    price = data[crypto_name]

    if crypto_name not in data:
        raise HTTPException(status_code=404, detail="Криптовалюта не найдена")
    
    

    return {
        "crypto": crypto_name,
        "price": price
    }


print("dsxhujgisdfbvghusdghjsbfhjsdgfhkdsvhfgjsdv")
