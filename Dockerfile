FROM nexus3.k8s.lan:50000/python:3.9.10-slim-bullseye-webdev

# Base image is running as user python (uid:1001)
# and group python (gid:1001)

HEALTHCHECK CMD curl --fail http://localhost:5000/

USER root

COPY requirements.txt run.sh /app/
COPY pizzaapp /app/pizzaapp/

RUN chown -R python:python /app

USER python

WORKDIR /app/

RUN pip install -r requirements.txt && \
    chmod +x run.sh

# Migrate in future to gunicorn 
# instead of using flask development server

CMD ["./run.sh"]
