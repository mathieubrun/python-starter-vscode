FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt /code
RUN pip3 install -r requirements.txt

COPY . /code

RUN pytest --cov=. --cov-report=term 

ENTRYPOINT ["gunicorn", "-w", "1", "-b", ":8000", "app:create_app()"]
