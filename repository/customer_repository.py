import abc

from virtualenv.run import Session


class CustomerRepository(metaclass=abc.ABCMeta):
    def find_by_id(self, db: Session, customer_id):
        pass