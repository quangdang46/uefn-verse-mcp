## https://dev.epicgames.com/documentation/en-us/fortnite/using-the-overshield-in-fortnite-creative

# Using the Overshield

Learn about the Overshield and how it can be used in your games.

![Using the Overshield](https://dev.epicgames.com/community/api/documentation/image/971b6619-45a6-4ec0-b4e1-a1ef1e377819?resizing_type=fill&width=1920&height=335)

The **Overshield** is an extra shield layer added to a player's existing [health](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#health) and [shield](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#shield). This is the first line of defense for players before their regular shields begin to deplete. The Overshield displays to the right of the health and shield bars, and starts out full with a default maximum value of 50. After the player takes damage and the shield depletes, it will automatically recharge if the player has received no damage for a certain amount of time. The default delay is 6.5 seconds. You can change the maximum value of the Overshield, as well as other Overshield settings, in the **My Island > Settings** tab.

The table below shows the Overshield as it appears in the players' HUD.

| Overshield in Use |  |  |
| --- | --- | --- |
| [The overshield when full](https://dev.epicgames.com/community/api/documentation/image/1bad7a2d-2c29-4b50-a0a6-57139f22ac3e?resizing_type=fit) | [The overshield depleted by damage](https://dev.epicgames.com/community/api/documentation/image/a177d50f-3efa-4235-9e92-7b0384160d39?resizing_type=fit) | [The overshield when regenerating](https://dev.epicgames.com/community/api/documentation/image/5a01b0b3-3957-40b5-a9ab-ea4d84d027ab?resizing_type=fit) |
| **Full Overshield** | **Overshield Depleted by Damage** | **Overshield Regenerating** |

In general, the Overshield is treated the same as regular shields, so damage that bypasses regular shields also bypasses the Overshield. Examples of this kind of damage include stink, [fall](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#fall-damage), fire, and storm damage. However, storm and fall damage do not stop the player's Overshield from recharging.

To enable the Overshield, press the **Tab** key to open the [Creative inventory](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary), click **My Island**, click the **Settings** tab, and scroll down until you locate **Allow Overshield**. Here you can toggle it **On** or **Off**. You can also modify the default options for the Overshield as shown below.

| Option | Value | Description |
| --- | --- | --- |
| **Overshield Max** | **50**, Pick a value | Determines the maximum amount of Overshield a player can have. |
| **Overshield Recharge Delay** | **6.5**, Pick an amount of seconds | The Overshield starts to recharge after this amount of time if the player takes no damage during the delay. |
| **Overshield Recharge Amount** | **1**, Pick a value | Determines how much the Overshield recharges each second, after the recharge delay has ended. |

You can also use the Team Settings & Inventory device, or the Class Designer device, to turn the Overshield off or on and change the Overshield options. These devices can be set to override the general island settings found in My Island.

[![Turning on the Overshield](https://dev.epicgames.com/community/api/documentation/image/4ceeb919-91f4-40f5-b5e8-adf9dc314416?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ceeb919-91f4-40f5-b5e8-adf9dc314416?resizing_type=fit)

*Click image for full size.*

## Using the Overshield on Your Island

An overshield can be useful when building is turned off, which is how this is used in Fortnite [Battle Royale](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#battle-royale). However, there are several other ways to use the Overshield in non-building-based island experiences.

Examples for when to use the overshield:

- If you make adventure or dungeon crawl games, you can set a lower maximum for [HP](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#hp). If you want players to have limited access to [items](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary), players have less need to find health items, and can rely on the Overshield to protect them.
- If you make a [PvP](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#pvp) game, and you want regenerating shields instead of standard shields.
- If you make long-range PvP games where there is a lot of inconsistent or random damage, and more sporadic engagements.

Examples for when to avoid using the overshield:

- Where there is too much good cover, and easily recharging shields would make the game less challenging and less fun.
- When a rechargeable shield breaks your game because it is [OP](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#op) (overpowered).
- When you want items to be hard to find, or if you want gaining shields to be a core part of survival gameplay and building up durability.
