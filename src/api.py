from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os

app = FastAPI()

PAGES_SUB_PATH = os.getenv("PAGES_SUB_PATH", "pages")

directory_path = f"{os.path.dirname(__file__)}/{PAGES_SUB_PATH}"

app.mount("/site", StaticFiles(directory=directory_path), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/site/index.html")