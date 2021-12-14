FROM python:3
RUN apt-get update -y

#RUN apt-get install -y python3-pip

RUN python --version
RUN pip --version

RUN python -m pip install --upgrade pip

RUN pip --version

ADD myToyota.py /
ADD myToyotaNew.py /
ADD myt.json /configs/
ADD requirements.txt /
ADD statistics.py /
ADD toyota.py /

RUN pip install -r requirements.txt
RUN pip install mytoyota

#CMD [ "python3", "./myToyota.py" ]

#CMD [ "python3", "./myToyotaNew.py" ]

CMD  [ "python3", "./toyota.py" ]
