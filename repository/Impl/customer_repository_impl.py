from virtualenv.run import Session

from repository.customer_repository import CustomerRepository


class CustomerRepositoryImpl(CustomerRepository):

    def find_by_id(self, db: Session, customer_id):
        return {'message': 'Success'}