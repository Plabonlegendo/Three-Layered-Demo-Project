import logging
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from configuration.bean_container import MainContainer
from configuration.cors_config import get_cors_middleware
from controller import customer_controller
from route.api_router import router

load_dotenv()
FILE_PATH_URL = os.getenv("FILE_PATH_URL")

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def create_app() -> FastAPI:
    app = FastAPI(
        title="API Documentation",
        description="Online Karzhe Hasanah System",
        version="0.1.0",
        debug=True
    )

    container = MainContainer()
    container.wire(modules=[customer_controller])

    return app

app = create_app()
app.add_middleware(get_cors_middleware)

# routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8802, workers=18)
