## https://dev.epicgames.com/documentation/en-us/fortnite/working-with-entities-and-components-in-unreal-editor-for-fortnite

# Working with Entities and Components

Learn how to build out entities and add data and behaviors to them with components.

![Working with Entities and Components](https://dev.epicgames.com/community/api/documentation/image/41706323-ef99-4701-a23c-68721d417e57?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

Below are the workflows for adding entities, [components](https://dev.epicgames.com/documentation/fortnite/component), and [prefabs](https://dev.epicgames.com/documentation/fortnite/prefabs-and-prefab-instances-in-unreal-editor-for-fortnite) to your project. You can use these workflows to create complex objects and add them to your experience.

## Creating an Entity

To create an entity:

## Adding More Entities Through the Outliner

Once you have an entity in the scene, you can add more entities through the Outliner.

Duplicating the entity creates more entities in the Outliner.

![](https://dev.epicgames.com/community/api/documentation/image/998a626d-8cfb-47ab-8cc0-dfda4137af35?resizing_type=fit)

You can also right-click on an entity in the Outliner and choose the following options:

- **Add Entity**: This option adds a new entity nested under the entity you originally selected.
- **Group Under New Entity**: This option creates a new entity that becomes the parent of the entity you originally selected. If your original entity was nested under another entity, the structure stays the same, with the new entity inserted between the original parent and child entities.

## Nesting and Structuring Entities

Placing entities into a hierarchical structure creates relationships between the entities in the hierarchy. The nesting structure has four levels:

- **Ancestor**: Any level above parent (parent, grandparent, great-grandparent, and so on).
- **Descendent**: Any level below the currently selected entity (children, grandchildren, and so on).
- **Parent**: Single ancestor one level above the currently selected entity.
- **Child**: Descendent one level below the currently selected entity.

In this structure, the Ancestor entity controls the lifetime of all the entities nested underneath.

[![An example of nested entities.](https://dev.epicgames.com/community/api/documentation/image/6a387086-9e6c-4187-beef-a538cd2a22dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6a387086-9e6c-4187-beef-a538cd2a22dd?resizing_type=fit)

In the example below, the **lamp post** on its own is a simple game object that can only do the one thing its component is set to do: be a static mesh of a lamp post.

[![](https://dev.epicgames.com/community/api/documentation/image/e3afb049-8283-407b-a249-49cb07ac5e49?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e3afb049-8283-407b-a249-49cb07ac5e49?resizing_type=fit)

When the **Rotation_Point** entity, **Dock_Lantern** entity, and **SpotLight** entity are nested beneath the **Default_Wooden_LightPost_Prefab_C** entity, the lamp post takes on the characteristics of its children, making the lamp post a more complex game object.

[![](https://dev.epicgames.com/community/api/documentation/image/d0f53264-744f-461d-8d67-7c5806068e66?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0f53264-744f-461d-8d67-7c5806068e66?resizing_type=fit)

There are a few reasons to do this:

- Scale the component functions of an entity to specify how the entity should work in the scene.
- Determine how child and descendent entities interact with the parent and ancestor entities.
- Hierarchical structuring represents object lifetime in-game; if the ancestor object is destroyed, then so are all the descendent and child objects.

  When grouping entities, rename the parent entity so you know what the entity is.

Nesting is a concept that you can take advantage of. For example, you can align architectural assets to reduce the likeliness of gaps in your buildings.

Descendent entities can be offset relative to the ancestor’s position in the world allowing you to set a central pivot point that controls the placement of the building’s walls, floors, and more when being duplicated or moved in the scene.

## Adding a Component

Adding a component to an entity determines the behavior of game objects in your project.

To add components to your entity and customize them from the **Details** panel:

Components can be simple, like a mesh, or complex, like a custom Verse script. You can assign multiple components to one entity to define how that entity behaves in your project. However, only one component type can be used on an entity at a time.

This means once you select a component type you cannot reuse that component type on the same entity. To use the same component you'll need to add another entity and add the same component to the new entity. For more information on which components are available in Scene Graph, refer to [Components](https://dev.epicgames.com/documentation/fortnite/components-in-unreal-editor-for-fortnite).

Don’t see the component you need? Try making your own! Check out how to [create your own components with Verse](https://dev.epicgames.com/documentation/fortnite/creating-your-own-component-using-verse-in-unreal-editor-for-fortnite).

Currently you can only add one of a given component subclass. For example, you can only have one `point_light_component` on your entity, but you can have one `point_light_component` and one `rect_light_component` on your entity. The same limitation applies to your custom components made in Verse.

![](https://dev.epicgames.com/community/api/documentation/image/b19104e9-523e-46c5-9d46-8e98729683b6?resizing_type=fit)

### Asset-Generated Components

An asset-generated component is a component class that is automatically created based on preexisting content in your project, such as a mesh, sound, or particle system asset. These assets may also expose properties that you can modify on the generated component.

## Overriding Components

You can override components in the **Details** panel of the [Prefab Editor](https://dev.epicgames.com/documentation/fortnite/prefab-editor-user-interface-in-unreal-editor-for-fortnite) or in the scene. This means that you can change the nature of the component by adding new functionality or changing the associated assets of the component without having to create a new entity or remove the current component.

Components can have 4 different override states. These states are visible on the component card:

| Image | Name | Description |
| --- | --- | --- |
|  | **No Override** | The component does not have an override. |
|  | **Override Here** | The component is overridden here at this level. |
|  | **Override Inside** | The component has an override state on one of its options. [INCLUDE:#state] |
|  | **Unique Override** | The override is unique to this prefab instance. [INCLUDE:#state] |

To override a component, do the following:

In the image below, all empty icons next to the components in the Details panel now have the override icon.

[![](https://dev.epicgames.com/community/api/documentation/image/203bbca4-5d2d-4f2d-a451-0833d6973926?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/203bbca4-5d2d-4f2d-a451-0833d6973926?resizing_type=fit)

Changing the default values of a component’s options also creates an override to that component’s function, such as increasing the default values on a light component. When you change default values, the component control button features a **+ icon** to signal that default values were changed.

[![](https://dev.epicgames.com/community/api/documentation/image/f27e28a3-d49f-48dd-b356-903a818234ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f27e28a3-d49f-48dd-b356-903a818234ac?resizing_type=fit)

## Clear Overrides

To go back to the original prefab design, do the following:

## Removing a Component

To remove components from entities:

[![](https://dev.epicgames.com/community/api/documentation/image/fcba2e1d-c4cc-4999-9a1e-241cae6cd0b9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fcba2e1d-c4cc-4999-9a1e-241cae6cd0b9?resizing_type=fit)

This workflow works in the Prefab Editor as well.

## Saving Entities as Prefabs

Once you create your entities and add components to them, you can save specific entities as a prefab. This means you can create multiple instances of the same entity and component structure, and that these changes propagate across them all instantly. To learn how to create prefabs and propagate changes, see [Prefabs and Prefab Instances](https://dev.epicgames.com/documentation/fortnite/prefabs-and-prefab-instances-in-unreal-editor-for-fortnite).

## Working with Scene Graph in Fortnite Creative

**Scene Graph Entity** support is available in Fortnite Creative. Using the **[Phone Tool](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#phone)** you have basic editing capabilities in Scene Graph using the controls and feedback you're familiar with during **[Edit Mode](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#edit-mode)**. The support feature also means you can interact with all entities and actors simultaneously in the scene using the Phone Tool.

These basic interactions between Fortnite Creative and Scene Graph are possible because entire entity hierarchies are selected as one object by the Phone Tool.

Scene Graph entities cannot be created in Creative edit Mode.
