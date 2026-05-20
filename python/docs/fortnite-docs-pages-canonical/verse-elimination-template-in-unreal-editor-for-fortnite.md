## https://dev.epicgames.com/documentation/en-us/fortnite/verse-elimination-template-in-unreal-editor-for-fortnite

# Verse Elimination Template

Use Verse and the Item Granter device to create changing loadouts.

![Verse Elimination Template](https://dev.epicgames.com/community/api/documentation/image/760f999d-cbf5-4aff-98f1-ae74671daaf8?resizing_type=fill&width=1920&height=335)

In **Verse Elimination**, players will battle with a loadout that changes with each elimination. These mechanics are achieved by linking devices like the **Item Granter** device to the Verse device.

This advanced Verse template will show you the use of these Verse APIs:

- Map container type
- Arrays
- Fort_character EliminateEvent subscription

## Overview

## Creating a New Project and Setting up the Game

[![Island Settings](https://dev.epicgames.com/community/api/documentation/image/b3691159-d3aa-4606-b054-e1f3bc71c0df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3691159-d3aa-4606-b054-e1f3bc71c0df?resizing_type=fit)

| Option | Value | Explanation |
| --- | --- | --- |
| **Eliminated Player’s Items** | Keep | Players will respawn with their loadout. |
| **Allow Item Drop** | False | Players cannot drop items from their inventory during the game. |
| **Environment Destruction** | Off | The environment will not be destroyed during the game. |

## Setting up the Devices

This tutorial uses the following devices:

- ~ x [Item Granters](https://www.fortnite.com/en-US/creative/docs/using-item-granter-devices-in-fortnite-creative)
- 1 x [End Game Device](https://www.fortnite.com/fortnite/en-US/creative/docs/using-end-game-devices-in-fortnite-creative)
- ~ x [Player Spawn Pad](https://www.fortnite.com/fortnite/en-US/creative/docs/using-player-spawn-pad-devices-in-fortnite-creative)

### Item Granter Device

[![Item Granter](https://dev.epicgames.com/community/api/documentation/image/980ebab7-d5e7-4cdc-aac4-91567bdccd23?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/980ebab7-d5e7-4cdc-aac4-91567bdccd23?resizing_type=fit)

Use an **Item Granter** device to grant players weapons. After you connect the Item Granter to the Verse device using direct event binding, the Verse script can shuffle the weapon’s order and award them with each elimination.

You can use any number of Item Granters. As long as you link them in the Verse device array, the game will scale accordingly.

From the Content Drawer, navigate to **Fortnite** > **Devices** and drag the Item Granters onto your map.

To set up this device, configure the **User Options** as follows:

| Option | Value | Explanation |
| --- | --- | --- |
| **Item Definition** | pick a weapon | Select one unique weapon per Item Granter device. |

### End Game Device

[![End Game](https://dev.epicgames.com/community/api/documentation/image/2cc53498-e2a3-4102-bb8f-7e00e95af825?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2cc53498-e2a3-4102-bb8f-7e00e95af825?resizing_type=fit)

Use an **End Game** device to end the round once conditions are met. Once eliminations reach a certain threshold, the Verse script will activate this device to end the round.

Use the default settings for this device.

### Player Spawn Pad

[![Player Spawn Pad](https://dev.epicgames.com/community/api/documentation/image/cf2c8c84-18a3-4354-b83d-7aefbed26d88?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf2c8c84-18a3-4354-b83d-7aefbed26d88?resizing_type=fit)

You can use **Player Spawn Pads** to spawn players onto your map. Evenly spread the spawn pads throughout your map to make sure players don’t group spawn.

Use the default settings for this device.

### Adding the Verse Scripts

[Add the following Verse scripts](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite), starting by referencing devices with the [@editable](https://dev.epicgames.com/documentation/fortnite/editable-properties-in-verse) function.

You can copy the code in the order it’s written. Comments are added within the script for clarity.

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Characters }
using { /Fortnite.com/Game }
using { /Verse.org/Simulation }
using { /Verse.org/Simulation/Tags }
using { /Verse.org/Random }
using { /UnrealEngine.com/Temporary/Diagnostics }

elimination_game_device := class(creative_device):
```

The above code shows the variable definitions.

Verse

```
    OnBegin<override>()<suspends>:void=
        # Can use this variable to scale the number of eliminations needed based on how many item granters there are in the experience
        set NumberOfEliminationsToWin = WeaponItemGranters.Length
        Print("Number of Weapon Item Granters: {WeaponItemGranters.Length}")

        # Randomize the order in which the weapons are granted
        set WeaponItemGranters = Shuffle(WeaponItemGranters)

        # Get all the players in the experience
        AllPlayers := GetPlayspace().GetPlayers()
```

The code above shows the logic that sets the game rule of how many eliminations are needed to win. The order of the Item Granter’s array is shuffled.

Players are added to a map to keep track of both their progress and which item they should be granted next.

Verse

```
    # Event that handles when a player is eliminated
    OnPlayerEliminated(Result:elimination_result):void=
        Print("Player Eliminated")
        EliminatingCharacter := Result.EliminatingCharacter
        if (FortCharacter := EliminatingCharacter?):
            if (EliminatingAgent := FortCharacter.GetAgent[]):
                GrantNextWeapon(EliminatingAgent)
```

 # Event that handles when a player is eliminated
OnPlayerEliminated(Result:elimination_result):void=
Print("Player Eliminated")
EliminatingCharacter := Result.EliminatingCharacter
if (FortCharacter := EliminatingCharacter?):
if (EliminatingAgent := FortCharacter.GetAgent[]):
GrantNextWeapon(EliminatingAgent)

The code above is the event that happens when a player is eliminated. The eliminating player is granted the next gun.

Verse

```
    # Check if there is a winner for the game, if not then grant the next weapon
    GrantNextWeapon(Agent:agent):void=
        if (var CurrentItemNumber:int = AgentMap[Agent]):
            if (IsVictoryConditionMet(CurrentItemNumber) = true):
                EndGame(Agent) # Game has been won
            else: # Game is not over yet
                set CurrentItemNumber = CurrentItemNumber + 1
                if (ItemGranter := WeaponItemGranters[CurrentItemNumber - 1]):
                    ItemGranter.GrantItem(Agent)
```

The code above is the logic to determine both which gun to grant the eliminating player and if they are on the last gun to end the match.

Verse

```
    # Check if the victory condition has been met and return the the result
    IsVictoryConditionMet(EliminationNumber:int)<transacts>:logic=
        if:
            EliminationNumber = NumberOfEliminationsToWin
        then:
            return true
        else:
            return false
```

 # Check if the victory condition has been met and return the the result
IsVictoryConditionMet(EliminationNumber:int)<transacts>:logic=
if:
EliminationNumber = NumberOfEliminationsToWin
then:
return true
else:
return false

The code above is the logic to check if the victory condition has been met.

Verse

```
    EndGame(Agent:agent):void=
        EndGameDevice.Activate(Agent)
```

 EndGame(Agent:agent):void=
EndGameDevice.Activate(Agent)

The code above is the logic that shows the End Game device calling for the winning player.

## Setting Up the Verse Device

[![Verse Device](https://dev.epicgames.com/community/api/documentation/image/90486920-9dc8-48b6-8884-d55c6d5463d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/90486920-9dc8-48b6-8884-d55c6d5463d2?resizing_type=fit)

The Verse device controls ending the game and granting guns on elimination through an array of Item Granters connected using direct event binding.

Compile your Verse script then find your device in the **Content Drawer**. Drag the Verse device onto an unseen area of your map to customize the settings.

Use this device to link direct event binding to the needed devices so they can be referenced by the Verse script.

[![Verse Direct Event Binding](https://dev.epicgames.com/community/api/documentation/image/08cc132e-b74d-4b22-8ce5-d9e07adb03a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08cc132e-b74d-4b22-8ce5-d9e07adb03a0?resizing_type=fit)

In the device’s **Details** panel, configure the settings to match each referenced device like the photo above.

To set up this device, configure the **User Options** as follows:

| Option | Value | Explanation |
| --- | --- | --- |
| **EndGameDevice** | End Game Device | Links the Verse device to the End Game device. |
| **WeaponItemGranters - 0** | Item Granter | Links the Item Granter to the Verse device. |
| **WeaponItemGranters - 1** | Item Granter2 | Links the Item Granter to the Verse device. |
| **WeaponItemGranters - 2** | Item Granter3 | Links the Item Granter to the Verse device. |
| **WeaponItemGranters - 3** | Item Granter4 | Links the Item Granter to the Verse device. |

Select **Launch Session** to test out your completed level.
