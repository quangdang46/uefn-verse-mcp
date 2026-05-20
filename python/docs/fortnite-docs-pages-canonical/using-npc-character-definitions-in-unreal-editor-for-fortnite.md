## https://dev.epicgames.com/documentation/en-us/fortnite/using-npc-character-definitions-in-unreal-editor-for-fortnite

# NPC Character Definitions

Create Character Definitions to add attributes that can be imported into the NPC Spawner device.

![NPC Character Definitions](https://dev.epicgames.com/community/api/documentation/image/be2561ac-88ed-4a80-83f0-57f31e3ee462?resizing_type=fill&width=1920&height=335)

This feature is in Early Access. You can publish an island with this feature, but be aware that through the Early Access period, changes may break your island and may require your active intervention.

Create **NPC Character Definitions** to modify NPCs beyond the **[NPC Spawner](https://dev.epicgames.com/documentation/fortnite/using-npc-spawner-devices-in-unreal-editor-for-fortnite)** device basic settings. With the NPC Spawner basic options, you can create instances of characters. Through Character Definitions, you can customize character type, behavior, and modifiers. You can even write [Verse scripts](https://dev.epicgames.com/documentation/fortnite/create-custom-npc-behavior-in-unreal-editor-for-fortnite) that further instruct character behaviors.

With Character Definitions, you can save the properties of custom characters as assets. Any NPC Spawner in your project can then reference and reuse these assets. After connecting the asset to an NPC Spawner device, you can use the device settings to override specific Character Definition properties.

[![NPC Character Definition in UEFN](https://dev.epicgames.com/community/api/documentation/image/580fad53-1a1f-4314-b810-a228fc6cc9dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/580fad53-1a1f-4314-b810-a228fc6cc9dd?resizing_type=fit)

The NPC Spawner device modifiers override any Character Definition modifiers to provide slight variations in NPC instances.

## Creating Character Definitions

[![Character Defeinition Thumbnail](https://dev.epicgames.com/community/api/documentation/image/03e60e81-02c0-41f6-bac8-6a65e072116c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/03e60e81-02c0-41f6-bac8-6a65e072116c?resizing_type=fit)

You can either create Character Definitions through the **Content Drawer** or directly through the NPC Spawner settings.

Your modified Character Definitions can be seen once imported into the NPC Spawner device. If you create a Character Definition within the NPC Spawner, your modifications are immediately reflected in the NPC Spawner device.

To create a Character Definition through the Content Drawer, follow these steps:

To create a Character Definition through the NPC Spawner device, follow these steps:

## Character Definitions

[![Character Definitions](https://dev.epicgames.com/community/api/documentation/image/3c75da74-df0a-4e4d-ab80-41a48ef663fb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c75da74-df0a-4e4d-ab80-41a48ef663fb?resizing_type=fit)

Through the Character Definition's settings, you can customize the following options.

- **NPC Character Type**
- **NPC Behavior**
- **NPC Character Modifiers**

### NPC Character Type

[![Character Type](https://dev.epicgames.com/community/api/documentation/image/daf4432b-dec4-45a9-ba8f-6af7a96f6f28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/daf4432b-dec4-45a9-ba8f-6af7a96f6f28?resizing_type=fit)

Select from the **NPC Character Type** dropdown to set the base properties for how your character exists in the gameplay. You can choose a character modeled after Fortnite guards and wildlife, or create customized behaviors with Verse.

This setting has contextual filtering and will trigger different options once selected.

| Character Type | Description |
| --- | --- |
| **Custom** | Behaviors are defined in Verse. |
| **Guard** | NPCs have the same functionality as the **[Guard Spawner](https://dev.epicgames.com/documentation/fortnite/using-guard-spawner-devices-in-fortnite-creative)**, though you can have more control over properties like movement and behavior. |
| **Participant** |  |
| **Wildlife** | Creates the subtype options of **Boar**, **Chicken**, **Raptor**, and **Wolf**. Each subtype has its own default behavior. Wildlife NPCs have the same functionality as the **[Wildlife Spawner](https://dev.epicgames.com/documentation/fortnite/using-wildlife-spawner-devices-in-fortnite-creative)**, though you can  control over properties like movement and behavior. |

Additional character types are available when working on specific brand islands. To learn more, see the [Custom IP Character Definitions](https://dev.epicgames.com/documentation/fortnite/using-npc-character-definitions-in-unreal-editor-for-fortnite#custom-ip-character-definitions) section on this page.

### NPC Character Behavior

[![Character Behavior](https://dev.epicgames.com/community/api/documentation/image/813eb689-3b00-4496-8b6f-d1983365c52b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/813eb689-3b00-4496-8b6f-d1983365c52b?resizing_type=fit)

After you select a character type, you can set the character's behavior. You can set behaviors as empty, default, or assigned through Verse.

| Character Behavior | Description |
| --- | --- |
| **Empty Behavior** | Available with Custom character types. Creates a blank behavior for NPCs to remain in their reference pose. This is useful to remove NPC behaviors so it will only be animated in Sequence cinematics. |
| **Default Behavior** | Available with the Guard and Wildlife character types. Allows you to alter the behavioral settings of characters intended to have the mannerisms of Battle Royale guards. |
| **Verse Behavior** | Available with all character types. Allows you to include any Verse scripts for your character. |

For more information on creating your own NPC Behaviors, check out the [Create Custom NPC Behavior page](https://dev.epicgames.com/documentation/fortnite/create-custom-npc-behavior-in-unreal-editor-for-fortnite).

### NPC Character Modifiers

[![Character Modifiers](https://dev.epicgames.com/community/api/documentation/image/862cdd73-f8a8-4502-b716-47f136218c14?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/862cdd73-f8a8-4502-b716-47f136218c14?resizing_type=fit)

Use **Character Modifiers** to customize the characteristics of your character. Each Character Type will have its own preset of starting modifiers automatically applied when you select it.

Click the plus arrow to add more Character Modifiers. You can only have one of each modifier active at a time.

[![](https://dev.epicgames.com/community/api/documentation/image/4b1b1459-4dc2-4ac3-9140-3e8e947e9732?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b1b1459-4dc2-4ac3-9140-3e8e947e9732?resizing_type=fit)

| Character Behavior | Description |
| --- | --- |
| **Awareness Modifier** | Modifies alertness and awareness. |
| **Cosmetic Modifier** | Modifies looks and cosmetics. You can choose between Fortnite Character Item Definitions (CIDs), which will display as internal names. |
| **Effects Modifier** | Modifies the effects applied to an NPC. |
| **Guard Perception Modifier** | Modifies sight and hearing. |
| **Health Modifier** | Modifies health and shield. |
| **Inventory Modifier** | Modifies an NPC's inventory. |
| **Navigation Modifier** | Modifies the NPC's navigation parameters. |
| **Patrol Path Modifier** | Modifies the patrol path. |
| **Persona Modifier (Experimental)** | Modifies the persona of the character. |
| **Sequencer Modifier** | Adds tags for NPCs spawned so they can be found by Sequencer. |
| **Team Modifier** | Modifies the team. You can apply a team number or specify if the NPC is considered a wildlife, creature, or neutral. |
| **UI Modifier** | Modifies the display information for an NPC, such as name and health bar. |

### Custom IP Character Definitions

A few brand partners have their own NPCs available through a NPC Character Definition.

Depending on the IP, you can find the unique NPCs in one or both of the following:

- The **NPC Character Type** which can include unique modifiers.
- Through the **Cosmetic Modifier** when selecting a **Custom** or **Guard** character type.

IP assets have specific rules and guidelines for use. Check the brand rules for the IP assets you intend to use. To learn more about the various brand partners and content, see [Game Collections](https://dev.epicgames.com/documentation/fortnite/game-collections-in-unreal-editor-for-fortnite).

You can only use brand assets in a project specific to the relevant IP property.

## Importing Character Definitions

[![Importing Character Definitions](https://dev.epicgames.com/community/api/documentation/image/eee7befe-63a1-4647-8baa-edb4a0551088?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eee7befe-63a1-4647-8baa-edb4a0551088?resizing_type=fit)

After your Character Definition is created and saved, import it into an NPC Spawner device's **NPC Character Definition** setting. Once imported, your NPC Spawner's character automatically updates to reflect your Character Definition.

You can use the same Character Definition for multiple devices and make slight variations to characters by overriding individual device settings. Any updates you make for the Character Definition will affect every device it's assigned to.

## Placing Character Definitions

You can place Character Definitions directly from the **Content Drawer** or through the NPC Spawner device.

To place multiple Character Definitions, you may need to save the level first.

Dragging a Character Definition from the Content Drawer is a shortcut with the same functionality as placing an NPC Spawner device with an assigned Character Definition.
