from fastapi import FastAPI

app  = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello FastAPI"}

data = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25},
    {"id": 3, "name": "Alice Johnson", "age": 28},
]