## https://dev.epicgames.com/documentation/en-us/fortnite/using-lock-devices-in-fortnite-creative

# Lock Devices

Attach this device to a wall section with a door to allow the door to be opened, closed, locked and unlocked using receivers.

![Lock Devices](https://dev.epicgames.com/community/api/documentation/image/7fc20bec-7bba-44d5-b8eb-d996089f8fb6?resizing_type=fill&width=1920&height=335)

The **Lock** device allows you to customize the state and accessibility of a door using signals sent by other devices. This device only works with assets that have a door attached.

## Device Options

You can configure this device with the following options.

| Option | Value | Description |
| --- | --- | --- |
| **Initial Door Position** | Open, **Closed** | Determines whether the door is open or closed at Game Start. |
| **Visible in Game** | **On**, Off | Determines whether or not the lock is visible in the game. |
| **Color** | **White**, Pick a color | Changes the color of the device to help players tell them apart. |
| **Starts Locked** | Unlocked, **Locked** | Determines whether the door is locked or unlocked at the start of the game. |
| **Hide Interaction When Locked** | Yes, **No** | Determines whether or not the player can see the interaction prompt when the door is locked. |

## Direct Event Binding

Below are the following direct event binding options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) listens for an event on a device then performs an action.

| Option | Description |
| --- | --- |
| **Unlock When Receiving From** | This function unlocks the door when an event occurs. |
| **Lock When Receiving From** | This function locks the door when an event occurs. |
| **Toggle Locked When Receiving From** | This function toggles the lock between locked and unlocked when an event occurs. |
| **Open When Receiving From** | This function opens the door when an event occurs. |
| **Close When Receiving From** | This function closes the door when an event occurs. |
| **Toggle Open When Receiving From** | This function toggles the door between open and closedwhen an event occurs. |

### Events

This device has no events.

## Gameplay Examples Using Locks

- [Dungeon Crawler](https://dev.epicgames.com/documentation/fortnite/dungeon-crawler-gameplay-example-in-fortnite-creative)
- [Timed Door](https://dev.epicgames.com/documentation/fortnite/timed-door-in-fortnite-creative)
