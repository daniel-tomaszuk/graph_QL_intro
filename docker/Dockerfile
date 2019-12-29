FROM python:3.7-buster

ENV WORKDIR '/app'
ENV MANAGEDIR 'f2f_Q3_2019'

WORKDIR ${WORKDIR}

COPY ${MANAGEDIR} ${WORKDIR}
RUN pip install -r requirements.txt
RUN chmod +x backend-entrypoint.sh

RUN echo 'alias clc="clear"' >> ~/.bashrc

EXPOSE 8000:8000
