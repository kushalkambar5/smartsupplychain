from pydantic import BaseModel
from typing import List, Optional

class RoutePointBase(BaseModel):
    lat: float
    lon: float
    sequence: int

class RoutePointCreate(RoutePointBase):
    route_id: int

class RoutePoint(RoutePointBase):
    id: int
    route_id: int

    class Config:
        from_attributes = True

class RouteBase(BaseModel):
    name: str

class RouteCreate(RouteBase):
    pass

class Route(RouteBase):
    id: int
    points: List[RoutePoint] = []

    class Config:
        from_attributes = True
