## https://dev.epicgames.com/documentation/en-us/fortnite/capture-the-flag-1-set-up-the-game-in-unreal-editor-for-fortnite

# 1. Set Up the Capture the Flag Game

Create your project and modify Island Settings to get started.

![1. Set Up the Capture the Flag Game](https://dev.epicgames.com/community/api/documentation/image/4ee3c8ae-0789-40e9-85e8-9d3e9ce5a791?resizing_type=fill&width=1920&height=335)

**Devices Used**:

- 1 x [Island Settings](https://dev.epicgames.com/documentation/fortnite/island-settings-in-unreal-editor-for-fortnite)

Use the **Search** bar to locate each setting faster.

[![search bar](https://dev.epicgames.com/community/api/documentation/image/1ea95d5d-96fa-4a19-96a0-141b8c2debee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ea95d5d-96fa-4a19-96a0-141b8c2debee?resizing_type=fit)

| Option | Value | Explanation |
| --- | --- | --- |
| **Max Players** | 24 | Increases the total number of players allowed, because this is a large map. |
| **Teams** | Team Index: 2 | This is where you set how many teams there are. |
| **Team Size** | Split Evenly | Players who join will be distributed to teams evenly. |
| **Default Class Identifier** | Class Slot: 1 | This is the default class assigned to players who join before the player chooses a class. |
| **Time Limit** | 60.0 | If no win condition is met, the match automatically ends in 60 minutes. |
| **Score To End** | 3 | The number of flag captures needed to win the game. |
| **Join in Progress** | Spawn | Players can join the match in progress. |
| **Respawn Type** | Wave | This determines how players respawn. Setting this to **Wave** means that all players who are eliminated within a certain period will respawn in a group. |
| **Autostart** | 60.0 | Determines that the game will automatically start after 60 seconds. |
| **Game Start Countdown** | 5.0 | How long players are in the waiting area before the game starts. |
| **Infinite Resources** | False | Player building is disabled in this game, so Infinite Resources is turned off. |
| **Allow Building** | None | This turns off player building. |
| **Building Can Destroy Environment** | False | Player building is disabled in this game. |
| **Environment Damage** | Off | Players are not allowed to attack or damage the environment. |
| **Structure Damage** | None | Players are not allowed to attack or damage structures on the island. |
| **Pickaxe Range Multiplier** | 4.0 | This multiplier grants players a wider range when using the pickaxe. |
| **Start with Pickaxe** | False | The pickaxe is only granted to certain classes in the game, so players are not automatically granted it at game start. |
| **Down But Not Out** | Off | Eliminated players will respawn quickly, so DNBO is not needed in this game. |
| **Eliminated Player's Items** | Delete | When a player is eliminated, they will respawn next to the Class Selectors, and will be granted items for their class. A player’s items are deleted when they are eliminated. |
| **Allow Item Drop** | False | Each class can use certain items; to keep class abilities unique, players cannot drop items even when eliminated. |
| **Fall Damage** | True | Players can take fall damage in this game. |
| **Show Wood Resource Count** | False | Building resources are not used in this game. |
| **Show Stone Resource Count** | False | Building resources are not used in this game. |
| **Show Metal Resource Count** | False | Building resources are not used in this game. |
| **Show Gold Resource Count** | False | Currency is not used in this game. |

## Next Section

- [![2. Create the Island](https://dev.epicgames.com/community/api/documentation/image/dff07ede-ffa6-4d85-908c-84c1ef939345?resizing_type=fit&width=640&height=640)

  2. Create the Island

  Build the bases, add colored elements to each base, and build the boundaries of your island.](https://dev.epicgames.com/documentation/fortnite/capture-the-flag-2-create-the-island-in-unreal-editor-for-fortnite)
