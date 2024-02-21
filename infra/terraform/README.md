## General info

Terraform configuration to create flask-api-pizzaapp stack

## Requirements

* Existing resource group:
```
az group create --name flaskapipizzaap-rg --location northcentralus
```
* main.tf file with configured variables
  * to get all variables check module's [variables.tf](https://github.com/mrachuta/terraform-resources/blob/master/modules/azure-aks-cheap-cluster-module/variables.tf) file
* module is taking care about integration of AKS with ACR (it grants AcrPull role to AKS Managed Identity)

## Usage

Create resources:
```
terraform apply
```
Destroy resources:
```
terraform destroy
```
