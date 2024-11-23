FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libjpeg-dev \
    libopenjp2-7-dev \
    libffi-dev \
    libglib2.0-dev \
    supervisor

WORKDIR /app

COPY . /app
RUN mkdir -p /app/logs
RUN pip install -r requirements.txt
RUN chmod +x /app/start.sh
CMD ["sh", "start.sh"]