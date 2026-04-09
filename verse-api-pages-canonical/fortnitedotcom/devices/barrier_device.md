## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/barrier_device

# map_controller_device class
Learn technical details about the map_controller_device class.
Used to control the behavior of the map & minimap. Activation for a given `agent` can occur automatically via the device's _Activate Automatically_ user option, by the `agent` entering and exiting the device's volume if using the _Activate on Trigger_ user option, or via events from other devices or verse. When more than one map controller is activated for a given `agent`, the one with the highest _Map Priority_ user option applies.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
## Members
This class has functions, but no data members.
### Functions
Function Name | Description
---|---
[`Activate`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/activate) |  Adds the map controller to the provided `Agent`'s map controller stack. If multiple map controllers are active for an `agent`, the one with the highest _Map Priority_ is used.
[`Activate`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/activate-1) |  Adds the map controller to all `agent`s in the experience. If multiple map controllers are active for an `agent`, the one with the highest _Map Priority_ is used.
[`Deactivate`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/deactivate) |  Removes the map controller from the provided `Agent`'s map controller stack. The next highest priority active map controller will be used, or if none exists, the default behavior will be restored.
[`Deactivate`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/deactivate-1) |  Removes the map controller from all `agent`s in the experience. The next highest priority active map controller will be used, or if none exists, the default behavior will be restored.
[`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/disable) |  Disables the device. Disabling the device will deactivate it for all `agents` in the experience, turn off the trigger functionality, and prevent it from responding to events.
[`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/enable) |  Enables the device. Enabling the device will allow it to be activated, both by incoming events, and by trigger if using _Activate on Trigger_.
[`GetCaptureBoxSize`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/getcaptureboxsize) |  Returns the _Capture Box Size_ (in meters).
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetCaptureBoxSize`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/map_controller_device/setcaptureboxsize) |  Sets the _Capture Box Size_ (in meters). _Capture Box Size_ refers to the length and width of the area used for both the map capture image as well as the activation trigger. Value is clamped between `25.0` and `2500.0` meters.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
