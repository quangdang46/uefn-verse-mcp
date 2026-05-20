## https://dev.epicgames.com/documentation/en-us/fortnite/end-of-round-team-swapping-in-fortnite-creative

# End of Round Team Swapping

Swap a player's team at the end of each round to create extra challenge!

![End of Round Team Swapping](https://dev.epicgames.com/community/api/documentation/image/4349d6a7-8bb3-4283-b678-e5ec11703bcf?resizing_type=fill&width=1920&height=335)

A player spawns onto your island, a creature comes running toward them. The player must protect themselves from the beast. With every victorious round, they will spawn onto a new team with a new weapon to try and successfully defend themselves against the creature’s attack.

The primary goal of the **End of Round Team Swapping** a gameplay example is to switch the player to a new team at the beginning of each round. In this example, the player eliminates a creature, which results in the end of the round and changes the player's team affiliation.

From this gameplay example you will learn how to create team swapping through customizing the Team Settings & Inventory trap device, [Round Settings devices](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) and [Creature Placer devices](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#creature-placer).

## Devices Used

To learn more about placing [devices](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#device), [props](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prop), and using the [grid](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#grid), see the [Video Tutorials](https://www.epicgames.com/fortnite/en-US/creative/docs/fortnite-creative-video-tutorials).

For this example, you will need:

- **4 x** [Player Spawn Pad devices](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- **4 x** [Creature Placer devices](using-creature-placer-devices-in-fortnite-creative)
- **4 x** [Round Settings devices](using-round-settings-devices-in-fortnite-creative)

## Traps Used

- **4 x** [Team Settings & Inventory devices](using-team-settings-and-inventory-devices-in-fortnite-creative)

## Placing Trap Devices

1. Press **Tab** to go into the [Creative Inventory](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).
2. Click **Devices > Team Settings & Inventory >** [Equip](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#equip) to add five Team Settings & Inventory devices to your [Quick Bar](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#quick-bar).
3. Press **Y** to place the first **Team Settings & Inventory device**.

   [![Placing the Team Settings & Inventory device trap](https://dev.epicgames.com/community/api/documentation/image/27908c47-51ed-47a6-91e4-a66367ea5204?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27908c47-51ed-47a6-91e4-a66367ea5204?resizing_type=fit)
4. Repeat the step above to place 3 more device traps. These devices determine the team and weapon for players during the game.
5. Edit the first **Team Settings & Inventory device** options to the following:

   [![Edit the Team Settings & Inventory device options](https://dev.epicgames.com/community/api/documentation/image/db94db65-c071-4c08-b73d-3c7de9371a65?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db94db65-c071-4c08-b73d-3c7de9371a65?resizing_type=fit)

   *Click image to enlarge.*

   | Option | Value | Explanation** |
   | --- | --- | --- |
   | **Team Name** | **Team 1** | Can provide any name you want to distinguish Team 1 from another team. |
   | **Team** | **TEAM 1** | This name will be recognized by the first Trigger device to distinguish which team can trigger the device. |
   | **Team Color** | **White** | Sets the team’s color for the device and the scoreboard. |
   | **Equip Granted Item** | **First Item** | Grants the first item available to the player. |
   | **Infinite Ammo** | **On** | Gives unlimited ammo to the player. |
   | **End Round When Receiving From** | **Channel 3** | When the creature is eliminated, it sends a signal to the Teams Settings & Inventory device and the signal ends the round. |
6. Edit the **Team Number** for each additional trap device to **Team 2**, **Team 3** and **Team 4**.
7. Edit **End Round When Receiving From** options for each additional trap devices to **Channel 6**, **Channel 9**, and **Channel 12**.
8. Add a weapon to the first device by standing on the trap device then clicking **Tab** to enter the Creative Inventory again.
9. Select **Weapons Tab > Rare Automatic Pistol > Equip**. The weapon appears in the [Quick Bar](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#quick-bar).
10. Left-click and drag the weapon from the **Quick Bar** until a [backpack icon](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#backpack-icon) appears, then release.

    [![Selecting weapons for the Team Settings & Inventory devices](https://dev.epicgames.com/community/api/documentation/image/295da68d-e668-4260-8b82-ff36b94ace89?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/295da68d-e668-4260-8b82-ff36b94ace89?resizing_type=fit)

    *Click image to enlarge.*
11. Repeat the above steps to add weapons to each Team Settings & Inventory device.

    In this example the Rare Automatic Pistol, Rare Submachine Gun, Epic MK-Seven Assault Rifle, and Legendary Combat SMG are provided to the different teams, but you can use any weapons you want for your teams.

## Instructions

Any options not mentioned in the instructions below should be left at their default values.

### Placing the Player Spawn Pads

1. Press **Tab** to go into the **Creative Inventory**.
2. Click **Devices > Creature Placer device** to add the Player Spawn Pad to your **Quick Bar**. Continue to add the following devices from the device menu:
3. Click **Place Now** Once all the devices are added to your Quick Bar, this takes you back onto the island and puts you into Create mode.
4. Place the first **Player Spawn Pad**.

   [![Place the first Player Spawn Pad](https://dev.epicgames.com/community/api/documentation/image/8112300a-23e4-4ddd-93d6-cf0d673bd95c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8112300a-23e4-4ddd-93d6-cf0d673bd95c?resizing_type=fit)
5. Edit the first Player Spawn Pad options to the following:

   [![Edit the first Player Spawn Pad options](https://dev.epicgames.com/community/api/documentation/image/442e87e7-808b-4cde-8b00-a2b208e54775?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/442e87e7-808b-4cde-8b00-a2b208e54775?resizing_type=fit)

   *Click image to enlarge.*

   | Option | Value | Explanation |
   | --- | --- | --- |
   | **Team** | **Team 1** | Sets the Player Spawn pad for Team 1. |
   | **Visible During Games** | **No** | Makes the Player Spawn pad invisible during the game. |
   | **When Player Spawns Transmit On** | **Channel 1** | When the player spawns into the game, a signal is sent to the Round Settings device. |
6. Copy and paste four more Player Spawn Pads beside the first and edit their transmission options to **Channel 4**, **Channel 7**, and **Channel 10**.

### Placing the Round Settings Device

### Placing Creature Placer Devices

## My Island Options

To enable team swapping at the start of each round you need to edit the Game options of your island.

### Game Options

Edit the following options under the **Game tab**.

[![Edit the Game options under My Island](https://dev.epicgames.com/community/api/documentation/image/5f78494f-9781-46ad-b630-288db70e5e51?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5f78494f-9781-46ad-b630-288db70e5e51?resizing_type=fit)

*Click image to enlarge.*

| Options | Value | Explanation |
| --- | --- | --- |
| **Teams** | **4** | Sets the number of teams in the game. |
| **Total Rounds** | **4** | Determines how many rounds are in the game. |
| **Team Rotation** | **Every Round** | Rotates the player to a different team at the beginning of a new round. |

## Playing Your Game

After building this game experience you should understand how to create rounds in your games and how to create and swap teams every round. You can use the Round Settings device to create rewards for teams during rounds and even edit a team’s inventory at the end of a round.

You can use [**Class Designers**](using-class-designer-devices-in-fortnite-creative) and [**Class Selector**](using-class-selector-devices-in-fortnite-creative) in place of teams to use with the Round Settings device to increase a player’s class status as they meet certain objectives in a round.
