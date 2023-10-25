FROM python:3.12.0-bookworm

WORKDIR /app

COPY . /app

CMD ["python", "generate_text.py"] 
