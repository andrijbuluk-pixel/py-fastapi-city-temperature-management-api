from fastapi import FastAPI

from City import router as CityRouter

app = FastAPI()

app.include_router(CityRouter.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
