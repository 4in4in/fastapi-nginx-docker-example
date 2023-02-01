

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index_route():
    return "index route"

@app.get("/route1")
async def test_route_1():
    return "route 1"