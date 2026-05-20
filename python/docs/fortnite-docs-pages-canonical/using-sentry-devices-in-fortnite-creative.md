## https://dev.epicgames.com/documentation/en-us/fortnite/using-sentry-devices-in-fortnite-creative

# Sentry Devices

Spawn customized sentries that attack players.

![Sentry Devices](https://dev.epicgames.com/community/api/documentation/image/cd0406a6-27eb-4ace-b492-ba37aed9fd66?resizing_type=fill&width=1920&height=335)

The **Sentry** device spawns an [artificial intelligence (AI)](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) bot that usually attacks players when they come in range. As a device, you can place sentries anywhere.

To find the Sentry device, go to the Creative inventory and select the Devices tab. From there you can search or browse for the device. For more information on finding devices see [Finding and Placing Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite).

If you're using multiple copies of a device on an island, it can be helpful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) them. You can choose names that relate to each device's purpose, so it's easier to remember what each one does.

## Device Options

Basic options include setting the sentry health and what weapons you want to arm a sentry with.

### Contextual Filtering

Some devices are affected by a feature called **contextual filtering**. This feature hides or displays options depending on the values selected for certain related options. This reduces clutter in the Customize panel and makes options easier to manage and navigate. To help identify them, values that trigger contextual filtering are in *italic*.

All options are listed, including those affected by contextual filtering; if they are hidden or displayed based on a specific option's value, there will be a note about it in the Description field for that option.

Default values are **bold**. Values that trigger contextual filtering are *italic*.

You can configure this device with the following options.

| Option | Value | Description |
| --- | --- | --- |
| **Weapon Type** | **Pistol**, Pick a weapon | Determines how the sentry will be armed when it spawns. |
| **Invulnerable** | **Off**, *On* | Determines whether a sentry can be damaged. If set to **On**, the next option, **Sentry Health**, does not show. |
| **Respawn on a Timer** | **On**, *Off* | Determines whether a sentry can respawn after elimination. If set to **Off**, the next option, **Respawn Time**, does not show. |
| **Respawn Time** | **1.0 seconds**, Pick a time | Determines the time, in seconds until a sentry respawns after it's eliminated. |
| **Range** | **10M**, Pick a range | The range (distance in meters) at which the sentry detects players. |
| **Show Visualization Range** | **On**, Off | Determines whether the sentry's range is visible while you're editing the device. |
| **Accuracy** | **Low**, Moderate, High, Deadshot | How accurate the sentry is when attacking players that are in range. |
| **Use Line of Sight** | **On**, Off | If set to **On**, sentry will only shoot at players within its [line of sight](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary). If set to **Off**, the sentry will attempt to shoot any player in range regardless of visibility. |
| **Use Adaptive Aim** | On, **Off** | Determines whether the sentry's aim improves based on how long it targets a player. |
| **Can Target Creatures** | Yes, **No** | Determines if the sentry can target Fiends and Wildlife that are on a different team from the sentry. If **Friendly Team** is set to **None**, the sentry will only target Wildlife if they are tamed by a player. |
| **Can Target Untamed Wildlife** | On, **Off** | Determines if the sentry can target wildlife on the wildlife team when no friendly team is set. |
| **Can Target Neutrals** | On, **Off** | Determines if the sentry can target the neutral team. |
| **Sentry Health** | **100**, Pick a value | Determines the amount of health the sentry has. |
| **Sentry Shield** | **No Shield**, Pick an amount of shield | Determines if the sentry has a shield, and if so, how much protection it gives. |
| **Friendly Team** | **None**, Pick a team | Determines which team the sentry will treat as friendly. |
| **Spawn on Game Start** | **On**, Off | Determines whether the sentry spawns when the game starts. |
| **Award Elimination** | **On**, Off | Determines whether the player is awarded an elimination for destroying the sentry. |
| **Score on Elimination** | **0**, Pick a score amount | Sets the amount of score awarded to the player for eliminating the sentry. |
| **Set Sentry Scale to Spawner Size** | **Off**, On | The spawner for the Sentry device can be resized. To make your sentry larger, resize the spawner and set this option to On. Otherwise, the sentry will spawn at the same size as the players. |
| **Time to Alert** | **Instant**, pick an amount of time | Sets how long the sentry waits to attack after it notices a player. |
| **Time to Cooldown** | **Instant**, pick an amount of time | Set how long it takes for the sentry return to idle after it is attacked. |
| **Show Alert Icon** | **On**, Off | Determines whether the Alert icon displays above the sentry. |

## Direct Event Binding

Following are the [direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) listens for an event on a device then performs an action.

| Option | Description |
| --- | --- |
| **Destroy Sentry When Receiving From** | Destroys the sentry when an event occurs. |
| **Join Team When Receiving From** | The sentry will join the [instigating](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) player's team when an event occurs. |
| **Reset Team When Receiving From** | The sentry's team is set to the team specified on its spawner when an event occurs. |
| **Pacify When Receiving From** | Prevents a sentry from entering an alert state when an event occurs. |
| **Enable Alert When Receiving From** | Allows the sentry to enter an alert state when an event occurs. |
| **Target Player When Receiving From** | The sentry will target an instigating player when an event occurs as long as the sentry is not on the same team as the player. |
| **Reset Alert Cooldown When Receiving From** | The sentry will reset its alert state when an event occurs. |

### Events

An [event](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| On Eliminated Send Event To | When the sentry is eliminated, it sends an event to the selected device, which triggers the selected function. |
| On Eliminating Player Send Event To | When the sentry eliminates a player, it sends an event to the selected device, which triggers the selected function. |
| On Attacking Send Event To | When a sentry an attack on a player, it sends an event to the selected device, which triggers the selected function. |
| On Eliminating a Creature Send Event To | When a sentry eliminates a creature, it sends an event to the selected device, which triggers the selected function. |
| On Alerted Send Event To | An event is sent to the selected device when alerted to the presence of a player, which triggers the selected function. |
| On Exiting Alert Send Event To | An event is sent to the selected device when the sentry is no longer in an alert state, which triggers the selected function. |
| On Entering Alert Cooldown Send Event To | When a sentry has lost track of all its targets, this sends an event to the selected device, which triggers the selected function. |

## Design Examples

Here are some examples of how you can use the Sentry device.

- [Ambush Sentry](https://dev.epicgames.com/documentation/fortnite/using-sentry-devices-in-fortnite-creative)
- [Guard Sentry](https://dev.epicgames.com/documentation/fortnite/using-sentry-devices-in-fortnite-creative)
- [Upgradeable Sentry](https://dev.epicgames.com/documentation/fortnite/using-sentry-devices-in-fortnite-creative)

### Ambush Sentry

You can use sentries with a lot of customizability to create traps with various resolutions beyond simply shooting them down. In this example, the player must flip a switch to deactivate the sentries.

You will need the following devices.

- 2 x **Sentry** device
- 1 x [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) device
- 1 x [Switch](https://dev.epicgames.com/documentation/fortnite/using-switch-devices-in-fortnite-creative) device

| Option | Value | Description |
| --- | --- | --- |
| **Trigger Sound** | Disabled | The trigger does not make a sound when activated. |
| **Trigger VFX** | Disabled | The trigger does not produce visual effects when activated. |
| **Visible in Game** | No | The Trigger device is not visible during gameplay. |
| **When Triggered Transmit On** | Channel 1 | When the trigger is activated, both sentries start attacking until the switch is activated. |

You now have the basic setup for a Sentry trap.

You can make the sentries destroyable instead, if you prefer them to not be deactivated with a button. They could also be set across a maze, creating a suddenly dangerous environment to navigate through once more. Their weapons, accuracy, and radius can all be fine tuned to get the level of threat you desire for your sentries.

### Guard Sentry

In this example, you can set up sentries players can use akin to defensive turrets, that will attack enemies not on their team, even wildlife. Follow these instructions to set it up.

You will need the following devices.

- 2 x **Sentry** devices
- 1 x [Timed Objective](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative) device
- 1 x [**Button**](using-button-devices-in-fortnite-creative) device
- 1 x [Wildlife Spawner](https://dev.epicgames.com/documentation/fortnite/using-wildlife-spawner-devices-in-fortnite-creative) device

| Option | Value | Description |
| --- | --- | --- |
| **Timer Label Text** | Sentries Active For... | Text displayed during the countdown. |
| **Completion Behavior** | Reset | Resets the Timed Objective device allowing it to be used again. |
| **Urgency Mode** | Disabled | The timer does not play special SFX during the last five seconds of the countdown. |
| **Start When Receiving From** | Channel 1 | Starts counting down when the Button device is pressed. |
| **When Completed Transmit On** | Channel 2 | After finishing the 10 second default countdown, sends a signal to despawn the sentries and allow them to be spawned again. |

You now have the basic functionality to temporarily spawn defensive sentries.

This design mentions a number of features that can be included into this. For example, you can adjust the time the sentries are available, and trigger them using a Signal Remote or with much longer delays for more tactical cooldowns. These can be restricted to certain classes, in PvP style gameplays, or allow a chaos element in a free-for-all where anyone can trigger them, or have them trigger when a player has an elimination streak.

### Upgradeable Sentry

For this example, by following these steps you can set up a static defensive sentry that players can upgrade into a more effective one.

You will need the following devices.

- 2 x **Sentry** devices
- 1 x [**Button**](using-button-devices-in-fortnite-creative) device
- 1 x [**Conditional Button**](using-conditional-button-devices-in-fortnite-creative) device
- 1 x [Wildlife Spawner](https://dev.epicgames.com/documentation/fortnite/using-wildlife-spawner-devices-in-fortnite-creative) device

| Option | Value | Description |
| --- | --- | --- |
| **Disable After Use** | Yes | The conditional button can only be used once. |
| **Key Items Required** | 10 | For this example, 10 Gold coins are required for players to activate the button and upgrade the sentry. |
| **When Activated Transmit On** | Channel 2 | Sends a signal that despawns the original sentry and spawns the upgraded one. |

You now have the basic functionality for upgrading sentries.

In any situation where sentries are summoned, whether defensively, aggressively, or even at traps, they can be upgraded or downgraded depending on actions that the player takes. This allows a wide breadth of opportunity in how to add alternative objectives or ways to keep them dynamic during gameplay. Make sure to set **Infinite Resources** to **Off** in your **My Island** settings or coins will not be deducted!

## Gameplay Examples Using Sentry Devices

- [Shooting Gallery](https://dev.epicgames.com/documentation/fortnite/shooting-gallery-in-fortnite-creative)
- [Random Sentry Fight](https://dev.epicgames.com/documentation/fortnite/random-sentry-fight-in-fortnite-creative)
