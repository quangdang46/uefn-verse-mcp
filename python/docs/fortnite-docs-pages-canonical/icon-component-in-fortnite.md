## https://dev.epicgames.com/documentation/en-us/fortnite/icon-component-in-fortnite

# Icon Component

The Icon Component provides a way to add a custom icon to items that you create.

![Icon Component](https://dev.epicgames.com/community/api/documentation/image/9b6df552-2936-4f9c-8943-3ccba4d47002?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

The `icon_component` is a Scene Graph [component](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#component) used to assign an icon to an [entity](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#entity). Refer to **[Working with Entities and Components](https://dev.epicgames.com/documentation/fortnite/working-with-entities-and-components-in-unreal-editor-for-fortnite)** for how to add a component to your entity.

## Class Description

The `icon_component` uses a **[Texture](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#texture)** [asset](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#asset) as a visual reference for the entity [in-game](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#in-game). 
It could be an item icon inside a backpack, a character portrait or an ability icon for a [hotbar](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#hotbar). The component holds a single field, Icon, which can be set in the [Prefab Editor](https://dev.epicgames.com/documentation/fortnite/prefab-editor-user-interface-in-unreal-editor-for-fortnite) or through [Verse](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#verse) script.

## Example

In the example below, the `icon_component` is added to an item prefab (for example an entity with an `item_component`) and a Texture icon representing the entity.

[![An example of the icon_component on an entity in the Prefab Editor.](https://dev.epicgames.com/community/api/documentation/image/60cc7503-ddda-4e24-a080-d35b7bb88532?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60cc7503-ddda-4e24-a080-d35b7bb88532?resizing_type=fit)

Icon Component

Now when the item is picked up by a player, the Icon is used in the hotbar and Backpack UI elements.

Once the [Custom Items and Inventory system](https://dev.epicgames.com/documentation/fortnite/custom-items-and-inventory-overview-in-fortnite) is enabled the `icon_component` is listed in the component dropdown list. For more information check out the [icon_component API reference](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/scenegraph) from the [Verse API](https://dev.epicgames.com/documentation/fortnite/verse-api).

## Verse: Icon

With Verse, the Icon field can be set on demand. Below is a script of an `icon_component` subclass that swaps the texture in the Icon field on a loop:

Verse

```
# Copyright Epic Games, Inc. All Rights Reserved.

using { /Verse.org/Assets }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }

# This is a subclass of the icon_component.
# You can add this component to an entity and it will cycle between icons from an editable list.
```

Below is a [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) you can call on an entity. Targeting an entity that has an `icon_component` displays the icon on the screen, providing the entity has a [player](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#player) for an ancestor:

Verse

```
# Copyright Epic Games, Inc. All Rights Reserved.

using { /UnrealEngine.com/Temporary/UI }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }

# Calling this function will display a texture block widget to the player screen.
# It sources the texture from the icon_component from the provided entity.
```

The `cycling_icon_component` is added to an entity prefab definition.

- The `cycling_icon_component` is added to an entity prefab definition.

  [![The cycling_icon_component is added to a prefab definition. These icons are added to an array in the Details panel and can be called by the Verse script to display in the HUD.](https://dev.epicgames.com/community/api/documentation/image/27cfe051-3aa9-49ab-97ea-78c64e8e1ace?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27cfe051-3aa9-49ab-97ea-78c64e8e1ace?resizing_type=fit)

  cycling_icon_component
- The Verse device, and an instance of the prefab, are placed in the scene.

  [![The Verse device and and instance of the prefab, are placed in the scene.](https://dev.epicgames.com/community/api/documentation/image/734cfc45-a30e-40c5-8987-5a7068a110c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/734cfc45-a30e-40c5-8987-5a7068a110c3?resizing_type=fit)

  Verse Device and Prefab
- Starting a session illustrates how the icon displays on all players screens and is updated when the icon changes.

  cycling_icon_component in the HUD

To learn more about using Verse to create [user interfaces (UI)](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#ui), see **[Creating UI with Verse](https://dev.epicgames.com/documentation/fortnite/creating-ui-with-verse-in-unreal-editor-for-fortnite)**.
