from typing import List
from .base import BaseModel
from .events import Event

class Calendar(BaseModel):
    _events: List[Event]
