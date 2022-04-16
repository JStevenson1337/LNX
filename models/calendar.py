from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Calendar:
    month: str
    date: datetime 
    name: str
    events: List[str]
    tags: List[str]
    locale: str
