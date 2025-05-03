from typing import Annotated
from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from application.db import r
from application.hash import get_hash

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    """Serve the main HTML page."""
    return FileResponse("static/index.html")


@app.get("/{short_url}")
def redirect_to_long_url(short_url: str):
    """Redirect to the original URL based on the short URL."""
    long_url = r.get(short_url)
    if long_url:
        return RedirectResponse(long_url)
    raise HTTPException(status_code=404, detail="URL not found")


@app.post("/shorten")
def shorten_url(long_url: Annotated[str, Form()], request: Request):
    """Generate a short URL for the given long URL."""
    short_code = get_hash(long_url)
    r.set(short_code, long_url)
    return f'{request.base_url}{short_code}'
