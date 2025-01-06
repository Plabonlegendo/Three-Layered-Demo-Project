from dependency_injector import containers, providers

from repository.Impl.customer_repository_impl import CustomerRepositoryImpl
from services.Impl.customer_service_impl import CustomerServiceImpl


class CustomerContainer(containers.DeclarativeContainer):
    customer_repository = providers.Singleton(CustomerRepositoryImpl)
    customer_service = providers.Singleton(CustomerServiceImpl, repository= customer_repository)


class MainContainer(containers.DeclarativeContainer):
    customer_container = providers.Container(CustomerContainer)
