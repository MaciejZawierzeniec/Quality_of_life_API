from collections import defaultdict
from typing import Dict, List

from quality_of_life.enums import ScoreColumn, GeoHierarchy


def get_ranking_by(cities, get_by: GeoHierarchy, limit: int, score_column: ScoreColumn = ScoreColumn.MEAN) -> List[Dict]:
    ranking = defaultdict(float)
    for element in cities:
        ranking[getattr(element, get_by)] += getattr(element, score_column)
    return sorted(_split_by(get_by, ranking), key=lambda x: x["ranking"], reverse=True)[:limit]


def _split_by(get_by, ranking):
    return [{get_by: key, "ranking": value}
            for key, value in ranking.items()]
