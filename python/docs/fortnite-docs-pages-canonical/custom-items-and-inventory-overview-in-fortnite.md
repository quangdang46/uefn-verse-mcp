## https://dev.epicgames.com/documentation/en-us/fortnite/custom-items-and-inventory-overview-in-fortnite

# Custom Items and Inventory Overview

Learn more about using Verse and Scene Graph to create custom items and customize the player inventory.

![Custom Items and Inventory Overview](https://dev.epicgames.com/community/api/documentation/image/aac30070-8a7e-4be8-b21f-b9cdb89b8bee?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

Item and inventory systems are a critical part of many kinds of games. You can customize Fortnite's player inventory using Scene Graph's entities and components to create items unique to your island.

[Items](https://dev.epicgames.com/documentation/fortnite/custom-items-and-inventory-overview-in-fortnite#items) are [objects](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#object) that players and [agents](https://dev.epicgames.com/documentation/fortnite/verse-glossary#agent) can use and own. [Inventories](https://dev.epicgames.com/documentation/fortnite/custom-items-and-inventory-overview-in-fortnite#inventories) include the existing Fortnite player inventory, as well as any custom inventories you create with the `inventory_component`. **Custom Items** **and Inventories** is a system for creating, controlling, and storing items. This system is an experimental feature that you must enable in **[Project Settings](https://dev.epicgames.com/documentation/fortnite/user-interface-reference-for-unreal-editor-for-fortnite#4-project-settings)**, and use with Scene Graph and Verse in Unreal Editor for Fortnite (UEFN).

## Scene Graph Basics

Scene Graph is an entity and component system, built on top of [Verse](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#verse). Entities are containers for components, and components give an entity functionality. You can attach entities to each other in a parent-child relationship, which creates hierarchies. A reusable arrangement of entities and components is called a prefab.

Refer to [Working with Entities and Components](https://dev.epicgames.com/documentation/fortnite/working-with-entities-and-components-in-unreal-editor-for-fortnite) for more information on entities and components. Refer to [Prefabs and Prefab Instances](https://dev.epicgames.com/documentation/fortnite/prefabs-and-prefab-instances-in-unreal-editor-for-fortnite) for more information on prefabs.

## Items

Items are created in Scene Graph by placing an `item_component` on an entity. [Inventories](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#inventory) treat the component like an object. The `item_component` supplies functionality, such as:

- Equipping and unequipping.
- Named categories for comparison and sorting.
- Helpful [functions](https://dev.epicgames.com/documentation/fortnite/verse-glossary#function-verse) and [events](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event).

[![An example of an item_component on an entity.](https://dev.epicgames.com/community/api/documentation/image/fac4305a-cfa4-447f-b2c7-f61f2cdeed1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fac4305a-cfa4-447f-b2c7-f61f2cdeed1e?resizing_type=fit)

item_component

By itself, the `item_component` provides limited options to an item. Additional [components](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#component) create something more interesting with increased functionality.

For more information, see [Item Componment](https://dev.epicgames.com/documentation/fortnite/item-component-in-fortnite).

## Inventories

Inventories are containers for items and control what happens to those items. An inventory is an [entity](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#entity) that has an `inventory_component` and works in the following ways:

- Being aware of all the items that exist inside it.
- Governing which items can enter or leave the inventory.
- Determining what happens when an incoming item wants to merge with an item already inside the inventory.

[![An example of an inventory_component on an entity.](https://dev.epicgames.com/community/api/documentation/image/e037fd0f-b6b2-4436-b6a8-e4d8845aa209?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e037fd0f-b6b2-4436-b6a8-e4d8845aa209?resizing_type=fit)

inventory_component

Since an item may only exist inside one inventory at a time, inventories also determine the ownership of item entities. Subentities of an inventory are only considered to be items inside the inventory if they also have an `item_component`, otherwise they are child subentities.

[![An example of a component and entity system.](https://dev.epicgames.com/community/api/documentation/image/dd75b76f-46be-4a5f-a443-7b900061ab98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd75b76f-46be-4a5f-a443-7b900061ab98?resizing_type=fit)

Component and Entity system

By default, inventories can hold an infinite number and variety of items. With Verse you can create restrictions and rules that affect adding and removal of items. For example:

- Add items to an inventory only if they have the correct category.
- Limit the number of items in an inventory.
- Prevent the last item from ever being removed from an inventory.
- Allow items of higher priority to eject items of lower priority when the inventory is full.
- Restrict an inventory to a single item.

## Inventory Trees

Inventories are aware of any inventories that are beneath them in the Scene Graph hierarchy. These child inventories are known as **subinventories**. You can leverage the tree of inventories in many ways.

For example, you can add an item to a parent inventory where it can find its way to a more specialized child inventory. You can think of this as giving a coin to the player and having it travel through the inventory system to a wallet (**Player Inventory** > **Backpack Inventory** > **Money Pouch Inventory**).

[![An example of a subinventory.](https://dev.epicgames.com/community/api/documentation/image/11c77cd2-203a-44dd-b93f-b274b28ef7a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11c77cd2-203a-44dd-b93f-b274b28ef7a8?resizing_type=fit)

Subinventory

To create more advanced inventory behavior, [writing Verse is necessary](https://verselang.github.io/book/).

## Verse: Inventories

There are two ways to add an item to an inventory.

- Call `AddItem()` to add an item specifically to one inventory.
- Calling the `AddItemDistribute()` function and using the inventory hierarchy to find the most suitable inventory or subinventory.

When the `AddItemDistribute()` function is called, the targeted inventory and all of its subinventories are given the opportunity to evaluate and claim the item. After each has been considered, the most suitable inventory attempts to add the item.

[![An example of an inventory system in Scene Graph.](https://dev.epicgames.com/community/api/documentation/image/7de2c2c6-e139-47c2-b31f-39555d851ad2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7de2c2c6-e139-47c2-b31f-39555d851ad2?resizing_type=fit)

Inventory

## Player Inventory Root

Players have an inventory by default. This is known as the **Inventory Root**. Unlike other inventories, the player’s Inventory Root cannot accept items. Instead, it acts as the parent for subinventories beneath it. This provides a way for you to target the Inventory Root with `AddItemDistribute()` and for an item to find an eligible inventory, even if the initial target cannot receive it.

For a player to receive items, they need to have one or more subinventories beneath the Inventory Root.

The above explanation does not affect entities that have an `inventory_component` added through Verse or via the [prefab editor](https://dev.epicgames.com/documentation/fortnite/prefab-editor-user-interface-in-unreal-editor-for-fortnite).

[![An example of the Inventory Root.](https://dev.epicgames.com/community/api/documentation/image/cffe33a8-693c-4250-8f3a-7c2617e45e62?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cffe33a8-693c-4250-8f3a-7c2617e45e62?resizing_type=fit)

Inventory Root
