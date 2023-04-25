FROM python:3.10

WORKDIR /app_user

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5001"]
