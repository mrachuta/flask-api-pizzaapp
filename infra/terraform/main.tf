data "azurerm_resource_group" "rg" {
  name = var.existing_rg
}

resource "azurerm_container_registry" "acr" {
  count               = var.provision_acr == true ? 1 : 0
  name                = var.acr_name
  resource_group_name = data.azurerm_resource_group.rg.name
  location            = data.azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
  tags = merge(
    {
      "managed_by" = "terraform"
    },
    var.extra_tags
  )
}

resource "azurerm_kubernetes_cluster" "aks" {
  count               = var.provision_aks == true ? 1 : 0
  name                = var.aks_name
  resource_group_name = data.azurerm_resource_group.rg.name
  location            = data.azurerm_resource_group.rg.location
  dns_prefix          = var.aks_name
  sku_tier            = "Free"
  node_resource_group = var.aks_resources_rg_name

  network_profile {
    network_plugin    = "kubenet"
    load_balancer_sku = var.aks_lb_sku
  }

  dynamic "api_server_access_profile" {
    for_each = (
      var.aks_lb_sku == "standard" && var.aks_auth_ip_ranges != null
    ) ? [1] : []
    content {
      authorized_ip_ranges = [
        var.aks_auth_ip_ranges
      ]
    }
  }

  default_node_pool {
    name                        = "default"
    temporary_name_for_rotation = "defaulttemp"
    node_count                  = 1
    vm_size                     = "Standard_B2s"
    os_disk_size_gb             = 32
    os_disk_type                = "Managed"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = merge(
    {
      "managed_by" = "terraform"
    },
    var.extra_tags
  )
}
