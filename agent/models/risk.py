from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RiskResultBase(BaseModel):
    route_id: int
    risk_score: float
    delay: int
    action: str
    created_at: datetime

class RiskResultCreate(RiskResultBase):
    pass

class RiskResult(RiskResultBase):
    id: int

    class Config:
        from_attributes = True
