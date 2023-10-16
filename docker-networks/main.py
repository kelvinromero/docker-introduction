from fastapi import FastAPI
from redis import Redis

app = FastAPI()
redis = Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"hello": "world!"}


@app.get("/search") # /search?query=abc
def search(query: str):
    redis.lpush("search_history", query)
    return {"query": query}


@app.get("/search/history")
def search_history():
    return redis.lrange("search_history", 0, -1)