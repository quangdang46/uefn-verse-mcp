## https://dev.epicgames.com/documentation/en-us/fortnite/conversation-device-design-examples

# Conversation Device Design Examples

Want to add interactive conversations to your island? See several ways you use this powerful device in Fortnite!

![Conversation Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/a6db2942-55b3-4b39-ad9c-0ebad6e85f37?resizing_type=fill&width=1920&height=335)

The **Conversation device** is a tool you can use to create interactive conversations between players and NPCs during gameplay. Keep reading to see some creative ways to make the most of this device on your own island.

Because conversation trees cannot be built in Creative, you can only use a Conversation device with Unreal Editor for Fortnite (UEFN). For more on this device, see [Conversations](https://dev.epicgames.com/documentation/fortnite/conversations-in-unreal-editor-for-fortnite).

## Basic NPC Conversation

The Conversation device is perfect for livening up your characters by providing interactions with players. In this example, you’ll use the **Character** device with the **Conversation** device to make this happen.

This example starts in **Creative**, then moves into **UEFN**.

### Devices Used

- 1 x Conversation device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [Character](https://dev.epicgames.com/documentation/fortnite/using-character-devices-in-fortnite-creative) device

### Set Up the Devices

1. From Creative, place a **Player Spawner** device.
2. Place a **Character** device.
3. Place a **Conversation** device.
4. Customize the Conversation device as follows

   [![](https://dev.epicgames.com/community/api/documentation/image/da59642f-6078-4e8d-a420-16c456c9dd06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/da59642f-6078-4e8d-a420-16c456c9dd06?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Conversation Type | Box |
   | Button Text Color | White |
   | Speaker Name | Tomatohead |
   | Show Indicator Bubble | Of |
5. Customize the Character device as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/4d1606a0-4a46-43ff-8dc9-e4f9aa357ad6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d1606a0-4a46-43ff-8dc9-e4f9aa357ad6?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Character | Tomatohead |
   | Use Animated Idle | On |
   | Emote | Air Guitar |
   | Interact Type | Send Event Only |
   | Interaction Text | Tal |
6. Configure the following event on the Character device so that when the player interacts with the character, the conversation will begin.

   [![](https://dev.epicgames.com/community/api/documentation/image/b0255d6e-9d8f-464a-a93a-b55e49be2a41?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b0255d6e-9d8f-464a-a93a-b55e49be2a41?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Interacted With Send Event To | Conversation Device | Initiate Conversation |
7. Configure the following event on the Conversation device so that when triggered in the conversation, the character will play the emote.

   [![](https://dev.epicgames.com/community/api/documentation/image/6c00ff8a-666a-4fe7-9b73-e788867fdbbc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c00ff8a-666a-4fe7-9b73-e788867fdbbc?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Interacted With Send Event To | Conversation Device | Initiate Conversation |
8. In UEFN, create a **Conversation Bank** called **Conversation**.
9. Create the following conversation:|

   [![](https://dev.epicgames.com/community/api/documentation/image/22fd27b1-2678-41b1-ad4b-d9ef3edae707?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22fd27b1-2678-41b1-ad4b-d9ef3edae707?resizing_type=fit)
10. Customize the Conversation device as follows:

    [![](https://dev.epicgames.com/community/api/documentation/image/494b8489-47b3-4c99-8892-fbbacac06ea9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/494b8489-47b3-4c99-8892-fbbacac06ea9?resizing_type=fit)

    | Option |  |
    | --- | --- |
    | Conversation | Conversation |

You now have the functionality for a basic conversation with an NPC!

### Design Tip

As you’ll see in the following examples, the Conversation device can create branching conversations with unique responses for different player choices. Even a conversation as simple as this can be helpful in making your world feel more lively!

## Shop Conversation

The Conversation device is great at giving the player clear choices to make during gameplay! In this example, you’ll create a shopping interface that simplifies the flow of choices for the player!

### Devices Used

- 1 x Conversation device
- 1 x Player Spawner device
- 1 x Character  device
- 1 x [Conditional Button](https://dev.epicgames.com/documentation/fortnite/using-conditional-button-devices-in-fortnite-creative) device
- 1 x [Item Placer](https://dev.epicgames.com/documentation/fortnite/using-item-placer-devices-in-fortnite-creative) device
- 3 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) devices

### Set Up the Basic Devices

1. Start with the **Greasy Grove POI** starter island.
2. Place a **Player Spawner** in the restaurant.
3. Customize the Player Spawner to set **Visible in Game** to **Off**.

   [![](https://dev.epicgames.com/community/api/documentation/image/17316f41-ac7b-45c0-8519-b7e06b6117d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/17316f41-ac7b-45c0-8519-b7e06b6117d6?resizing_type=fit)
4. Place a Character device behind the counter.
5. Customize the Character device as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/f3fb2d71-2dac-4ff3-a639-831a68314a3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f3fb2d71-2dac-4ff3-a639-831a68314a3d?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Character | Beef Boss |
   | Use Animated Idle | On |
   | Interact Type | Send Event Only |
   | Interaction Text | Shop |
6. Place a **Conditional Button** device in front of the counter and register one **Gold** to the device.
7. Place an **Item Placer** device in another part of the restaurant and register one Gold to the device.
8. Place an **Item Granter** device and register an **Ice Cream Cone** to the device.
9. Customize the Item Granter as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/0c694653-3a4c-414a-a258-bd4a206e3a59?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c694653-3a4c-414a-a258-bd4a206e3a59?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | On Grant Action | Keep All |
   | Equip Granted Item | Yes |
10. Duplicate this device twice, registering a Pizza Slice and Banana to each duplicate respectively.

When duplicating the device, make sure to clear out the registered items before adding new ones!

### Configure the Conversation

1. Place a **Conversation** device.
2. Customize the Conversation device as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/5701a1bd-2e50-44c0-9337-239e6a22d1ed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5701a1bd-2e50-44c0-9337-239e6a22d1ed?resizing_type=fit)

   undefined

   | Option | Value |
   | --- | --- |
   | Speaker Name | Shop |
   | Show Indicator Bubble | Off |
3. Configure the following events on the Conversation device so that each of the first three conversation events will grant a different food item.

   [![](https://dev.epicgames.com/community/api/documentation/image/71493cce-3d8e-4772-b0b4-1a732f05c0d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/71493cce-3d8e-4772-b0b4-1a732f05c0d5?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Conversation Event One Send Event To | Ice Cream Item Granter | Grant Item |
   | On Conversation Event Two Send Event To | Pizza Slice Item Granter | Grant Item |
   | On Conversation Event Three Send Event To | Banana Item Granter | Grant Item |
4. Configure the following event on the Conditional Button device so that when the player pays one Gold, they will be able to buy food.

   [![](https://dev.epicgames.com/community/api/documentation/image/d20bb2fb-428c-44af-a9df-802c2d66d50b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d20bb2fb-428c-44af-a9df-802c2d66d50b?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Activated Send Event To | Conversation Device | Initiate Conversation |
5. In UEFN, create a Conversation Bank called **Shop Conversation.**
6. Create the following conversation:

   [![](https://dev.epicgames.com/community/api/documentation/image/a55719cd-b20e-49a6-ac5f-e6ecf5d95c52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a55719cd-b20e-49a6-ac5f-e6ecf5d95c52?resizing_type=fit)
7. Customize the Conversation device as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/0d4548c9-e2df-4a8c-9d32-f2cd409fad73?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d4548c9-e2df-4a8c-9d32-f2cd409fad73?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Conversation | ShopConversation |

### Design Tip

The Conversation device has a number of nodes that can help you create unique gameplay in the conversation itself. The Restart Conversation node can create looping conversations such as this one, and the Random node is great for making your conversations more dynamic and surprising!

## Build a Shipwreck Experience!

Because the **Conversation** device can call events on other devices at specific moments in the conversation, you can use **Fixed Point Camera** devices to create a more cinematic conversation!

### Devices Used

- 1 x Conversation device
- 1 x Player Spawner device
- 1 x Character device
- 1 x [Boat Spawner](https://dev.epicgames.com/documentation/fortnite/using-boat-spawner-devices-in-fortnite-creative) device
- 2 x [Fixed Point Camera](https://dev.epicgames.com/documentation/fortnite/using-fixed-point-camera-devices-in-fortnite-creative) devices
- 1 x [Post Process](https://dev.epicgames.com/documentation/fortnite/using-post-processing-devices-in-fortnite-creative) device

### Set Up the Basic Devices

1. Start with the **Oasis Island** starter island.
2. Place a **Player Spawner** device on the island.
3. Customize it so **Visible in Game** is **Off**.
4. Place a **Character** device.
5. Customize the Character device as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/76c10536-9019-466c-b2e9-a370b62130c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76c10536-9019-466c-b2e9-a370b62130c2?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Character | Castaway Jonesy |
   | Use Animated Idle | On |
   | Emote | Cheer |
   | Interact Type | Send Event Only |
6. Place a **Boat Spawner** device in the water.
7. Customize the Boat Spawner as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/797bcaab-1ef7-4242-a107-9b5f222c3851?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/797bcaab-1ef7-4242-a107-9b5f222c3851?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | Enabled During Phase | None |  |
   | Visible During Game | Off |  |

### Configure the Cameras

### Set Up the Conversation

### Bind Functions / Events

Direct event binding is how you set devices to communicate directly with other devices. This involves setting functions and events for the devices involved.

You now have a shipwreck narrative experience!

### Design Tip

The Conversation device can trigger any events from within the conversation, allowing all of these camera switches! Think of all of the other devices that can be connected to a conversation. Maybe monsters will spawn at a specific point in your conversation if the player picks the wrong option, or maybe the player will get a health boost if they correctly solve a riddle!

Visible in Option
