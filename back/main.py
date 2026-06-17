from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendRequest(BaseModel):
    mood: str
    activity: str
    tempo: str

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/recommend")
def recommend(data: RecommendRequest):

    if data.activity == "Studying":
        return {
            "genre": "Lo-fi Hip Hop",
            "artists": ["Nujabes", "Jinsang", "Idealism"],
            "reason": "Great for concentration."
        }

    elif data.activity == "Driving":
        return {
            "genre": "City Pop",
            "artists": ["Mariya Takeuchi", "Miki Matsubara"],
            "reason": "Perfect for driving."
        }

    elif data.activity == "Exercising":
        return {
            "genre": "Rock",
            "artists": ["Muse", "Green Day"],
            "reason": "Boosts energy."
        }

    return {
        "genre": "R&B",
        "artists": ["Crush", "Daniel Caesar"],
        "reason": "Comfortable everyday listening."
    }