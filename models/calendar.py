from dataclasses import dataclass
from datetime import datetime
from typing import List
from privacystate import Privacy

@dataclass
class Calendar:
    month: str
    date: datetime 
    name: str
    events: List[str]
    tags: List[str]
    locale: str
    privacy: Privacy

@classmethod
def fields(cls):
    return [
        field.name
        for field in fields(cls)
    ]

@classmethod
def privatefields(cls):
    return [
        field.name
        for field in fields(cls)
        if field.name not in ["_uid", "locale"]
    ]
