FROM python:3.9.6
LABEL author='parygin' version=2.0.0
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
