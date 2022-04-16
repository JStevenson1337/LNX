from dataclasses import dataclass, field
from typing import List
from .base import BaseModel
from .events import Event

@dataclass
class Calendar(BaseModel):
    _events: List[Event] = field(default_factory=list)
