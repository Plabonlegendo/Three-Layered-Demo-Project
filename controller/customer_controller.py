import fastapi
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from configuration.bean_container import MainContainer
from configuration.db.db_config import get_db
from services.customer_service import (
    CustomerService
)

from dependency_injector.wiring import Provide, inject


router = fastapi.APIRouter(prefix="/online-karze-hasanah-system/api/v1/private")


@router.get("/customers", response_model=dict, tags=["customers"])
@inject
def get_customer_profile(
        customer_id: int,
        db: Session = Depends(get_db),
        customer_service: CustomerService = Depends(Provide[MainContainer.customer_container.customer_service])
        # payload: dict = Depends(decode_token)
):
    result = customer_service.get_customer_profile(db=db, customer_id=customer_id)

    return jsonable_encoder(result)
