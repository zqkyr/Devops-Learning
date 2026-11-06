FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install flask mysqlclient
RUN pip install flask mysqlclient
EXPOSE 5002
CMD ["python", "app.py"]
