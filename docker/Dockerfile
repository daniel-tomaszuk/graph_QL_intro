FROM python:3.7

ENV WORKDIR '/app'
ENV MANAGEDIR 'f2f_Q3_2019'

WORKDIR ${WORKDIR}

COPY . ${WORKDIR}
RUN chmod +x ${WORKDIR}/backend-entrypoint.sh
RUN pip install -r requirements.txt

EXPOSE 8000:8000
