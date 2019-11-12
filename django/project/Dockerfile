FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update
RUN apt-get upgrade -f -y --force-yes
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/