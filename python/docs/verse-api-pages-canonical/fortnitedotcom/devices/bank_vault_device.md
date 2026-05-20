## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device

# bank_vault_device class

Learn technical details about the bank_vault_device class.

A vault door that requires a start of a sequence to damage a number of weakpoints to open.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `creative_object`:

| Name | Description |
| --- | --- |
| [`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) | Base class for creative devices and props. |
| [`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) | Base class for creative_device. |

## Exposed Interfaces

This class exposes the following interfaces:

| Name | Description |
| --- | --- |
| [`bank_vault_interface`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_interface) |  |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `ActivateWeakpointEvent` | `listenable(payload)` | Triggers when a weakpoint is activated. The weakpoint will begin to glow, but does not become vulnerable until a subsequent `WeakpointVulnerableEvent`.   - Sends the `agent` that activated the vault or none if the sequence was triggered by a function, and the `int` index of the weakpoint from 0-4, in order of activation. |
| `DestroyWeakpointEvent` | `listenable(payload)` | Triggers when a weakpoint is destroyed.   - Sends the last `agent` that damaged the weakpoint or the `agent` that started the sequence if no external damage was done or none if the sequence was triggered by a function, and the `int` index of the weakpoint from 0-4, in order of activation. |
| `MaxWeakpointHealth` | `?float` | The max health of this device's weakpoints. |
| `OpenEvent` | `listenable(payload)` | Triggers when the vault is opened either by the destruction of its weakpoints or by an event.   - Sends the last `agent` that damaged a weakpoint or the `agent` that started the sequence if no external damage was done or none if the sequence was triggered by a function. |
| `RequireThermite` | `?logic` | Whether the player needs thermite when interacting with the door to start the vault opening sequence. |
| `StartSequenceEvent` | `listenable(payload)` | Triggers when the vault sequence is started by a player or event.   - Sends the `agent` that triggered this event, if applicable. |
| `WeakpointDamagePerSecond` | `?float` | Damage dealt to the active weakpoint each second. Negative numbers heal the weakpoint. Weakpoints can only be damaged while the vault sequence is active. |
| `WeakpointTakesExternalDamage` | `?logic` | Whether the weakpoint takes damage from weapons and items while vault sequence is active. |
| `WeakpointVulnerableEvent` | `listenable(payload)` | Triggers when a weakpoint becomes vulnerable.   - Sends the `agent` that activated the vault or none if the sequence was triggered by a function, and the `int` index of the weakpoint from 0-4, in order of activation. |

### Functions

| Function Name | Description |
| --- | --- |
| [`DestroyActiveWeakpoint`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/destroyactiveweakpoint) | Destroy the active weakpoint. Requires the device to be enabled. Must have active weakpoint. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/disable) | Disable the device. Pauses vault sequence. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/enable) | Enable the device. |
| [`ForceOpen`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/forceopen) | Destroys the remaining weakpoints and opens the vault door. Requires the device to be enabled. |
| [`GetActiveWeakpointHealth`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/getactiveweakpointhealth) | Get active weakpoint's health. If there is no active weakpoint, returns false. |
| [`GetActiveWeakpointIndex`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/getactiveweakpointindex) | Gets the active weakpoint's index starting at `0`, regardless of device's enabled state. Returns false if there is no active weakpoint, such as when the sequence is not active or directly after a weakpoint is destroyed. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`GetWeakpointCount`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/getweakpointcount) | Gets the total number of weakpoints. |
| [`IsEnabled`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/isenabled) | Succeeds if the device is enabled, fails if it's disabled. |
| [`IsSequenceActive`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/issequenceactive) | Whether the vault sequence is currently active and not paused. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`PauseSequence`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/pausesequence) | Disable the weakpoint vulnerability and freeze the progress of each one. Weakpoints can only be damaged while the vault sequence is active. |
| [`Reset`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/reset) | Restores vault to default state, deactivates the device, and heals all weakpoints to max health. Requires the device to be enabled. |
| [`RestoreActiveWeakpoint`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/restoreactiveweakpoint) | Restores the active weakpoint to full health. Requires the device to be enabled. Must have active weakpoint. |
| [`SetActiveWeakpointHealth`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/setactiveweakpointhealth) | Set active weakpoint's health. Setting it to `0.0` will destroy the weakpoint. Clamps to maximum of WeakpointMaxHealth. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`StartSequence`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_device/startsequence) | Begin the sequence of events to open the vault door without thermite, or unpauses the sequence if it was paused. Requires the device to be enabled. Weakpoints can only be damaged while the vault sequence is active. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
