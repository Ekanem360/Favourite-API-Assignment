from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to my API"

@app.get("/about")
def get_about():
    return {
        "name": "ETIDO EKANEM",
        "age": 20,
        "city": "Port Harcourt"
    }

@app.get("/hobbies")
def get_hobbies():
    return ["Coding", "Football", "Reading", "Gaming", "Music"]

@app.get("/favorite-food")
def get_favorite_food():
    return {
        "name": "Jollof Rice and Turkey",
        "origin": "West Africa",
        "spicy": True
    }

@app.get("/skills")
def get_skills():
    return [
        {"skill": "Python", "level": "intermediate"},
        {"skill": "FastAPI", "level": "beginner"},
        {"skill": "SQL", "level": "intermediate"},
        {"skill": "Git", "level": "intermediate"}
    ]

