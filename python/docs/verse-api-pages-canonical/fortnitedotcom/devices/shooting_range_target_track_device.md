## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device

# shooting_range_target_track_device class

Learn technical details about the shooting_range_target_track_device class.

A set of customizable pop up targets that can be hit by players to trigger various events.

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
| `BullseyeHitEvent` | `listenable(payload)` | Signaled when target is hit in the bullseye area. |
| `HitEvent` | `listenable(payload)` | Signaled when the target is hit by a player. |
| `HopDownEvent` | `listenable(payload)` | Signaled when the target moves down slightly, making it harder to hit. |
| `HopUpEvent` | `listenable(payload)` | Signaled when the target moves up slightly, making it harder to hit. |
| `KnockdownEvent` | `listenable(payload)` | Signaled when the target is hit by a player. |
| `PopDownEvent` | `listenable(payload)` | Signaled when the target moves from standing upright to laying flat. |
| `PopUpEvent` | `listenable(payload)` | Signaled when the target moves from laying flat to standing upright. |

### Functions

| Function Name | Description |
| --- | --- |
| [`ActivateTrack`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/activatetrack) | Activates the movement track. |
| [`DeactivateTrack`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/deactivatetrack) | Deactivates the movement track. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/disable) | Disables this device. |
| [`DisableTrackMovement`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/disabletrackmovement) | Disables movement on the track. This prevents any movement from occurring, until track movement is enabled again. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/enable) | Enables this device. |
| [`EnableTrackMovement`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/enabletrackmovement) | Enables movement on the track. This does not start the target moving, it only enables movement. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`HopDown`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/hopdown) | Moves an active (standing upright) target attached to the track down slightly, in an effort to make it harder to hit |
| [`HopUp`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/hopup) | Moves an active (standing upright) target attached to the track up slightly, in an effort to make it harder to hit |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveToEnd`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/movetoend) | Starts the target moving toward the end of the track. |
| [`MoveToStart`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/movetostart) | Starts the target moving toward the start of the track. |
| [`PopDown`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/popdown) | Causes the target attached to the track to transition from standing upright (active) to lying flat (inactive) |
| [`PopUp`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/popup) | Causes the target attached to the track to transition from lying flat (inactive) to standing upright (active) |
| [`Reset`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/shooting_range_target_track_device/reset) | Resets the target to its initial settings. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
