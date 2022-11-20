import math
import sys
import sympy
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/prime/{number}")
async def is_prime_number(number : str):
    ret = {'return': ''}
    if number.isnumeric():
        ret['return'] = sympy.isprime(number)
    return ret


@app.get("/numdiv/{number}")
async def is_max(number: int):
    return sys.maxsize