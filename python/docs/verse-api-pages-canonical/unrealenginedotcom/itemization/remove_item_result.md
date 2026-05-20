## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/itemization/remove_item_result

# remove_item_result class

Learn technical details about the remove_item_result class.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /UnrealEngine.com/Itemization }` |

## Members

This class has data members, but no functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `Inventory` | `inventory_component` | The inventory which the item was removed from. |
| `RemovedAmount` | `int` | Total stack count of items removed as a result of this transaction. |
| `RemovedItems` | `[]entity` | Items that were removed from this inventory as a result of the transaction. |
| `ModifiedItem` | `?(entity, int)` | Item whose stack size changed as a result of the transaction. |
