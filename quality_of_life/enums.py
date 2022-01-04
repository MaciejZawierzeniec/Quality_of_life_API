from enum import Enum


class ScoreColumn(str, Enum):
    HOUSING = 'Housing'
    COST_OF_LIVING = 'Cost of Living'
    STARTUPS = 'Startups'
    VENTURE_CAPITAL = 'Venture Capital'
    TRAVEL_CONNECTIVITY = 'Travel Connectivity'
    COMMUTE = 'Commute'
    BUSINESS_FREEDOM = 'Business Freedom'
    SAFETY = 'Safety'
    HEALTHCARE = 'Healthcare'
    EDUCATION = 'Education'
    ENVIRONMENTAL_QUALITY = 'Environmental Quality'
    ECONOMY = 'Economy'
    TAXATION = 'Taxation'
    INTERNET_ACCESS = 'Internet Access'
    LEISURE_AND_CULTURE = 'Leisure & Culture'
    TOLERANCE = 'Tolerance'
    OUTDOORS = 'Outdoors'
    MEAN = 'mean'


class GeoHierarchy(str, Enum):
    CONTINENT = 'Continent'
    COUNTRY = 'Country'
    CITY = 'City'
