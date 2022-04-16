from dataclasses import field
from typing import List
from .base import BaseModel
from .events import Event

class Calendar(BaseModel):
    _events: List[Event] = field(default_factory=list)
