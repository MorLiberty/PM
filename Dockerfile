FROM docker.elastic.co/beats/filebeat:7.5.0
WORKDIR ~
USER root
RUN yum -y install python3
RUN yum -y install wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install -U numpy
ADD Logs.py /
RUN chmod 777 /Logs.py
CMD ["python3","/Logs.py"]