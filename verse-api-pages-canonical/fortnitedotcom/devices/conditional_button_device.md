## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device

# conditional_button_device class
Learn technical details about the conditional_button_device class.
Used to create a specialized button which can only be activated when `agent`s are carrying specific items.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`ActivatedEvent` | `listenable(payload)` |  Signaled when this device is activated. Sends the `agent` that activated this device.
`NotEnoughItemsEvent` | `listenable(payload)` |  Signaled when this device fails to activate because `agent` didn't have the required items. Sends the `agent` that attempted to activate the device.
### Functions
Function Name | Description
---|---
[`Activate`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/activate) |  Activates this device. `Agent` is used as the instigator of the action.
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/disable) |  Disables this device.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/enable) |  Enables this device.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetInteractionTime`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/getinteractiontime) |  Returns the time (in seconds) that an interaction with this device will take to complete.
[`GetItemCount`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/getitemcount) |  Returns how many items an `Agent` has of the item stored at `KeyItemIndex`.
[`GetItemCountRequired`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/getitemcountrequired) |  Returns the total quantity of a specific key item type that needs to be collected in order to activate the switch.
[`GetItemScore`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/getitemscore) |  Returns the score to be awarded for a key item.
[`GetRemainingItemCountRequired`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/getremainingitemcountrequired) |  Returns the remaining quantity of a specific key item type that needs to be collected in order to activate the switch.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`HasAllItems`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/hasallitems) |  Returns if the `Agent` has all of the items required to interact with this Device.
[`IsHoldingItem`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/isholdingitem) |  Returns if the `Agent` is currently holding any of the items stored in the Device.
[`IsHoldingItem`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/isholdingitem-1) |  Returns if the `Agent` is currently holding the item stored at `KeyItemIndex`.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Reset`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/reset) |  Resets this device to its original settings.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetInteractionText`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/setinteractiontext) |  Sets the text that appears when `agent`s approach the device. `Text` is limited to `150` characters and will revert back to default if empty.
[`SetInteractionTime`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/setinteractiontime) |  Sets the time (in seconds) that an interaction with this device should take to complete.
[`SetItemCountRequired`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/setitemcountrequired) |  Sets the quantity of a specific key item type that needs to be collected in order to activate the switch. `KeyItemIndex` ranges from `0` to number of key item types - 1.
[`SetItemScore`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/setitemscore) |  Sets the score to be awarded for a key item. `KeyItemIndex` ranges from `0` to number of key item types - 1.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`Toggle`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/conditional_button_device/toggle) |  Toggles the conditional button state. `Agent` is used as the instigator of the action.
