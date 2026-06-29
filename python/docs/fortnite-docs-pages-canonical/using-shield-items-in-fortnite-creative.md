## https://dev.epicgames.com/documentation/en-us/fortnite/using-shield-items-in-fortnite-creative

# Shield Items

Give players a boost for protection in combat play.

![Shield Items](https://dev.epicgames.com/community/api/documentation/image/9b01a642-3615-4c7f-b2a2-454411ce527c?resizing_type=fill&width=1920&height=335)

A **shield** is a method of protection that can take incoming damage while leaving the player's health unchanged. You can offer **shield [items](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary)** as an aid for players to use during combat that increase a player's shield health when consumed.

Shield, like health, has a bar that can be filled to **100**.

You can change the [My Island Settings](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) option **Max Shields** to alter the maximum shields players can have during gameplay.

[![Player Health and Shield](https://dev.epicgames.com/community/api/documentation/image/bd5d31e1-d004-4a09-9cb7-a8392ff35ac9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bd5d31e1-d004-4a09-9cb7-a8392ff35ac9?resizing_type=fit)

*Shield health displays at the bottom left of the screen as a blue bar with a shield icon to the left. The green bar beneath it indicates the player’s health.*

You can use these items in multiple ways. Some shield items can be drunk for an individual increase in shield health. Other items can have a shared area of effect for all players within in a thrown radius.

Visit our [video tutorials](https://mediaspace.unrealengine.com/playlist/dedicated/208434573/1_gxu6mwv5/1_qfnz9w5c) to learn more about working with items and for tips to enhance gameplay.

Shield items include:

- **Small Shield Potion**
- **Shield Potion**
- **Shield Bubble**
- **Shield Keg**

## Finding and Placing Items

[![Finding Shield Consumables](https://dev.epicgames.com/community/api/documentation/image/ce08f55f-d218-473c-bfff-8244a042c668?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce08f55f-d218-473c-bfff-8244a042c668?resizing_type=fit)

*Click image to enlarge.*

Clicking **Equip** will add the item to your [Equipment bar](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).

When you're back in Create mode, you can view any items you've [equipped](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) by pressing the **F** key. You can select equipped items by either scrolling your middle mouse button or by pressing its corresponding number on your keyboard.

From the [Chest](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) tab, you can select either **Create Chest** or **Create Llama** to store the items in a [chest](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#chest) or a [llama](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#llama) for use [in-game](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#ingame).

[![Shield Chest](https://dev.epicgames.com/community/api/documentation/image/f736e875-42a6-4156-b8d8-ec6003f2208f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f736e875-42a6-4156-b8d8-ec6003f2208f?resizing_type=fit)

*Click image to enlarge.*

Chest and llamas are a great way to offer item bundles to players. Selecting **Add To Chest** will add the item to the **Chest** tab. Each time you click **Add To Chest**, the item count will increase by one, shown as a yellow box on the Chest tab.

You can add up to fifteen items to the **Chest** tab. When it’s full, the **Add To Chest** tab will disappear. To add more items, you first have to remove items from the **Chest** tab.

## Managing Items

[![Shield Loadout Bar](https://dev.epicgames.com/community/api/documentation/image/5f9edb81-487c-4a6a-a296-2170fba06efb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5f9edb81-487c-4a6a-a296-2170fba06efb?resizing_type=fit)

*Click image to enlarge.*

You can manage these items when you are in [Play inventory](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#play-inventory). To access the **Play** inventory screen, press **Tab** and click **Play** in the top navigation bar. Here, you can swap item positions or drop them from your Equipment bar.

Instead of dropping these items on the ground, it's best to either spawn the items onto the map with the [**Item Spawner**](using-item-spawner-devices-in-fortnite-creative) or grant them to players with the [**Item Granter**](using-item-spawner-devices-in-fortnite-creative).

You cannot reposition or copy items with the phone tool. To delete an item from your inventory in Create mode, you will have to select either *Respawn* or *Back To Hub* from the *Menu*. When you do this, your inventory clears.

## Using Shield Items

|  | Item | Usage |
| --- | --- | --- |
| [Small Shield Potion](https://dev.epicgames.com/community/api/documentation/image/1f2a70be-b096-4946-9a4f-a4bc1fc7b469?resizing_type=fit) | **Small Shield Potion** | Restores 25 points of health when consumed. This item can only fill the shield bar up to 50, and has a two-second delay before it applies a player. |
| [Shield Potion](https://dev.epicgames.com/community/api/documentation/image/cab0647e-d0a4-4965-980c-7479b0736f9a?resizing_type=fit) | **Shield Potion** | Restores 50 points of health when consumed. This item has a five-second delay before applying to players. |
| [Shield Bubble](https://dev.epicgames.com/community/api/documentation/image/25ae20c8-87a3-49ee-899b-fe47c58b323f?resizing_type=fit) | **Shield Bubble** | Creates a bubble that blocks projectiles and explosives. Hostile players can still enter the bubble and attack from the inside the shield's radius.  [Shield Bubble](https://dev.epicgames.com/community/api/documentation/image/43eba4e5-f0e0-4d1b-af53-a2ab4dab0a31?resizing_type=fit) |
| [Shield Keg](https://dev.epicgames.com/community/api/documentation/image/c4d93161-f99a-4b92-a401-eba06001d604?resizing_type=fit) | **Shield Keg** | Rapidly restores the shield of everyone within its blast radius.  [Shield Keg Radius](https://dev.epicgames.com/community/api/documentation/image/9462d60b-a8c1-4872-adc8-c1b1d7626986?resizing_type=fit) |

## Registering Items

[![Registered Consumables](https://dev.epicgames.com/community/api/documentation/image/9f119d6a-cda3-46bc-9742-3a5b85d909a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f119d6a-cda3-46bc-9742-3a5b85d909a8?resizing_type=fit)

You can drop items directly onto devices that can either hold or grant items. Above shows the [**Conditional Button**](using-conditional-button-devices-in-fortnite-creative), which holds one Small Shield Potion and an Item Spawner that holds one Shield Keg.

This pair of devices can be set up for players to exchange one Small Shield Potion in exchange for a Shield Keg. To do so, these items must first be [registered](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#register) to the devices that will hold the information.

[![Registering Consumables](https://dev.epicgames.com/community/api/documentation/image/d028dfb3-609f-4f8a-b76e-920c86219a5c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d028dfb3-609f-4f8a-b76e-920c86219a5c?resizing_type=fit)

To register an item for this kind of device, follow the steps below. (You can also watch a [video tutorial](https://mediaspace.unrealengine.com/media/RegisteringCraftingConsumablesinFortniteCreative/1_zpmj3v0g) that shows you how to register items, for [crafting](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#crafting) or other [in-game](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#ingame) use.)

To register an item for this kind of device, follow these steps.

The compatible device will automatically register the dropped item. Compatible devices that can hold items include:

- **Vending Machine**
- **Team Settings & Inventory**
- **Class Designer**
- **Capture Item Spawner**
- **Item Granter**
- **Item Spawner**
- **Conditional Button**
- **Elimination Manager**
- **Item Remover**

Use these devices to set up your own system for granting and spawning items onto your island.
