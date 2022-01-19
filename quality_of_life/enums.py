from enum import Enum


class ScoreColumn(str, Enum):
    HOUSING = 'housing'
    COST_OF_LIVING = 'cost_of_living'
    STARTUPS = 'startups'
    VENTURE_CAPITAL = 'venture_capital'
    TRAVEL_CONNECTIVITY = 'travel_connectivity'
    COMMUTE = 'commute'
    BUSINESS_FREEDOM = 'business_freedom'
    SAFETY = 'safety'
    HEALTHCARE = 'healthcare'
    EDUCATION = 'education'
    ENVIRONMENTAL_QUALITY = 'environmental_quality'
    ECONOMY = 'economy'
    TAXATION = 'taxation'
    INTERNET_ACCESS = 'internet_access'
    LEISURE_AND_CULTURE = 'leisure_and_culture'
    TOLERANCE = 'tolerance'
    OUTDOORS = 'outdoors'
    MEAN = 'mean'


class GeoHierarchy(str, Enum):
    CONTINENT = 'continent'
    COUNTRY = 'country'
    CITY = 'city'
