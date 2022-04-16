from datetime import datetime
from typing import List
from dataclasses import dataclass, fields


@dataclass
class Events:
    _uid: str
    title: str
    date: datetime.date
    time: datetime.time
    summary: str
    description: str
    tags: List[str]
    locale: str

    @classmethod
    def fields(cls):
        return [
            field.name
            for field in fields(cls)
            if not field.name.startswith("_")
        ]
