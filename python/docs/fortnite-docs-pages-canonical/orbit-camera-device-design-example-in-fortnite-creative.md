## https://dev.epicgames.com/documentation/en-us/fortnite/orbit-camera-device-design-example-in-fortnite-creative

# Orbit Camera Device Design Example

See how to incorporate the Orbit Camera in a game of hide-and-seek!

![Orbit Camera Device Design Example](https://dev.epicgames.com/community/api/documentation/image/72567f77-0ea3-4d7e-b513-372e9f07d90d?resizing_type=fill&width=1920&height=335)

When you combine the **Orbit Camera** device with assets from the **Hiding Props Gallery** device, you have the foundation for a wacky game of hide-and-seek — the orbit camera provides players with a tricky new camera angle they can use to spy on their surroundings as they stay out of view!

This design example is not a full mini-game, but it is a fun mechanic to use in a hide-and-seek game!

## Porta-Peek Hide-and-Seek Device Mechanics

For this game, you will place the devices, then configure and [bind](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) them.

### Devices Used

- 1 x **Portapotty** from the [**Hiding Props Gallery** device](using-hiding-prop-gallery-devices-in-fortnite-creative)
- 1 x [**Orbit Camera** device](using-orbit-camera-devices-in-fortnite-creative)
- 1 x [Timer device](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative)

### Add the Portapotty

Don't be fooled by the **Hiding Props Gallery** name — this is a collection of devices! They will be found under the **Devices category** in [**Creative inventory**](using-devices-in-fortnite-creative).

[![](https://dev.epicgames.com/community/api/documentation/image/b45e3b7f-ad88-4ba6-a45d-c48c2bd51f40?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b45e3b7f-ad88-4ba6-a45d-c48c2bd51f40?resizing_type=fit)

For this design example, the Portapotty uses the default options, but you will come back to this device later to configure other settings.

### Add the Orbit Camera Device

The **Orbit Camera** device provides a view that a player can rotate easily, unlike a fixed camera view that is stationary in relation to the player. This gives the player a chance to look at what's going on outside of their hiding spot and peer in any direction.

### Add a Timer Device

The **Timer** device will help control the transition of the camera so the player has time to get inside the Portapotty before the orbit camera takes over.

### Bind Device Functions and Events

[Direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) is how you set devices to communicate directly with other devices. This involves setting [functions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) and [events](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event) for the devices involved.

For the **Portapotty** device, configure the following **events**:

[![](https://dev.epicgames.com/community/api/documentation/image/5c3352d6-7613-4ad9-b35d-4716fefa2f43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5c3352d6-7613-4ad9-b35d-4716fefa2f43?resizing_type=fit)

| Event | Select Device | Select Event |
| --- | --- | --- |
| **On Hide Send Event To** | Timer Device | Start |
| **On Stop Hiding Send Event To** | Camera: Orbit | Remove from Player |

And there you go! A fun way to add a new mechanic to your hiding games.

Playtest this mechanic and note how the camera view changes when you enter the Portapotty.

## Design Tip

You can add this type of camera to any of the hiding props, so give it a try and see what kinds of games you can invent on your own island!
