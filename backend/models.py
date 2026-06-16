from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Text
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)

    strava_id = Column(Integer, unique=True)

    name = Column(String)

    date = Column(String)

    sport_type = Column(String)

    distance_m = Column(Float)

    moving_time_s = Column(Integer)

    average_speed = Column(Float)

    elevation_gain = Column(Float)

    raw_json = Column(Text)

class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(
        Integer,
        primary_key=True
    )

    strava_id = Column(
        Integer,
        unique=True
    )

class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(
        Integer,
        primary_key=True
    )

    strava_id = Column(
        Integer,
        unique=True
    )

    access_token = Column(Text)

    refresh_token = Column(Text)

    expires_at = Column(Integer)