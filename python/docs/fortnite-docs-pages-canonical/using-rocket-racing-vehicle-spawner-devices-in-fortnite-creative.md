## https://dev.epicgames.com/documentation/en-us/fortnite/using-rocket-racing-vehicle-spawner-devices-in-fortnite-creative

# Rocket Racing Vehicle Spawner Device

Customize this vehicle to use the same game mechanics as Rocket Racing, but on your own island.

![Rocket Racing Vehicle Spawner Device](https://dev.epicgames.com/community/api/documentation/image/ba59b8bf-5572-4a27-81f4-968d689768bf?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [Getting Started with Devices](https://dev.epicgames.com/documentation/fortnite/getting-started-with-devices-in-fortnite)

The**Rocket Racing Vehicle Spawner** device, available in UEFN and Fortnite Creative, spawns a vehicle with Rocket Racing (RR) mechanics built for high-speed racing and aerial control.

These vehicles offer greater mobility and customization than most, allowing players to drive across terrain, climb vertical surfaces, and even travel upside down using sticky wheels. The vehicle does not use fuel or support passengers, focusing on fast, responsive movement.

The RR Vehicle Spawner device is a great starting point if you want to create your own racing game. It offers the same mechanics as Rocket Racing, and dozens of options that you can adjust for specific gameplay needs.

You can tune the mechanics for a more grounded driving experience or push them further to create high-mobility, platforming-style gameplay.

For help on how to find the RR Vehicle Spawner device, see [Using Devices](https://dev.epicgames.com/edc/manage/assets/using-devices-in-fortnite-creative).

If you're using multiple copies of a device on an island, it can be useful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#rename-a-device) them. Choosing names that relate to a device's purpose makes it easier to remember what each one does, and easier to find a specific device when using the [**Event Browser**](event-browser-in-fortnite-creative).

## RR Vehicle Controls

Driving an RR vehicle uses the following controls. Understanding these actions will help you work out how to configure the vehicle for your specific gameplay.

- **Throttle** Moves the vehicle forward.
- **Brake** Moves the vehicle in reverse.
- **Steer Left** Turns to the left.
- **Steer Right** Turns to the right.
- **Jump** Makes the vehicle jump into the air. Press the **left mouse button**.
- **Thruster** Like a jump but extended. Press and **hold the left mouse button** to activate the thruster.
- **Turbo** This is the applied boost. Press the **mouse wheel** to engage.
- **Rocket Drift** When a driver steers sharply into a turn, this can push the rear tires outside of the curve. When the back wheels slide while the driver maintains control of the front wheels, this is called drifting. Press the **Shift** key to drift.
- **Air Dodge** While airborne, use an air dodge to attach to walls or ceilings by turning the vehicle while pressing the **right mouse button**.
- **Reverse Camera** This reverses the camera for a rear view. When released, the camera returns to a front view. Press **Q** to reverse the camera, then release to return to the forward camera view.

## Vehicle Skin Options

Players have full control over their own car [cosmetics](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#cosmetics) through their [lockers](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#locker). Any cosmetics a player is awarded or purchases for Rocket Racing is available in the player's locker. The RR vehicle will spawn with the selected car cosmetics when a player drives the vehicle.

The selected [skin](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#outfit) has no effect on the vehicle's performance.

## Device Options

You can configure this device with the following options.

Default values are **bold**. Values that trigger contextual filtering are *italic*.

| Option | Value | Description |
| --- | --- | --- |
| **Visible During Game** | **On**, Off | Determines whether the spawner device is visible during the game. If set to **Off**, the device has no collision properties. |
| **Vehicle Can be Destroyed from Collision** | **On**, Off | This option only displays if the **Vehicle Indestructible** option is set to **On**. If this option is set to **On**, the vehicle can be destroyed when colliding with objects in the environment. |
| **Wall Ricochet Enabled** | **On**, Off | Controls whether the vehicle will ricochet (bounce) off walls it collides with. |
| **Base Top Speed** | **1.0X**, Pick or enter a multiplier | Uses a multiplier to determine the vehicle's top speed without turbo or boost. Values greater than 1.0 increase the top speed, and less than 1.0 decrease it. |
| **Base Acceleration** | **1.0X**, Pick or enter a multiplier | Controls how quickly the vehicle picks up speed when the throttle is held down. |
| **Base Deceleration** | **1.0X**, Pick or enter a multiplier | Controls how quickly the vehicle slows down when the throttle is released. |
| **Drift Boost Speed** | **1.0X**, Pick or enter a multiplier | How much speed you gain on exiting a drift boost. |
| **Drift Boost Duration** | 1.0X, Pick or enter a multiplier | How long the boost bonus speed lasts after a successful drift. |
| **Drift Boost Meter Gain Rate** | 1.0X, Pick or enter a multiplier | Sets how quickly the Drift Boost Meter Fills while drifting. |
| **Oversteer Enabled** | **On**, Off | Determines whether the vehicle can be oversteered in a turn. |
| **Thrust Meter Starting Amount** | **100.0%**, Pick or enter a percentage | The percentage of Thrust Meter a vehicle starts with. |
| **Thrust Meter Consumption Rate** | **1.0X**, Pick a multiplier | How fast the Thrust Meter is consumed when the Thrust button is held down. |
| **Turbo Starting Amount** | **0.5 Charges**, Pick or enter a number | How many tanks of Turbo a player starts with. |
| **Turbo Passive Gain Rate** | 1.0X, Pick a multiplier | How quickly Turbo tanks fill up passively (when not drifting). |
| **Turbo Drift Gain Rate** | 1.0X, Pick a multiplier | How quickly the turbo tanks fill up when a player is drifting. |
| **Turbo Speed** | 1.0X, Pick a multiplier | How much speed is added to a vehicle when a player uses Turbo. |
| **Turbo Base Duration** | **2.0 Seconds**, Pick or enter an amount | How long the Turbo Speed effect lasts. |
| **Self Demolish Enabled** | **On**, Off | Determine if the player is able to demolish their own vehicle. |
| **Enabled During Phase** | None, **Always**, Pre-Game Only, Gameplay Only, Create Only | Determines the game [phases](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-glossary#game-phase) during which the device will be enabled. Pre-game includes all phases prior to the game starting, including waiting for other players in the lobby and the countdown to start of game. |
| **Enable Respawn** | On, Off | Determines whether the vehicle will respawn after it is destroyed. |
| **Respawn Time** | **Instant (0.0)**, Pick an amount .25 - 300 seconds | If Respawn is enabled, this setting determines the interval between destruction and respawning. |
| **Respawn Vehicle when Enabled** | **Yes**, No, Only if Needed | If this is set to **Yes**, a vehicle will spawn when the device is enabled. Choosing Only If Needed will not reset an existing vehicle. |
| **Destroy Vehicle when Disabled** | **On**, Off | Destroys a spawned vehicle when the spawner is disabled. |
| **Activating Team** | **Any**, Pick or enter a number | Determines the team this vehicle belongs to. |
| **Allowed Class** | No Class, **All**, Any, Pick or enter a number | Determines which classes can use this vehicle. Values for this option are:   - **None:** All players, including players with no class assigned, can use the vehicle. - **Any:** Any player with a class assigned can use the vehicle. - **No Class:** Only players with no class assigned can use the vehicle. - **Pick a class:** Pick a class identifier; only players assigned that class can use the vehicle. |
| **Vehicle Indestructible** | On, **Off** | If set to **On**, the vehicle will not take on damage and the **Vehicle Health** option below will be hidden. |
| **Vehicle Collision Destroy Speed** | **1.0X**, Pick or enter a number | This option only displays if the **Vehicle Can Be Destroyed from Collision** option is set to **On**. Determines the speed required to destroy the vehicle if it collides with a wall or other object. Numbers higher than 1.0 require more speed to inflict damage, while numbers less than 1.0 require less. |
| **Only Ricochet Off Of Track Pieces** | On, **Off** | This option only displays if the **Wall Ricochet Enabled** option is set to **On**. Determines whether this vehicle only ricochets off of track pieces. |
| **Vehicle Health** | **2500**, Pick or enter a number | This option only displays if the **Vehicle Indestructible** option is set to **Off**. Determines how much damage the vehicle can take before it is destroyed. |
| **Destroy When Stuck Underwater** | **On**, Off | Determines whether the vehicle will self-destruct when stuck underwater. |
| **Water Destruction Timer** | Never, Instant, **5 seconds**, Pick a time | This option only displays when the **Destroy When Stuck Underwater** option is set to **On**. When the vehicle is too deep in water to drive, it is destroyed after this delay. |
| **Air Dodge Reset on Landing** | **On**, Off | Determines whether the **Air Dodge Count** option's value resets each time the vehicle's wheels touch a surface. |
| **Air Dodge Count** | **1**, Pick or enter a number | Sets how many times a player can air-dodge while airborne. |
| **Air Dodge Use Delay** | **0.0 Seconds**, Pick or enter a time | Determines how long a player has to wait between air dodges. |
| **Base Braking Power** | **1.0X**, Pick or enter a multiplier | How quickly the vehicle slows down when the brake is used. |
| **Base Maximum Aerial Speed** | 1.0X, Pick or enter a multiplier | This option sets the maximum base speed when traveling through the air. If the vehicle exceeds this speed, the vehicle will start to lose speed. |
| **Drift Top Speed** | 1.0X, Pick or enter a multiplier | The maximum speed a vehicle can reach while in a drift. Any faster than this, and the vehicle will start to lose speed. |
| **Drift Deceleration Rate** | 1.0X, Pick or enter a multiplier | If the vehicle goes faster than the **Drift Top Speed**, this option controls how rapidly your vehicle loses speed during the drift. |
| **Drift Acceleration Rate** | 1.0X, Pick or enter a multiplier | If the vehicle is going below the **Drift Top Speed**, this sets how rapidly the vehicle will accelerate toward the top speed during the drift. |
| **Gravity Aerial Scalar** | 1.0X, Pick or enter a multiplier | Scales the forces of gravity on the vehicle when it is in the air. |
| **Jump Force** | 1.0X, Pick or enter a multiplier | How much force is applied when using jump. |
| **Oversteer Threshold** | **1.0X**, Pick or enter a multiplier | Determines when the vehicle will start to drift from oversteer when continually steering in one direction. A lower value results in more slip. |
| **Surface Counter Gravity Degree Threshold** | **180.0**X, Pick or enter a multiplier | Controls what surfaces the vehicle will stick to when grounded on them. Values range from a completely upside down surface (180 degrees) to a flat upright surface (0 degrees). |
| **Surface Latch Degree Threshold** | **180.0**X, Pick or enter a multiplier | Controls what surfaces the vehicle will attempt to latch on to when running into them in the air. Values range from a completely upside down surface (180 degrees) to a flat upright surface (0 degrees). |
| **Thrust Meter Replenishes on Landing** | **On**, Off | Determines whether the Thrust Meter fully replenishes when the vehicle's tires touch a surface. |
| **Thrust Meter Replenishes Over Time** | On, **Off** | Determines whether the Thrust Meter will regenerate over time. If set to On, two more options show. |
| **Thrust Meter Replenish Delay** | **0.5 Seconds**, Pick or enter an amount | This option only displays if the **Thrust Meter Replenishes Over Time** option is set to **On**. How long it takes for the Thrust Meter to begin replenishing after the player releases the Thrust button. |
| **Thrust Meter Replenish Rate** | 1.0X, Pick or enter a multiplier | This option only shows if **Thrust Meter Replenishes Over Time** is set to **On**. This is the rate at which the Thrust Meter replenishes over time when it is not being used. |
| **Thruster Force** | 1.0X, Pick or enter a multiplier | The amount of force applied when a thruster is active. |
| **Thruster Max Upward Speed** | 1.0X, Pick or enter a multiplier | The maximum upward speed a thruster can achieve. |
| **Turbo Bonus Zone Speed Duration** | **0.25 Seconds**, Pick or enter an amount | The amount of time added to the duration of Turbo if a player successfully activates a turbo bonus zone. |
| **Required Demolish Action Duration** | **0.25 Seconds**, Pick or enter an amount | The amount of time the player must hold the demolish button in order to demolish their vehicle. |

## Functions and Events

For more information on how events and functions work, see [Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite).

### Functions

| Option | Description |
| --- | --- |
| **Enable** | Enables the vehicle spawner when an event occurs. |
| **Disable** | Disables the spawner when an event occurs. |
| **Respawn Vehicle** | When an event occurs, the vehicle respawns. This also destroys the existing vehicle if there is one. |
| **Destroy Vehicle** | If the vehicle this spawner spawned still exists, it will be destroyed when an event occurs. |
| **Assigns Driver** | This assigns the instigating player as the driver for this vehicle when an event occurs. |

### Events

Events in UEFN are **read-only**. When you set a function on another device that binds to an event on this device, the events are set automatically but cannot be edited.

In Creative, you can link events to functions as well as functions to events.

| Option | Description |
| --- | --- |
| **On Player Enters Vehicle** | When a player enters the spawned vehicle, this sends an event to the selected device, which triggers the selected function. |
| **On Player Exits Vehicle** | When a player exits the spawned vehicle, this sends an event to the selected device, which triggers the selected function. |
| **On Vehicle Spawns** | When a vehicle is spawned or respawned, this sends an event to the selected device, which triggers the selected function. |
| **On Vehicle Is Destroyed** | When a vehicle is destroyed, this sends an event to the selected device, which triggers the selected function. |
