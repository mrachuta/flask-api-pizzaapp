FROM nexus3.k8s.lan:50000/python:3.9.10-slim-bullseye-webdev

ADD manage.py requirements.txt run.sh /app/
ADD pizzaapp /app/pizzaapp/

# /app is WORKDIR, inherited from base image

RUN chown -R python:python . && \
    chmod +x run.sh manage.py && \
    pip install -r requirements.txt

CMD ["./run.sh"]