## https://dev.epicgames.com/documentation/en-us/fortnite/description-component-in-fortnite

# Description Component

Learn how to add textual data to your items in the Custom Items and Inventories system with the Description Component.

![Description Component](https://dev.epicgames.com/community/api/documentation/image/304b4251-0dfe-4ee3-b5e7-a0bb9dff1454?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

The `description_component` is a Scene Graph component. It contains text data about the item, such as its name and description. Refer to **[Working with Entities and Components](https://dev.epicgames.com/documentation/fortnite/working-with-entities-and-components-in-unreal-editor-for-fortnite)** for how to add a [component](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#component) to your [entity](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#entity).

The component's text data can be used by other systems. Any kind of entity could utilize this component, but it is usually most helpful for player-facing information such as a [character](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#character), an [item](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#item), a vehicle, a location and more. The `description_component` has three editable fields that can be modified in the [Prefab Editor](https://dev.epicgames.com/documentation/fortnite/prefab-editor-user-interface-in-unreal-editor-for-fortnite) and also with [Verse](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#verse):

- **`Name`**: The name of the entity.
- **`Description`**: A long description of the entity.
- **`Short Description`**: A brief description of the entity.

See **[Components](https://dev.epicgames.com/documentation/fortnite/components-in-unreal-editor-for-fortnite)** for a complete list of item and inventory components.

When the Custom Items and Inventory system is enabled the `description_component` is shown in the component dropdown list. For more information, check out the `description_component` API reference from the [Verse API](https://dev.epicgames.com/documentation/fortnite/verse-api).

## Example

In the example below, the `description_component` is added to an item [prefab](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prefab) (an entity with an `item_component`).

[![An example of the description_component in the Prefab Editor.](https://dev.epicgames.com/community/api/documentation/image/12ad55a2-f90b-4e75-85f8-0184780fd4eb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12ad55a2-f90b-4e75-85f8-0184780fd4eb?resizing_type=fit)

Description Component

Now when the item is picked up by a player, the `Name` and `Description` fields from the `description_component` are shown in the Backpack UI.

An example of the Item Details Component in a project used to define a Cube item.

## Verse: Description

Through Verse the `description_component` properties can be dynamically modified or new ones added.

You can use the examples below to set up the `description_component` in your project using Verse.

Below is a subclass of the `description_component`. It selects a random entry from an array of names to be used as the value for `Name` in the component.

Verse

```
# Copyright Epic Games, Inc. All Rights Reserved.

using { /Verse.org/SceneGraph }
using { /Verse.org/Presentation }
using { /Verse.org/Simulation }
using { /Verse.org/Random }

# The text we want to use for names in our description_component must be declared outside of the class.
```
