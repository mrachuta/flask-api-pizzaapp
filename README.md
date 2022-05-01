## Project name
flask-api-pizzaapp - Simple Flask application used demonstrate Python-based CI/CD process in Jenkins.

## Table of contents
- [Project name](#project-name)
- [Table of contents](#table-of-contents)
- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Using](#using)

## General info
Because of lack of advanced examples of CI/CD processes based on Jenkins and Python (at least I was not able to find such examples when I started my career as DevOps Engineer), this project has been created.  
It consists of simple Flask application (Python) and Jenkins pipelines (Declarative syntax mixed with scripted).
Pipelines are covering:
- CI process 
  * build,
  * test,
  * static code analysis,
  * build docker image,
  * deployment to artifactory
- CD process
  * release package creation including tagging
  * deployment to test, uat or prod env
  
## Technologies
* Application: Python3
* Pipelines: Jenkins (Groovy)

Code was tested on following platforms:
* Python 3.9
* Kubernetes v1.21.9 (containerd 1.4.12+azure-3)
* Jenkins 2.332.1

Used libraries:
* available in requirements.txt


## Setup

1. Clone git repo to localhost.
2. Install required packages.
3. Use following commands:
    ```
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```

## Using    

To start application, perform:
```
python manage.py runserver
```
After start, you can access app using following URL in your browser:
```
http://127.0.0.1:5000/
```
