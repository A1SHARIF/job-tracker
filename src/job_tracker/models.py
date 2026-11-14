from dataclasses import dataclass
from datetime import date
from enum import Enum


class Status(Enum):
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    ASSESSMENT = "assessment"
    OFFER = "offer"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"


@dataclass
class Application:
    company: str
    role: str
    applied_on: date
    status: Status = Status.APPLIED
    follow_up_on: date | None = None
    notes: str = ""
