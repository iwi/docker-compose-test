FROM jupyter/minimal-notebook:latest

ENV LANG en_US.UTF-8
ENV LC_ALL C.UTF-8

USER root

RUN apt-get update -qq \
 && apt-get install -qqy \
       gcc \
 && apt-get autoclean \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && pip install --upgrade pip

USER jovyan

COPY requirements.txt /home/jovyan/work/requirements.txt

RUN pip install -r requirements.txt
