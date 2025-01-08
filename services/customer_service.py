import abc


class CustomerService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_customer_profile(self, election_schedule_id: int, page: int = 1, size: int = 10):
        pass

