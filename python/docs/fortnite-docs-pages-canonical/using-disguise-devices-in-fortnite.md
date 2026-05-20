## https://dev.epicgames.com/documentation/en-us/fortnite/using-disguise-devices-in-fortnite

# Disguise Devices

Use the Disguise device to provide players the option to hide their true identity.

![Disguise Devices](https://dev.epicgames.com/community/api/documentation/image/29dabdfd-dd2c-44f2-b0fb-3dae5444b7c4?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [Getting Started with Devices](https://dev.epicgames.com/documentation/fortnite/getting-started-with-devices-in-fortnite)

You can use the **Disguise** device to apply a disguise to players. Disguises are specific character [outfits](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#outfit) that change a player's appearance. You can use this device to create new types of gameplay:

- Create stronger team identities.
- Make more immersive roleplay mechanics.
- Create social deduction games, where one or more players is secretly pitted against the other players.
- Create a spy experience, where players must disguise themselves to infiltrate a location or organization.
- Stage a jailbreak or other escape scenario, where disguises can help the players get away.

For help on how to find the **Disguise** device, see **[Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite)**.

## Using the Device

Here is the general workflow for using this device.

![Demonstration of how Disguise device works](https://dev.epicgames.com/community/api/documentation/image/4eaf5f03-b533-45a3-b9e9-95007bdc334e?resizing_type=fit)

Demonstration of how Disguise device works

If you're using multiple copies of a device on an island, it can be useful to rename them. Choosing names that relate to a device's purpose makes it easier to remember what each one does, and easier to find a specific device when using the [Event Browser](https://dev.epicgames.com/documentation/fortnite/event-browser-in-fortnite-creative).

## Device Options

Default values are **bold**.

| Options | Values | Description |
| --- | --- | --- |
| **Disguise to Apply** | **Default Combat - Random**, Default Casual - Random, Pick a combat or casual character | Determines what outfit the device applies to the player.  Additional characters are available for brand islands. To learn more, see the [Brand Island Characters](https://dev.epicgames.com/documentation/fortnite/using-disguise-devices-in-fortnite#brand-island-characters-nbsp) section below. |
| **Disguise Breaks on Attack** | On Attack, On Damage Anything, **On Damage Opponent**, Off | Determines if the disguise comes off when the disguised player attacks.   - **On Attack**: The disguise comes off if the disguised player initiates any attack. - **On Damage Anything**: The disguise comes off if the player's attack does any damage. - **On Damage Opponent**: The disguise comes off only if the player's attack does damage to an opponent. |
| **Disguise Breaks on Damage** | **On Damaged**, On Damaged By Opponent, On DBNO, On Eliminated, Off | Determines if the disguise comes off when the disguised player takes damage.   - **On Damaged**: The disguise comes off if the disguised player takes any damage. - **On Damaged by Opponent**: The disguise comes off when the disguised player takes damage from a hostile entity. - **On DBNO**: The player's disguise only comes off if they are put into a Down But Not Out state. - **On Eliminated**: The player's disguise comes off if they take enough damage to be eliminated. |
| **Apply Disguise on Player Spawn** | - **Creative**: On, **Off** - **UEFN**: True (checked), **False (unchecked)** | Determines if a disguise is automatically applied to a player when they spawn. This is subject to the Team to Apply To and Class to Apply To option values, if they are set. |
| **Replace Existing Disguise** | - **Creative**: **On**, Off - **UEFN**: **True (checked)**, False (unchecked) | By default, this will apply a new disguise that replaces any existing disguise the player has on. If this is set to **Off (False)**, and the player already has a disguise on, they keep their existing disguise. |
| **Start Enabled** | - Creative: On, Off - UEFN: True (checked), False (unchecked) | Determines if the device is enabled when the game starts. If this is set to **Off (False)**, the device must be enabled using event binding or Verse. |
| **Team to Apply To** | **Any**, Pick or enter a team number | Determines which team the player must belong to for the disguise to be applied. |
| **Invert Team Filter** | - Creative: On, **Off** - UEFN: True (checked), **False (unchecked)** | If this is set to **On (True)**, all teams have the disguise applied except the one set in the **Team to Apply To** option. |
| **Class to Apply To** | **Any**, Pick or enter a class number | Determines which class the player must have in order for the disguise to be applied. |
| **Invert Class Filter** | - Creative: On, **Off** - UEFN: True (checked), **False (unchecked)** | If this is set to **On (True)**, all classes have the disguise applied except the one set in the **Class to Apply To** option. |

## Brand Island Characters

For select brand islands, the Disguise device includes additional characters.

| Brand | Characters |
| --- | --- |
| **Squid Game** | - Front Man - Games Guard (various styles) - Game Manager - Games Player (various styles and random option)   To learn more about the feature set, see [Working With Squid Game Islands](https://dev.epicgames.com/documentation/fortnite/working-with-squid-game-islands-in-unreal-editor-for-fortnite). |
| *Star Wars*™ | - Civilian (various styles and random option) - Moon Trader (various styles and random option) - Rebel Trooper (various styles and random option) - Mandalorian (various styles) - Stormtrooper - Clone Trooper   To learn more about the feature set, see [Working With STAR WARS™ Islands](https://dev.epicgames.com/documentation/fortnite/working-with-star-wars-islands-in-fortnite). |

## Functions and Events

  For more information on how events and functions work, see [Getting Started with Devices](https://dev.epicgames.com/documentation/fortnite/getting-started-with-devices-in-fortnite).

While you can set both functions and events in Creative (or in a Live Edit session in UEFN), you can only set functions in UEFN, and **events are read-only**.

## Functions

| Option | Description |
| --- | --- |
| **Apply Disguise to Instigator When Receiving From** | Applies the disguise to the instigating player when an event occurs. |
| **Apply Disguise to All When Receiving From** | Applies the disguise to all players when an event occurs. |
| **Remove Disguise from Instigator When Receiving From** | Removes a disguise applied by this device from the instigating player when an event occurs. |
| **Remove Disguise from All When Receiving From** | Removes a disguise applied by this device from all players when an event occurs. |
| **Enable When Receiving From** | Enables the device when an event occurs. |
| **Disable When Receiving From** | Disables the device when an event occurs. |
| **Remove Any Disguise From Instigator** | Removes any applied disguise from the instigating player when an event occurs. |
| **Remove Any Disguise From All** | Removes any applied disguises from all players when an event occurs. |

## Events

Events in UEFN are **read-only**. When you set a function on another device that binds to an event on this device, the events are set automatically.

In Creative, you can link events to functions, and functions to events.

| Option | Description |
| --- | --- |
| **On Disguise Applied Send Event To** | When a player has a disguise applied from this device, an event occurs, which triggers a function on the bound device. |
| **On Disguise Broken Send Event To** | If a disguise applied by this device is broken, an event occurs, which triggers a function on the bound device. |
| **On Disguise Removed Send Event To** | If a disguise applied by this device is removed, an event occurs, which triggers a function on the bound device. |
| **On Disguise Applied Any Send Event To** | When any disguise is applied to a player, an event occurs, which triggers a function on the bound device. |
| **On Disguise Broken Any Send Event To** | When any disguise is broken, an event occurs, which triggers a function on the bound device. |
| **On Disguise Removed Any Send Event To** | If any disguise is removed, an event occurs, which triggers a function on the bound device. |
