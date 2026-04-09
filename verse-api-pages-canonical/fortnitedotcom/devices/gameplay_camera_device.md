## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/gameplay_camera_device

# popup_dialog_device class
Learn technical details about the popup_dialog_device class.
Used to create HUD text boxes that give players information, and allows responses to be customized to player choices.
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
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`DismissedEvent` | `listenable(payload)` |  Signaled when this device is dismissed by an `agent`. Sends the `agent` who dismissed the popup.
`RespondingButtonEvent` | `listenable(payload)` |  Signaled when _Button_ on this device is pushed by an `agent`. Sends the `agent` that pushed the button. Sends the `int` index of the button that was clicked.
`ShownEvent` | `listenable(payload)` |  Signaled when this device is shown to an `agent`. Sends the `agent` looking at the popup.
`TimeOutEvent` | `listenable(payload)` |  Signaled when this device times out while an `agent` is looking at it. Sends the `agent` who was looking at the popup.
### Functions
Function Name | Description
---|---
[`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/disable) |  Disables this device.
[`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/enable) |  Enables this device.
[`GetButtonText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/getbuttontext) |  Returns the _Button Text_ for this popup at a specified index.
[`GetDescriptionText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/getdescriptiontext) |  Returns the _Description_ text for this popup.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTitleText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/gettitletext) |  Returns the _Title_ text for this popup.
[`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Hide`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/hide) |  Hides the popup from `Agent`.
[`Hide`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/hide-1) |  Hides the popup from all `agent`s in the experience.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetButtonCount`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/setbuttoncount) |  Sets the number of buttons this popup has. Button Count is not updated on active Popups.
[`SetButtonText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/setbuttontext) |  Sets the _Button Text_ for a button at a specific index on this popup.
  * `Text` should be no more than `24` characters.
  * If `Text` is empty the button will show _OK_ instead.
  * Button 1 uses `Index` 0.

[`SetDescriptionText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/setdescriptiontext) |  Sets the _Description_ text for this popup. `Text` should be no more than `350` characters.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetTitleText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/settitletext) |  Sets the _Title_ text for this popup. `Text` should be no more than `32` characters.
[`Show`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/show) |  Shows the popup to `Agent`.
[`Show`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/popup_dialog_device/show-1) |  Shows the popup to all `agent`s in the experience.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
