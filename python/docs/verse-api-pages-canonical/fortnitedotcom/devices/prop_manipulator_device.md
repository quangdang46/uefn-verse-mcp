## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device

# prop_manipulator_device class

Learn technical details about the prop_manipulator_device class.

Used to manipulate the properties of one or more props in a specified area (e.g. Visibility/Destructibility).

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
| `DamagedEvent` | `listenable(payload)` | Signaled when props affected by this device are damaged. Sends the `agent` that damaged the prop. |
| `DestroyedEvent` | `listenable(payload)` | Signaled when props affected by this device are destroyed. Sends the `agent` that destroyed the prop. |
| `HarvestingEvent` | `listenable(payload)` | Signaled when prop resource nodes affected by this device are harvested. Sends the `agent` that harvested resources from the prop. |
| `ResourceDepletionEvent` | `listenable(payload)` | Signaled when prop resource nodes affected by this device are completely depleted of energy. Sends the `agent` that depleted the prop's energy. |

### Functions

| Function Name | Description |
| --- | --- |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/disable) | Disables this device. |
| [`DisableResourceNodeOverrides`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/disableresourcenodeoverrides) | Sets the *Override Resource* option to *No*. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/enable) | Enables this device. |
| [`ExhaustResources`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/exhaustresources) | Empties the resources of all props affected by this device. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`HideProps`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/hideprops) | Hides all props affected by this device. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`RestockResources`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/restockresources) | Restocks the resources of all props affected by this device. |
| [`RestoreHealth`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/restorehealth) | Restores health of all props affected by this device. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`SetResourceOverridesActive`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/setresourceoverridesactive) | Sets the *Override Resource* option to *Yes*. |
| [`ShowProps`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_manipulator_device/showprops) | Shows all props affected by this device. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
