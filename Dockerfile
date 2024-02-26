FROM python:3.11

# Set work dir
WORKDIR /opt/app

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

COPY ./app .

CMD uvicorn main:app --host=0.0.0.0 --port 8000
