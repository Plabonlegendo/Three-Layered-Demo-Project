import logging

from fastapi import Request

from main import app

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    log.info(f"Request Path: {request.url.path}")

    response = await call_next(request)

    log.info(f"Response: {response.status_code}")
    return response
