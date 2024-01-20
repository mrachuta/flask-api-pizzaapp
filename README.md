## Project name
flask-api-pizzaapp - Simple Flask application used demonstrate Python-based CI/CD process in Jenkins.

## Table of contents
- [Project name](#project-name)
- [Table of contents](#table-of-contents)
- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
  - [Development mode](#development-mode)
  - [PROD Kubernetes](#prod-kubernetes)
- [Usage](#usage)

## General info
Because of lack of advanced examples of CI/CD processes based on Jenkins and Python (at least I was not able to find such examples when I started my career as DevOps Engineer), this project was created.  
It consists of simple Flask application (Python) and Jenkins pipelines (declarative syntax mixed with scripted).
Pipelines are covering:
- Continious Integration process 
  * build,
  * security checks,
  * unit tests,
  * static code analysis
- Continious Delivery process
  * build docker image,
  * deployment to artifactory,
  * release-package creation (including tagging and conditions-check)
- Continious Deployment process
  * deployment to dev, uat and prod env
  
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

### Development mode

1. Clone git repo to localhost.
2. Install required packages.
3. Use following commands:
    ```
    flask --app pizzaapp.app db init
    flask --app pizzaapp.app db migrate
    flask --app pizzaapp.app db upgrade
    ```
4. To start application, perform:
    ```
    flask --app pizzaapp.app run
    ```
After start, you can access app using following URL in your browser:
```
http://127.0.0.1:5000/
```
### PROD Kubernetes

* For infra setup see following file [README.md](./infra/terraform/README.md)  
* For kubernetes cluster components and helm deployment see following file [README.md](./infra/kubernetes/README.md)

## Usage

Application:
List of all endpoints is available at http://127.0.0.1:5000/

Example:
POST
```
curl -L -X POST -H "Content-Type: application/json" -d "{\"name\": \"testpizza\", \"price\": \"29.99\"}"  http://127.0.0.1:5000/api/v1/pizza
```
GET
```
curl -L -X GET http://127.0.0.1:5000/api/v1/pizza
```
