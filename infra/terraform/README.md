## General info

Terraform configuration to create flask-api-pizzaapp stack

## Requirements

* Existing resource group:
```
az group create --name flaskapipizzaap-rg --location northcentralus
```
* vars file created with following content
```
$ cat flaskapipizzaap-rg.auto.tfvars
existing_rg           = "flaskapipizzaap-rg"
acr_name              = "fapaacr01"
aks_name              = "fapaaks01"
aks_resources_rg_name = "flaskapipizzaap-rg-fapaaks01"
aks_lb_sku            = "basic"
```

## Usage

Create resources:
```
terraform apply
```
Destroy resources:
```
terraform destroy
```
