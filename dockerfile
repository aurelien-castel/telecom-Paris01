FROM python:3.10-slim

RUN pip install --no-cache-dir seccomp

COPY wrapper.py /app/wrapper.py

WORKDIR /app

ENTRYPOINT ["python", "wrapper.py"]
