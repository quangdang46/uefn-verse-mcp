## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/tracker_device

# tracker_device class

Learn technical details about the tracker_device class.

Allows creation and HUD tracking of custom objectives for `agent`s to complete.

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
| `CompleteEvent` | `listenable(payload)` | Signaled when the tracked value reaches `GetTarget` for an `agent`. Sends the `agent` that reached `GetTarget` for their tracked value. |

### Functions

| Function Name | Description |
| --- | --- |
| [`Assign`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/assign) | Assigns the device to `Agent` (and any `agent`s sharing progress). |
| [`AssignToAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/assigntoall) | Assigns this device to all valid `agent`s. |
| [`ClearPersistence`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/clearpersistence) | Clears tracked progress for `Agent`. Only valid if *Use Persistence* is set to *Use*. |
| [`Complete`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/complete) | The objective immediately completes. |
| [`DecreaseTargetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/decreasetargetvalue) | Decreases the target value for `Agent` by 1. |
| [`Decrement`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/decrement) | Decrease the tracked value by *Amount to Change on Received Signal* for `Agent`. |
| [`GetActiveAgents`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/getactiveagents) | Returns an array of agents that currently have this tracker active. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/gettarget) | Returns the target value that must be achieved in order for `CompleteEvent` to trigger. Clamped to `0 <= GetTarget <= 10000`. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`GetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/getvalue) | Returns the current total tracked value for all players. |
| [`GetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/getvalue-1) | Returns the current total tracked value for the team at `TeamIndex`. |
| [`GetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/getvalue-2) | Returns the current tracked value for `Agent`. |
| [`HasReachedTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/hasreachedtarget) | Is true if `Agent` has reached the *TargetValue* for the tracker. |
| [`IncreaseTargetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/increasetargetvalue) | Increases the target value for `Agent` by 1. |
| [`Increment`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/increment) | Increases the tracked value by *Amount to Change on Received Signal* for `Agent`. |
| [`IsActive`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/isactive) | Is true if `Agent` currently has the tracker active. |
| [`Load`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/load) | Loads tracked progress for `Agent`. Only valid if *Use Persistence* is set to *Use*. |
| [`LoadForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/loadforall) | Loads tracked progress for all valid `agent`s. Only valid if *Use Persistence* is set to *Use*. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`Remove`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/remove) | Removes this device from `Agent` (and any `agent`s sharing progress). |
| [`RemoveFromAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/removefromall) | Removes this device from all valid `agent`s. |
| [`Reset`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/reset) | Resets the progress for `Agent` (and any `agent`s sharing progress). |
| [`Save`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/save) | Saves tracked progress for `Agent`. Only valid if *Use Persistence* is set to *Use*. |
| [`SetDescriptionText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/setdescriptiontext) | Sets a description for the `tracker_device`, which is displayed if *Show on HUD* is enabled. `Text` has a 64 character limit. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`SetTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/settarget) | Sets the target value that must be achieved in order for `CompleteEvent` to trigger. Clamped to `0 <= TargetValue <= 10000`. |
| [`SetTitleText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/settitletext) | Sets the title for the `tracker_device`, which is displayed if *Show on HUD* is enabled. `Text` has a 32 character limit. |
| [`SetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/setvalue) | Sets the current tracked value for the device for all active players. |
| [`SetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/setvalue-1) | Sets the current tracked value for the device for the Team at the `TeamIndex`. If *Sharing* is set to *Individual*, this will set the value for all team members. If *Sharing* is set to *All*, this will set the value for all players. |
| [`SetValue`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/tracker_device/setvalue-2) | Sets the current tracked value for the device for a specific 'Agent'. If *Sharing* is set to *Team*, this will set the value for their team. If *Sharing* is set to *All*, this will set the value for everyone. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
