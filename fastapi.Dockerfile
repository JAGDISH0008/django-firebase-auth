FROM python:3.8
WORKDIR /code
COPY fastapi.requirements.txt /code/
RUN pip install -r fastapi.requirements.txt
COPY fastapi /code/