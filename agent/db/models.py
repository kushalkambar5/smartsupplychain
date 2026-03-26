from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from agent.db.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    lat = Column(Float)
    lon = Column(Float)
    radius_km = Column(Float)
    severity = Column(String)
    start_time = Column(DateTime)
    duration = Column(Integer)
    confidence = Column(Float)
    source = Column(String)

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    points = relationship("RoutePoint", back_populates="route")
    impacts = relationship("RouteImpact", back_populates="route")
    risk_results = relationship("RiskResult", back_populates="route")

class RoutePoint(Base):
    __tablename__ = "route_points"

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    lat = Column(Float)
    lon = Column(Float)
    sequence = Column(Integer)

    route = relationship("Route", back_populates="points")

class RouteImpact(Base):
    __tablename__ = "route_impacts"

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    impact_score = Column(Float)
    min_distance = Column(Float)

    route = relationship("Route", back_populates="impacts")
    event = relationship("Event")

class RiskResult(Base):
    __tablename__ = "risk_results"

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    risk_score = Column(Float)
    delay = Column(Integer)
    action = Column(String)
    created_at = Column(DateTime)

    route = relationship("Route", back_populates="risk_results")
