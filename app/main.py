import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.api import api_routes
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.include_router(api_routes.api_router)


origins = [
    "http://localhost:3000",  # React app
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/health")
def check_health():
    return {"message" : "Application running perfectly"}



