# Start from a base image that only has Python3.7 on it
FROM python:3.7

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]