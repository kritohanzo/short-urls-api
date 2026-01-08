FROM python:3.12-alpine

COPY ./requirements.txt .
RUN pip install uv && uv pip install --system --no-cache-dir -r requirements.txt && uv cache clean

WORKDIR /code
COPY . /code

CMD ["uvicorn", "sources.app:app", "--host", "0.0.0.0", "--port", "8000"]
