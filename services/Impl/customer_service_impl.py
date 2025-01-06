from sqlalchemy.orm import Session

from repository.customer_repository import CustomerRepository
from services.customer_service import CustomerService


class CustomerServiceImpl(CustomerService):
    def __init__(self, repository: CustomerRepository):
        self.repository: CustomerRepository = repository

    def get_customer_profile(self, db: Session, customer_id: int):
        return self.repository.find_by_id(db, customer_id)