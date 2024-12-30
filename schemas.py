from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class User(BaseModel):
    id: int
    address: str
    fullname: int
    age: int
    email: str


class ReadUser(BaseModel):
    id: int
    address: str
    fullname: int
    age: int
    email: str
    class Config:
        from_attributes = True


