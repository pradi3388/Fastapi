from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/predict")
async def root():
    return {"message": "Hello World"}

@app.get("/predict")
async def root():
    return {"message": "Hello India"}