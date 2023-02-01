FROM python:3.10-alpine

WORKDIR /service

COPY requirements.txt .

RUN pip install --requirement requirements.txt

COPY main.py .

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
