# We strongly recommend using the required_providers block to set the
# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=3.63.0"
    }
  }
  backend "azurerm" {
    resource_group_name  = "mzra-rg"
    storage_account_name = "mzrasa01"
    container_name       = "terraform-remote-state"
    key                  = "terraform.tfstate"
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  skip_provider_registration = true
  features {}
}
