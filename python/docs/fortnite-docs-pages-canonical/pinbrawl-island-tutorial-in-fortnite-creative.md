## https://dev.epicgames.com/documentation/en-us/fortnite/pinbrawl-island-tutorial-in-fortnite-creative

# PinBrawl Island Tutorial

Using pinballs, brawl your way to victory by collecting coin-granting orbs to purchase weapons and battle rivals.

![PinBrawl Island Tutorial](https://dev.epicgames.com/community/api/documentation/image/442a1201-3a92-494b-8ae9-e6024f05e305?resizing_type=fill&width=1920&height=335)

PinBrawl is not a solo game and is meant to be played with two to four players.

In this three-part tutorial, you will create an angled pinball stage along with a brawl arena and a pre-game lobby. Players will use the **Baller Device** to run over coins and collect as much gold as they can. This gold can be used to purchase weapons for the final brawl.

Players will start their gameplay in the pre-game lobby and learn the rules of the game while they wait. After the autostart, players will respawn on the pinball arena and automatically teleport into their Baller vehicles. They can then use the vehicle to collect as many coins as they can.

The pinball round will last for two minutes. After the round ends, players will be teleported out of their vehicles and into the brawl arena. In the brawl arena, players will rush to purchase weapons and then battle for victory.

The [island code](playing-games-in-fortnite-creative) for this tutorial is **5433-9518-6615**.

To play through this island, click **CHANGE** in the **Fortnite Lobby** screen. On the Discover screen, click the **Island Code tab** and enter the code for the Hoverboard Racing Island. Once you've seen all the gameplay features, you can explore this tutorial and recreate it on your own island.

## Devices Used

The following devices were used to create this gameplay:

- 8 x [Player Spawn Pad](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 4 x [Player Reference](using-player-reference-devices-in-fortnite-creative)
- 4 x [Baller Spawner](using-baller-spawner-devices-in-fortnite-creative)
- 20 x [Pinball Bumper](https://dev.epicgames.com/documentation/fortnite/using-pinball-bumper-devices-in-fortnite-creative)
- 20 x [Pinball Flipper](https://dev.epicgames.com/documentation/fortnite/using-pinball-flipper-devices-in-fortnite-creative)
- 50 x [Collectibles Gallery](using-collectible-object-devices-in-fortnite-creative)
- 4 x [Teleporter](using-teleporter-devices-in-fortnite-creative)
- 5 x [Barrier](using-barrier-devices-in-fortnite-creative)
- 1 x [Timed Objective](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)
- 5 x [Item Granter](using-item-granter-devices-in-fortnite-creative)
- 1 x [HUD Controller Device](using-hud-controller-devices-in-fortnite-creative)
- 2 x [HUD Message Device](using-hud-message-devices-in-fortnite-creative)
- 4 x [Vending Machine](https://dev.epicgames.com/documentation/fortnite/using-vending-machine-devices-in-fortnite-creative)
- 2 x [Item Spawner](using-item-spawner-devices-in-fortnite-creative)

## Props, Prefabs, and Galleries

A variety of props and Gallery items were used to design this island. When recreating this island, test your creativity by envisioning a theme while mixing and matching items from various categories.

Be sure to fill any open areas with appealing props and terrains like grass and trees.

## Overview of Tutorial Steps

1. Create a new island using a [starter island](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#starter-island).
2. Customize the island settings.
3. Setting up the pre-game lobby.
4. Setting up the pinball arena.
5. Setting up background devices.
6. Set up the brawl arena devices.
7. Set up the brawl devices.

## Create Your Island

To [build your island](https://mediaspace.unrealengine.com/media/Creating+an+Island/1_mi1aqt1y/208434573), use the following steps.

The portal will automatically load and teleport you into the island.

Be sure to check out our short [video tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials) to learn more about the beginning steps to create your island.

## Customize the Island Settings

You can increase the numbers for **Max Players** to add more players. If you increase the player size, you will have to also increase the size of the pinball arena. In addition, you will have to increase the number of **Player Spawn Pads**, **Baller Devices**, **Teleporters**, and **Vending Machines** to match.

To modify gameplay settings, press the **TAB** key. From the upper **MY ISLAND** tab, you can access the tabs GAME, SETTINGS and UI.

[![My Island Menus](https://dev.epicgames.com/community/api/documentation/image/357c4457-57a8-4cc9-88e3-154b7a38a63a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/357c4457-57a8-4cc9-88e3-154b7a38a63a?resizing_type=fit)

### My Island - Game

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Max Players** | 4 | Only four players can join the game. |
| **Spawn Limit** | 1 | Players can not respawn after elimination. |
| **Last Standing Ends Game** | On | Sets it so the last player standing wins the game. |
| **Autostart** | 60 Seconds | Sets the amount of time players will stay in the Pre-Game lobby. Only applies to Published islands. |
| **Game Start Countdown** | 10 Seconds | Sets the start countdown to 10 seconds. |
| **Vehicle Trick Score Multiplier** | 0.0 | Disables vehicle scores. |
| **Vehicle Impacts Damage Objects** | No | Disables the Baller Device from destroying structures. |
| **Vehicle Impacts Damage Vehicles** | No | Disables the Baller Devices from damaging each other. |

### My Island - Settings

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Infinite Ammo** | On | Players will not have to restock on ammo during gameplay. |
| **Infinite Resources** | Off | Players will only have the resources they collect during gameplay. |
| **Allow Building** | None | Disables players from building during gameplay. |
| **Building Can Destroy Environment** | No | Disables player-built structures from destroying the environment. |
| **Environment Damage** | Off | Disables players from destroying the environment. |
| **Allow Item Drop** | No | Players can not drop items from their inventories. |
| **Always Show Name Plates** | Always Hide | Player locations will be hidden during gameplay. |
| **Allow Manual Respawning** | No | Players can not respawn into the game. |
| **Show Wood Resource Count** | No | Wood resources will not be shown on the HUD. |
| **Show Stone Resource Count** | No | Stone resources will not be shown on the HUD. |
| **Show Metal Resource Count** | No | Metal resources will not be shown on the HUD. |
| **Show Gold Resource Count** | Yes | The player's Gold amount will be shown on the HUD. |

### My Island - UI

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Round Win Condition** | Time Alive | The last player alive wins the game. |

## Setting Up Pinball Devices

[![Pinball Arena Device Overview](https://dev.epicgames.com/community/api/documentation/image/b8f63215-68ab-42f8-979a-ba4148789fd2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8f63215-68ab-42f8-979a-ba4148789fd2?resizing_type=fit)

*Use the photo as a visual reference on device placement and creative possibilities.*

In this section, you will use the following devices:

- **Player Spawn Pad**
- **Baller Device**
- **Pinball Bumper**
- **Pinball Flipper**
- **Collectibles Gallery**
- **Barrier Device**

### Player Spawn Pad

Begin by placing and customizing the spawn pads for the pinball’s spawn area.

[![Player Spawn Pad](https://dev.epicgames.com/community/api/documentation/image/800aee67-3842-419e-8646-d3539fb22850?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/800aee67-3842-419e-8646-d3539fb22850?resizing_type=fit)

In the bottom right corner of the **My Island** tab, click **Channel Browser** to view used channels.

This step is important as it sets the device to send a signal to the baller vehicle that automatically pushes players into it. After the game countdown, players will automatically sit in the device.

### Baller Spawner

You will now place and customize the **Baller Spawner**.

[![Baller Device](https://dev.epicgames.com/community/api/documentation/image/be08e886-bca6-4e4b-8a0e-fe793e171d60?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be08e886-bca6-4e4b-8a0e-fe793e171d60?resizing_type=fit)

### Designer Tips

For **Assigns Driver When Receiving From**, each Baller spawner should have a channel number corresponding to its Player Spawn Pad’s **When Player Spawned Transmit On** option.

When a player spawns from the pad it will transmit a signal that will be sent to the receiving device, the Baller Spawner.

### Pinball Bumper

You will next locate and place the Pinball Bumper.

[![Pinball Bumper Device](https://dev.epicgames.com/community/api/documentation/image/391503f3-04f6-4b9b-8927-edab42c9bf2d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/391503f3-04f6-4b9b-8927-edab42c9bf2d?resizing_type=fit)

The pinball devices are set to have high knockbacks so players can be launched into the air and use their grappling tools to swing. There is no set amount of Pinball Bumpers to place.

### Pinball Flipper

You will now locate and place the Pinball Flipper.

[![Pinball Flipper Device](https://dev.epicgames.com/community/api/documentation/image/4d8e5d3a-64cc-4fd9-9970-ccf3ee29d3e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d8e5d3a-64cc-4fd9-9970-ccf3ee29d3e2?resizing_type=fit)

There is no set amount of Pinball Flippers to place. With both the Pinball Bumper and Flipper customized, use your phone tool to copy and paste both devices in a unique pattern to serve as an obstacle.

### Collectibles Gallery

Next, select the Collectibles Gallery devices that players will run over to collect for gold.

[![Collectibles Gallery](https://dev.epicgames.com/community/api/documentation/image/db800073-c027-46e0-9c14-059867db7afb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db800073-c027-46e0-9c14-059867db7afb?resizing_type=fit)

There is no set amount of collectible items to place.

### Designer Tips

For your pinball arena, try to create challenges for overachieving players. Reward these players with special items like status buff items or extra gold. Play around with props and items from the **Gallery** tab to offer these challenges.

[![Arena challenges](https://dev.epicgames.com/community/api/documentation/image/77fe6ec0-457a-4214-802d-cf7d66272ba0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/77fe6ec0-457a-4214-802d-cf7d66272ba0?resizing_type=fit)

In the photo above, rings from the **Galleries** tabs are used as a base for players to grapple as they aim for coins.

You can type **Ring Gallery A** in the **Galleries** search tab to use the pieces in this example.

### Barrier Devices

The last step in the pinbrawl area is to add the Barrier devices that will hold players in the pinbrawl arena.

[![Barrier Device](https://dev.epicgames.com/community/api/documentation/image/a55f1076-f8c5-40f2-97d2-0ce2595decdc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a55f1076-f8c5-40f2-97d2-0ce2595decdc?resizing_type=fit)

[![Completed Barrier Placement](https://dev.epicgames.com/community/api/documentation/image/3cc3a017-7c30-4f41-929a-70b2caae2701?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3cc3a017-7c30-4f41-929a-70b2caae2701?resizing_type=fit)

With these devices, players cannot fly off of the arena as they swing and boost with their vehicles.

### Designer Tips

Since players launch and fall from great heights, decorate the arena with a boundary to reassure players they wont fall off the arena.

It may be overwhelming for players to fall and launch at great heights with sky visuals. Assure players they won’t fall off the map by offering boundaries in the arena like in the photo below. They won't know there's a barrier device placed to keep them safe inside.

[![Arena Boundary](https://dev.epicgames.com/community/api/documentation/image/d4004f48-4a03-4907-91a7-4c278bc6057c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4004f48-4a03-4907-91a7-4c278bc6057c?resizing_type=fit)

Try adding colorful lights to your arena by using **Beacons** from the **Lights** category in the GALLERIES tab.

Especially if you placed **Music Blocks** as floor pieces when building the arena, use audio devices like **Radio** to play tunes throughout your arena. If you do, the radio will trigger visual effects with the music blocks.

## Setting Up Background Devices

You will use the following devices in this section:

- **Item Granter**
- **Gold (Item)**
- **Timed Objective**
- **Player Reference**
- **HUD Controller**

There are many background devices that drive gameplay. These devices should not be seen by players. Place these devices in a hidden area.

### Item Granter

Head to a spot underneath your pinball arena to set up the Item Granter that will grant players gold.

[![Item Granter](https://dev.epicgames.com/community/api/documentation/image/38d4463b-1b7b-4374-962a-a884a5cfb7f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38d4463b-1b7b-4374-962a-a884a5cfb7f4?resizing_type=fit)

Next, you will [register](https://mediaspace.unrealengine.com/media/RegisteringCraftingConsumablesinFortniteCreative/1_zpmj3v0g) gold to this device that wil be granted from triggering players.

[![Gold Consumable](https://dev.epicgames.com/community/api/documentation/image/1919a446-45d9-468b-8423-127025eb235c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1919a446-45d9-468b-8423-127025eb235c?resizing_type=fit)

[![Registering Gold to Item Granter](https://dev.epicgames.com/community/api/documentation/image/7b5c8538-5974-4a0c-94a4-5510e80b43aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7b5c8538-5974-4a0c-94a4-5510e80b43aa?resizing_type=fit)

### Designer Tips

If you have added challenges to your arena, reward the players who overachieve with status buffs like **Slurp Mushroom** and **Jelly Bean** that will aid their gameplay.

To do so repeat the steps above to offer as an aiding reward. You can use a new item from the Collectibles Gallery to represent the rewarding items.

Be sure to place new Item Granters on unused channels for the setting **Grant Items When Receiving From**. This channel should match the setting **When Item Picked Up Transmit On** for the Collectibles Gallery item that you chose.

### Timed Objective

Next, add the Timed Objective that will end the pinball round and transmit a signal that will push players to the brawl arena.

[![Timed Objective Device](https://dev.epicgames.com/community/api/documentation/image/891616a5-a569-4476-a655-47295e4c4f93?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/891616a5-a569-4476-a655-47295e4c4f93?resizing_type=fit)

Next, you will connect the Timed Objective device to the Player Reference. This will allow the Player Reference to activate and become the representing device for players.

### Designer Tips

Players are only able to directly send signals to devices through triggering, like pressing a button or standing on the device. Since players are not able transmit indirect signals during gameplay, the Player Reference device can serve as a spokesperson for the player and send the required signal onced triggered by another device.

### Player Reference

Select and place Player Reference devices that will represent each player.

[![Player Reference Device](https://dev.epicgames.com/community/api/documentation/image/5beb72e1-b310-43ea-b7af-41bef24742b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5beb72e1-b310-43ea-b7af-41bef24742b0?resizing_type=fit)

Step 4 is important for teleporting your players to the next area.

### HUD Controller Device

Next, select and place the HUD Controller device. This device will control which core pieces of information will show on the player’s screen.

By using this device, you can set it so only the information that’s relevant to your gameplay will show and hide information that’s not needed.

[![HUD Controller Device](https://dev.epicgames.com/community/api/documentation/image/b4a58c70-7302-4507-8b1d-8a20e87f465e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b4a58c70-7302-4507-8b1d-8a20e87f465e?resizing_type=fit)

## Setting Brawl Arena Devices

[![Brawl Room Device Overview](https://dev.epicgames.com/community/api/documentation/image/46c2f46a-6355-4d1a-afc2-d8e1cf7c081a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46c2f46a-6355-4d1a-afc2-d8e1cf7c081a?resizing_type=fit)

In this section, you will use the following devices:

- **Teleporter**
- **Vending Machine**

Start by selecting the teleporters that will connect to the Player Reference Pads. When triggered from the Timer, the Player Reference Device will send a signal to these teleports that will transfer players to various locations in your brawl arena.

### Teleporter

Start by equipping and placing the Teleporter.

[![Teleporter Device](https://dev.epicgames.com/community/api/documentation/image/9db7c0ca-b873-4023-8eef-14007f586ac8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9db7c0ca-b873-4023-8eef-14007f586ac8?resizing_type=fit)

### Vending Machine

Place the Vending Machine and select weapons to register them to the device.

[![Vending Machine Device](https://dev.epicgames.com/community/api/documentation/image/1539b7ce-7062-40a2-b2cc-14c25f0f103b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1539b7ce-7062-40a2-b2cc-14c25f0f103b?resizing_type=fit)

The Vending Machine should now rotate a display of each weapon with their corresponding gold cost.

You have now completed building and setting up the brawl arena. The last step is to set up the pre-game lobby where players will initially spawn during gameplay.

### Designer Tips

You can edit this step to use only one weapon per Vending Machine. This way, players can purchase weapons faster.

You could also use the [**Conditional Button**](using-conditional-button-devices-in-fortnite-creative) and Item Spawner instead of the Vending Machine. This pair of devices can be used for faster weapon granting as well.

You can also alter the required gold for each weapon to match the amount of gold granted per coin on your arena.

## Setting Up the Pre-Game Lobby

[![Pre-Game Devices Overview](https://dev.epicgames.com/community/api/documentation/image/3c65c3e4-7594-4b09-b100-726fece9fd7f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c65c3e4-7594-4b09-b100-726fece9fd7f?resizing_type=fit)

*This photo can be used as a visual reference on device placement and creative possibilities.*

You will use the following devices in this section:

- **Billboard**
- **Player Spawn Pad**

### Billboard Device

Begin by placing and customizing the billboard devices.

[![Billboard Device](https://dev.epicgames.com/community/api/documentation/image/de046455-bf49-4b99-a550-7abde3afabe2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de046455-bf49-4b99-a550-7abde3afabe2?resizing_type=fit)

Repeat steps 2 - 3 on the opposite wall.

### Designer Tips

Billboards are an excellent way for Creators to relay information to players as free-standing text. When placing billboards, you want to make sure your text is unobstructed and clear for players to easily read.

### Player Spawn Pads

Next you will place and customize the Player Spawn Pads.

[![Player Spawn Pad](https://dev.epicgames.com/community/api/documentation/image/149a01e0-8124-4c37-a7ee-fbb32d6180ed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/149a01e0-8124-4c37-a7ee-fbb32d6180ed?resizing_type=fit)

When players load into the game, they will be immediately introduced to the game rules you provided on the billboards. Effectively communicating game rules will allow for players to enjoy the gameplay with no frustrations.

### Designer Tips

When communicating game rules, be brief and specific with your text. Try to avoid displaying a long message on one billboard.

Add props from the **PreFabs** and **Galleries** tab to decorate your lobby with items that best fit your theme. Add devices like **Customizable Light** to lighten dark areas in your structures.

You have now completed the Pinbrawl Tutorial.
