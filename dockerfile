FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN pip install -r requirements.txt

WORKDIR /usr/app/src

COPY wiki_wordcount.py ./

CMD [ "python", "wiki_wordcount.py"]