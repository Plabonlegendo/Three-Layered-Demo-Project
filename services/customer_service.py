import abc
import json
import logging

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.customer_model import Candidate
from utils.json_serializer_util import custom_encoder


class CustomerService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_customer_profile(self, election_schedule_id: int, page: int = 1, size: int = 10):
        pass

