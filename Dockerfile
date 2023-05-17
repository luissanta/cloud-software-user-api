FROM python:3.10

WORKDIR /app_user

COPY .env.local /app_user/.env

RUN export $(cat /app_user/.env | xargs)

COPY . /app_user

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "-w", "2", "--threads", "2", "wsgi:app"]
