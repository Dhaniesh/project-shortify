from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import redis
import os
import hashlib
import uuid
redis_host = os.environ.get("REDIS_HOST")
redis_port = os.environ.get("REDIS_PORT")

r = redis.Redis(host=redis_host, port=redis_port)


def get_hash(long_url):
    salt = uuid.uuid4()
    hash_object = hashlib.sha256((long_url + str(salt)).encode())
    short_code = hash_object.hexdigest()[:8]
    return short_code


try:
    r.ping()
    print("Connected to Redis successfully!")
    r.set('mykey', 'Hello from Python and Redis!')
    value = r.get('mykey')
    print(f"Value from Redis: {value.decode()}")
except redis.exceptions.ConnectionError as e:
    print(f"Could not connect to Redis: {e}")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
def get_root():
    return FileResponse("static/index.html")


@app.get('/{short_url}')
def get_root(short_url):
    long_url = r.get(short_url)
    if long_url:
        return RedirectResponse(long_url.decode())
        # return long_url
    else:
        return "no urls found"


@app.post('/shortern')
def shortern_url(long_url: Annotated[str, Form()], request: Request):
    short_code = get_hash(long_url)
    r.set(short_code, long_url)
    return f'{request.base_url}{short_code}'
