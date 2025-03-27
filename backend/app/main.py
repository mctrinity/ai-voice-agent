from fastapi import FastAPI
from app.api.routes import calls

app = FastAPI()

app.include_router(calls.router, prefix="/calls")


@app.get("/")
def root():
    return {"message": "AI Voice Agent backend is running"}
