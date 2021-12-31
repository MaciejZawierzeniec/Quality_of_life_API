from typing import Dict, List

from quality_of_life.repo.repository import read_dataset


def get_city_ranking(limit: int) -> List[Dict]:
    qol = read_dataset("quality_of_life_extended.csv")
    ranking = [
        {"city": element[0], "ranking": element[1]}
        for element in list(zip(qol["UA_Name"], qol["mean"]))
    ]
    return sorted(ranking, key=lambda x: x["ranking"], reverse=True)[:limit]
