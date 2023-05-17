FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

ENV DOTENV_PATH=/app/.env

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]

