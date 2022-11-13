FROM python:3.7


WORKDIR /app

COPY requirements.txt requirements.txt

COPY . . 

CMD ["python3", "src/main.py"]
