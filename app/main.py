from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import router as api_router
from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.metrics.prometheus import metrics

setup_logging(settings.log_level)

app = FastAPI(title=settings.app_name)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

api.include_router(api_router)
api.include_router(health_router)

@app.get("/metrics")
def prometheus_metrics():
    return Response(metrics(), media_type="text/plain")

