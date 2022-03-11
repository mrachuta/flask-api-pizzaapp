FROM python:3.9.10-slim-bullseye
  
ADD manage.py requirements.txt run.sh /app/
ADD pizzaapp /app/pizzaapp/

WORKDIR /app

RUN apt update && apt install -y libpq-dev gcc &&\
    useradd -ms /bin/bash -u 1001 python &&\
    chown -R python:python /app &&\
    chmod +x run.sh manage.py &&\
    pip install -r requirements.txt

EXPOSE 5000
USER python

CMD ["/app/run.sh"]