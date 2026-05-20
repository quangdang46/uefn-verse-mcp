## https://dev.epicgames.com/documentation/en-us/fortnite/parkour-elimination-1-set-up-the-game-in-unreal-editor-for-fortnite

# 1. Set Up the Parkour Elimination Game

Create a new project and set up the Island Settings.

![1. Set Up the Parkour Elimination Game](https://dev.epicgames.com/community/api/documentation/image/79f42b23-736f-4a81-9a5b-3db8af94dd22?resizing_type=fill&width=1920&height=335)

To set up your island:

Use the **Search** bar to locate each setting faster.

[![search bar](https://dev.epicgames.com/community/api/documentation/image/cc9ca6ee-5b4f-4c19-87cf-a706eed8c872?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc9ca6ee-5b4f-4c19-87cf-a706eed8c872?resizing_type=fit)

| Option | Value | Explanation |
| --- | --- | --- |
| **Teams** | Free For All | Players all fight each other. |
| **Max Players** | 4 | A maximum of 4 players can play in this game mode. |
| **Default Class Identifier** | Class Slot: 1 | This is required for the teleportation check. Anyone who is 1 has not cleared the race section yet. |
| **Total Rounds** | 3 | The game is played 3 times. |
| **End Game On Match Point Win** | True | If someone wins twice, they win the whole thing. |
| **Time Limit** | "10.0": 10 minutes | Each round lasts a maximum of 10 minutes. |
| **Win Condition** | Most Round Wins | The requirement to win the game. |
| **Eliminations To End** | 10 | It takes 10 eliminations to win the elimination portion of the game. |
| **Autostart** | "60": 1 minute | The game will wait 60 seconds once there are at least 2 people before starting the game. |
| **Starting Shields** | "100.0": 100% Shields | Players spawn with full shields. |
| **Allow Overshield** | True | Players will get 50 shield from the [overshield](https://www.fortnite.com/en-US/creative/docs/fortnite-creative-glossary#overshield). |
| **Infinite Ammo** | True | Players have infinite ammo. |
| **Infinite Items** | False | Players do not have infinite items. |
| **Allow Building** | None | Players cannot build on the map. |
| **Environmental Damage** | "0.0": off | Players cannot damage the environment. |
| **Start With Pickaxe** | False | Players do not have the pickaxe |
| **Eliminated Player's Items** | Keep | Players do not lose the shotgun they equip with the starting area coin when eliminated. |
| **Allow Item Drop** | False | Prevents players from dropping their weapon on the ground and losing it. |
| **Respawn Time** | "1.0": 1 second | It takes 1 second to respawn on elimination. |
| **Spawn Immunity Time** | "5.0": 5 seconds | After respawning, players are invulnerable for 5 seconds or until they shoot. |
| **Allow Mantling/Sprinting/Sliding/Shoulder Bashing** | True | All these settings are needed for parkour. |
| **Glider Redeploy** | False | The glider cannot be deployed in the game. |
| **Show Wood/Stone/Metal Resource Count** | False | Removes these unused UI elements from the game. |
| **Show Gold Resource Count** | True | Shows the gold coin you pick up at the start of the match. |
| **Game Score Display Time** | "7.0": 7 seconds | Time that the scoreboard shows at end of the game. |
| **Round Score Display Time** | "7.0": 7 seconds | Duration of the scoreboard before a new round. |
| **HUD Info Type** | Score | The HUD element tracks score up to 10 to show progress and displays the top 3. |
| **Max Trackers On HUD** | 1 | One HUD Element for the Score is needed. |
| **Round Win Condition** | Eliminations | The per-round win condition is getting to 10 eliminations. |
| **Tiebreaker 1/2/3** | Damage Dealt/Health/Damage Taken | Determines the tiebreakers in order of importance. |
| **First/Second Scoreboard Column** | Eliminations/Eliminated | Determines what the scoreboard will display |

## Next Section

- [![2. Pre-Game Area](https://dev.epicgames.com/community/api/documentation/image/12213ce2-653b-42da-aa99-68c83859798d?resizing_type=fit&width=640&height=640)

  2. Pre-Game Area

  Build the pre-game area.](https://dev.epicgames.com/documentation/fortnite/parkour-elimination-2-pregame-area-in-unreal-editor-for-fortnite)
