## https://dev.epicgames.com/documentation/en-us/fortnite/create-an-item-pickup-interactable-component-in-fortnite

# Create an Item Pickup Interactable Component

Create a custom interactable component so custom items that players pick up are added to the player's inventory.

This feature is in an experimental state so you can try it out, provide feedback, and see what we are planning. You cannot publish a project that uses Custom Inventory and Items at this time.

Please keep in mind that we do not guarantee backward compatibility for assets created at the Experimental stage, the APIs for these features are subject to change, and we may remove entire experimental features or specific functionality at our discretion. Check out the list of known issues before you start working with the feature.

This tutorial shows you how to create a custom "item pickup" interactable component that allows players to pick up custom items, and that adds the picked up item to the player's inventory.

## Before Your Begin

You should be familiar with UEFN, Scene Graph, and Verse code in order to successfully complete this tutorial.

## Set Up Your Project

Follow these steps to set up your project and enable Custom Inventory and Items.

## Write the Verse Code

The `interactable_component` is a Scene Graph component that is used to handle general interaction. By default, players can press an input to interact with an entity that has the component. Follow these steps to customize this component.

An `interactable_component` requires an entity to have a `mesh_component` to interact with. It is necessary for the object to have collision that can be checked against when something is trying to interact with the entity.

1. Select the entity you are going to add the custom interactable component to. In the Details panel, click +Component and select New Verse Component. The Create Verse Component window opens.

   You can also create a Verse component by adding a new Verse file using Verse Explorer.
2. Under **Choose a Template**, select **Scene Graph Component**.
3. At the bottom, in the **Component Name** field, type item_interactable_component. Then click Create.
4. In the menu bar, click **Verse > Verse Explorer**. Locate your new Verse component, right click it and select **Open in Visual Studio Code**.
5. In the new Verse file, delete the existing code, since you are going to write the whole thing in this tutorial. First add the required modules. You can copy and paste them from the snippet below.

   Verse

   ```
   using { /Verse.org/Simulation }
   using { /Verse.org/SceneGraph }
   using { /UnrealEngine.com/Itemization }
   ```

   using { /Verse.org/Simulation }
   using { /Verse.org/SceneGraph }
   using { /UnrealEngine.com/Itemization }
6. Next, add a helper function to get the root inventory from a specified player.

   Verse

   ```
   GetInventoryRoot(Agent:agent)<decides><transacts>:inventory_component =
           Inventory := (for (I : Agent.FindDescendantComponents(inventory_component)) { I })[0]
   ```

   GetInventoryRoot(Agent:agent)&lt;decides&gt;&lt;transacts&gt;:inventory_component =
   Inventory := (for (I : Agent.FindDescendantComponents(inventory_component)) { I })[0]
7. Before creating the new custom component, you need to declare a new message type constant outside of the scope of our class. This message is the default value if the function is unable to get a name from an item's `item_details_component`. Typically this message type is written at the very bottom of the Verse file.

   Verse

   ```
   DefaultInteractionMessage<localizes>:message = "Interact"
   ```

   DefaultInteractionMessage&lt;localizes&gt;:message = &quot;Interact&quot;
8. Define a new Scene Graph that inherits from the `interactable_component`. This is the `item_interactable_component`.

   Verse

   ```
   item_interactable_component := class(interactable_component) :
   ```

   item_interactable_component := class(interactable_component) :
9. Add an optional `cancelable` variable. This custom component will need to subscribe to an event to know when a player interacts with the item. This variable saves a reference to that subscription, and will cancel it if needed.

   Verse

   ```
   var SucceededEventHandler : ?cancelable = false
   ```

   var SucceededEventHandler : ?cancelable = false
10. Next, override the `OnAddedToScene` function so that it sets the optional variable when the parent of the entity that owns this component changes (such as when it is placed in the world). Set `SucceededEventHandler` to call the subscribe function on `SucceededEvent`. This will also define the `OnSucceededEvent` function so that it triggers when interaction occurs.

    Verse

    ```
    OnAddedToScene<override>():void =
          if(not SucceededEventHandler?):
             set SucceededEventHandler = option{SucceededEvent.Subscribe(OnSucceededEvent)}
    ```

    OnAddedToScene&lt;override&gt;():void =
    if(not SucceededEventHandler?):
    set SucceededEventHandler = option{SucceededEvent.Subscribe(OnSucceededEvent)}
