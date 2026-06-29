## https://dev.epicgames.com/documentation/en-us/fortnite/components-in-unreal-editor-for-fortnite

# Components

Components allow you to add functionality and behavior to your Scene Graph entities.

![Components](https://dev.epicgames.com/community/api/documentation/image/9bfad83d-00b5-4add-98c1-69bd86cd8244?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

Components are what provide data and behavior to the entities in Scene Graph. Components define what an entity is supposed to be doing in the scene.

In Scene Graph components are focused, meaning they reference one behavior or characteristic. When a component is added to an entity, this establishes an association between the entity and the component behavior assigned to it.

Components have editable properties that can be physical, like a static mesh and particle system, or logical, like a gameplay tag or custom Verse code that defines the movement of a platform. By default, all entities have a transform component to specify where the entity exists in the world.

The following is the full list of components that are part of Scene Graph in UEFN:

- [![Interactable Components](https://dev.epicgames.com/community/api/documentation/image/e07eb6c2-c804-4b20-959a-fa48771bfa04?resizing_type=fit&width=640&height=640)

  Interactable Components

  Components that enable interactions using Scene Graph.](https://dev.epicgames.com/documentation/fortnite/interactable-components)
- [![Keyframed Movement Component](https://dev.epicgames.com/community/api/documentation/image/9b144a8c-33bf-4d06-bd1f-9fd2325dbea4?resizing_type=fit&width=640&height=640)

  Keyframed Movement Component

  The Keyframed Movement component lets you animate entities by adding keyframes in Unreal Editor for Fortnite.](https://dev.epicgames.com/documentation/fortnite/keyframed-movement-component-in-unreal-editor-for-fortnite)
- [![Light Components](https://dev.epicgames.com/community/api/documentation/image/282abe38-4d8b-4bcf-af6d-c83057ad9dea?resizing_type=fit&width=640&height=640)

  Light Components

  Use the different types of light components to add lighting to your project.](https://dev.epicgames.com/documentation/fortnite/light-components-in-unreal-editor-for-fortnite)
- [![Mesh Component](https://dev.epicgames.com/community/api/documentation/image/201b1699-f1f8-4e9e-9eeb-2e0458de99ae?resizing_type=fit&width=640&height=640)

  Mesh Component

  The Mesh component adds a mesh to an entity, giving it a form.](https://dev.epicgames.com/documentation/fortnite/mesh-component-in-unreal-editor-for-fortnite)
- [![Particle System Component](https://dev.epicgames.com/community/api/documentation/image/c270301b-d750-4fbd-83b6-313d8133ef24?resizing_type=fit&width=640&height=640)

  Particle System Component

  Use a particle system component to add Niagara effects to your project.](https://dev.epicgames.com/documentation/fortnite/particle-system-component-in-unreal-editor-for-fortnite)
- [![Sound Component](https://dev.epicgames.com/community/api/documentation/image/a5d8cc61-9f97-4b76-84a7-375809b58183?resizing_type=fit&width=640&height=640)

  Sound Component

  Use the sound component to add sound to your project.](https://dev.epicgames.com/documentation/fortnite/sound-component-in-unreal-editor-for-fortnite)
- [![Inventory Component](https://dev.epicgames.com/community/api/documentation/image/7edc88ec-c687-41ef-89d3-97c83f0b0d88?resizing_type=fit&width=640&height=640)

  Inventory Component

  The Inventory Component provides a way to create custom inventories.](https://dev.epicgames.com/documentation/fortnite/inventory-component-in-fortnite)
- [![Fort Inventory Component](https://dev.epicgames.com/community/api/documentation/image/d97ff61f-9118-42f2-8bec-d0668f6405d9?resizing_type=fit&width=640&height=640)

  Fort Inventory Component

  Design a custom Fortnite inventory for your island using fort_inventory_component.](https://dev.epicgames.com/documentation/fortnite/fort-inventory-component-in-fortnite)
- [![Item Component](https://dev.epicgames.com/community/api/documentation/image/721f7816-6f70-4416-a44b-faf8a6d73694?resizing_type=fit&width=640&height=640)

  Item Component

  The Item Component provides a way to create custom items that have custom properties.](https://dev.epicgames.com/documentation/fortnite/item-component-in-fortnite)
- [![Icon Component](https://dev.epicgames.com/community/api/documentation/image/45225689-7572-4e20-bed0-3dac03120724?resizing_type=fit&width=640&height=640)

  Icon Component

  The Icon Component provides a way to add a custom icon to items that you create.](https://dev.epicgames.com/documentation/fortnite/icon-component-in-fortnite)
- [![Description Component](https://dev.epicgames.com/community/api/documentation/image/d9059f3a-403e-4118-ad37-698ddc95f64f?resizing_type=fit&width=640&height=640)

  Description Component

  Learn how to add textual data to your items in the Custom Items and Inventories system with the Description Component.](https://dev.epicgames.com/documentation/fortnite/description-component-in-fortnite)
- [![Stackable Component](https://dev.epicgames.com/community/api/documentation/image/769f6bf9-98e6-4686-b873-1f86e8cd66b1?resizing_type=fit&width=640&height=640)

  Stackable Component

  The Stackable Component provides a way for an entity to form stacks.](https://dev.epicgames.com/documentation/fortnite/stackable-component-in-fortnite)
- [![Fort Item Pickup Interactable Component](https://dev.epicgames.com/community/api/documentation/image/ff25075e-0932-471c-a60b-ad0d5dc5b198?resizing_type=fit&width=640&height=640)

  Fort Item Pickup Interactable Component

  The fort_item_pickup_interactable_component allows UEFN characters pickup items into their inventory.](https://dev.epicgames.com/documentation/fortnite/fort-item-pickup-interactable-component-in-fortnite)

Don't see the component you need? Try making your own! Check out how to [create your own component in Verse](https://dev.epicgames.com/documentation/en-us/uefn/creating-your-own-component-using-verse-in-unreal-editor-for-fortnite).
