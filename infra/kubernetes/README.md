## General info

Basic Kubernetes cluster setup to run flask-api-pizzaapp

## Requirements

* Existing k8s cluster (example here: AKS)

## Usage

* Create namespaces:
```
kubectl apply -f namespaces.yaml
```
* Deploy ingress-nginx:
  ```
  kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml
  ```
* Deploy cert-manager:
  ```
  kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml
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
    * If you need to create registry secret to access ACR from AKS see following guide: https://azuredevcollege.com/trainingdays/day7/challenges/image-pull-secret.html
  * Replace *@JWT_SECRET@*, *@DB_NAME@*, *@DB_USER@* and *@DB_PASS@* with proper values in helm command (see next step)
  * Run following command:
    ```
    helm upgrade --install flask-api-pizzaapp ./helm/flask-api-pizzaapp \
    --wait --timeout 10m --atomic \
    --namespace dev-env \
    --values ./helm/environments/my-dev-env.yaml \
    --set image.repository=my-repo/flask-api-pizzaapp \
    --set image.tag=latest \
    --set ingress.host=flask-api-pizzaapp.my.ingress.dot.com \
    --set env.secrets.FLASK_JWT_SECRET=@JWT_SECRET@ \
    --set env.secrets.FLASK_DB_NAME=@DB_NAME@ \
    --set env.secrets.FLASK_DB_USER=@DB_USER@ \
    --set env.secrets.FLASK_DB_PASS=@DB_PASS@
    ```
