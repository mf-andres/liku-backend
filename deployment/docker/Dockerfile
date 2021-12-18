FROM python:3.9-slim-buster

## Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Setup project
COPY ./liku_backend /liku_backend

# Run server
CMD ["uvicorn", "liku_backend.entrypoint.app:app", "--host", "0.0.0.0", "--port", "8000"]
