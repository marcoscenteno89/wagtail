FROM python:3.7
LABEL maintainer="marcoscenteno89@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD . /app/

# RUN python manage.py migrate
RUN useradd wagtail
RUN chown -R wagtail /app
USER wagtail

# EXPOSE 8000
# CMD gunicorn serve.wsgi:application --bind 0.0.0.0:8000 --workers 3