FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD . /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD  python manage.py makemigrations && python manage.py migrate
COPY . /