
FROM python:3
RUN apt-get update -y
#RUN apt-get install -y python3-pip

ADD myToyota.py /
ADD myt.json /configs/
ADD requirements.txt /
ADD statistics.py /
ADD toyota.py /

RUN pip install -r requirements.txt
RUN pip install mytoyota

#CMD [ "python3", "./myToyota.py" ]

CMD  [ "python3", "./toyota.py" ]
