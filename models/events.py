from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import uuid4
from .base import BaseModel, form_field

@dataclass
class Event(BaseModel):
    date: datetime.date = form_field("date")
    time: datetime.time = form_field("time")
    summary: str = form_field("textarea")
    description: str = form_field("textarea")
