from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    type: str
    lat: float
    lon: float
    radius_km: float
    severity: str
    start_time: datetime
    duration: int
    confidence: float
    source: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        from_attributes = True
