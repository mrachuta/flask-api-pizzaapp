module "aks_cheap_cluster" {
  source = "github.com/mrachuta/terraform-resources.git//modules/azure-aks-cheap-cluster-module?ref=feature%2Fadd-aks-module"

  existing_rg                = "mzra-rg"
  provision_acr              = true
  provision_aks              = true
  acr_name                   = "mzraacr01"
  acr_grant_pull_role_to_aks = true
  aks_name                   = "mzraaks01"
  aks_resources_rg_name      = "mzra-rg-mzraaks01"
  aks_lb_sku                 = "basic"
  nginx_ingress_additional_params = {
    "controller.service.externalTrafficPolicy" = "Local"
  }
  aks_scaling_details_default_node = {
    enabled       = true
    days          = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_time_HH = 07
    start_time_MM = 00
    stop_time_HH  = 22
    stop_time_MM  = 30
    timezone      = "UTC"
  }
}
