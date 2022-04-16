from dataclass import dataclass
from datetime import datetime


@dataclass
class Events():
    uid: str
    title: str
    date: datetime.date
    time: datetime.time
    summary: str
    description: str
    tags: List[str]
    locale: str