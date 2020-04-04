FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx libncurses5-dev curl

# We copy this file first to leverage docker cache
COPY ./requirements.txt /home/requirements.txt

WORKDIR /home/app

RUN pip3 install -r /home/requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "/home/app/app.py" ]
