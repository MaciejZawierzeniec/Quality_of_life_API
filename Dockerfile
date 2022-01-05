FROM python:3.8.12-slim-buster
WORKDIR /code
COPY quality_of_life /code/quality_of_life
COPY quality_of_life_extended.csv requirements.txt  /code/
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt
CMD ["python", "-m", "quality_of_life"]
