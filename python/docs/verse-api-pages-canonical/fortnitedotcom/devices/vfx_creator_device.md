## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device

# vfx_creator_device class

Learn technical details about the vfx_creator_device class.

Used to create and customize your own visual effects. This is more flexible than the `vfx_spawner_device`, which gives you a selection of pre-made visual effects to choose from but limits how much you can customize or change those effects.

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

This class has functions, but no data members.

### Functions

| Function Name | Description |
| --- | --- |
| [`Begin`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/begin) | Starts playing the effect. |
| [`Begin`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/begin-1) | Starts the effect at `Agent`'s location. This option is only valid if *Stick to Player* is enabled. |
| [`BeginForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/beginforall) | Starts the effect at every `agent`'s location. This option is only valid if *Stick to Player* is enabled. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/disable) | Disables this device. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/enable) | Enables this device. |
| [`End`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/end) | Ends playing the effect. |
| [`End`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/end-1) | Ends the effect at `Agent`'s location. This option is only valid if *Stick to Player* is enabled. |
| [`EndForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/endforall) | Ends the effect at every `agent`'s locations. This option is only valid if *Stick to Player* is enabled. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`Remove`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/remove) | Removes the effect from `Agent` and continues playing at the device location. This option is only valid if *Stick to Player* is enabled. |
| [`RemoveFromAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/removefromall) | Removes the effect for every `agent` and continues playing at the device location. This option is only valid if *Stick to Player* is enabled. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`SpawnAt`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/spawnat) | Spawns the effect at `Agent`'s location. This option is only valid if *Stick to Player* is enabled. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`Toggle`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/toggle) | Toggles between `Begin` and `End`. |
| [`Toggle`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/toggle-1) | Toggles between `Begin` and `End`. |
| [`ToggleEnabled`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/toggleenabled) | Toggles between `Enable` and `Disable`. |
| [`ToggleForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/toggleforall) | Toggles between `BeginForAll` and `EndForAll`. |
| [`TogglePause`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/togglepause) | Pauses the effect if the effect is running. If the effect is paused, unpauses the effect. Pausing an effect causes the effect to freeze in place. |
| [`TogglePause`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/togglepause-1) | Pauses the effect at `Agent`'s locations if it is playing, or resumes the effect if it is paused. When paused the effect freezes in place. |
| [`TogglePauseForAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vfx_creator_device/togglepauseforall) | Pauses the effect at every `agent`'s locations if it is playing, or resumes the effect if it is paused. When paused the effect freezes in place. |
