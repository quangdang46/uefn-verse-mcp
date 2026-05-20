## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/capture_area_device

# capture_area_device class

Learn technical details about the capture_area_device class.

Used to create a zone that can trigger effects once players enter it. Can be set up to be capturable by a team, to provide a score while held, or to require a specific item as a drop-off.

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
| `AgentEntersEvent` | `listenable(payload)` | Signaled when an `agent` enters this device area. Sends the `agent` that entered this device area. |
| `AgentExitsEvent` | `listenable(payload)` | Signaled when an `agent` exits this device area. Sends the `agent` that exited this device area. |
| `AreaIsContestedEvent` | `listenable(payload)` | Signaled when this device is contested. Sends the `agent` that is contesting this device. |
| `AreaIsScoredEvent` | `listenable(payload)` | Signaled when this device is scored. Sends the `agent` that scored this device. |
| `CaptureProgress` | `?float` | The current capture progress of the capture area. As a team captures the area, the value will increase from 0.0 to 1.0, with 1.0 representing a fully captured area. If the device supports neutralization or decay, the value will drop back towards 0.0 as it returns to neutral. If the device is disabled, the capture progress is set to 0.0. |
| `ControlChangeEvent` | `listenable(payload)` | Signaled when this device control changes. Sends the `agent` that triggered this device control change. |
| `ControlChangeStartsEvent` | `listenable(payload)` | Signaled when this device control change starts. Sends the `agent` that is triggering this device control change. |
| `FirstAgentEntersEvent` | `listenable(payload)` | Signaled when the first `agent` enters this device area. Sends the `agent` that entered this device area. |
| `ItemIsConsumedEvent` | `listenable(payload)` | Signaled when an item is consumed by this device. Sends the `agent` that provided the item to this device. |
| `ItemIsDeliveredEvent` | `listenable(payload)` | Signaled when an item is delivered to this device. Sends the `agent` that delivered the item to this device. |
| `LastAgentExitsEvent` | `listenable(payload)` | Signaled when the last `agent` exits this device area. Sends the `agent` that exited this device area. |
| `NeutralizeEvent` | `listenable(payload)` | Signaled when this device enters the neutralized state. Sends the `agent` that was responsible for neutralizing the area (the player in the area at the time of neutralization, prioritized by the one who has been in the area the longest), if one exists. |

### Functions

| Function Name | Description |
| --- | --- |
| [`ActivateObjectivePulse`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/activateobjectivepulse) | Activates the objective pulse for this device. |
| [`AllowCapture`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/allowcapture) | Allows this device to be captured. |
| [`DeactivateObjectivePulse`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/deactivateobjectivepulse) | Deactivates the objective pulse for this device. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/disable) | Disables this device. |
| [`DisallowCapture`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/disallowcapture) | Disallows this device from being captured. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/enable) | Enables this device. |
| [`GetAgentsInVolume`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/getagentsinvolume) | Returns an array of agents that are currently occupying the Capture Area. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetHeight`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/getheight) | Returns the *Capture Height* (in meters) of the capture area. |
| [`GetRadius`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/getradius) | Returns the *Capture Radius* (in meters) of the capture area. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`GiveControl`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/givecontrol) | Gives control of this device to the capturing `agent`'s team. |
| [`IsInArea`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/isinarea) | Is true when `Agent` is in the Capture Area. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`Neutralize`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/neutralize) | Clears control of this device for all teams. |
| [`Reset`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/reset) | Resets control of this device for all teams. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`SetHeight`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/setheight) | Sets the *Capture Height* (in meters) of the capture area. |
| [`SetRadius`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/setradius) | Sets the *Capture Radius* (in meters) of the capture area. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`ToggleCaptureAllowed`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/togglecaptureallowed) | Toggles between `AllowCapture` and `DisallowCapture`. |
| [`ToggleEnabled`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/capture_area_device/toggleenabled) | Toggles between `Enable` and `Disable`. |
