## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/itemization/canadditem

# item_component class
Learn technical details about the item_component class.
Anything using this component should be considered an item. Required to interact with inventories.
|
---|---
Verse `using` statement | `using { /UnrealEngine.com/Itemization }`
## Inheritance Hierarchy
This class is derived from `component`.
Name | Description
---|---
[`component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component) |  Base class for authoring logic and data in the SceneGraph. Using components you can author re-usable building blocks of logic and data which can then be added to entities in the scene. Components are a very low level building block which can be used in many ways. For example:
  * Exposing engine level concepts like mesh or sound
  * Adding gameplay capabilities like damage or interaction
  * Storing an inventory for a character in the game

As components are generic there is no specific way that they must be used. It is up to the needs of your experience if you use one big game component or if you break up logic into many small components. Classes deriving from component must also specify `<final_super>` to be added to entities. This ensures the class will always derive directly from `component`. Further subclassing of the initial derived component is allowed and does not require specifying `<final_super>` on the derived classes. Only one instance of a component from each subclass group can be added to an entity at a time. For example, given this group of components, only one light_component can exist on a single entity. To create multiple lights you should use multiple entities. light_component := class(component){} capsule_light_component := class(light_component){} directional_light_component := class(light_component){} spot_light_component := class(light_component){} sphere_light_component := class(light_component){} rect_light_component := class(light_component){} ============================================================================== Component Lifetime Components move through a series of lifetime functions as they are added to entities, added to the scene, and begin running in the simulation. Components should override these methods to perform setup and run their simulation. As a component shuts down it will then move through shutdown version of these functions, giving users the opportunity to clean up any retained state on the component before it is disposed . Lifetime Methods: OnAddedToScene OnBeginSimulation -> OnSimulate OnEndSimulation OnRemovingFromScene ==============================================================================
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`Categories` | `[]item_category` |  Add one or more category instances to help define and organize this item.
`ChangeEquippedEvent` | `listenable(payload)` |  Broadcast when this item is equipped or unequipped.
`ChangeInventoryEvent` | `listenable(payload)` |  Broadcast when this item changes inventory.
`Entity` | `entity` |  The parent entity of this component.
  * Components must have a parent entity pointer provided when being constructed.
  * Components cannot be moved between parents.

`TickEvents` | `?tick_events` |  Set callbacks to `TickEvents.PrePhysics` and `TickEvents.PostPhysics` to receive per-frame updates before and after physics is updated on your object.
### Functions
Function Name | Description
---|---
[`Drop`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/drop) |  Removes the item from its inventory and places it in the simulation world. Works on orphaned items i.e. outside the world or any inventory. Fails if the item is already a pickup. The transform of the item will not be altered except to unparent it from any inventory.
[`Equip`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/equip) |  Attempts to equip this item within the inventory it is currently in. Fails if not in an inventory or if equip_item_query_event contains any errors after querying.
[`GetParentInventory`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/getparentinventory) |  Returns the inventory_component this item currently resides in. Fails if it cannot find a valid parent inventory.
[`IsEquipped`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/isequipped) |  Succeeds if this item is considered currently within an inventory and equipped.
[`IsInScene`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/isinscene) |  Succeeds if the component is currently in the scene.
  * After `OnAddedToScene` is called this call succeeds.
  * After `OnRemovingFromScene` is called this call fails.

[`IsSimulating`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/issimulating) |  Succeeds if the component is currently simulating.
  * After `OnBeginSimulation` is called this call succeeds.
  * After `OnEndSimulation` is called this call fails.

[`OnAddedToScene`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/onaddedtoscene) |  Called when the component is added to the scene by parenting it under the simulation entity or another entity already in the scene.
  * Querying for components in the scene is valid after this phase completes.

[`OnBeginSimulation`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/onbeginsimulation) |
[`OnBeginSimulation`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/onbeginsimulation) |  Called when the component begins simulating within the scene.
  * Use this to set up TickEvent callbacks or other setup that must be guaranteed to complete immediately.
  * `OnAddedToScene` is guaranteed to run before `OnBeginSimulation`.

[`OnEndSimulation`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/onendsimulation) |
[`OnEndSimulation`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/onendsimulation) |  Called when the component ends simulation within the scene.
  * Simulation ends on a component when the experience resets, the parent entity is removed from the scene.
  * Cached TickEvents cancelables should be canceled in `OnEndSimulation`.
  * `OnSimulate` task will be canceled before `OnEndSimulation` is called.
  * `OnEndSimulation` is only called on components that have already had `OnBeginSimulation` called.

[`OnReceive`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/onreceive) |  Respond to a scene event. Return true to consume the event and halt propagation to the next entity.
[`OnRemovingFromScene`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/onremovingfromscene) |  Called when the component is about to be removed from the scene.
  * Components are removed from a scene when the parent entity is removed from the scene.
  * `OnRemovingFromScene` is only called on components that have already had `OnAddedToScene` called.

[`OnSimulate`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/onsimulate) |  Called when the component begins simulating within the scene.
  * Use this to add asynchronous/suspends update logic for a component.
  * `OnBeginSimulation` is guaranteed to run before `OnSimulate`.
  * `OnSimulate` will be cancelled before `OnEndSimulation`

[`PickUp`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/pickup) |  Fails if this item is already in an inventory, or the inventory cannot accept the item.
[`RemoveFromEntity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/removefromentity) |  Removes the component from the entity.
  * Removed components are removed from the scene and can only be added back to the same entity.
  * Flows through `OnEndSimulation`-> `OnRemovingFromScene`.

[`SendDown`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component/senddown) |  Send a scene event to this component, invoking OnReceive. Return true to consume the event and halt propagation to the next entity.
[`Unequip`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component/unequip) |  Attempts to unequip this item. Fails if not in an inventory, not currently equipped or if unequip_item_query_event contains any errors after querying.
