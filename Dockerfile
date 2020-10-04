
LABEL maintainer ="peaga.inc@gmail.com"
LABEL vendor = "Peaga Inc."
LABEL version = "1.1"

FROM Python:latest
ENV PYTHONUNBUFFERD 1
RUN mkdir /OllinCafe
WORKDIR /OllinCafe
ADD requirements.txt /OllinCafe/
RUN pip install - upgrade pip && pip install -r requirements.txt
ADD . /OllinCafe/