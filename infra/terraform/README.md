## General info

Terraform configuration to create flask-api-pizzaapp stack

## Requirements

* Existing resource group:
```
az group create --name flaskapipizzaap-rg --location northcentralus
```
* vars file created
```
touch flaskapipizzaapp.auto.tfvars
```
with following content:
```
$ cat flaskapipizzaapp.auto.tfvars
existing_rg           = "myrg01"
provision_acr         = "true"
acr_name              = "myaks01"
provision_aks         = "true"
aks_name              = "myacr01"
aks_resources_rg_name = "myrg01-myaks01"
```
* if you want to adjust more parameters, take a look at [main.tf](./main.tf) and [variables.tf](https://github.com/mrachuta/terraform-resources/blob/master/modules/azure-aks-cheap-cluster-module/variables.tf)
* moudule by default is integrating AKS with ACR by granting AcrPull role to AKS Managed Identity

## Usage

Create resources:
```
terraform apply
```
Destroy resources:
```
terraform destroy
```
