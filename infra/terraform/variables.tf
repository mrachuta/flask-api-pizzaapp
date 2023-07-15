variable "existing_rg" {
  type        = string
  default     = "myexistingrg01"
  description = "Existing resoure group name; have to be created manually outside of terraform"
}

variable "extra_tags" {
  type        = map(string)
  default     = {}
  description = "Additional tags to be added to each resource"
}

variable "acr_name" {
  type        = string
  default     = "myacr01"
  description = "Name of Azure Container Registry"
}

variable "aks_name" {
  type        = string
  default     = "myaks01"
  description = "Name of AKS cluster; will be used also as DNS prefix"
}

variable "aks_resources_rg_name" {
  type        = string
  default     = "myacr01_rg"
  description = "Name of resource group where AKS resources will be placed; will be created automatically"
}

variable "aks_lb_sku" {
  type        = string
  default     = "basic"
  description = "Type of loadbalancer for AKS; use 'standard' to restrict ranges to access Kubernetes (AKS) cluster API"
}

variable "aks_auth_ip_ranges" {
  type        = string
  default     = null
  description = "IP range to be able to access Kubernetes (AKS) cluster API"
}
