## https://dev.epicgames.com/documentation/en-us/fortnite/accolades-device-gameplay-examples-in-fortnite-creative

# Accolades Device Gameplay Examples

Use the Accolades device to reward players with Battlepass XP.

![Accolades Device Gameplay Examples](https://dev.epicgames.com/community/api/documentation/image/44ae1752-6414-4529-9b50-13171d113ab7?resizing_type=fill&width=1920&height=335)

The goal of these gameplay examples is to demonstrate several uses for the [Accolades device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#accolades-device). After following these examples, creators will understand how to use the Accolades device with [Trackers](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#tracker), [Creature Managers](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#creature-manager), [HUD Messages](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary), and other devices to award players with [accolades](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) that will grant [Battle Pass](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#battle-pass) [XP](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#xp) (after the island is published and goes through [calibration](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#calibration)).

Unlike most gameplay examples here, this page contains multiple examples that all center on the Accolades device. There will be an [ingredients list](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#ingredients-list) and instructions for each separate example. You can use any or all of these methods on your island. If you experiment, you might even find other ways to use the Accolades device!

## Accolade for Eliminating a Specific Creature Type

For this example, the player will be awarded an accolade for eliminating four Ranged Ice [Fiends](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#fiend).

### Ingredients List

Below is a list of the devices used in this example. Locate the devices by pressing the **Tab** key to open the Creative menu and selecting the Devices category. For convenience, drag each device into your [Quick Bar](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#quick-bar) at the bottom of the inventory screen.

To learn more about placing props and using the grid, see the [Video Tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials).

**Devices**

- [Creature Spawner device](using-creature-spawner-devices-in-fortnite-creative): 1
- [Creature Manager device](using-creature-manager-devices-in-fortnite-creative): 1
- [Accolades device](using-accolades-devices-in-fortnite-creative): 1
- [Tracker device](using-tracker-devices-in-fortnite-creative): 1
- [HUD Message device](using-hud-message-devices-in-fortnite-creative): 1

### Instructions

Any options not mentioned in the instructions below should be left at their default values.

1. Set up the **Creature Spawner** device by customizing the options shown below. The accolade is for eliminating 4 Ranged Ice Fiend creatures, so you need to spawn that kind of creature for the player to fight.
2. Set up the **Creature Manager** device by customizing the options shown below. The Creature Manager will send a signal on Channel 25 when the player eliminates a Ranged Ice Fiend.
3. Set up the **Tracker** device by customizing the options shown below. The Tracker will keep a count of how many Ranged Ice Fiends are eliminated. Each time the Tracker receives a signal on Channel 25, it raises the count by one. When the Tracker count reaches 4, it completes and sends a signal on Channel 24.
4. Set up the **Accolades** device by customizing the options shown below. The Accolades device receives a signal from the Tracker on Channel 24, and awards the accolade to the player.
5. Set up the **HUD Message** device by customizing the options shown below. The Accolades device can be set up to send a message to the HUD Message device when an accolade is awarded. Then the HUD Message will display a message to tell the player the accolade was awarded.

### End Result

When you play through this gameplay example, after you eliminate 4 Ice Ranged Fiends you will see something similar to the image below.

[![Example 1 End Result](https://dev.epicgames.com/community/api/documentation/image/b38349b3-c580-427f-ac83-002dff4329ef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b38349b3-c580-427f-ac83-002dff4329ef?resizing_type=fit)

## Accolade for Team Eliminating Specific Creature Type

This is a more complicated version of the previous accolade. This accolade is awarded to a team that eliminates three creatures of a specific type during a round. For example, Team 1 must eliminate three Fiends before a round ends, for the whole team to be awarded the accolade.

### Ingredients List

Below is a list of the devices used in this example. Locate the devices by pressing **Tab** to open the **Creative inventory** and clicking the **Devices** tab. For convenience, drag each device into your Quick Bar at the bottom of the inventory screen.

To learn more about placing props and using the grid, see the [Video Tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials).

**Devices**

- [Creature Spawner device](using-creature-spawner-devices-in-fortnite-creative): 1
- [Creature Manager device](using-creature-manager-devices-in-fortnite-creative): 1
- [Accolades device](using-accolades-devices-in-fortnite-creative): 1
- [Tracker device](using-tracker-devices-in-fortnite-creative): 1
- [HUD Message device](using-hud-message-devices-in-fortnite-creative): 1

### Instructions

Any options not mentioned in the instructions below should be left at their default values.

1. Set up the **Creature Spawner** device by customizing the options shown below. The accolade is for the team to eliminate 3 Fiend creatures, so you need to spawn that kind of creature for the team to fight.
2. Set up the **Creature Manager** device by customizing the options shown below. The Creature Manager will send a signal on Channel 30 when a player eliminates a Fiend.
3. Set up the **Tracker** device by customizing the options shown below. The Tracker will keep a count of how many Fiends are eliminated by players on a team. Each time the Tracker receives a signal on Channel 30, it raises the count by one. When the Tracker count reaches 3, it completes and sends a signal on Channel 40.
4. Set up the **Accolades** device by customizing the options shown below. The Accolades device receives a signal from the Tracker on Channel 40, and awards the accolade to the team.
5. Setup the **HUD Message** device by customizing the options shown below. The Accolades device can be set up to send a message to the HUD Message device when an accolade is awarded. Then the HUD Message will display to tell the player the accolade was awarded.

### End Result

When you play through this gameplay example, after your team eliminates 3 Fiends you will see something similar to the image below.

[![Example 2 End Result](https://dev.epicgames.com/community/api/documentation/image/26928c67-e596-4a19-afa3-fd78a8c09099?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/26928c67-e596-4a19-afa3-fd78a8c09099?resizing_type=fit)

## Accolade for Eliminating Enemy Player

In this example, players are awarded an accolade for eliminating five enemy players, across multiple rounds.

### Ingredients List

Below is a list of the devices used in this example. Locate the devices by pressing **Tab** to open the **Creative inventory** and clicking the **Devices** tab. For convenience, drag each device into your Quick Bar at the bottom of the inventory screen.

To learn more about placing props and using the grid, see the [Video Tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials).

**Devices**

- [Accolades device](using-accolades-devices-in-fortnite-creative): 1
- [Tracker device](using-tracker-devices-in-fortnite-creative): 1
- [HUD Message device](using-hud-message-devices-in-fortnite-creative): 1

### Instructions

Any options not mentioned in the instructions below should be left at their default values.

1. Set up the **Tracker** device by customizing the options shown below. The Tracker will keep a count of eliminations performed by the player. Each time the player eliminates another player, the Tracker raises the count by one. When the Tracker count reaches 5, it completes and sends a signal on Channel 37.
2. Set up the **Accolades** device by customizing the options shown below. The Accolades device receives a signal from the Tracker on Channel 37, and awards the accolade to the player.
3. Set up the **HUD Message** device by customizing the options shown below. The Accolades device can be set up to send a message to the HUD Message device when an accolade is awarded. Then the HUD Message will display to tell the player the accolade was awarded.

### End Result

When you play through this gameplay example, after you eliminate 5 enemy players you will see the message "5 Enemies Eliminated" displayed on your screen.

## Accolade for Storm Phase Completed

This accolade awards an accolade as soon as a storm phase ends. All players who survive a storm phase will get the accolade.

### Ingredients List

Below is a list of the devices used in this example. Locate the devices by pressing **Tab** to open the **Creative inventory** and clicking the **Devices** tab. For convenience, drag each device into your Quick Bar at the bottom of the inventory screen.

To learn more about placing props and using the grid, see the [Video Tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials).

**Devices**

- [Advanced Storm Controller](using-advanced-storm-controller-devices-in-fortnite-creative): 1
- [Advanced Storm Beacon](https://dev.epicgames.com/documentation/fortnite/advanced-storm-beacon): 3
- [Accolades device](using-accolades-devices-in-fortnite-creative): 1
- [HUD Message device](using-hud-message-devices-in-fortnite-creative): 1

### Instructions

Any options not mentioned in the instructions below should be left at their default values.

1. Set up the **Advanced Storm Controller** by customizing the options as shown below. By default, the Advanced Storm Controller will generate a storm when the game starts. The Advanced Storm Controller is set up to send a signal on Channel 26 when a storm phase ends.
2. Next add the **Advanced Storm Beacons**. Set up the Advanced Storm Beacons by customizing the options as shown below. Each Advanced Storm Beacon adds a phase to the storm. On the sample island there are a total of three phases, and when each phase ends the controller sends a signal on Channel 26.
3. Add the **Accolades** device. Set up the Accolades device by customizing the options as shown below. When a storm phase ends, the Advanced Storm Controller sends a signal on Channel 26. The Accolades device receives a signal on Channel 26, and awards the accolade to the player.
4. Setup the **HUD Message** device by customizing the options shown below. The Accolades device can be set up to send a message to the HUD Message device when an accolade is awarded. In this case, all players who survive the storm phase will be awarded the accolade. Then the HUD Message will display to tell all surviving players that the accolade was awarded.

### End Result

When you play through this gameplay example, you will see something similar to the image below when a storm phase ends.

[![Example 4 End Result](https://dev.epicgames.com/community/api/documentation/image/f90f3aba-7b5a-42fe-a25b-79ccdb934d5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f90f3aba-7b5a-42fe-a25b-79ccdb934d5e?resizing_type=fit)

## Accolade for Opening Chests

In this example, when any player opens two chests in one round, the player is awarded an accolade.

### Ingredients List

Below is a list of the devices and props used in this example. Locate the devices by pressing **Tab** to open the **Creative inventory** and clicking the **Devices** tab. For convenience, drag each device into your Quick Bar at the bottom of the inventory screen.

To learn more about placing props and using the grid, see the [Video Tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials).

**Devices**

- [Tracker device](using-tracker-devices-in-fortnite-creative): 1
- [Accolades device](using-accolades-devices-in-fortnite-creative): 1
- [HUD Message device](using-hud-message-devices-in-fortnite-creative): 1

**Props**

- The **Chest and Ammo Gallery**
- Items to put in a chest (weapons, ammo, other items)

### Instructions

To create this gameplay example, you will need to create some chests for players to open. You can do this in two ways:

- You can use the **Chest and Ammo Gallery**. Place the Gallery, then pick up and place whichever chests you want to use. When a player opens the chest, a random selection of loot will drop from the chest.
- You can manually select items, weapons, or ammo in the Creative inventory. Once you have selected something you want to put in the chest, click the **Add to Chest** button below the Quick Bar. Add as many things as you want to the chest. Then click the **Chest** tab, and click the **Create Chest** button. This will create a wooden chest containing the specific items you selected. You can create multiple chests with the same list of items, or you can click **Remove** or **Reset** to change the contents of the chest.

Next you'll add the devices and customize their options.

Any options not mentioned in the instructions below should be left at their default values.

1. Set up the **Tracker** device by customizing the options shown below. The Tracker will keep a count of how many chests the player opens. Each time the player opens a chest, the Tracker raises the count by one. When the Tracker count reaches 2, it completes and sends a signal on Channel 32.
2. Set up the **Accolades** device by customizing the options shown below. The Accolades device receives a signal from the Tracker on Channel 32, and awards the accolade to the player.
3. Setup the **HUD Message** device by customizing the options shown below. The Accolades device can be set up to send a message to the HUD Message device when an accolade is awarded. Then the HUD Message will display to tell the player the accolade was awarded.

### End Result

When you play through this gameplay example, after you two chests you will see something similar to the image below.

[![Example 5 End Result](https://dev.epicgames.com/community/api/documentation/image/46ac28b5-30c0-4166-8b4a-150e3fca953f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46ac28b5-30c0-4166-8b4a-150e3fca953f?resizing_type=fit)

## Accolade for Timer Completed

In this example, when the timer reaches zero during a round the player is awarded an accolade.

### Ingredients List

Below is a list of the devices used in this example. Locate the devices by pressing **Tab** to open the **Creative inventory** and clicking the **Devices** tab. For convenience, drag each device into your Quick Bar at the bottom of the inventory screen.

To learn more about placing props and using the grid, see the [Video Tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials).

**Devices**

- [Timer device](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative): 1
- [Accolades device](using-accolades-devices-in-fortnite-creative): 1
- [HUD Message device](using-hud-message-devices-in-fortnite-creative): 1

### Instructions

Any options not mentioned in the instructions below should be left at their default values.

1. Set up the **Timer** device by customizing the options shown below. The Timer will start counting down when the game starts. By default, when the Timer finishes the countdown it registers a success. On success, it sends a signal on Channel 34, then the Timer is disabled. The Accolades device receives the signal on Channel 34 and awards the accolade. By default, the Timer applies to all players, so any players who are still active when the timer completes will receive the accolade.
2. Set up the **Accolades** device by customizing the options shown below. The Accolades device receives a signal from the Timer on Channel 34, and awards the accolade to the players who are still active.
3. Setup the **HUD Message** device by customizing the options shown below. The Accolades device can be set up to send a message to the HUD Message device when an accolade is awarded. Then the HUD Message will display to tell the player the accolade was awarded.

### End Result

When you play through this gameplay example, after you have survived a storm phase you will see something similar to the image below.

[![Example 6 End Result](https://dev.epicgames.com/community/api/documentation/image/d388b060-cb45-47a8-bf15-82628265263e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d388b060-cb45-47a8-bf15-82628265263e?resizing_type=fit)

## Conclusion

If you play through the example island, you can see how all of the above gameplay examples work together in a game. In the **Creative lobby**, click the **Discover** box to display the **Discover** screen. Click the **Island Code** tab, and enter **2034-7205-6925**. An information box for the island displays. Click **Play** to start playing the game!
