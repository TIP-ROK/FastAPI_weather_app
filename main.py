from fastapi import FastAPI
import requests
import uvicorn
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get('/{city}')
async def weather(city: str):
    """write city name. Example: biskek"""
    bishkek = requests.get(url=f'https://wttr.in/+{city}?format=j1').json()
    my_weather = {
        'maxtemp': bishkek['weather'][1]['maxtempC'],
        'mintemp': bishkek['weather'][1]['mintempC']
    }
    response_data = jsonable_encoder(my_weather)
    return {f'Weather of {city.capitalize()} today is : {response_data}'}


@app.get('/')
async def home():
    return 'Example to request is: http://localhost:8000/bishkek'


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port=8000,
        reload=True,
        host='localhost'
    )
