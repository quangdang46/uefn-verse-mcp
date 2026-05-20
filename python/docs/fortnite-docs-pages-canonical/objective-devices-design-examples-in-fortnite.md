## https://dev.epicgames.com/documentation/en-us/fortnite/objective-devices-design-examples-in-fortnite

# Objective Devices Design Examples

Explore ways you can set up distinct objectives in a game.

![Objective Devices Design Examples](https://dev.epicgames.com/community/api/documentation/image/801d0ba3-6c1d-4292-a7e7-4b14dedd441e?resizing_type=fill&width=1920&height=335)

You can use the Objective device to create objectives for a game that you can customize to fit your game mechanics. With this device, you can link team-based objectives to a distinct object that players can then destroy to reach the game objective.

[![](https://dev.epicgames.com/community/api/documentation/image/b5fa1eb7-12f0-465f-8fa5-84d1071279bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b5fa1eb7-12f0-465f-8fa5-84d1071279bc?resizing_type=fit)

## Example One: Basic Device Features

In this example, you will see how some basic features for this device work.

### Devices Used

- 1 x [Objective](https://dev.epicgames.com/documentation/fortnite/using-objective-devices-in-fortnite-creative) device
- 1 x [Button](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative) device

### Build Steps Overview

[![](https://dev.epicgames.com/community/api/documentation/image/a9ef9076-8fc9-4322-bb02-bb12a7520842?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9ef9076-8fc9-4322-bb02-bb12a7520842?resizing_type=fit)

### Instructions

The Objective device can be customized to fit into most island themes.

The image above shows all of the shapes available. These shapes can be changed by adjusting the mesh value in the device.

Choose a mesh and then proceed to the next step.

[![](https://dev.epicgames.com/community/api/documentation/image/fe67b51f-cf24-4707-818d-73d81ab827b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fe67b51f-cf24-4707-818d-73d81ab827b6?resizing_type=fit)

One powerful feature of the Objective device is your ability to control how it can be destroyed. You can choose to have the object take normal damage, or make it invulnerable to harm so that it can only be destroyed by an event sent from another device.

To configure the device to explode when an event is sent by another device, add a **Button** device to your island, then use the following settings on the Objective device:

[![](https://dev.epicgames.com/community/api/documentation/image/d08f66ae-8715-4ba7-8387-abbef6e9f0a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d08f66ae-8715-4ba7-8387-abbef6e9f0a2?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/3d1de007-a489-4248-925a-13cfedf9103b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d1de007-a489-4248-925a-13cfedf9103b?resizing_type=fit)

### Design Tip

Try adding Objective devices that score bonus points in the game mode you have created on your island!

## Example 2: Use More than One Objectives Device

[![](https://dev.epicgames.com/community/api/documentation/image/0635d6ce-6cf0-4b83-958e-b4ab29d34023?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0635d6ce-6cf0-4b83-958e-b4ab29d34023?resizing_type=fit)

In this example, you'll expand on the first example by making a big Objective device invulnerable until players have disabled a smaller Objective device.

### Devices Used

- 2 x Objective devices
- 1 x Button device

### Build Steps Overview

### Place the Button Device

Place a Button device and configure it with the following settings:

[![](https://dev.epicgames.com/community/api/documentation/image/a43cbd3f-8c24-4384-9a67-32c365d06ab0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a43cbd3f-8c24-4384-9a67-32c365d06ab0?resizing_type=fit)

### Place a Large Objective Device

Change the **Invulnerable** setting to **Off.**

Customize the **Health**  to **300**.

Adjust the following additional settings:

[![](https://dev.epicgames.com/community/api/documentation/image/6fbaaf83-c901-45f6-a628-7221f2f471d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6fbaaf83-c901-45f6-a628-7221f2f471d2?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/b13bc313-6a1c-44dc-8004-4dbdc8cebe20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b13bc313-6a1c-44dc-8004-4dbdc8cebe20?resizing_type=fit)

Once you have adjusted the Health values, turn the **Invulnerable** setting back **On.**

[![](https://dev.epicgames.com/community/api/documentation/image/56f01210-3dfa-42f4-9a6d-986143a98599?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56f01210-3dfa-42f4-9a6d-986143a98599?resizing_type=fit)

### Place a Small Objective Device

Change the **Invulnerable** setting to **Off,** then customize the **Health** to **100**.

Change the **Invulnerable** setting back to **On**.

Next, change the following settings on the device:

[![](https://dev.epicgames.com/community/api/documentation/image/5100746f-299e-4457-8b29-3e9ee801e496?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5100746f-299e-4457-8b29-3e9ee801e496?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/33419ab9-3743-4ed3-99c2-65c98aeafa4c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/33419ab9-3743-4ed3-99c2-65c98aeafa4c?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/c33c3eb6-7474-487a-a3b6-14f413872bac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c33c3eb6-7474-487a-a3b6-14f413872bac?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/c00568d9-4b42-44ff-b8f4-b4de0bda47e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c00568d9-4b42-44ff-b8f4-b4de0bda47e8?resizing_type=fit)

 Configure the events:

[![](https://dev.epicgames.com/community/api/documentation/image/afdea4d9-3980-4c87-9494-4c9dcd9deda3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/afdea4d9-3980-4c87-9494-4c9dcd9deda3?resizing_type=fit)

### Design Tip

Try linking events from other devices to make your Objective device destructible!

## Example 3: Create a Multiplayer Game

[![](https://dev.epicgames.com/community/api/documentation/image/18400186-3539-42ab-845d-1d072ad59c96?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/18400186-3539-42ab-845d-1d072ad59c96?resizing_type=fit)

In this example, you’ll create an asymmetrical multiplayer game mode for up to 10 players.

One team will attack a mall to destroy the **Pizza Pete Objective** device inside, while the other team will try to stop them!

### Devices Used

- 1 x Button device
- 1 x Objective device
- 1 x [End Game](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative) device
- 10 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) devices (2 teams of 5)
- 2 x Team Settings & Inventory devices
- 1 x [Air Vent](https://dev.epicgames.com/documentation/fortnite/using-air-vent-devices-in-fortnite-creative) device
- 10 [Item Spawner](https://dev.epicgames.com/documentation/fortnite/using-item-spawner-devices-in-fortnite-creative) devices

### Build Steps Overview

1. Place the **Mega Mall** prefab.
2. Build the **Cityscape Silhouette**.
3. Place **Player Spawners** for both teams.
4. Place the **Item Spawners**.
5. Place and configure the **Objective** device.
6. Place and configure the **End Game** device.
7. Configure the **game settings**.

### Place the Mega Mall Prefab

[![](https://dev.epicgames.com/community/api/documentation/image/c73fd472-39a3-47c9-a33a-24a975c739d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c73fd472-39a3-47c9-a33a-24a975c739d0?resizing_type=fit)

Start by placing the **Mega Mall** prefab from the **Retail Row Collection** in the center of your island.

[![](https://dev.epicgames.com/community/api/documentation/image/0fe9479d-9b35-41d6-921e-ea3dd869b33a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0fe9479d-9b35-41d6-921e-ea3dd869b33a?resizing_type=fit)

Next, copy a section of prefab wall and use copies to construct a wall around the entire mall.

Make sure that the wall is at least three squares high, and place the wall back far enough to provide ample room around the mall prefab.

[![](https://dev.epicgames.com/community/api/documentation/image/14a344ee-3126-4f00-bab1-7a023a2f9f35?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14a344ee-3126-4f00-bab1-7a023a2f9f35?resizing_type=fit)

### Build the Cityscape Silhouette

To achieve the look of a busy city setting at night, you can use prefabs from the **Mega CIt******y** C**ollect******ion** combined with black blocks and neon signs to create the illusion of a cityscape at night.

[![](https://dev.epicgames.com/community/api/documentation/image/86866ea2-0b46-48fc-aed9-5bd45b82a89c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86866ea2-0b46-48fc-aed9-5bd45b82a89c?resizing_type=fit)

Start by placing a few Mega City buildings around the outside of your retaining wall. You might not want to place them directly on the ground because you need as much of the outline of the building as possible to be visible from inside the retaining wall.

[![](https://dev.epicgames.com/community/api/documentation/image/bb26588f-c513-4b4f-8253-4a3fee89cfc9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb26588f-c513-4b4f-8253-4a3fee89cfc9?resizing_type=fit)

This is the same building prefab as seen from the ground outside the retaining wall. Note that it is not sitting on the ground, but is floating up in the air so that players inside the play space can see as much of the building as possible.

[![](https://dev.epicgames.com/community/api/documentation/image/8c266554-45f8-410a-9456-60193d22bf61?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c266554-45f8-410a-9456-60193d22bf61?resizing_type=fit)

The next important piece used in constructing your face city silhouette comes from the **Primitive Shapes Gallery B** objects.

Pick the big cube, and scale it to make it as tall and as long as possible in one direction.

Change the color of the object to black marble.

[![](https://dev.epicgames.com/community/api/documentation/image/3d806735-f66e-43b5-aa2b-eb586da202a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d806735-f66e-43b5-aa2b-eb586da202a7?resizing_type=fit)

Use these blocks to fill in the spaces around the prefab buildings, placing them around as though they were smaller buildings at the foot of the larger prefab towers.

[![](https://dev.epicgames.com/community/api/documentation/image/acb70de3-9220-4185-b769-f619cd2981e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/acb70de3-9220-4185-b769-f619cd2981e2?resizing_type=fit)

As you place the blocks, be sure to check how they look from inside the wall that encloses the play space. Ensure that there are no obvious gaps.

[![](https://dev.epicgames.com/community/api/documentation/image/48cfd589-2809-4ece-90ea-0db9aaf5b69a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48cfd589-2809-4ece-90ea-0db9aaf5b69a?resizing_type=fit)

Place the **Mega City Sign Gallery** and choose a few signs to place on empty sections of the black blocks. This will help them look like the silhouettes of stores and restaurants in the dark.

[![](https://dev.epicgames.com/community/api/documentation/image/a46a4152-2697-4ac5-a4ab-5c1c630a1c86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a46a4152-2697-4ac5-a4ab-5c1c630a1c86?resizing_type=fit)

### Place the Player Spawners

Place **Spawner Spawner** devices for both teams. Set the spawners for **Team 1** outside the mall building on the far side of the pizza restaurant.

[![](https://dev.epicgames.com/community/api/documentation/image/e8b72bff-3c63-4ead-bda1-42a6ba355788?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8b72bff-3c63-4ead-bda1-42a6ba355788?resizing_type=fit)

Configure the settings on the first Spawner device and then copy it for the rest of the team spawn locations.

[![](https://dev.epicgames.com/community/api/documentation/image/f191e36c-b800-4f2f-bda4-50e82045097b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f191e36c-b800-4f2f-bda4-50e82045097b?resizing_type=fit)

Configure a Player Spawner device for **Team 2** using the following settings:

[![](https://dev.epicgames.com/community/api/documentation/image/aaef3f53-2129-4422-8191-6a092bc7e6d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aaef3f53-2129-4422-8191-6a092bc7e6d8?resizing_type=fit)

Copy and place the Team 2 starting locations inside the mall:

[![](https://dev.epicgames.com/community/api/documentation/image/603d2a7c-f734-41ef-b4fb-0e08c149c81d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/603d2a7c-f734-41ef-b4fb-0e08c149c81d?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/bb914c9d-fc78-4235-a085-017edde8ea26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb914c9d-fc78-4235-a085-017edde8ea26?resizing_type=fit)

### Place the Item Spawners

To create variety in the game, place Item Spawners around the map where the teams will have easy access to them.

[![](https://dev.epicgames.com/community/api/documentation/image/86614420-4364-418d-9306-b280bb53dfc5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86614420-4364-418d-9306-b280bb53dfc5?resizing_type=fit)

Place whatever weapons you want in the Item Spawner device, and configure it with the following settings:

[![](https://dev.epicgames.com/community/api/documentation/image/ca2be211-6129-4b70-9561-0c8aa432975c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca2be211-6129-4b70-9561-0c8aa432975c?resizing_type=fit)

Copy the Item Spawners to locations close to the starting devices for both teams.

### Place the Large Objective Device

Use the same process of configuring the Objective devices in the game mode that you used in the second example above.

[![](https://dev.epicgames.com/community/api/documentation/image/e180febc-d9a6-40bd-ba87-ac5f8599729c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e180febc-d9a6-40bd-ba87-ac5f8599729c?resizing_type=fit)

Place the large objective device close to the hovering sign over the mall prefab.

Change the **Invulnerable** setting to **Off**, then customize the **Health** to **300**.

Adjust the following additional settings:

[![](https://dev.epicgames.com/community/api/documentation/image/8b81ddec-50bd-4115-aea6-c38ca4f6c51b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8b81ddec-50bd-4115-aea6-c38ca4f6c51b?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/92a11eeb-61de-4854-9131-0726c3e6514c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/92a11eeb-61de-4854-9131-0726c3e6514c?resizing_type=fit)

Once you have adjusted the Health values, turn the **Invulnerable** setting back **On**.

[![](https://dev.epicgames.com/community/api/documentation/image/c416fcaf-c429-45f7-abaf-06d0b78e2c57?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c416fcaf-c429-45f7-abaf-06d0b78e2c57?resizing_type=fit)

### Place the Small Objective Device

Place a small Objective device elsewhere in the mall. In this example, the device was placed in the small room adjoining the main room of the pizza restaurant.

Change the **Invulnerable** setting to **Off**, then customize the **Health** to **100**.

Change the **Invulnerable** setting back to **On**.

Change the following settings:

[![](https://dev.epicgames.com/community/api/documentation/image/74972e6d-2903-48b6-98e9-9d9d64260004?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/74972e6d-2903-48b6-98e9-9d9d64260004?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/318831d2-e742-4055-afb7-ee7177645ad5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/318831d2-e742-4055-afb7-ee7177645ad5?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/6cd0ca09-112a-466a-a6f6-cb5e4710fdc1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cd0ca09-112a-466a-a6f6-cb5e4710fdc1?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/fe2b37ff-86ae-4461-a154-36408267c0e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fe2b37ff-86ae-4461-a154-36408267c0e2?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/2a5d117b-a376-424b-8a60-d6d592718f08?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2a5d117b-a376-424b-8a60-d6d592718f08?resizing_type=fit)

 Configure the device events:

[![](https://dev.epicgames.com/community/api/documentation/image/72a30b02-e29e-4c8f-99d3-52b0b8b9546f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/72a30b02-e29e-4c8f-99d3-52b0b8b9546f?resizing_type=fit)

### Place and Configure the End Game Device

Place the **End Game** device on the island.

[![](https://dev.epicgames.com/community/api/documentation/image/30a3ca15-2f20-4d24-8c17-8eeb89764ed9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30a3ca15-2f20-4d24-8c17-8eeb89764ed9?resizing_type=fit)

Configure it with the following settings:

[![](https://dev.epicgames.com/community/api/documentation/image/c8f00753-e620-4681-87fa-16bca5288c2a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c8f00753-e620-4681-87fa-16bca5288c2a?resizing_type=fit)

### Adjust the Game and World Settings

Configure the **Game mode** using the following settings:

[![](https://dev.epicgames.com/community/api/documentation/image/7721335c-5a4c-49fe-9639-b578e2bdd23b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7721335c-5a4c-49fe-9639-b578e2bdd23b?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/5e2c27e1-035f-48c8-9127-09b2a9487e2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e2c27e1-035f-48c8-9127-09b2a9487e2c?resizing_type=fit)

Finally, change the **World Ambiance Time of Day** setting to **11:00 PM** to create the effect of a city skyline at night.

[![](https://dev.epicgames.com/community/api/documentation/image/dd3f0316-59d2-4eb7-975c-e66d118b84c9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd3f0316-59d2-4eb7-975c-e66d118b84c9?resizing_type=fit)

### Design Tip

You could adjust the number of Player Spawners to control the number of players in the game, or change the Item Spawners to create all sorts of interesting game variations.
