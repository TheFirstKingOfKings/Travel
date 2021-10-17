FROM ubuntu:20.04

LABEL maintainer="ankoz2000@mail.ru"

RUN apt-get update -y
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

WORKDIR /usr/src/app

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "./run.py"]

