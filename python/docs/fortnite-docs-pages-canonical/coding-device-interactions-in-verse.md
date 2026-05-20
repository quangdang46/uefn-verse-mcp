## https://dev.epicgames.com/documentation/en-us/fortnite/coding-device-interactions-in-verse

# Coding Device Interactions

Use Verse to code your own functions and behavior that run when events occur

![Coding Device Interactions](https://dev.epicgames.com/community/api/documentation/image/f9ed8322-3609-4cd1-9d28-8be1014e4484?resizing_type=fill&width=1920&height=335)

If you're familiar with [Direct Event Binding](https://dev.epicgames.com/documentation/fortnite/direct-event-binding-in-unreal-editor-for-fortnite), the concept of [events](https://dev.epicgames.com/documentation/fortnite/verse-glossary) and functions you're used to working with for Creative devices also translates to Verse. You can use Verse to code your own functions and behavior that run when events occur!

The following sections describe the different ways you can work with Creative device events in Verse and code your own logic.

## Binding Functions to Creative Device Events

You can subscribe to events that Creative devices expose in their API. For example, the [Button](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-button-devices-in-fortnite-creative) device's class `button_device` exposes `InteractedWithEvent`, which occurs whenever the player interacts with the Button device. You can call `Subscribe()` on the event and pass the identifier of the function that you want to call whenever the event is signaled.

[Subscribing](https://dev.epicgames.com/documentation/fortnite/verse-glossary#subscribe) allows you to specify a function to call when an event is signaled, referred to as **binding** to an event. The bound function is referred to as a [handler](https://dev.epicgames.com/documentation/fortnite/verse-glossary#handler). In the example below, the handler is `OnButtonInteractedWith`.

Depending on the [event](https://dev.epicgames.com/documentation/fortnite/verse-glossary) definition, the [function signature](https://dev.epicgames.com/documentation/fortnite/verse-glossary#function-signature) must match what the event expects to call. For example, subscribing to the event `InteractedWithEvent` for the `button_device` expects to be given a function with one parameter of type `agent`, so the `OnButtonInteractedWith` function should look like this:

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

hello_world_device := class(creative_device):
    @editable
    MyButtonDevice:button_device = button_device{}

    OnBegin<override>()<suspends>:void=
        # Bind OnButtonInteractedWith function to the InteractedWithEvent of the Button device
        MyButtonDevice.InteractedWithEvent.Subscribe(OnButtonInteractedWith)
```

When you call `Subscribe()` on a device event, the function returns a `cancelable` result. Calling `Cancel()` on a `cancelable` variable unsubscribes the function handling the event, so the function will no longer be called when the event is signaled.

If you want to store a single `cancelable` result you can use a container like an option. You can't directly create a `cancelable` variable, but you can set up an `option` variable to hold the result of a subscription.

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

spawner_button := class(creative_device):

    @editable
    Button:button_device = button_device{}

    # Container for storing the event subscription
    var ButtonSubscription:?cancelable = false
```

If your Verse device has multiple event subscriptions, it's a good idea to use a container like an array to store all the `cancelable` results from each event subscription so you can cancel them later. Because `Subscribe()` returns a `cancelable` result, you can set your `cancelable` array values when you first subscribe to events.

### Spawning Item When Player Presses Button Example

[![Item spawner spawns item when player interacts with button](https://dev.epicgames.com/community/api/documentation/image/ecaccafe-eb27-43b9-8fa7-7d76e7effac2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ecaccafe-eb27-43b9-8fa7-7d76e7effac2?resizing_type=fit)

In this section, you'll learn to create an [item spawner](https://www.epicgames.com/fortnite/en-US/creative/docs/using-item-spawner-devices-in-fortnite-creative) that spawns its item when the player interacts with a [button](https://www.epicgames.com/fortnite/en-US/creative/docs/using-button-devices-in-fortnite-creative).

1. Start by placing an [Item Spawner](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-item-spawner-devices-in-fortnite-creative) device and [Button](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-button-devices-in-fortnite-creative) device in your level. For how to place devices in your level, see Object Placement in [UEFN Controls for Creative Users](https://dev.epicgames.com/documentation/fortnite/guide-to-uefn-controls-for-creative-users-in-unreal-editor-for-fortnite).
2. Set what item will spawn for the Item Spawner device. See [Item Spawner](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-item-spawner-devices-in-fortnite-creative) for more details.
3. Create a Verse device with editable properties for the Button device and Item Spawner device. See [Adding a Verse Reference to a Creative Device in Your Level](https://dev.epicgames.com/documentation/en-us/uefn/customize-device-properties-in-verse).
4. Add a `cancelable` option variable to the device to track the Button device subscription.
5. Subscribe to the `InteractedWithEvent`, cast the result to an `option`, and assign it to the `ButtonSubscription` variable.
6. In the event handler for the `InteractedWithEvent`, call `ItemSpawner.SpawnItem()`. Then cancel the subscription by accessing the value inside the `ButtonSubscription` option and calling `Cancel()`.
7. The following is the full Verse code for spawning an item when the player interacts with the Button device. Interacting with the button device a second time will not spawn another item.

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Verse.org/Simulation }

        spawner_button := class(creative_device):

           @editable
           Button:button_device = button_device{}

           @editable
           ItemSpawner:item_spawner_device = item_spawner_device{}
   ```

   Start your game and interact with the button to spawn an item. Because you canceled the `InteractedWithEvent`, the button should spawn an item only once.

Check out the [Tagged Lights Puzzle Tutorial](tagged-lights-puzzle-in-verse) for a game example that uses this device subscription and canceling!

## Awaiting a Creative Device Event

You can subscribe to events but there's another way to wait for an event to occur. You can call `Await()` on a Creative device event, which is an [async](https://dev.epicgames.com/documentation/fortnite/verse-glossary#async) function call and can take time to complete. This means you must use it within an async context, such as a concurrency expression or a function with the suspends specifier. To learn more about concurrency, check out Time Flow and Concurrency.

In the following example, the Verse device waits for the player to interact with the [Trigger](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-trigger-devices-in-fortnite-creative) device before anything else can occur. If they interact with either of the Button devices before the Trigger device, nothing will happen. After the player interacts with the Trigger device, the player must make a choice and choose between the two buttons. They can only interact with one of the buttons and only interact once for something to occur because the code uses a `race` expression to race between the two button events. For more details on how this concurrency expression works, check out Race.

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

make_a_choice_device:= class(creative_device):

    @editable
    MakeChoice:trigger_device = trigger_device{}

    @editable
    RedButton:button_device = button_device{}
```

These events only wait once. If you want to repeat waiting for these events, you can use a loop expression to repeat this logic as many times as you want.

## Next Step: Devices Module

You learned here how to work with item spawners and buttons, but there are more creative devices that you can use and subscribe to from your own device. You can find this information in the Verse [API Reference](https://dev.epicgames.com/documentation/fortnite/verse-api). Go to the [Devices module](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices) to see all the creative devices you can work with in Verse.
