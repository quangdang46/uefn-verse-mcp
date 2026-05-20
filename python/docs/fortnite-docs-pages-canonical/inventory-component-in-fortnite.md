## https://dev.epicgames.com/documentation/en-us/fortnite/inventory-component-in-fortnite

# Inventory Component

The Inventory Component provides a way to create custom inventories.

![Inventory Component](https://dev.epicgames.com/community/api/documentation/image/0cf13c25-0b9e-4c19-bf8e-0b24b3f33a21?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

The `inventory_component` is a [Scene Graph](https://dev.epicgames.com/documentation/fortnite/scene-graph-in-unreal-editor-for-fortnite) component used as a container for Items. For how to add a [component](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#component) to your [entity](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#entity), see **[Working with Entities and Components](https://dev.epicgames.com/documentation/fortnite/working-with-entities-and-components-in-unreal-editor-for-fortnite)**.

Entities are only considered [items](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#item) if they have an `item_component`. Without one, entities are not added to inventories properly and [Custom Items and Inventory](https://dev.epicgames.com/documentation/fortnite/custom-items-and-inventory-overview-in-fortnite) functionality may break.

- References to an “item” are referring to an entity with an `item_component`.
- References to “inventories” are referring to an entity with an `inventory_component`.

## Class Description

An `inventory_component` turns an entity into a container for items. 
The entity could be a player, a treasure chest, or anything that can hold items.

By default an inventory can hold an infinite number of any kind of item. Through Verse you can write logic inside the component to create restrictions and custom behaviors so an inventory can be tailored to your experience.

The component is listed as `inventory_component` in the component dropdown list. For more information, check out the [inventory_component API](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/inventory_component) reference from the [Verse API](https://dev.epicgames.com/documentation/fortnite/verse-api).

[![The chest prefab has been given an inventory_component, allowing it to store items.](https://dev.epicgames.com/community/api/documentation/image/f19aff97-61af-4915-93d5-b797bed2c996?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f19aff97-61af-4915-93d5-b797bed2c996?resizing_type=fit)

An example of the inventory_component.

While a prefab may have an `inventory_component` (which makes it capable of storing items), it may not have the necessary components for player interaction, user interface, and other requirements for the exchange of items. Multiple components may be necessary to mediate between the treasure chest and an entity created to retrieve or store items inside it.

## Verse: Inventories

Items added to the inventory become children of the `inventory_component`'s entity. Along with the normal scene graph hierarchy functionality, Inventories can manage themselves and their owned items with specific properties and [methods](https://dev.epicgames.com/documentation/fortnite/method):

- **`AddItem()`** - Adds items (including subinventories).
- `RemoveItem()` - Removes items (includes subinventories).
- `AddItemDistribute()` - Add items to the targeted inventory, or any subinventories if the target cannot accept the item.
- `GetItems()` - Retrieve items or return immediate children.
- `FindItems()` - Find functions return all descendents.
- `GetInventories()` - Returns immediate child subinventories of this inventory.
- `FindInventories()` - Returns all descendant subinventories of this inventory.

  `AddItemEvent` and `RemoveItemEvent` - Subscribable events that trigger when an item enters or exits this inventory.
- `GetEquippedItems()` - Can be used for equipping items.
- `EquipItemEvent` - Track equipping items with events.
- `UnequipItemEvent` - Track unequipping items with events.

## Inventory Root

Players have an inventory by default called the**Inventory Root**. The following explanation does not affect entities that have an `inventory_component` added through Verse or the prefab editor.

Unlike other inventories, the player’s Inventory Root cannot accept items. Instead, it acts as the parent for subinventories beneath it. This provides a way to target the Inventory Root using **AddItemDistribute()** which finds an eligible inventory for an item, even if the initial target inventory cannot receive it.

Players must have one or more subinventories beneath the Inventory Root to receive items.

When a player has a single, top-level inventory, other systems can use it as an entry point, even without knowing internal inventory details. Whenever traversing the Scene Graph downwards the Inventory Root is always the first inventory found when searching an entity tree for an entity with an `inventory_component`. This makes the inventory root a sensible target to attach new inventories to.

Verse

```
# This helper function gets the first inventory component from a child entity of an agent.
# This will be the inventory root.
(Agent:agent).GetInventoryRoot()<transacts><decides>:inventory_component =
    for (Child : Agent.GetEntities(), InventoryComponent := Child.GetComponent[inventory_component]){InventoryComponent}[0]
```

# This helper function gets the first inventory component from a child entity of an agent.
# This will be the inventory root.
(Agent:agent).GetInventoryRoot()<transacts><decides>:inventory_component =
for (Child : Agent.GetEntities(), InventoryComponent := Child.GetComponent[inventory_component]){InventoryComponent}[0]

The root inventory is only automatically added to players. New entities created with an `inventory_component` do not have the same restriction.

## Inventories Configuration

Every player has an inventory configuration when they are added to a scene. This configuration determines which subinventories they begin with. All players start with an inventory root, but the configuration determines whether they start with any subinventories. The configuration can be set inside the Island settings, under **Custom Inventory Configuration**.

[![An example of using the Custom Inventory Configuration to determine which inventory players begin the game with.](https://dev.epicgames.com/community/api/documentation/image/e99ff95d-4389-487e-8b45-b93af6a0641f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e99ff95d-4389-487e-8b45-b93af6a0641f?resizing_type=fit)

Custom Inventory Configuration

Below you can see the difference between the two initial configurations provided with the feature. In both cases, new subinventories need to be added as descendants of the Inventory Root. The BR Style configuration comes with a number of Fortnite subinventories. Refer to **[Fort Inventory Component](https://dev.epicgames.com/documentation/fortnite/fort-inventory-component-in-fortnite)** for more information on Fort Inventories.

[![Examples of configuring inventories in Scene Graph.](https://dev.epicgames.com/community/api/documentation/image/b89668d8-faf6-47ff-bda3-312f31b46c82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b89668d8-faf6-47ff-bda3-312f31b46c82?resizing_type=fit)

Inventory Configuration

## Verse Example

Below is a script for a device that uses the helper function `GetInventoryRoot[]` defined in [Verse: Inventories](https://dev.epicgames.com/documentation/fortnite/inventory-component-in-fortnite#verse-inventories) above. The device has an `editable` field that can be modified in the scene. It adds the selection of items to each player when the player is added to the simulation, functioning like an item granter. Calling `AddItemDistribute()` ensures that all subinventories are checked to see if they can receive the item:

Verse

```
# Copyright Epic Games, Inc. All Rights Reserved.

using { /Fortnite.com/Devices }
using { /Fortnite.com/Itemization }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Itemization }
```

## Filtering Inventories with Scene Events

When an inventory is targeted to receive or remove an item, it receives a [Scene Event](https://dev.epicgames.com/documentation/fortnite/scene-events-in-unreal-editor-for-fortnite). An `add_item_query_event` when adding, and a `remove_item_query_event` when removing (the item entity added or removed from the inventory also receives the scene event). The responses to these events are what cause the `AddItem()` and `RemoveItem()` functions to succeed or fail.

By overriding how these events are received, the entry or exit of items from an inventory can be controlled. This provides a way to create inventory rules, such as checking the item type before adding, only allowing a certain number of items in the inventory, and more.

The `OnReceive()` function is implemented in the base component class and is available to all Scene Graph components, including the `inventory_component`. It is triggered when an entity receives any Scene Event.  By overriding `OnReceive()` you can modify the received Scene Event and add an error to it that causes the add or remove to fail for the inventory. You can write a unique error class to be used in these instances. See the code snippet below for an error class example.

A common requirement of inventories is to apply rules to what items may exist inside. Below is a script for a custom `inventory_component` which overrides the component method `OnReceive()`. Here it has been used to make a maximum Inventory size rule:

Verse

```
# Copyright Epic Games, Inc. All Rights Reserved.

using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Itemization }

# This error can be created if the inventory is at capacity.
no_slots_add_item_error := class(add_item_error):
```

The video above illustrates how the `custom_inventory_component` adds three items to the inventory and rejects additional items.

The above behavior only works on the player because the `custom_inventory_component` has been added to an entity which has then been attached to the player root inventory as a child. Below is a device example code snippet illustrating this behavior:

Verse

```
# Copyright Epic Games, Inc. All Rights Reserved.

using { /Fortnite.com/Devices }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Itemization }

# This device will add a sub inventory using the custom_inventory_component.
```

`AddItemDistribute()` used in the `custom_loadout_device` defined above places items in any eligible subinventory. If the player has other subinventories, the item may end up in them. To control this, remove subinventories or write rules inside the `OnReceive()` function.

[![A comparison of the way Fortnite Battle Royale uses Inventory configuration versus an empty inventory configuration.](https://dev.epicgames.com/community/api/documentation/image/1331235b-a13f-49c8-8b4f-38c87ca8d99e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1331235b-a13f-49c8-8b4f-38c87ca8d99e?resizing_type=fit)

Inventory Configuration Examples

See the above diagram for how the `custom_inventory_component` would be added as a subinventory via the `inventory_giver_device`.

For more gameplay examples of inventories and how to use the `inventory_component`, see the tutorials in [Custom Items and Inventories with Scene Graph](https://dev.epicgames.com/documentation/fortnite/custom-items-and-inventories-with-scene-graph-in-uefn).
