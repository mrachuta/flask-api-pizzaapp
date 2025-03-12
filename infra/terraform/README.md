## General info

Terraform configuration to create flask-api-pizzaapp stack

## Requirements

* Registered providers:
  ```
  az provider register --namespace Microsoft.Storage
  az provider register --namespace Microsoft.ContainerService
  az provider register --namespace Microsoft.Kubernetes
  az provider register --namespace Microsoft.ContainerRegistry
  az provider register --namespace Microsoft.ManagedIdentity
  az provider register --namespace Microsoft.App
  az provider register --namespace Microsft.Insights
  ```
* Existing resource group:
  ```
  az group create --name myrg01 --location northcentralus

  ```
* Storage account with container created:
  ```
  az storage account create --resource-group myrg01 --name mysa01 --sku Standard_LRS --encryption-services blob
  az storage container create --name terraform-remote-state --account-name mysa01
  ```
* terraform.tf file updated:
  ``` 
  resource_group_name
  storage_account_name
  ```
* vars file created
  ```
  touch flaskapipizzaapp.auto.tfvars
  ```
  with following content:
  ```
  $ cat flaskapipizzaapp.auto.tfvars
  existing_rg           = "myrg01"
  provision_acr         = true
  acr_name              = "myaks01"
  provision_aks         = true
  aks_name              = "myacr01"
  aks_resources_rg_name = "myrg01-myaks01"
  az_cli_path           = "/path/to/your/az"
  ```
* if you want to adjust more parameters, take a look at [main.tf](./main.tf) and [variables.tf](https://github.com/mrachuta/terraform-resources/blob/master/modules/azure-aks-cheap-cluster-module/variables.tf)
* module by default is integrating AKS with ACR by granting AcrPull role to AKS Managed Identity

## Usage
Initalize terraform:
```
terraform init
```
Create resources:
```
terraform apply
```
Destroy resources:
```
terraform destroy
```
