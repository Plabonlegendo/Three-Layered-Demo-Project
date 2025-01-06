from fastapi import APIRouter

from controller import (
    customer_controller
)

router = APIRouter()

# routers
router.include_router(customer_controller.router)

# metadata for models
# candidate_model.Base.metadata.create_all(bind=engine)
