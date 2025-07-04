
FROM python:3.11-slim

WORKDIR /app

COPY backend /app/backend
COPY app.py /app/
COPY .env /app/

RUN pip install --no-cache-dir flask flask-cors psycopg[binary] python-dotenv requests pycountry google-genai

CMD ["python", "app.py"]