output "rg_id" {
  value = data.azurerm_resource_group.rg.id
}

output "acr_address" {
  value = azurerm_container_registry.acr.login_server
}
