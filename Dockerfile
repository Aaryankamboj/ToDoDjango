FROM ubuntu
WORKDIR /app
COPY requirements.txt /app
COPY todo_site /app/todo_site

RUN apt-get update && \
    apt install -y python3 python3-pip && \
    pip install -r requirements.txt

WORKDIR /app/todo_site

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
