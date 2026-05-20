## https://dev.epicgames.com/documentation/en-us/fortnite/using-signal-remote-manager-devices-in-fortnite-creative

# Signal Remote Manager Devices

Give your players the ability to send signals to devices on your island and make things happen!

![Signal Remote Manager Devices](https://dev.epicgames.com/community/api/documentation/image/2a0bc3fd-fb40-4e39-8d68-386443804ad1?resizing_type=fill&width=1920&height=335)

A **Signal Remote** is a device players can carry and use to send signals to other devices. You can use the **Signal Remote Manager** to manage how and where these signals are sent. This gives players the ability to send signals from held items [in-game](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).

For example, a player can activate their Signal Remote to send a signal that teleports them back to their base area.

## Finding and Placing the Signal Remote Manager

[![Finding the Signal Remote Manager Device](https://dev.epicgames.com/community/api/documentation/image/36aed0c9-0790-402e-9043-1410e39c1627?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36aed0c9-0790-402e-9043-1410e39c1627?resizing_type=fit)

Finding the Signal Remote Manager Device

*Click image to enlarge.*

## Finding and Placing a Signal Remote

You need to use a Signal Remote with the Signal Remote Manager. Although it doesn't look like a weapon, the Signal Remote is found on the **Weapons** tab in the Creative inventory.

You need to grant your players a Signal Remote using a [Class Designer](using-class-designer-devices-in-fortnite-creative), an [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) device, or a [chest](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary). This Signal Remote can "fire" signals on two channels: a primary and a secondary.

[![Finding the Signal Remote](https://dev.epicgames.com/community/api/documentation/image/b8515020-582f-4341-ab83-954a8886397c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8515020-582f-4341-ab83-954a8886397c?resizing_type=fit)

Finding the Signal Remote

*Click image to enlarge.*

If you're using multiple copies of a device on an island, it can be helpful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) them. You can choose names that relate to each device's purpose so it's easier to remember what each one does.

## Device Options

When you customize the options on the Signal Remote Manager, the values will affect how the Signal Remote works.

You can configure the Signal Remote Manager with the following options.

Default values are **bold**.

### Device Options

| Option | Value | Description |
| --- | --- | --- |
| **Enabled at Game Start** | **On**, Off | Determines whether the device is [enabled](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) at the start of the game. |
| Cooldown Time | 3 seconds, Pick or enter an amount of time | Determines the length of time the [cooldown](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) lasts after you activate the Signal Remote. |
| **Signal Remote Tier** | Common, **Uncommon**, Rare, Epic, Legendary | Determines the rarity tier of the signal remote this device is paired with. |
| **Activate Events Immediately** | On, **Off** | Determines whether the event activates as soon as the player presses the input control. |
| **Remote Sound Enabled** | **On**, Off | Determines whether the device should play default SFX or not. |

## Direct Event Binding

[Direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) allows devices to communicate directly, which makes your workflow more intuitive, and gives you more freedom to focus on your design ideas.

Below are the [functions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) and [events](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) for this device.

### Functions

Direct event binding uses functions as receivers. A function listens for one device's event to tell another device to perform a function.

| Option | Select Device | Select Event | Description |
| --- | --- | --- | --- |
| **Enable When Receiving From** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available events. | This function enables the device when an event occurs. If more than one device or event can enable this device, click **Add** to add a new line. |
| **Disable When Receiving From** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available events. | This function disables the device when an event occurs. If more than one device or event can disable this device, click **Add** to add a new line. |

### Events

Direct event binding uses events as transmitters. An event tells another device to perform a function.

| Option | Select Device | Select Event | Description |
| --- | --- | --- | --- |
| **On Primary Activation Send Event To** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available functions. | When the player activates the Signal Remote's primary function, the device sends an event to the selected device, which triggers the selected function. |
| **On Secondary Fire Send Event To** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available functions. | When the player activates the Signal Remote's secondary function, the device sends an event to the selected device, which triggers the selected function. |

## Design Examples

Here are some examples of how you can use the Signal Remote Manager.

- [Door Lock](https://dev.epicgames.com/documentation/fortnite/using-signal-remote-manager-devices-in-fortnite-creative)
- [Restock Remote](https://dev.epicgames.com/documentation/fortnite/using-signal-remote-manager-devices-in-fortnite-creative)
- [Remote Hacking](https://dev.epicgames.com/documentation/fortnite/using-signal-remote-manager-devices-in-fortnite-creative)

The Signal Remote Manager device requires one of the Signal Remote A through D weapons to be registered to it in order to transmit signals correctly. This means you can have four different Signal Remote Manager devices within the same map, one per Signal Remote weapon. Then, through either a Class Manager, Item Spawner or Item Granter, you need to give this to the player to use.

For these examples, all three use the Class Designer device. Place a Class Designer anywhere on the map and customize it with the following settings.

[![Class Designer Settings](https://dev.epicgames.com/community/api/documentation/image/9974f58f-4eee-4e38-8dd6-d5e653c5ca13?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9974f58f-4eee-4e38-8dd6-d5e653c5ca13?resizing_type=fit)

| Option | Value | Description |
| --- | --- | --- |
| **Class Identifier** | 1 | This will be used as the default class for all examples. |
| **Equip Granted Item** | First Item | The Signal Remote will be automatically equipped upon spawning. |

Next, go to the Game tab in your My Island settings and make sure to set the Default Class Identifier as follows. This will ensure that you spawn with the Signal Remote weapon at the beginning of each design example.

[![My Island Game Tab, Default Class Identifier](https://dev.epicgames.com/community/api/documentation/image/db4ba5c4-e457-488e-b6fb-64ceb4e09188?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db4ba5c4-e457-488e-b6fb-64ceb4e09188?resizing_type=fit)

My Island Game Tab, Default Class Identifier

*Click image to expand.*

| Which Tab in My Island | Option | Value | Description |
| --- | --- | --- | --- |
| Game | **Default Class Identifier** | 1 | This will be used as the default class for all examples. |

### Door Lock

The most basic functionality of the Signal Remote Manager device is in sending two signals — such as one to open or unlock a door, and the other to close it. This is demonstrated in the following example and video.

You will need the following devices.

- 1 x **Signal Remote Manager** and **Signal Remote** weapon
- 1 x [Lock](https://dev.epicgames.com/documentation/fortnite/using-lock-devices-in-fortnite-creative)

You now have a lockable door operated by a Signal Remote weapon.

You can also use this game mechanic for enabling and disabling other devices. Lock a car remotely so nobody else can use it. Make walls vanish and reappear with a toggle for an advanced line of defense. These openings can be used as shortcuts on the team, and restricted to certain classes or globally used.

### Restock Remote

You can use Signal Manager devices to set primary and secondary fire to trigger Teleporter devices. This gives players a way to restock immediately during a firefight without being eliminated, and provides a way to teleport to a central location..

You will need the following devices.

- 1 x **Signal Remote Manager** and **Signal Remote**
- 2 x [Teleporter](https://dev.epicgames.com/documentation/fortnite/using-teleporter-devices-in-fortnite-creative)
- Multiple [Vending Machines](https://dev.epicgames.com/documentation/fortnite/using-vending-machine-devices-in-fortnite-creative)

You now have a Signal Remote weapon able to teleport the player between two different locations.

Game modes with longer respawns or limited lives can benefit from this method of re-engagement, where running in and being eliminated might not be the best way to get back in the fight. There can also be two assault points that a player can choose between after respawning.

### Remote Hacking

You can use more complex interactions with a signal manager. They can be used offensively in game modes like Capture the Flag, Search and Destroy or Domination to give a unique identity to certain classes.

You will use the following devices.

- 1 x **Signal Remote Manager** and **Signal Remote**
- Multiple [**Customizable Lights**](using-customizable-light-devices-in-fortnite-creative)
- 1 x [Timed Objective Device](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)

You have now set up a Signal Remote weapon that operates as a remote hacking device.

Set the cooldown time longer than 1 second. This was used for demonstration, but the actual class should have a longer cooldown. You could also combine the above elements, to open shortcuts that are normally locked and might be poorly defended. Alternatively, you can set classes to temporarily activate Sentry devices on a cooldown, which help defend the base when it is attacked.
