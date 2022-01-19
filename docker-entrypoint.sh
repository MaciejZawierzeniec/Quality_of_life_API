#!/bin/sh
set -e

./wait-for-it.sh db:5432 &


python quality_of_life/db/populate_db.py &
python -m quality_of_life &
pytest --cov=quality_of_life --cov-fail-under=65 tests/unit/api/endpoints/test_ranking.py
# tail -f /dev/null
