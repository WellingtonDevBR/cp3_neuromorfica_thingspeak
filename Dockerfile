FROM python:3.7


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install mysql-connector-python
RUN pip install mysql-connector-python

COPY . . 

CMD ["python3", "src/repository/mysql.py"]
