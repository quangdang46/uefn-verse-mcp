## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device

# billboard_device class
Learn technical details about the billboard_device class.
Used to display custom text messages on a billboard.
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
This class has functions, but no data members.
### Functions
Function Name | Description
---|---
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetShowBorder`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/getshowborder) |  Returns `true` if the device border is enabled.
[`GetTextSize`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/gettextsize) |  Returns the _Text Size_ of the device _Text_.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`HideText`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/hidetext) |  Hides the billboard text.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetShowBorder`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/setshowborder) |  Sets the visibility of the device border mesh. This also determines whether the device collision is enabled.
[`SetText`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/settext) |  Sets the device _Text_.
[`SetTextSize`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/settextsize) |  Sets the _Text Size_ of the device _Text_. Clamped to range [8, 24].
[`ShowText`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/showtext) |  Shows the billboard text.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`UpdateDisplay`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/billboard_device/updatedisplay) |  Updates the device display to show the current _Text_.
