FROM python:3.12.3
LABEL authors="DomoLabo"

RUN pip install "paho-mqtt<2.0.0"

WORKDIR /app
COPY ./Application.py ./MQTTConfig.py ./Objects.py ./Request.py ./main.py /app

RUN chown -R 5000:5000 /app

ENTRYPOINT ["python", "main.py"]
