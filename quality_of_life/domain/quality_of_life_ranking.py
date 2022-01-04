from collections import defaultdict
from typing import Dict, List

from quality_of_life.enums import ScoreColumn, GeoHierarchy
from quality_of_life.repo.repository import read_dataset


def get_ranking_by(get_by: GeoHierarchy, limit: int, score_column: ScoreColumn = ScoreColumn.MEAN) -> List[Dict]:
    qol = read_dataset("quality_of_life_extended.csv")
    ranking = defaultdict(float)
    for element in list(zip(qol[get_by], qol[score_column])):
        ranking[element[0]] += element[1]
    return sorted(_split_by(get_by, ranking), key=lambda x: x["ranking"], reverse=True)[:limit]


def _split_by(get_by, ranking):
    return [{get_by: key, "ranking": value}
            for key, value in ranking.items()]
