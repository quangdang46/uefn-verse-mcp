## https://dev.epicgames.com/documentation/en-us/fortnite/item-component-in-fortnite

# Item Component

The Item Component provides a way to create custom items that have custom properties.

![Item Component](https://dev.epicgames.com/community/api/documentation/image/df0dba04-85a6-455d-8d97-7adb75b36fe1?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

In the [Custom Items and Inventories system](https://dev.epicgames.com/documentation/fortnite/custom-items-and-inventory-overview-in-fortnite), an `item_component` becomes a class that defines what an item is and isn’t. Refer to **[Working with Entities and Components](https://dev.epicgames.com/documentation/fortnite/working-with-entities-and-components-in-unreal-editor-for-fortnite)** for how to add a [component](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#component) to an [entity](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#entity).

Entities are only considered items if they have an `item_component`. Without one, entities will not be added to inventories properly and lots of Custom Item and Inventories functionality may be broken.

- References to an “item” are directly referring to an entity with an `item_component`.
- References to “inventories” are directly referring to an entity with an `inventory_component`.

## Class Definition

Attaching an `item_component` to an entity turns the entity into an [item](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#item). Items have a number of properties that can be leveraged by other components:

- They can be manipulated by inventories.
- Picked up and dropped.
- Items may be equipped and unequipped.

More functionality can be given to an item with additional components that expose different features and basic Fortnite gameplay. You can also write your own [custom Verse components](https://dev.epicgames.com/documentation/fortnite/creating-your-own-component-using-verse-in-unreal-editor-for-fortnite). For more information check out the `item_component` API reference from the [Verse API](https://dev.epicgames.com/documentation/fortnite/verse-api).

See **[Components](https://dev.epicgames.com/documentation/fortnite/components-in-unreal-editor-for-fortnite)** for a complete list of Custom Items and Inventories components.

[![An example of the item_component in the Prefab Editor.](https://dev.epicgames.com/community/api/documentation/image/36b56aae-0b02-4534-9907-3920bfdb732d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36b56aae-0b02-4534-9907-3920bfdb732d?resizing_type=fit)

Item Component

By giving an `item_component` to this prefab, it can now be stored as an item inside an inventory.

## Verse: Items

The `item_component` contains fields, [functions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function), and [events](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event) to make use of through [Verse](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#verse).

- `GetParentInventory[]` - Provides a way for items to identify their parent inventory.

- `Categories` - An array of `item_category` that can be used to sort and characterize.
- `Equip()`, `Unequip()`, and `IsEquipped[]` - These functions help to manage the item's equipped state.
- `ChangeEquippedEvent` - This event fires on an item component whenever Equip() or Unequip() are called.
- `ChangeInventoryEvent` - Monitor items moving between inventories.

## Example

Item components are required by entities to function as items. The [Prefab editor](https://dev.epicgames.com/documentation/fortnite/prefab-editor-user-interface-in-unreal-editor-for-fortnite) has limited editable properties, so to get the most out of the component you will need to use Verse.

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Itemization }

# This device will create an item for all players when they are added to Playspace. Once the item is created it will pick itself up to the Player's inventory.
item_giver_device := class(creative_device) :
```

Functionality can easily be added to Items by subclassing the `item_component`. Subclassing can modify the basic properties, or add new functions and fields specific to your experience.

Verse

```
using { /UnrealEngine.com/Itemization }
using { /Fortnite.com/Itemization/FortniteItemCategories }

custom_item_component := class(item_component) :

    # We could populate the Categories array with Fortnite and/or custom item categories.
    #For example here, we are using the Resource item_category type.
    Categories<override>:[]item_category = array{Resource}
```

---
