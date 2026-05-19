## https://dev.epicgames.com/documentation/en-us/fortnite/failure-in-verse

# Verse Parkour Template
Create a parkour game with Verse to customize your gameplay.
![Verse Parkour Template](https://dev.epicgames.com/community/api/documentation/image/87062f56-6d4c-4224-97bf-136d2e4b0bab?resizing_type=fill&width=1920&height=335)
The **Verse Parkour Template** will show you how to create a game mode where players can strategically maneuver through obstacles and platforms to collect batteries.
In this game mode, players will collect four batteries to complete the level. Time will extend if they find the secret battery. When time runs out, the player returns to the beginning.
This template demonstrates some basic language features like:
  * For Loops
  * Subscriptions
  * Arrays
  * Device API

Complex concepts, like concurrency, will not be used in this template.
##  Overview
The following is an overview of the steps you'll need to recreate this island in the ideal sequence:
  1. [Create a new project](https://dev.epicgames.com/documentation/fortnite/project-organization-in-unreal-editor-for-fortnite) and [modify Island Settings](https://dev.epicgames.com/documentation/fortnite/island-settings-in-unreal-editor-for-fortnite) to set up the game.
  2. Build the arena.
  3. Set up devices.
  4. Add the Verse Script.
  5. [Set up the Verse device](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite).

##  Creating a New Project and Setting up the Game
  1. Open UEFN and create a new empty project.
  2. Select **Island Settings** device in the **Outliner** and locate **User Options - Game Rules**.
[![Island Settings](https://dev.epicgames.com/community/api/documentation/image/bab965c4-40f3-41d0-b0df-5791a368bec8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bab965c4-40f3-41d0-b0df-5791a368bec8?resizing_type=fit)
  3. Modify the User Options as shown below.
Option  |  Value  |  Explanation
---|---|---
**Join in Progress** |  Spawn |  Specifies what to do when a player joins while a game is in progress. Set to **Spawn** if you want players to join in progress.
**Game Win Condition** |  Most Scores Win |  The player with the highest score will win the game.
**Round Win Condition** |  Score |  Players with the highest score will win the round.
**Locomotion Preset** |  Custom |  Quickly configure locomotion settings to match a first-party experience and opt in to future changes to that preset or use cutom settings to lock in behavior.
**Allow Mantling/Sprinting/Sliding/Shoulder Bashing** |  True |  Players will be able to parkour over their environment.
**PBWs Generate Ledges** |  False |  If **Allow Mantling** is set to **True** , this option determine sif **Player Built Walls** will generage ledge launch props. If **Allow Mantling** is set to **Off** , then PBWs will not generate ledges.
**Glider Redeploy** |  False |  Determines whether players can frelly deploy their gliders without the use of items.
**Movement Speed Tunings** |  Ch 4 Movemenet |  Determines the movement speed tunings that should be used for player locomotion.
**Allow Boosted Jump** |  False |  Boosted Jump allows players to perform a higher and faster jump when they are sprinting near an edge.
**Allow Roll Landing** |  False |  Roll Landing allows players to roll upon reaching the ground.
**Allow Wall Kick** |  False |  Determines whether players can kick off of walls.
**Allows Wall Scramble** |  False |  Determines whether players can run up walls for a short distance.
**Auto Pickup Consumables** |  Yes |  Determines if the player automatically collects Consumables. **Auto Only** hides the pickup interaction UI.
**Infinite Building Resources/Gold/World Resources/Durability** |  Players will be able to collect all resources in their environment. |
**Start With Pickaxe** |  False |  Players will not start the game with a pickaxe.
**Pickaxe Destruction** |  None |  The pickaxe will not damage the environment.
**Auto Pickup Items** |  Yes |  Players will automatically pick up items they come into contact with.
**First Scoreboard Column** |  Score |  The scoreboard will show the score in the first column.

##  Building the Arena
This map uses the **Cyber City Prop Gallery** , which can be found under **Fortnite > Galleries > Props**.
Recreate this map with platforms and obstacles for players to parkour over.
##  Setting up the Devices
This tutorial uses the following devices:
  * ~ [Player Spawn Pad](https://www.fortnite.com/fortnite/en-US/creative/docs/using-player-spawn-pad-devices-in-fortnite-creative)
  * 5 x [Item Granter](https://www.fortnite.com/fortnite/en-US/creative/docs/using-item-granter-devices-in-fortnite-creative)
  * 1 x [End Game](https://www.fortnite.com/fortnite/en-US/creative/docs/using-end-game-devices-in-fortnite-creative)
  * 1 x [Damage Volume](https://www.fortnite.com/fortnite/en-US/creative/docs/using-damage-volume-devices-in-fortnite-creative)
  * 1 x [Timer](https://www.fortnite.com/fortnite/en-US/creative/docs/using-timer-devices-in-fortnite-creative)
  * 1 x [HUD Message](https://www.fortnite.com/fortnite/en-US/creative/docs/using-hud-message-devices-in-fortnite-creative)
  * 1 x [Verse Device](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite)

###  Player Spawn Pad Device
[![Player Spawn Pad](https://dev.epicgames.com/community/api/documentation/image/b73e6881-67fd-4dd3-89b4-80f9bfa57f5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b73e6881-67fd-4dd3-89b4-80f9bfa57f5e?resizing_type=fit)
Use a **Player Spawn Pad** device to spawn players onto the map. At the start of your map, place a spawn pad for each player, which you can find under **Fortnite > Devices > Player Spawn Pad**.
To set up this device, configure the **User Options** as follows:
Option  |  Value  |  Explanation
---|---|---
**Visible In Game** |  False |  This device will not be visible in game.
###  Item Granter Device
[![Item Granter Device](https://dev.epicgames.com/community/api/documentation/image/0dac5159-30fc-4678-a3dd-c3039907cada?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0dac5159-30fc-4678-a3dd-c3039907cada?resizing_type=fit)
In UEFN, dragging a [Consumable](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-items-in-fortnite-creative) from the **Content Drawer** automatically places it in an **Item Spawner** device. Drag a [Battery](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-power-crafting-items-in-fortnite-creative) item onto the map, which you can find under **Fortnite > Items > Battery**.
To set up this device, configure the **User Options** as follows:
Option  |  Value  |  Explanation
---|---|---
**Time Before Spawn** |  0.1 |  This determines the amount of time before the item spawns.
**Respawn Item on Timer** |  False |  The battery will not respawn once picked up.
**Base Visible During Game** |  False |  The device will not be visible in the game.
**Run Over Pickup** |  True |  Players will automatically pick up this item.
**Item Scale** |  2.0 |  This determines the size of the battery.
Copy and paste this device four more times and place them around your map.
###  End Game Device
[![End Game Device](https://dev.epicgames.com/community/api/documentation/image/dfc401a9-0bca-40ff-80ce-34d73c54d851?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dfc401a9-0bca-40ff-80ce-34d73c54d851?resizing_type=fit)
Place an **End Game** device to end the game when activated.
To set up this device, configure the **User Options** as follows:
Option  |  Value  |  Explanation
---|---|---
**Custom Victory Callout** |  enter text |  Enter the text you want displayed for the winning player.
###  Damage Volume Device
[![Damage Volume Device](https://dev.epicgames.com/community/api/documentation/image/1eb1c84f-daa6-4b66-8ac9-aa50e1534c31?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1eb1c84f-daa6-4b66-8ac9-aa50e1534c31?resizing_type=fit)
The **Damage Volume** device is a boundary that can damage players within its zone. Place this device below your map and adjust the **Zone Width** , **Depth** , and **Height** to cover the bottom of your arena to instantly eliminate fallen players.
To set up this device, configure the **User Options** as follows:
Option  |  Value  |  Explanation
---|---|---
**Damage** |  500 |  This device deals enough damage to instantly eliminate players who fall.
###  Timer Device
[![Timer Device](https://dev.epicgames.com/community/api/documentation/image/30a7ae3d-6875-4ce6-aac4-6728138e1ce8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30a7ae3d-6875-4ce6-aac4-6728138e1ce8?resizing_type=fit)
Place a **Timer** device near the End Game device. This device will count down the time until the player is eliminated and must start over.
To set up this device, configure the **User Options** as follows:
Option  |  Value  |  Explanation
---|---|---
**Duration** |  30 |  The timer will last for 30 seconds.
**Start at Game Start** |  True |  The timer begins when the game starts.
**Applies To** |  Player |  When the timer starts, it applies to a specific player.
**Success on Timer End** |  False |  When the timer reaches its end, it will not count as a success.
**Visible During Game** |  Hidden |  The device will be hidden in the game.
**Timer Running Text** |  enter text |  Enter the text you want displayed for the timer.
###  HUD Message
[![HUD Message Device](https://dev.epicgames.com/community/api/documentation/image/44c9e202-8a7c-4191-8ba5-62997a20f003?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/44c9e202-8a7c-4191-8ba5-62997a20f003?resizing_type=fit)
Use a **HUD Message** device to display engaging messages to players.
To set up this device, configure the **User Options** as follows:
Option  |  Value  |  Explanation
---|---|---
**Display Time** |  2.0 |  The message will display for two seconds before disappearing.
**Show on Round Start** |  False |  This message will not be displayed when the round starts, but when a battery is picked up.
###  Adding the Verse Scripts
[Add the following Verse scripts](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite), starting by referencing devices with the [@editable](https://dev.epicgames.com/documentation/fortnite/editable-properties-in-verse) function.
You can copy the code in the order it’s written. Comments are added within the script for clarity.
Verse
```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Characters }
using { /Verse.org/Simulation}
using { /UnrealEngine.com/Temporary/Diagnostics }

log_parkour := class(log_channel){}

# This is a Verse-authored creative device that can be placed in a level
# This script example is a take on Parkour where the objective is to gather 4 batteries before the timer expires
#

```

Copy full snippet(40 lines long)
The script above shows how to use @editable to expose Creative Devices, arrays, and floatsto UEFN. For your script to call on them later, the devices must first be defined in Verse.
Verse
```

| # Messages to display when a battery is collected

---|---

|     BatteryCollectedMessage<localizes>(Amount:int) : message = "You collected {Amount} battery"

|     BatteriesCollectedMessage<localizes>(Amount:int) : message = "You collected {Amount} batteries"

|

|     # Messages for collecting the secret battery and the completion message

|     AllBatteriesCollectedMessage<localizes> : message = "You collected all of the batteries!"

|     SecretBatteryCollectedMessage<localizes> : message = "You collected the secret battery, additional time added!"

```

# Messages to display when a battery is collected BatteryCollectedMessage<localizes>(Amount:int) : message = "You collected {Amount} battery" BatteriesCollectedMessage<localizes>(Amount:int) : message = "You collected {Amount} batteries" # Messages for collecting the secret battery and the completion message AllBatteriesCollectedMessage<localizes> : message = "You collected all of the batteries!" SecretBatteryCollectedMessage<localizes> : message = "You collected the secret battery, additional time added!"
Copy full snippet(7 lines long)
The script above shows how to define a function that returns a parametrized message based on the Amount of batteries collected. It also defines the messages to show when all batteries and the secret one are collected.
Verse
```
    # Runs when this device_script is started in a running game
    OnBegin<override>()<suspends>:void=
        # You can output to the log like this to determine what your script is up to
        Logger.Print("Parkour Race Script Started!")

        # Subscribing to the AgentSpawnedEvent.
        # When the player spawns, the function "HandleAgentSpawned" is called.
        PlayerSpawnDevice.SpawnedEvent.Subscribe(HandleAgentSpawned)
        # Same for the Timer. We subscribe to when it expires
        TimerDevice.FailureEvent.Subscribe(HandleTimerExpired)

```

Copy full snippet(23 lines long)
The OnBegin function defines what happens when the game starts while the for loop to the event of picked-up batteries.
Verse
```

|  # A function that is called when the Agent Spawns from the Player Spawn Pad

---|---

|     HandleAgentSpawned(Agent:agent):void=

|         Logger.Print("Agent Spawned!")

|         # Reset the Timer Device to ensure respawning players get the full amount of time

|         TimerDevice.Reset(Agent)

|         TimerDevice.Start(Agent)

```

# A function that is called when the Agent Spawns from the Player Spawn Pad HandleAgentSpawned(Agent:agent):void= Logger.Print("Agent Spawned!") # Reset the Timer Device to ensure respawning players get the full amount of time TimerDevice.Reset(Agent) TimerDevice.Start(Agent)
Copy full snippet(6 lines long)
Above is the code for when the player spawns that resets the timer and starts it over.
Verse
```
    # Function that is called when a battery item is picked up from the Item Spawners
    HandleBatteryPickedUp(Agent:agent):void=
        # Increment the number of batteries collected
        set BatteriesCollected = BatteriesCollected + 1
        # This is how you can output the number of batteries to the log. Useful for debugging
        Logger.Print("Number of batteries picked up: {BatteriesCollected}")

        # Check to see if there are enough batteries collected to the end the game
        if:
            BatteriesCollected >= BatteryItemSpawners.Length

```

Copy full snippet(32 lines long)
Above is the code that handles a battery being picked up. If all of the batteries have been picked up, the EndGame method is called. If not, HUD messages are displayed for players and the next battery is spawned.
Verse
```

|     HandleSecretBatteryPickedUp(Agent:agent):void=

---|---

|         Logger.Print("Picked up secret battery")

|         # Get the time remaining so we can add additional time to it

|         var TimeRemaining:float = TimerDevice.GetActiveDuration( Agent )

|         var TimeToAdd:float = (TimeRemaining + SecretBatteryTimeReward)

|         # Add additional time to the Timer Device, but don't go over the initial starting time

|         TimerDevice.SetActiveDuration(Min(TimeToAdd, TimerDevice.GetMaxDuration()), Agent )

|

|         HUDMessageBattery.SetText(SecretBatteryCollectedMessage)

|         HUDMessageBattery.Show(Agent)

```

HandleSecretBatteryPickedUp(Agent:agent):void= Logger.Print("Picked up secret battery") # Get the time remaining so we can add additional time to it var TimeRemaining:float = TimerDevice.GetActiveDuration( Agent ) var TimeToAdd:float = (TimeRemaining + SecretBatteryTimeReward) # Add additional time to the Timer Device, but don't go over the initial starting time TimerDevice.SetActiveDuration(Min(TimeToAdd, TimerDevice.GetMaxDuration()), Agent ) HUDMessageBattery.SetText(SecretBatteryCollectedMessage) HUDMessageBattery.Show(Agent)
Copy full snippet(10 lines long)
Above is the code that adds time to the Timer device when the secret battery is picked up. It is set to not go over the Timer device’s starting time of 30 seconds. This code also displays an on-screen message.
Verse
```
    # Function that is called when the timer expires
    HandleTimerExpired(MaybeAgent:?agent):void=
        Logger.Print("Timer Ended")

        if (Agent := MaybeAgent?):
            Agent

            # Eliminate the player
            if:
                FortCharacter:fort_character = Agent.GetFortCharacter[]

```

Copy full snippet(12 lines long)
Above is the code that eliminates the player when time runs out. The player is then respawned and the timer is reset in the HandleAgentSpawned method.
Verse
```
    # Asynchronous function that handles the end of the game
    EndGame(Agent:agent)<suspends>:void=
        HUDMessageBattery.SetText(AllBatteriesCollectedMessage)
        HUDMessageBattery.Show(Agent)
        # Wait for three seconds before ending the game
        Sleep(3.0)
        EndGameVictoryDevice.Activate(Agent)

    # Runs when this device_script is stopped or the game ends

```

Copy full snippet(12 lines long)
Above is the code that ends the game. Using Sleep(3.0) is an example of using an [asynchronous](https://dev.epicgames.com/documentation/fortnite/verse-glossary#async) method.
###  Setting up the Verse Device
[![Verse Device](https://dev.epicgames.com/community/api/documentation/image/43c67da5-552c-43cc-84f9-3392655802d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43c67da5-552c-43cc-84f9-3392655802d0?resizing_type=fit)
Compile your Verse script then find your device in the **Content Drawer**. Drag the Verse device onto an unseen area of your map to customize the settings.
[![Verse Details Panel](https://dev.epicgames.com/community/api/documentation/image/ff3fb803-d5fd-4048-91ba-fad02b272bbc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff3fb803-d5fd-4048-91ba-fad02b272bbc?resizing_type=fit)
In the device’s **Details** panel, configure the settings to match each referenced device like the photo above.
To set up this device, configure the **User Options** as follows:
Option  |  Value  |  Explanation
---|---|---
**PlayerSpawnDevice** |  Player Spawn Pad |  Select this option from the drop down box to reference devices.
**EndGameVictoryDevice** |  End Game Victory Device |  Select this option from the drop down box to reference devices.
**TimerDevice** |  Timer |  Select this option from the drop down box to reference devices.
**HUDMessageBattery** |  HUD Message Device Battery |  Select this option from the drop down box to reference devices.
**PlayerSpawnDevice** |  Player Spawn Pad |  Select this option from the drop down box to reference devices.
**BatteryItemSpawners - 0** |  Battery Spawner 1 |  Select this option from the drop down box to reference devices.
**BatteryItemSpawners - 1** |  Battery Spawner 2 |  Select this option from the drop down box to reference devices.
**BatteryItemSpawners - 2** |  Battery Spawner 3 |  Select this option from the drop down box to reference devices.
**BatteryItemSpawners - 3** |  Battery Spawner 4 |  Select this option from the drop down box to reference devices.
**SecretBatteryItemSpawner** |  Battery Spawner - Secret |  Select this option from the drop down box to reference devices.
**SecretBatteryTimeReward** |  10.0 |  The time reward for collecting the secret battery.
Select **Launch Session** to test out your completed level.
