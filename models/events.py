from dataclasses import dataclass
from datetime import datetime
from .base import BaseModel, form_field

@dataclass
class Event(BaseModel):
    date: datetime.date = form_field("date")
    time: datetime.time = form_field("time")
    summary: str = form_field("textarea")
    description: str = form_field("textarea")
