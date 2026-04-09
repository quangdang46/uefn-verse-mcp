## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/itemization/unequip_item_result

# find_inventory_event class
Learn technical details about the find_inventory_event class.
When adding an item, 'find_inventory_event' is used as a first pass to find the best inventory for an item. It is sent downwards. 'add_item_query_event' can be used to veto inventory choices. It is sent upwards.
|
---|---
Verse `using` statement | `using { /UnrealEngine.com/Itemization }`
## Exposed Interfaces
This class exposes the following interfaces:
Name | Description
---|---
[`scene_event`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/scene_event) |  An event which can be sent through the scene graph.
## Members
This class has data members, but no functions.
### Data
Data Member Name | Type | Description
---|---|---
`ItemComponent` | `item_component` |
`ChosenInventory` | `??inventory_component` |
`ChosenInventoryPriority` | `?float` |
