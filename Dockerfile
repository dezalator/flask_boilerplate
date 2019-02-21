FROM python:3.7-slim-stretch
RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN apt-get -y install gcc

COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install gunicorn
VOLUME [ "/code" ]
COPY . /code/
COPY docker /code/docker
CMD ["/code/docker/start.sh"]

