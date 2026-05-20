## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/itemization

# Itemization module

Learn technical details about the Itemization module.

- [`Fortnite.com`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom)
- **`Itemization`**

  - [`FortniteItemCategories`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fortniteitemcategories)
  - [`FortniteRarities`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fortniterarities)

## Classes and Structs

| Name | Description |
| --- | --- |
| [`fort_inventory_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_component) | `fort_inventory_component` is a shared class for all Fortnite inventories, with appropriate default UI and behavior. The HUD when using the BR Style Inventory Configuration will only be shown when using the default configuration. If new inventories are added you will need to create your own custom HUD using Verse UI. |
| [`fort_inventory_weapon_hotbar_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_weapon_hotbar_component) | `fort_inventory_weapon_hotbar_component` is the UEFN inventory for Fortnite weapons and gadgets. |
| [`fort_inventory_build_hotbar_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_build_hotbar_component) | `fort_inventory_build_hotbar_component` is the UEFN inventory for Fortnite build tools. |
| [`fort_inventory_harvest_tool_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_harvest_tool_component) | `fort_inventory_harvest_tool_component` is the UEFN inventory for the Fortnite harvest tool. |
| [`fort_inventory_trap_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_trap_component) | `fort_inventory_trap_component` is the UEFN inventory for the Fortnite trap slot. |
| [`fort_inventory_resources_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_resources_component) | `fort_inventory_resources_component` is the inventory for Fortnite resources. |
| [`fort_inventory_ammo_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_ammo_component) | `fort_inventory_ammo_component` is the inventory for Fortnite ammo. |
| [`fort_inventory_currencies_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_inventory_currencies_component) | `fort_inventory_currencies_component` is the inventory for Fortnite currencies. |
| [`fort_item_pickup_interactable_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/itemization/fort_item_pickup_interactable_component) | Place this component onto an entity to allow it to be added to an agent inventory on interaction. The owning entity should have an item_component and a mesh_component. This component expects the interacting agent to have a subentity with an inventory_component. |
