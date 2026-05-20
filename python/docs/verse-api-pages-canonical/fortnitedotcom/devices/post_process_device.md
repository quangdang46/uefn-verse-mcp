## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/post_process_device

# post_process_device class

Learn technical details about the post_process_device class.

Used to apply Post Process Effects to players through the creative device rather than a Post Process Volume.

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
| `BlendingInCompleteEvent` | `listenable(payload)` | Signaled when a blend in event has finished. Sends the `agent` that used this device. |
| `BlendingOutCompleteEvent` | `listenable(payload)` | Signaled when a blend out event has finished. Sends the `agent` that used this device. |

### Functions

| Function Name | Description |
| --- | --- |
| [`BlendIn`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/blendin) | Starts blending in the post process effect to the set strength only for the instigating `Agent`. |
| [`BlendInForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/blendinforall) | Starts blending in the post process effect to the set strength for all players. |
| [`BlendOut`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/blendout) | Starts blending out the post process effect to 0 strength only for the instigating `Agent`. |
| [`BlendOutForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/blendoutforall) | Starts blending out the post process effect to 0 strength for all players. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/disable) | Disables this device only for the instigating `Agent`. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/disable-1) | Disables this device for all players. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/enable) | Enables this device only for the instigating `Agent`. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/enable-1) | Enables this device for all players. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`Reset`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/reset) | Resets to the starting strength, ending any ongoing blending only for the instigating `Agent`. |
| [`ResetForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/post_process_device/resetforall) | Resets to the starting strength, ending any ongoing blending for all players. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
