#!/bin/sh
set -e

./wait-for-it.sh db:5432 &


python quality_of_life/db/populate_db.py &
python -m quality_of_life
# tail -f /dev/null
