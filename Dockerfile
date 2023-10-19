FROM nexus3.k8s.lan:50000/python:3.9.10-slim-bullseye-webdev

# Base image is running as user python (uid:1001)
# and group python (gid:1001)

ENV CONUSER=python \
    CONGROUP=python

ADD --chown=${CONUSER}:${CONGROUP} requirements.txt run.sh /app/
ADD --chown=${CONUSER}:${CONGROUP} pizzaapp /app/pizzaapp/

WORKDIR /app/

RUN rm -rf pizzaapp/migrations && \
    pip install -r requirements.txt && \
    chmod +x run.sh && \

CMD ["./run.sh"]
