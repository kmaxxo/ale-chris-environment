FROM ubuntu:18.04

# Set the locale
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx libncurses5-dev

# We copy this file first to leverage docker cache
COPY ./requirements.txt /home/requirements.txt

WORKDIR /home/app

RUN pip3 install -r /home/requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "/home/app/app.py" ]
