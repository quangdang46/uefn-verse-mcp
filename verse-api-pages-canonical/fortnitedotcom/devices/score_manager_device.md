## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device

# score_manager_device class
Learn technical details about the score_manager_device class.
Used to manipulate scores using in-experience triggers. If _Activating Team_ is set to a specific team, then you should use the `agent` overloads of each function. The `agent`'s team will be used to determine if that `agent` is allowed to affect the state of the device.
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
`MaxTriggersEvent` | `listenable(payload)` |  Signaled when the this device reaches its maximum number of triggers as defined by _Times Can Trigger_. Sends the `agent` who last triggered the device.
`ScoreOutputEvent` | `listenable(payload)` |  Signaled when the this device awards points to an `agent`. Sends the `agent` who received the points.
### Functions
Function Name | Description
---|---
[`Activate`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/activate) |  Grant points to `Agent`.
[`Activate`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/activate-1) |  Grants points.
[`Decrement`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/decrement) |  Decrements the score quantity to be awarded by the next activation by `1`.
[`Decrement`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/decrement-1) |  Decrements the score quantity to be awarded by the next activation by `1`.
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/disable) |  Disables this device.
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/disable-1) |  Disables this device.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/enable) |  Enables this device.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/enable-1) |  Enables this device.
[`GetCurrentScore`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/getcurrentscore) |  Returns the current score for `Agent`.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetScoreAward`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/getscoreaward) |  Returns the score to be awarded by the next activation.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Increment`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/increment) |  Increments the score quantity to be awarded by the next activation by `1`.
[`Increment`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/increment-1) |  Increments the score quantity to be awarded by the next activation by `1`.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Reset`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/reset) |  Resets this device to its original state.
[`Reset`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/reset-1) |  Resets this device to its original state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetScoreAward`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/setscoreaward) |  Sets the score to be awarded by the next activation to `Value`.
[`SetToAgentScore`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/score_manager_device/settoagentscore) |  Sets the score to be awarded by the next activation to `Agent`'s current score.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
