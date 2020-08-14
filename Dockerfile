FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app/app

WORKDIR /app/app
RUN pip install -r requirements.txt