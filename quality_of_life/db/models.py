from sqlalchemy import Column, Integer, Float, String

from quality_of_life.db.database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    country = Column(String)
    continent = Column(String)
    housing = Column(Float)
    cost_of_living = Column(Float)
    startups = Column(Float)
    venture_capital = Column(Float)
    travel_connectivity = Column(Float)
    business_freedom = Column(Float)
    safety = Column(Float)
    healthcare = Column(Float)
    education = Column(Float)
    environmental_quality = Column(Float)
    economy = Column(Float)
    taxation = Column(Float)
    internet_access = Column(Float)
    leisure_and_culture = Column(Float)
    tolerance = Column(Float)
    outdoors = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    mean = Column(Float)




