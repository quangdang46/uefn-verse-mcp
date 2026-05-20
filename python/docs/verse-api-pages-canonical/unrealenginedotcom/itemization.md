## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/itemization

# Itemization module

Learn technical details about the Itemization module.

- [`UnrealEngine.com`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom)
- **`Itemization`**

## Classes and Structs

| Name | Description |
| --- | --- |
| [`add_item_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/add_item_result) |  |
| [`remove_item_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/remove_item_result) |  |
| [`equip_item_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/equip_item_result) |  |
| [`unequip_item_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/unequip_item_result) |  |
| [`find_inventory_event`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/find_inventory_event) | When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices. It is sent upwards. |
| [`add_item_error`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/add_item_error) |  |
| [`add_item_query_event`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/add_item_query_event) | When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices. It is sent upwards. |
| [`remove_item_error`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/remove_item_error) |  |
| [`remove_item_query_event`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/remove_item_query_event) |  |
| [`inventory_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/inventory_component) | Inventory components hold items. An entity with an inventory component can be considered to have an inventory. The inventory component controls which items can enter or exit. They also determine whether an item can be equipped. |
| [`item_category`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_category) | item_category is used to classify items. |
| [`change_equipped_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/change_equipped_result) |  |
| [`change_inventory_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/change_inventory_result) |  |
| [`equip_item_error`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/equip_item_error) |  |
| [`equip_item_query_event`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/equip_item_query_event) |  |
| [`unequip_item_error`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/unequip_item_error) |  |
| [`unequip_item_query_event`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/unequip_item_query_event) |  |
| [`item_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component) | Anything using this component should be considered an item. Required to interact with inventories. |
| [`item_details_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_details_component) | Deprecated. Please use description_component instead. |
| [`item_icon_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_icon_component) | Deprecated. Please use icon_component instead. |
