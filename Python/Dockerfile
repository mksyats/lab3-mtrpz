FROM python:3.12.3-bullseye

WORKDIR /app

COPY . /app

RUN pip install -r requirements/requirements.txt

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
