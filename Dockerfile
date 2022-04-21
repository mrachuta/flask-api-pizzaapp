FROM nexus3.k8s.lan:50000/python:3.9.10-slim-bullseye-webdev

# Base image is running as user python (uid:1001)
# and group python (gid:1001)

ENV CONUSER=python \
    CONGROUP=python

ADD --chown=${CONUSER}:${CONGROUP} manage.py requirements.txt run.sh /app/
ADD --chown=${CONUSER}:${CONGROUP} pizzaapp /app/pizzaapp/

RUN chmod +x run.sh manage.py &&\
    pip install -r requirements.txt

CMD ["./run.sh"]
