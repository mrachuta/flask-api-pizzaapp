FROM nexus3.k8s.lan:50000/python:3.9.10-slim-bullseye-webdev
  
ADD manage.py requirements.txt run.sh /app/
ADD pizzaapp /app/pizzaapp/

WORKDIR /app

RUN useradd -ms /bin/bash -u 1001 python &&\
    chown -R python:python /app &&\
    chmod +x run.sh manage.py

EXPOSE 5000
USER python

RUN pip install -r requirements.txt

CMD ["/app/run.sh"]