11. The `SucceededEvent` subscription needs to be cleaned up once an item has been picked up, or it might interfere with other code once the item is in an inventory. You
    can do this by overriding the `OnRemovingFromScene` function.
    This activates when the parent of the item entity changes. Use it here to `cancel()` the event subscription. If successful it will also invalidate the `SucceededEventHandler`.

    Verse

    ```
    OnRemovingFromScene<override>():void =
        if(SucceededEventHandler?.Cancel()):
    		   set SucceededEventHandler = false
    ```

    OnRemovingFromScene&lt;override&gt;():void =
    if(SucceededEventHandler?.Cancel()):
    set SucceededEventHandler = false
12. In **step 10** the `OnSucceededEvent` function is subscribed to `SucceededEvent`, but it doesn't exist in the code yet. So you need to write a new function with the same signature. In **step 6**, you used the helper function `GetInventoryRoot[]`  to retrieve the root inventory from the interacting player. Now call the `AddItemDistribute()` function to provide the entity owning this component.

    Verse

    ```
    OnSucceededEvent(Agent:agent):void =
            if(PickupInventory := GetInventoryRoot[Agent]):
                if(PickupInventory.AddItemDistribute(Entity).GetSuccess[]):
    ```

    OnSucceededEvent(Agent:agent):void =
    if(PickupInventory := GetInventoryRoot[Agent]):
    if(PickupInventory.AddItemDistribute(Entity).GetSuccess[]):
13. The last bit of code needed for this component is the override for the `InteractMessage[]` function.
    This returns the message that is shown onscreen when a player is looking at the item, before they pick it up. This will check the entity owning this component to see if it also has an `item_details_component`. If it does, this retrieves the name of the item. Otherwise, if the entity did not have an `item_details_component` or it was removed for some reason, this uses the `DefaultInteractionMessage` we declared earlier.

    Verse

    ```
    InteractMessage<override>(Agent:agent)<reads><decides>:message =
            if(Details := Entity.GetComponent[item_details_component]):
                Details.Name
            else:
                DefaultInteractionMessage
    ```

    InteractMessage&lt;override&gt;(Agent:agent)&lt;reads&gt;&lt;decides&gt;:message =
    if(Details := Entity.GetComponent[item_details_component]):
    Details.Name
    else:
    DefaultInteractionMessage

## Setting Up the Prefab

Now that you have written your `item_interactable_component`, you can make an example item to showcase it. Follow these steps to create a Scene Graph prefab and attach the new component.

1. Right-click in the Content Browser, and from the context menu select **Entity Prefab Definition**. Name the new prefab **Item_Cube**.

   [![Right-click in the Content Browser, and select Entity Prefab Definition. This creates a new Scene Graph prefab.](https://dev.epicgames.com/community/api/documentation/image/0fbab0d8-19ae-408c-b443-97eb63436156?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0fbab0d8-19ae-408c-b443-97eb63436156?resizing_type=fit)
2. Open the new prefab, and add the following components by clicking **+Component** in the **Details** panel.

   - `item_component`
   - `item_details_component` - fill out the fields in this component:

     - **Name**
     - **Description**
     - **Short Description**
   - `mesh_component` - select the cube primitive or another cube.
   - `item_interactable_component`

   [![](https://dev.epicgames.com/community/api/documentation/image/9d92eaa1-41f0-4a70-a9d6-6d92dcc133ff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d92eaa1-41f0-4a70-a9d6-6d92dcc133ff?resizing_type=fit)

The video below shows the `item_interactable_component` in action. When the player interacts with the **Item_Cube** prefab you created, the item is added to the player's inventory.

Here is the complete script for this tutorial.

Verse

```
using { /Verse.org/Simulation }
using { /Verse.org/SceneGraph }
using { /UnrealEngine.com/Itemization }

# This function returns the first subentity with an inventory_component. Use this to get the root inventory of an agent.
GetInventoryRoot(Agent:agent)<decides><transacts>:inventory_component =
        Inventory := (for (I : Agent.FindDescendantComponents(inventory_component)) { I })[0]
```

---
