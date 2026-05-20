## https://dev.epicgames.com/documentation/en-us/fortnite/mazey-escape-in-fortnite-creative

# Mazey Escape

Create a maze that demonstrates the different ways devices signal each other.

![Mazey Escape](https://dev.epicgames.com/community/api/documentation/image/9766ea1d-cf2f-4658-a61f-4d6ce5eaec09?resizing_type=fill&width=1920&height=335)

[![Mazey Escape Gameplay Example](https://dev.epicgames.com/community/api/documentation/image/270c65b2-908f-448f-b3d0-8056321f3315?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/270c65b2-908f-448f-b3d0-8056321f3315?resizing_type=fit)

This example demonstrates the use of Perception Triggers to activate various devices placed in a maze.

*Mazey Escape Video*

## Ingredients

**You Need:**

- **4 Item Spawner devices**
- **1 Item Granter device**
- **2 Conditional Button devices**
- **2 Lock Devices**
- **9 Perception Trigger devices**
- **1 Trigger device**

## Method

The player must acquire torches scattered all over the maze to unlock doors that finally lead to the exit. Not all the torches are visible. The only way to get them is to explore every corner of the maze.

- There are 2 sections in the maze, separated by a locked door.
- To get out of the first section, the player must find 4 torches.
- In the second section, the player must also find 4 torches to unlock the door to leave the maze.
- Perception Triggers are scattered all over the maze. But not all of them are enabled at the same time. The player will have to run around the maze in a specific order to activate the triggers, collect the torches, and finally unlock the doors.

### Item Spawner Device Options

In this example, two Item Spawners are placed in each section of the maze. Follow these steps for all four of them.

1. Drop a Torch onto the Item Spawners to register it.
2. Set the **Items Respawn option** to **Off**. We want the Torches to spawn only once.
3. Set the **Time between spawns** option to **Never**.
4. Set the **Run over pickup** option to **On**.
5. Set the **Enabled At Game Start** option to **No.** We want the Item Spawners to be enabled by the activation of specific Perception Triggers.
6. The four Item Spawners are enabled by different channels. Set the **Enable When Receiving From** option to these channel numbers.

### Item Granter Device Options

The Item Granter is placed outside of the play area. It is set up to remotely award the player a torch when activated by a Perception Trigger. To set up the Item Granter, follow the steps below.

### Conditional Button Device Options

The Conditional Button signals the Lock Device to unlock the door. To activate the Conditional Button, the player must possess four torches and the Conditional Buttons must also be enabled. Follow these steps for both Conditional Buttons.

### Lock Device Device Options

The Lock Device is set up to lock the doors for each section by default. They are unlocked only when the Conditional Buttons tell them to do so. Set up the two Lock Devices using the steps below.

### Perception Triggers Device Options

In this example, a variety of configurations are used to demonstrate the various forms of signalling between the 9 Perception Triggers and other devices.

**Device 1**: This device awards the player a torch when the player looks at the device, and awards the player a torch when the player looks away from the device. Follow these steps to set up the first device.

**Device 2**: This device activates the Item Spawner next to it when the device sees the player. It enables the third Perception Trigger when the device loses sight of the player. Follow these steps to set up Device 2.

**Device 3**: This enables the fourth Perception Trigger when it sees a player. Follow these steps to set up Device 3.

**Device 4**: This device activates the Item Spawner next to it when the device sees the player. It enables the first Conditional Button when the device loses sight of the player. Follow these steps to set up Device 4.

**Device 5**: This device is enabled when the Conditional Button is activated. When the player looks at this device, it enables the next device. Follow these steps to set up Device 5.

**Device 6**: This activates the Item Spawner next to it when the device sees the player. It enables the seventh and eighth Perception Triggers when the device loses sight of the player. Follow these steps to set up Device 6.

**Device 7**: This awards the player a torch when the player looks at the device. Follow these steps to set up Device 7.

**Device 8**: This activates the Item Spawner next to it when the device sees the player. It enables the ninth Perception Trigger and the second Conditional Button when the device loses sight of the player. Follow these steps to set up Device 8.

**Device 9**: This awards the player a torch when the player looks at the device. Follow these steps to set up Device 9.

### Trigger Device Options

The Trigger is placed right after the 2nd door. It simply ends the game when the player walks out of the door and steps over it. Be sure to also place a Team & Inventory Setting device outside the play area to receive this signal to end the game.
