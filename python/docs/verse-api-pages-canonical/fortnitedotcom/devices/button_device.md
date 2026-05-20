## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/button_device

# button_device class

Learn technical details about the button_device class.

Used to create a button which can trigger other devices when an agent interacts with it.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `creative_object`:

| Name | Description |
| --- | --- |
| [`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) | Base class for creative devices and props. |
| [`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) | Base class for creative_device. |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `InteractedWithEvent` | `listenable(payload)` | Signaled when an `agent` successfully interacts with the button for `GetInteractionTime` seconds. Sends the `agent` that interacted with the button. |

### Functions

| Function Name | Description |
| --- | --- |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/disable) | Disables this device. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/enable) | Enables this device. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetInteractionTime`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/getinteractiontime) | Returns the duration of the interaction required to activate this device (in seconds). |
| [`GetMaxTriggerCount`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/getmaxtriggercount) | Returns the maximum amount of times this button can be interacted with before it will be disabled.   - `GetTriggerMaxCount` will be between `0` and `10000`. - `0` indicates no limit on trigger count. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`GetTriggerCountRemaining`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/gettriggercountremaining) | Returns the number of times that this button can still be interacted with before it will be disabled. Will return `0` if `GetMaxTriggerCount` is unlimited. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`SetInteractionText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/setinteractiontext) | Sets the text that displays when an `agent` is close to this button and looks at it. `Text` is limited to `64` characters. |
| [`SetInteractionTime`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/setinteractiontime) | Sets the duration of the interaction required to activate this device (in seconds). |
| [`SetMaxTriggerCount`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/button_device/setmaxtriggercount) | Sets the maximum amount of times this button can be interacted with before it will be disabled.   - `MaxCount` must be between `0` and `10000`. - `0` indicates no limit on trigger count. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
