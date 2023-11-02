#!/usr/bin/env bash

set -euo pipefail

CERT_MANAGER_VER='v1.13.1'
NGINX_INGRESS_VER='v1.8.2'

echo 'Creating namespaces'
kubectl apply -f ./namespaces.yaml

echo "Applying cert manager version ${CERT_MANAGER_VER}"
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/${CERT_MANAGER_VER}/cert-manager.yaml
echo 'Finished, sleep for 60 seconds'
sleep 60

echo 'Applying cert-manager clusterissuer'
kubectl apply -f ./letsencrypt-staging-clusterissuer.yaml

echo 'Applying secrets'
kubectl apply -f ./acr-registry-secret-dev-env.yaml ./acr-registry-secret-uat-env.yaml ./acr-registry-secret-prod-env.yaml

echo "Applying ingress-nginx version ${NGINX_INGRESS_VER}"
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-${NGINX_INGRESS_VER}/deploy/static/provider/cloud/deploy.yaml
echo 'Sleep for 60 seconds'
sleep 60

echo 'Getting loadBalancer IP address...'
until kubectl get svc ingress-nginx-controller -n ingress-nginx \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}' |
  grep -m 1 -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'; do
  echo 'Sleeping for 5 seconds...'
  sleep 5
done
