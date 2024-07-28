from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")

def home():
    return {"Hello": "World"}

@app.get("/about")

def about():
    return {"About": "This is a FastAPI project"}




  
  
  

