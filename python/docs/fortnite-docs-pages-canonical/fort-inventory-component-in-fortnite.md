## https://dev.epicgames.com/documentation/en-us/fortnite/fort-inventory-component-in-fortnite

# Fort Inventory Component

Design a custom Fortnite inventory for your island using fort_inventory_component.

![Fort Inventory Component](https://dev.epicgames.com/community/api/documentation/image/4b42e7a4-2922-440d-bfad-cd427d650b2d?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

The Custom Items and Inventories system uses inventories and sub-inventories to compartmentalize items by sorting, adding, and retrieving items. Refer to **[Working with Entities and Components](https://dev.epicgames.com/documentation/fortnite/working-with-entities-and-components-in-unreal-editor-for-fortnite)** for how to add a [component](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#component) to your [entity](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#entity).

Entities are only considered [items](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#item) if they have an `item_component`. Without one, entities will not be added to inventories properly as well as Custom Item and Inventories functionality may be broken.

- References to an “item” are referring to an entity with an `item_component`.
- References to “inventories” are referring to an entity with an `inventory_component`.

## Class Description

The `fort_inventory_component` is a subclass of the `inventory_component`. Its purpose is to provide compatibility between Fortnite gameplay and the new Custom Items and Inventories system. By default players are given an [Inventory Root](https://dev.epicgames.com/documentation/fortnite/inventory-component-in-fortnite#root-inventory), and then a number of specialized subclasses are added to the Root as sub-inventories.

Whether or not an [agent](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#agent) spawns with these Fortnite subinventories is determined by the **Custom Inventory Configuration** asset that exists in the Island Settings (refer to **[Inventory Component](https://dev.epicgames.com/documentation/fortnite/inventory-component-in-fortnite)** for more information).

See **[Components](https://dev.epicgames.com/documentation/fortnite/components-in-unreal-editor-for-fortnite)** for a complete list of itemization components.

You can access the `fort_inventory_component` from the component dropdown list. For more information, check out the `fort_inventory_component` API reference from the [Verse API](https://dev.epicgames.com/documentation/fortnite/verse-api).

## Fortnite and the Custom Inventory and Items Feature

Fortnite relies on the `fort_inventory` subclasses to do specific things:

|  |  |
| --- | --- |
| `fort_inventory_component` | Base subclass for all the other Fort Inventories. Also used to hold the Edit Mode tool. Required for Edit Mode. |
| `fort_inventory_build_hotbar_component` | Holds the build recipe items. Required for Edit Mode. |
| `fort_inventory_weapon_hotbar_component` | Holds equippable Fortnite items like weapons and [consumables](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#consumables). Filters items by `item_category.WorldItem`. |
| `fort_inventory_collectibles_component` | Filters items by the  `item_category.Collectible`. |
| `fort_inventory_resources_component` | Stores the default Fortnite [resources](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#resource), wood, brick and metal. Filters items by the  `item_category.Resource` |
| `fort_inventory_ammo_component` | Stores Fortnite ammo types. Filters items by the  `item_category.Ammo`. |
| `fort_inventory_trap_component` | Holds a single item instance. Only allows items with the  `item_category.Trap`. |
| `fort_inventory_currencies_component` | Stores any item with the  `item_category.Currency`. |
| `fort_inventory_harvest_tool_component` | Holds the Player [Harvest Tool](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#harvesting-tool). Required for Edit Mode. |

[![A diagram illustrating the relationship between the Inventory Root and the additional child inventories.](https://dev.epicgames.com/community/api/documentation/image/b596929b-fc30-490f-93c5-ba0f2e770cf2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b596929b-fc30-490f-93c5-ba0f2e770cf2?resizing_type=fit)

Battle Royale Inventory Configuration

In the diagram above, subinventories are arranged as part of the inventory hierarchy.

## Verse: Fort Inventories

These components provide an approximation of the Fortnite: Battle Royale inventory behavior. For example, when items with the ammo `item_category` are added to the inventory root via `AdditemDistribute()`, they are placed inside the `fort_inventory_ammo_component`. Another example is the `fort_inventory_weapon_hotbar_component` inventory which is limited to five slots, as it is in Fortnite.

You can find the Fortnite `item_category` definitions in the `FortniteItemCategories` module in the `Fortnite.digest.verse`. You can add these categories to your items to make them appear inside the Fort Inventories.

## Example

Like other Scene Graph components, the `fort_inventory_component` and its subclasses can also be added and removed through [Verse](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#verse).

Below is a script for getting specific `fort_inventory_component`s and reading the items inside them. You can write your own systems to leverage Custom Items and Inventories alongside Fortnite Items since they inherit all the functionality of the base `inventory_component`.

Verse

```
# Copyright Epic Games, Inc. All Rights Reserved.

using { /Fortnite.com/Devices }
using { /Fortnite.com/Itemization }
using { /UnrealEngine.com/Itemization }
using { /Verse.org/Presentation }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }
```
