from pydantic import BaseModel
from typing import Optional

class RouteImpactBase(BaseModel):
    route_id: int
    event_id: int
    impact_score: float
    min_distance: float

class RouteImpactCreate(RouteImpactBase):
    pass

class RouteImpact(RouteImpactBase):
    id: int

    class Config:
        from_attributes = True
