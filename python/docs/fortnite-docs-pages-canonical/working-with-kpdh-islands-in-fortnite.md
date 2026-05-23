## https://dev.epicgames.com/documentation/en-us/fortnite/working-with-kpdh-islands-in-fortnite

# Working with KPop Demon Hunters Islands

Learn about the available feature set for KPop Demon Hunters, including exclusive assets and a starter island.

![Working with KPop Demon Hunters Islands](https://dev.epicgames.com/community/api/documentation/image/476c6bf8-bba9-4bb5-8f28-8e5c70b84ae0?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [Accessing Brand Content](https://dev.epicgames.com/documentation/fortnite/accessing-brand-content-in-fortnite)

Bring the world of **KPop Demon Hunters** to your islands with curated assets in Fortnite Creative and Unreal Editor for Fortnite (UEFN). The branded content includes features like a starter island, HUNTR/X characters, multiple demon enemy types, and gameplay items.

Build islands where players gain the HUNTR/X as allies and defend the human realm from demons. You can design your environment with items such as the crashed HUNTR/X plane, posters, Honmoon material, and Gwi-Ma vista. Incorporate brand colors and Fortnite assets to expand your island design.

## Access Content Through Island Templates

You can gain access to the KPop Demon Hunters feature set by using the templates in UEFN or Creative.

### KPop Demon Hunters Starter Island

Use the **KPop Demon Hunters Starter Island** template in UEFN to start building with the brand features, and examine how existing Fortnite assets are connected to create the city. You can access the project template in the UEFN project browser under the **Brand Templates** tab.

KPop Demon Hunters Starter Island

To get the best experience from the template, use the editor and an instance of the Fortnite game client (session) together. From the Fortnite session, you can see HUNTR/X and demon non-player characters (NPCs) in action, use gameplay items, and try out weapons.

Use the [Outliner](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#outliner-panel) to examine all the assets used to design the island.

#### Kitbash with Fortnite Assets

The starter island showcases locations inspired by iconic scenes from the movie, like the bathhouse and plaza where the Saja Boys first perform, created by [kitbashing](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#kitbash) with Fortnite assets. You can create similar scenes using a mix of [props](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prop), [prefabs](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prefab), and additional assets from [galleries](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#gallery). The starter island uses assets from galleries like **Mega City**, **Chapter 4 Jungle**, and **Paradise**.

![Template Envrionments](https://dev.epicgames.com/community/api/documentation/image/5965e1b8-0ccd-4a39-a90e-e89e9ee5efc8?resizing_type=fit&width=1920&height=1080)![Template Envrionments](https://dev.epicgames.com/community/api/documentation/image/51638d38-9edd-4c47-8cfc-449c38c62ead?resizing_type=fit&width=1920&height=1080)![Template Envrionments](https://dev.epicgames.com/community/api/documentation/image/a0603392-2b1e-4071-b1e3-35f1a0630458?resizing_type=fit&width=1920&height=1080)![Template Envrionments](https://dev.epicgames.com/community/api/documentation/image/3d4b96dc-aa4e-403b-bc6e-c87c6b79dc95?resizing_type=fit&width=1920&height=1080)

**Template Envrionments**

The environment design of the building assets are put together using an off-grid setup, instead of the general [Fortnite grid-snapping](https://dev.epicgames.com/documentation/fortnite/using-grid-snapping-in-unreal-editor-for-fortnite) that automatically snaps building pieces together. In the template, the Fortnite Cell Snap in the viewport toolbar is disabled to create more unique shapes and configurations that match the theme of the island. You can control how freely assets move based on a custom grid size you define in the viewport toolbar. This workflow works well with buildings on a non-destructible island.

To learn more about these grid and snapping options, see [Viewport Toolbar](https://dev.epicgames.com/documentation/fortnite/viewport-toolbar).

#### Gameplay

The starter island includes minor gameplay to highlight and provide the opportunity to try out the toolset.

The experience starts in an alleyway where you can hire the HUNTR/X NPCs, and equip Rumi’s Empowered Sword, which triggers demon NPCs to spawn. After you defeat the demons, make your way to the bathhouse for a second wave. The combat is completed as you travel through the bathhouse and to the plaza. At the plaza, celebrate with HUNTR/X and hop on stage for a jam session.

The table below describes some key functionality in the template.

|  |  |
| --- | --- |
| Functionality | Description |
| **Bathhouse Reactive Environment** | To capture the moody bathhouse, the design team added dynamic assets, like the water material, that gradually changes colors as you enter. This was designed to mimic the movie where demons spawn from the Honmoon barrier into the bathhouse.  The design is set through a [Volume](https://dev.epicgames.com/documentation/fortnite/using-volume-devices-in-fortnite-creative) device that enables a [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) and a [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) device when you enter it. The Trigger device enables the play function of the [Cinematic Sequence](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) device. The level sequence on the device animates changing values of the assets. To learn more, see [Gameplay Events in Sequencer](https://dev.epicgames.com/documentation/fortnite/gameplay-events-in-sequencer-in-unreal-editor-for-fortnite). |
| **Plaza Cut Scene** | When you approach HUNTR/X in the plaza, you trigger a [cutscene](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#cutscene) where the pop group emotes in celebration. The cutscene is created using the **Cinematic Sequence** device.  To create a scene focused on the girls, a [HUD Controller](https://dev.epicgames.com/documentation/fortnite/using-hud-controller-devices-in-fortnite-creative) device is used to hide the heads-up display ([HUD](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#hud)). |
| **Victory Jam Session** | Hop on the soda can stage to jam out and attract a crowd.  On the stage is a [Mutator Zone](https://dev.epicgames.com/documentation/fortnite/mutator-zone) device that enables the [Crowd Volume](https://dev.epicgames.com/documentation/fortnite/using-crowd-volume-devices-in-fortnite-creative) for the concert audience. To further define the celebration style, the [gold aura](https://dev.epicgames.com/documentation/fortnite/working-with-kpdh-islands-in-fortnite#gold-and-demon-vfx-auras) visual effect is added to the player through the [Visual Effect Powerup](https://dev.epicgames.com/documentation/fortnite/using-visual-effect-powerup-devices-in-fortnite-creative) device. |

![Kpop Demon Hunters Starter Island Device Set Ups ](https://dev.epicgames.com/community/api/documentation/image/3bc706ae-74c1-415a-b7e2-555875dd1546?resizing_type=fit&width=1920&height=1080)![Kpop Demon Hunters Starter Island Device Set Ups ](https://dev.epicgames.com/community/api/documentation/image/de4accc5-d66d-4b1f-99a9-6c4cb4689d2e?resizing_type=fit&width=1920&height=1080)![Kpop Demon Hunters Starter Island Device Set Ups ](https://dev.epicgames.com/community/api/documentation/image/dfd6713d-bd7f-47aa-92c9-a54e79c63bc0?resizing_type=fit&width=1920&height=1080)

**Kpop Demon Hunters Starter Island Device Set Ups**

### Other Ways to Create Brand Islands

You can also make a KPop Demon Hunters island using any template from the **Island Templates** tab in UEFN, and selecting **KPop Demon Hunters** from the **Brand** dropdown. In Creative, you can build using the KPop Demon Hunters grid templates.

After you create your island, you have access to curated assets for KPop Demon Hunters to design and build your gameplay. The feature set includes assets like hero characters, demons, items, and widgets. You can access the feature set in the respective KPop Demon Hunters folder in UEFN and Creative.

|  |  |
| --- | --- |
|  |  |
| **UEFN Content Browser** | **Creative Content Menu** |

To learn more about accessing brand feature sets, see [Accessing Brand Content](https://dev.epicgames.com/documentation/fortnite/accessing-brand-content-in-fortnite).

## HUNTR/X NPCs

Protect the Honmoon with the HUNTR/X characters. Create engaging gameplay where players can fight along or against the demon-hunting pop group.

With the KPop Demon Hunters Character Spawner device, you can add HUNTR/X members to your islands. These NPCs have built-in artificial intelligence ([AI](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#artificial-intelligence)) for interacting with players and navigating the island. Each of the girls has her own themed pickaxe, created by their power from the Honmoon.

The device is a redesign of the Guard Spawner device. This configuration means the new device inherits the same settings, but swaps out the Guard Type dropdown with the KPop Demon Hunters Character dropdown. To learn more about the settings, such as hiring a character, see [Guard Spawner Devices](https://dev.epicgames.com/documentation/fortnite/using-guard-spawner-devices-in-fortnite-creative).

|  |  |  |
| --- | --- | --- |
| [Zoey in UEFN](https://dev.epicgames.com/community/api/documentation/image/4ea7281e-293c-41e9-9e11-e81bb6111cee?resizing_type=fit) | [Rumi in UEFN](https://dev.epicgames.com/community/api/documentation/image/f3caec0c-47cf-4e51-8700-d843b1b4c8be?resizing_type=fit) | [Mira in UEFN](https://dev.epicgames.com/community/api/documentation/image/fa709548-712a-4ac7-b307-3167ceee9ebc?resizing_type=fit) |
| **Zoey** | **Rumi** | **Mira** |

You can spawn Rumi, Mira, and Zoey in devices that use character [outfits](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#outfit) like:

- [Character device](https://dev.epicgames.com/documentation/fortnite/using-character-devices-in-fortnite-creative)
- [NPC Spawner device](https://dev.epicgames.com/documentation/fortnite/using-npc-spawner-devices-in-unreal-editor-for-fortnite)
- [Guard spawner device](https://dev.epicgames.com/documentation/fortnite/using-guard-spawner-devices-in-fortnite-creative)

The pickaxe for the characters is not available from these devices.

To use HUNTR/X characters in the **Character** or **Guard Spawner** devices, go to the **Details** panel, and use the **Character Cosmetic** dropdown.

To use them in the **NPC Spawner** device, create a new **NPC Character Definition**, and use the **Character Cosmetic NPC** **Modifier**.

## Demon NPCs

Add enemies to your island with devices that spawn demons inspired by the movie.

These devices are built on pre-existing Fortnite devices and redesigned to fit the KPop Demon Hunters brand. The table below lists each device and its corresponding base version, for you to view available device options.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| **Demon Spawner** | **Demon Placer** | **Demon Manager** |
| **Base Device:** [Creature Spawner](https://dev.epicgames.com/documentation/fortnite/using-creature-spawner-devices-in-fortnite-creative) | **Base Device:** [Creature Placer](https://dev.epicgames.com/documentation/fortnite/using-creature-placer-devices-in-fortnite-creative) | **Base Device:** [Creature Manager](https://dev.epicgames.com/documentation/fortnite/using-creature-manager-devices-in-fortnite-creative) |

The Demon Manager pairs with the Demon Spawner and Demon Placer devices to set attributes like health, speed, and damage for each demon type. Through the devices, you can choose from eleven demon types.

|  |  |  |  |
| --- | --- | --- | --- |
|  | [Kpop Demon Hunters in UEFN and Creative](https://dev.epicgames.com/community/api/documentation/image/6bbb263f-9898-4c8b-b4d0-872d8e23aa95?resizing_type=fit) |  | [Kpop Demon Hunters in UEFN and Creative](https://dev.epicgames.com/community/api/documentation/image/b5857d66-e41b-4467-a063-46d99b5f10d8?resizing_type=fit) |
| **Demon** | **Shield Demon** | **Small Demon** | **Poison****Demon** |
|  |  |  |  |
| **Ranged Demon** | **Ranged Ice** | **Ogre** | **Exploding Ogre** |
|  |  |  |  |
| **Poison Ogre** | **Mega Ogre** | **Mega Ogre - Loot** |  |

## Gameplay Items and Weapons

The feature set includes items and weapons to immerse players in the KPop Demon Hunters world.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| **Rumi’s Empowered Sword** | **Mira's X-tra Spicy Ramyeon** | **Zoey's Bubble Shield** | **Tiger's Teleporting Mask** |

You can provide this content to players from devices like:

- [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative)
- [Item Placer](https://dev.epicgames.com/documentation/fortnite/using-item-placer-devices-in-fortnite-creative)
- [Team Settings and Inventory](https://dev.epicgames.com/documentation/fortnite/team-settings-inventory)
- [Loot chests](https://dev.epicgames.com/documentation/fortnite/using-chest-and-ammo-gallery-devices-in-fortnite-creative)

### Rumi’s Empowered Sword

Grant players the ability to slice their way to victory with **Rumi's Empowered Sword**.

Rumi’s Empowered Sword

The energy-infused sword includes the following actions:

- **Attack:** Primary slice attack. Players can hold the attack trigger to perform three consecutive slashes.
- **Energy Slash:** Secondary attack that fires an arc projectile.
- **Falling Slam:** Falling ground attack invoked when attacking while in the air.

### Mira's X-tra Spicy Ramyeon

Add the spice to your island with the **Mira's X-tra Spicy Ramyeon** consumable item for healing.

Mira's X-tra Spicy Ramyeon

### Zoey's Bubble Shield

**Zoey's Bubble Shield** is a throwable item that produces a golden Honmoon for protection and increases players' shields when inside.

Zoey's Bubble Shield

### Tiger's Teleporting Mask

Players can equip the **Tiger's Teleporting Mask** item to teleport a short distance.

Tiger's Teleporting Mask

## Custom HUD

Add KPop Demon Hunters colors and design elements into your user interface (UI) with custom [widgets](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#widget) for a cohesive look. The widgets include UI elements for:

- Health
- Shield
- Character
- Equipped item or weapon
- Quickbar
- Team vitals

[![KPop Demon Hunters in Fortnite](https://dev.epicgames.com/community/api/documentation/image/a2ccdd03-d83a-4297-a1e5-b92f9630738f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2ccdd03-d83a-4297-a1e5-b92f9630738f?resizing_type=fit)

KPop Demon Hunters HUD

You can use the widgets in UEFN with the [HUD Controller device](https://dev.epicgames.com/documentation/fortnite/using-hud-controller-devices-in-fortnite-creative).

The following table lists the available widgets and corresponding settings in the HUD device.

| Widget | HUD Device Option | Description |
| --- | --- | --- |
| **UW_HUD_PlayersInfoStack** | **Player Info Widget** | Combines the player's and their teammates' information. It references the following widgets:   - **UW HUD PlayerInfoBlock:** Element design that shows the player's health and shield. - **UW HUD TeammateInfo:** Element design that shows the health and shield for the player's teammates. |
| **UW_HUD_EquippedInforBlock** | **Equipped Item Info Widget Override** | Element for your selected item. Includes ammo when applicable. |
| **UW_HUD_QuickbarSlot** | **Quickbar Slot Widget Override Class** | Element design for your inventory UI. |

With the device options, you can adjust the UI layout to suit your preferences. The assets to create the widgets, like textures and material instances, are available in the UEFN from the C**ontent Drawer > All > KPop Demon Hunters Starter > UI** folder.

The KPop Demon Hunters Starter Island includes editable widgets in the project files. This means you can adjust the widget attributes to customize the UI further. To learn more about UI for your island, see [In-Game User Interfaces](https://dev.epicgames.com/documentation/fortnite/ingame-user-interfaces-in-unreal-editor-for-fortnite).

[![](https://dev.epicgames.com/community/api/documentation/image/bc862d49-6219-43d2-9616-ca1997858dbd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc862d49-6219-43d2-9616-ca1997858dbd?resizing_type=fit)

## Prop Gallery

Included in the feature set are themed props for your environment design. Use the crashed plane, HUNTR/X posters, and statue variants to tie in themes from the movie.

[![KPop Demon Hunters Prop Gallery in Unreal Editor for Fortnite](https://dev.epicgames.com/community/api/documentation/image/186ef48f-0678-40fd-a172-bce759568a48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/186ef48f-0678-40fd-a172-bce759568a48?resizing_type=fit)

KPop Demon Hunters Prop Gallery

The posters are exposed as textures, meaning you can add them to other assets like you would with any material. For example, you can use the [Decal device](https://dev.epicgames.com/documentation/fortnite/decal-device-in-unreal-editor-for-fortnite) to place the textures into your island.

## Gwi-Ma Vista

Set the tone of combat scenes or objectives with the **Gwi-Ma** vista in UEFN. This asset is designed as a background element, and brings pressure from the demon ruler. Included in the vista is a visual effect (VFX) of incoming souls.

Gwi-Ma Vista

## Honmoon Shader

Cover your island with the Honmoon magical barrier. The Honmoon asset is available in UEFN as a [material](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#material) with color options for gold or blue with purple edging. You can use the material to communicate the strength of HUNTR/X's bond with each other and fans, as well as the threat level of demons, where gold represents the strongest connection and complete blockage of the demon realm.

|  |  |
| --- | --- |
| [Blue Honmoon in Unreal Editor](https://dev.epicgames.com/community/api/documentation/image/986adc18-a02d-464a-ad99-9e2949c92df2?resizing_type=fit) | [Gold Honmoon in Unreal Editor](https://dev.epicgames.com/community/api/documentation/image/f59d3fbd-e247-498c-b763-5b3325c5ba5f?resizing_type=fit) |
| Blue Honmoon | Gold Honmoon |

To use the material and edit the colors, you must create a material [instance](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#instance). The instance exposes parameters for you to adjust.

You can drag the original material onto assets on your island, but it will use the default golden color and not be editable.

To create the material instance:

Double-click the material instance to adjust parameters like glow (emissive), color, opacity, and fade. To learn more about this asset type, see the [Material Instances](https://dev.epicgames.com/documentation/unreal-engine/instanced-materials-in-unreal-engine?application_version=5.5) page of the Unreal Engine documentation.

[![](https://dev.epicgames.com/community/api/documentation/image/51679a81-1e1a-4957-a3f4-cab59b68ba29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51679a81-1e1a-4957-a3f4-cab59b68ba29?resizing_type=fit)

Blue Honmoon Material Instance and Parameters

The KPop Demon Hunters Starter Island template uses the material with the plane static mesh from the [Place Actors](https://dev.epicgames.com/documentation/fortnite/user-interface-reference-for-unreal-editor-for-fortnite#level-editor-toolbar) dropdown to create a barrier and set the [level design flow](https://dev.epicgames.com/documentation/fortnite/level-design-best-practices-in-fortnite-creative#flow). The mesh is duplicated, with one instance using the gold color and the other using blue. You can edit the general shapes or create more custom meshes using the in-editor [modeling tools](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite).

In the starter island, the Honmoon changes from blue to gold to represent the progression of the gameplay. The set up for this feature is similar to the bathhouse reactive environment where a level sequence plays after you exit the building to switch the shaders.

## Honmoon Storm

Incorporate the Honmoon as the island storm to increase the intensity for players. When you place a storm device in your KPop Demon Hunters island, the Storm Visuals dropdown in the device settings updates with an Honmoon Storm option.

Honmoon Storm

You can use the following devices to set the storm:

- **[Basic Storm Controller:](https://dev.epicgames.com/documentation/fortnite/basic-storm-controller)** Generates a single storm phase.
- [Advanced Storm Controller:](https://dev.epicgames.com/documentation/fortnite/using-advanced-storm-controller-devices-in-fortnite-creative) Generates multiple storm phases.

## Gold and Demon VFX Auras

Immerse players in your islands with (VFX) auras in UEFN. The auras are created with the [Niagara](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#niagara) system. The two aura types, gold and demon, create gameplay opportunities, like distinguishing teams or indicating a special ability. In the KPop Demon Hunters Starter Island, the gold aura is applied when you begin a jam session.

|  |  |
| --- | --- |
|  |  |
| **Gold Aura** | **Demon Aura** |

The auras are in the **All > KPop Demon Hunters > PlayerAuras** folder. There are two VFX assets for each aura type, one to apply to players and the other to add to objects. You can drag the aura VFX assets labeled static mesh in the viewport and onto an object.   
    
To add the aura for players:

You can add the powerup to your island for players to apply to themselves, or use the device's **Spawn** function to activate it based on an event.

You must use the device to assign the aura to players. Avoid adding the player VFX in the viewport, as it will fail validation.

## Additional Design Elements

As you build your island, keep in mind brand elements like color and themes from the movies. Take the time to understand the brand so that fans of the film can connect with it.

For example, think of the colors that surround HUNTR/X and the Saja Boys. Use those color schemes to make distinctions in your island. You can pull colors from the assets. Also consider elements like lighting to establish the theme. You can play with lighting and color to contrast between HUNTR/X vs. demons or players vs. demons. The lighting in the starter island is set to capture the nightlife, Honmoon danger, and moody bathhouse fight.

To learn more about designing your game and tips for incorporating assets, check out the following pages:

- [How To Design a Game](https://dev.epicgames.com/documentation/fortnite/how-to-design-a-game-in-fortnite-creative)
- [Level Design Best Practices](https://dev.epicgames.com/documentation/fortnite/level-design-best-practices-in-fortnite-creative)
- [Lighting and Color](https://dev.epicgames.com/documentation/fortnite/making-cinematics-2-lighting-and-color-in-unreal-editor-for-fortnite)

## Publishing Islands

To publish KPop Demon Hunters islands, you must be a member of the [Fortnite Developer Program](https://create.fortnite.com/enroll) and opt into additional terms and conditions for the brand in the [Creator Portal](https://create.fortnite.com/welcome). Your island must also align with the brand guidelines. To learn more about the brand rules and becoming a developer, see [KPop Demon Hunters Brand Rules](https://dev.epicgames.com/documentation/fortnite/kpop-demon-hunters-brand-rules-in-fortnite).

### IARC Audience Restrictions

Any islands that you create must have an age-appropriate rating. The Creator Portal is set up to guide you through this process, as part of the island publishing workflow. As a general rule, you should create your island with all audiences in mind.

The table below shows each Rating Authority and region, along with their age-appropriate ratings for your island.

|  |  |  |
| --- | --- | --- |
| Rating Authority | Region | Maximum Age Rating Category |
| [ESRB](https://www.esrb.org/ratings-guide/) | North America | T |
| [PEGI](https://pegi.info/what-do-the-labels-mean) | Europe & UK | 12 |
| [ACB](https://www.classification.gov.au/classification-ratings/what-do-ratings-mean) | Australia | M |
| [Classlnd](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1) | Brazil | 12 |
| [USK](https://usk.de/die-usk-alterskennzeichen/) | Germany | 16 |
| [GRAC](https://www.grac.or.kr/english/) | South Korea | 12 |
| Russia | Russia | 12 |
| [IARC General](https://www.globalratings.com/ratings-guide.aspx) | Rest of World | 12 |
