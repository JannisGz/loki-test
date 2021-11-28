# Dockerfile to create a Docker Image for the log_creator python app

FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

USER root

COPY ./log-creator-python .

RUN chmod 777 ./start_up.sh

ENTRYPOINT ["./start_up.sh"]