## General info

Basic Kubernetes cluster setup required to run flask-api-pizzaapp

## Requirements

* Existing k8s cluster (example here: AKS). You can create cluster using terraform module in [terraform](../terraform) directory.

## Usage
* Get cluster credentials
  ```
  az aks get-credentials --resource-group myrg01 --name myaks01 --admin
  ```
* Create namespaces:
  ```
  kubectl apply -f namespaces.yaml
  ```
* Deploy cert-manager:
  ```
  kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.1/cert-manager.yaml
  ```
* Cert manager basic setup (Let's encrypt)
  * Set correct e-mail in yaml file:
    ```
    sed -i 's/admin@mydomain.com/me@insanedomain.com/g' letsencrypt-staging-clusterissuer.yaml
    ```
  * Create clusterIssuer object:
    ```
    kubectl apply -f letsencrypt-staging-clusterissuer.yaml
    ```
  * This is staging certificate; if you want to create prod certificate use Let's Encrypt prod API: *https://acme-v02.api.letsencrypt.org/directory*
* Deploy flask-api-pizzaapp using helm chart
  * Create yaml file basing on [dev-env.yaml](../../helm/environments/dev-env.yaml), for example *my-dev-env.yaml*
    * If you need to create registry secret to access ACR from AKS you can use existing service principal (https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#service-principal) or ACR admin account (WARNING, it's unsafe: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#admin-account)
  * Replace *@JWT_SECRET@*, *@DB_NAME@*, *@DB_USER@* and *@DB_PASS@* with proper values in helm command (see next step)
  * Run following command:
    ```
    helm upgrade --install flask-api-pizzaapp ./helm/flask-api-pizzaapp \
    --wait \
    --timeout 10m \
    --atomic \
    --namespace dev-env \
    --values ./helm/nodejs-colorizedapp/values.yaml \
    --values ./helm/environments/my-dev-env.yaml \
    --set image.repository=my-repo/flask-api-pizzaapp \
    --set image.tag=latest \
    --set ingress.host=flask-api-pizzaapp.my.ingress.dot.com \
    --set env.secrets.FLASK_JWT_SECRET=@JWT_SECRET@ \
    --set env.secrets.FLASK_DB_NAME=@DB_NAME@ \
    --set env.secrets.FLASK_DB_USER=@DB_USER@ \
    --set env.secrets.FLASK_DB_PASS=@DB_PASS@
    ```
