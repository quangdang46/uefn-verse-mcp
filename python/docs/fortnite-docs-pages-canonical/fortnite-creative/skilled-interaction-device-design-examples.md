## https://dev.epicgames.com/documentation/en-us/fortnite-creative/skilled-interaction-device-design-examples

# Skilled Interaction Device Design Examples

See how to create fun mini-games where players can practice various in-game skills.

![Skilled Interaction Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/2a37c87f-55b6-42d4-9a1a-e426c4160758?resizing_type=fill&width=1920&height=335)

This interactive device is perfect for creating fun mini-games where players can practice various in-game skills.

### Starting a Fire

Use the **Skilled Interaction** device to quickly make a more engaging interaction for basic gameplay moments like lighting a campfire!

### Devices Used

- 1 x Skilled Interaction device
- 1 x Player Spawner device
- 1 x Campfire device

### Set Up the Devices

## Bind Functions and Events

[Direct event binding](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#directeventbinding) is how you set devices to communicate directly with other devices. This involves setting [functions](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#function) and [events](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#event) for the devices involved.

You now have the basic functionality for a custom fire-starting interaction!

### Design Tip

Setting the size of the **Perfect** interaction zone to **0%** makes it so that there is only one successful interaction zone. This is especially  good for simple interactions like this one where there’s no difference in outcome between **Good** and **Perfect**.

## Build a Volcano Escape

You can configure the Skilled Interaction device to require multiple player successes to complete the interaction. When paired with a time limit, this can create a tense and exciting interaction!

### Devices Used

- 1 x Skilled Interaction device
- 1 x Player Spawner device
- 1 x [Water](https://dev.epicgames.com/documentation/fortnite/using-water-devices-in-fortnite-creative) device
- 1 x [Baller Spawner](https://dev.epicgames.com/documentation/fortnite/using-baller-spawner-devices-in-fortnite-creative) device
- 1 x [Button](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative) device

### Set Up the Basic Gameplay

### Set Up the Skilled Interaction

| Event | Select Device | Select Function |
| --- | --- | --- |

You now have the basic functionality for a volcano escape!

### Design Tip

With the events that the Skilled Interaction device can send, anything is possible. Use these interactions to trigger doors unlocking, new gameplay areas opening, item upgrades, or anything else you can imagine. Get creative with how to tailor the interactions to the action that the player is performing!

## Build a Fishing Quest Mini-Game

The Skilled Interaction device can be combined with a **Fishing Zone** and some **Item Granter** devices to create a fun and engaging fishing mini-game! With some other devices, you’ll create a basic quest in which the player must fish successfully to unlock a new gameplay area!

### Devices Used

- 1 x Skilled Interaction device
- 1 x Player Spawner device
- 1 x [Fishing Rod Barrel](https://dev.epicgames.com/documentation/fortnite/using-fishing-rod-barrel-devices-in-fortnite-creative) device
- 2 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) devices
- 1 x [Fishing Zone](https://dev.epicgames.com/documentation/fortnite/using-fishing-zone-devices-in-fortnite-creative) device
- 1 x [Lock](https://dev.epicgames.com/documentation/fortnite/using-lock-devices-in-fortnite-creative) device
- 1 x [Character](https://dev.epicgames.com/documentation/fortnite/using-character-devices-in-fortnite-creative) device
- 1 x [HUD Message](https://dev.epicgames.com/documentation/fortnite/hud-message-device) device
- 1 x [Tracker](https://dev.epicgames.com/documentation/fortnite/using-tracker-devices-in-fortnite-creative) device

### Set Up the Basic Fishing Devices

1. Begin with the **Mountain Ridge Island** starter island.
2. Place the **Lockie’s Lighthouse** prefab near the water.
3. Place a **Player Spawner** device and customize so it does not show in-game:

   [![](https://dev.epicgames.com/community/api/documentation/image/91ec32a3-071e-4465-af2a-e877fa99200b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/91ec32a3-071e-4465-af2a-e877fa99200b?resizing_type=fit)
4. Place a **Fishing Rod Barrel** device next to the lighthouse.
5. Place an **Item Granter** device and register a **Flopper** to the device.
6. Customize the Item Granter:

   [![](https://dev.epicgames.com/community/api/documentation/image/4d50c515-9d1e-428e-8bb1-fc2161ccd8ea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d50c515-9d1e-428e-8bb1-fc2161ccd8ea?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Drop Items at Player Location | Alway |
7. Duplicate the Item Granter and rename the duplicate to **Perfect Item Granter**. Unregister the **Flopper** and register a **Slurpfish**.
8. Place a **Fishing Zone** device in the water and customize:

   [![](https://dev.epicgames.com/community/api/documentation/image/bad0107e-ba0d-4e3b-b4de-0ad0f697ac8c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bad0107e-ba0d-4e3b-b4de-0ad0f697ac8c?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Pool Type | Trigger Only |
9. Place a **Skilled Interaction** device and customize:

   [![](https://dev.epicgames.com/community/api/documentation/image/b011b8b8-d3b4-483e-be62-16c63207a2ff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b011b8b8-d3b4-483e-be62-16c63207a2ff?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/d8c993f3-b4ed-4f18-b3a3-30ccb44e41af?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d8c993f3-b4ed-4f18-b3a3-30ccb44e41af?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Description Text | The better you do, the better the fish! |
   | UI Type | Bar |
   | Movement Type | Wiggle |
   | Wiggle Time Min | 0.25 Seconds |
   | Wiggle Time Max | 0.5 Seconds |
   | Movement Speed | 100% |
   | Good Zone Size | 25% |
   | Position Zone Randomly | On |
   | Scrubber Color | White |

### Set Up the Quest Devices

### Bind Functions and Events

You now have a working fishing mini-game connected to a quest system!

### Design Tip

This type of fishing mini-game is very common in cozy farming games and other similar games. But more and more games of all genres are adding fishing as a fun side mechanic that players can use to unlock additional items.

Consider different types of games that could benefit from a fishing mini-game and try adding one!
