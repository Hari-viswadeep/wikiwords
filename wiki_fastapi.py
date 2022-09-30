from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def read_root(query):
    return query