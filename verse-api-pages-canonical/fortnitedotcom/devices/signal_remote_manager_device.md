## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/signal_remote_manager_device

# player_movement_settings_device class
Learn technical details about the player_movement_settings_device class.
Used to update the player character's movement settings on different movement mode.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
## Exposed Interfaces
This class exposes the following interfaces:
Name | Description
---|---
[`enableable`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/enableable) |  Implemented by classes whose instances can be enabled and disabled.
## Members
This class has functions, but no data members.
### Functions
Function Name | Description
---|---
[`AddTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/addto) |  Adds the movement settings to the provided agent, activating if it is in the highest priority.
  * The highest priority device is applied to players and test players. Ties are broken by which is applied most recently.
  * Fails if the provided agent is unsupported including NPC agents like Guard, Wildlife or Custom NPCs.

[`AddToAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/addtoall) |  Adds the movement settings to all the agents in the scene, activating if it is in the highest priority.
  * The highest priority device is applied to players and test players. Ties are broken by which is applied most recently.

[`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/disable) |  Disables this device, revoking its change to the registered player characters.
Disabling this does not clear the list of registered players.
[`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/enable) |  Enables this device, allowing its properties to affect the registered player characters' movement.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetPriority`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/getpriority) |  Returns the priority of the device, the active device in the highest priority will be applied to the provided agents.
[`GetRegisteredAgents`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/getregisteredagents) |  Returns the player agents registered to this device.
[`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`IsEnabled`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/isenabled) |  Succeeds if the object is enabled, fails if it's disabled.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`RemoveFrom`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/removefrom) |  Removes the movement settings from the provided agent. Fails if the provided agent doesn't have the movement settings applied.
[`RemoveFromAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_movement_settings_device/removefromall) |  Removes the movement settings from all the active agents.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
