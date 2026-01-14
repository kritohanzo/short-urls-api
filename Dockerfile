FROM python:3.12-slim

RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install uv && uv pip install --system --no-cache-dir -r requirements.txt && uv cache clean

WORKDIR /code
COPY . /code

CMD ["python", "-m", "sources.app"]
