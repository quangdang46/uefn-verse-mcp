## https://dev.epicgames.com/documentation/en-us/fortnite/using-stink-flower-devices-in-fortnite-creative

# Stink Flower Devices

Place a plant pod in the environment that players can hit with a pickaxe to toss a stink-bomb toward enemies.

![Stink Flower Devices](https://dev.epicgames.com/community/api/documentation/image/533c670a-e2ea-44ff-b085-6765fcae6af6?resizing_type=fill&width=1920&height=335)

**Stink Flowers** can launch projectiles that act like stink grenades, and give you a new way to provide stink resources for players so you have a broader selection of items to place on your island.

There are lots of ways this can enhance your island experience:

- Provide a more dynamic and interactive environment for players.
- Give players more ways to interact with your game mechanics.
- Give players additional tools to play strategically.
- Establish that there are multiple ways to locate and use resources.

## Device Options

This device has some basic functionality, like whether the pod launches when hit. Additionally, there are some advanced options, like whether the pod regrows automatically and whether it can regrow infinitely.

Creative, default values are bold. Values that trigger [contextual filtering](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#contextual-filtering) to provide more options are italic.

| Option | Value | Description |
| --- | --- | --- |
| **Launch on Hit** | **On**, Off | Determines if hitting the plant launches a projectile explodes on impact. If this is set to Off the plant will explode immediately upon being hit. |
| **Enabled During Phase** | **Always**, None, Pre-Game Only, Gameplay Only, Create Only | Enable the device during a specific phase. The Pre-Game phase includes all phases before the Game starts. If the device is enabled when you are editing your island in Create mode, launching or exploding the plant will not cause damage. |
| **Grow Automatically** | **True**, Initial Only, Regrowth Only, False | Determines if the plant regrows automatically, or if it only grows when the device receives a signal. This doesn't apply while you are editing the island.   - **True**: The plant regrows automatically. - **Initial Only**: The plant automatically grows once. - **Regrowth Only**: The plant only automatically regrows after launching a projectile or being destroyed. - **False**: The plant only grows when the device receives a signal. |
| **Initial Delay** | **None**, Pick or enter a number | Determines the time delay before the plant grows for the first time. The timer resets if the device is disabled. |
| **Regrowth Delay** | None, **15 Seconds**, Pick or enter a number | When the plant launches a projectile or is destroyed, this determines the time delay before the plant regrows. The timer resets if the device is disabled. |
| **Infinite Regrowths** | **On**, *Off* | Determines if the plant can regrow indefinitely after launching a projectile or being destroyed. If you set this to **Off**, another option displays below this one. |
| **Maximum Regrowths** | **10**, Pick or enter a number up to 100 | This option only displays if you have set the **Infinite Regrowths** option to **Off**. Determines the number of times a plant can regrow after launching a projectile or being destroyed. This applies across the device's lifetime, and is not affected by whether the device is enabled or disabled. |
| **Can Grow in Storm** | **On**, Off | Determines if the plant regrows while it is in a storm. |
| **Hide when Disabled** | **True**, False, Show Leaves | Determines if the device is visible when disabled.   - **True**: The device is not visible when disabled. - **False**: The device is visible when disabled. - **Show Leaves**: When the device is disabled, only the leaves will be displayed. |

## Direct Event Binding System

[Direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) allows devices to communicate directly, which makes your workflow more intuitive, and gives you more freedom to focus on your design ideas.

Below are the [functions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) and [events](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event) for this device.

### Functions

| Option | Select Device | Select Event | Description |
| --- | --- | --- | --- |
| **Enable When Receiving From** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available events. | This function enables the device when an event occurs. If more than one device or event can enable this device, click **Add** to add a new line. |
| **Disable When Receiving From** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available events. | This function disables the device when an event occurs. If more than one device or event can disable this device, click **Add** to add a new line. |
| **Grow When Receiving From** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available events. | This function causes the plant to grow when an event occurs. If more than one device or event can make the plant grow, click **Add** to add a new line. |
| **Explode When Receiving From** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available events. | This function causes the plant to explode when an event occurs. If more than one device or event can make the plant explode, click **Add** to add a new line. |

### Events

| Option | Select Device | Select Function | Description |
| --- | --- | --- | --- |
| **On Grow Send Event To** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available functions. | When the plant grows, the device sends an event to the selected device, which triggers the selected function. |
| **On Explode Send Event To** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available functions. | When the plant explodes, the device sends an event to the selected device, which triggers the selected function. |
| **On Launch Send Event To** | Click the arrow to display a list of available devices. | Click the arrow to display a list of available functions. | When the plant launches a projectile, the device sends an event to the selected device, which triggers the selected function. |
