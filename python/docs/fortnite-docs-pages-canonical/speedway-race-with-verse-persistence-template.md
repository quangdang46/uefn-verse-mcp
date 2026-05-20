## https://dev.epicgames.com/documentation/en-us/fortnite/speedway-race-with-verse-persistence-template

# Speedway Race with Verse Persistence Template

Learn how to add a local leaderboard and round-specific logic to your racing game!

![Speedway Race with Verse Persistence Template](https://dev.epicgames.com/community/api/documentation/image/faa0b8be-0901-4d13-a1f6-2060514fedc1?resizing_type=fill&width=1920&height=335)

The **Speedway Race with Verse Persistence** template is the Creative template [Designing a Speedway Race](https://dev.epicgames.com/documentation/en-us/fortnite-creative/design-a-speedway-race-in-fortnite-creative) converted to UEFN, with the following functionality added to the project:

- A persistent local leaderboard in the pre-game lobby using Verse Persistence that only shows on the first round.
- A system that assigns players to cars at the start line depending on their finish order in a previous round, using Verse Persistence.
- A starting lineup that displays each player’s stats using a cinematic and Verse.
- And more!

[![](https://dev.epicgames.com/community/api/documentation/image/e8a98b47-5f52-4389-96fc-11e9366b973a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8a98b47-5f52-4389-96fc-11e9366b973a?resizing_type=fit)

The goal for the Creative template Designing a Speedway Race was to use race track assets to build a unique race mode with some quality-of-life features. With this UEFN template, a holistic approach was taken to replace and upgrade many features throughout the map, to take advantage of UEFN’s powerful capabilities.

The following sections explore these updates in more detail.

## Upgrading the Tutorial Zone

You can find the leaderboard in the Tutorial Zone. Each time you load in for your first round on the map, you get 30 seconds to look at the current leaderboard and explore the tutorial area.

This area is built to be visually compelling for players seeking some racing fun, while also providing rich details on how to build a map just like it. The tutorial zone was redesigned from the creative template to feel more clean and open, and skylights were added to bring in some of that natural Lumen light.

When you load the template in UEFN, you can read about the setup of each group of devices and Verse scripts to learn how the template was built and implement them in your own experiences.

The Tutorial Zone is where most of our devices are located so you can browse them and understand their logic. These include core retention devices, Accolades, and Analytics. Accolades devices only grant XP when you finish a lap or finish a race.

You can set up Analytics devices to track various data points to help you improve your project in future updates. This template tracks how often each checkpoint is completed and how often people pick up silver coins during the race. Both give data on how easy or difficult a particular checkpoint or coin can be to reach. Based on this data, you can adjust the position or number of these objects in future releases to make the whole game flow more seamlessly and provide a better racing experience.

## Cleaning up the Outliner

After converting the project to UEFN, the **Outliner** was crowded with a long list of unorganized assets.

Although everything still worked, the names of vehicles, barriers, and other items had numbers appended to them, making it difficult to understand the project structure. The conversion process automatically added these numbers to ensure each asset and device had a unique name.

To manage this, a file system was added to the project to organize all the objects based on their location and functionality. Although it takes time to organize, this system means you can move or delete groups of objects or entire areas much more efficiently than in Creative.

[![](https://dev.epicgames.com/community/api/documentation/image/aba93d42-fd95-4d15-b99c-1cbf4839b44b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aba93d42-fd95-4d15-b99c-1cbf4839b44b?resizing_type=fit)

## Persistent Local Leaderboard

Because of the lack of persistable data in the original creative map, previous race winners and player stats couldn’t be tracked. In the updated UEFN template map, using Verse and Verse Persistence means we can store player data across game sessions, to monitor lifetime player stats and create local leaderboards. You can only access player data for players that are in the current session, so the leaderboard will only reflect the stats of players currently playing.

We decided on "podiums" and "lap time" as being the most important [persistable](https://dev.epicgames.com/documentation/fortnite/using-persistable-data-in-verse) stats to track per player. Players only earn a podium when they place in the top 3 finishing players, while the best lap time tracks the fastest racers. We also added an extra stat named “points”. Players are awarded points based on their placement during the race, so players who race a lot but don’t necessarily place well can still earn a large number of points. With these stats, we found a way to acknowledge the fiercest, the fastest, and most dedicated racers all in one.

The converted template uses a pre-game lobby with local leaderboards that show off each player’s lifetime stats. These stats are sorted so that the players with the best lifetime points stat show up at the front, and the top three players are highlighted to show off their skill. These stats are also shown on the HUD during the starting lineup cinematic, letting players scope out the competition and remember who to look out for during the race.

[![](https://dev.epicgames.com/community/api/documentation/image/7af78be5-4e55-4733-ad6f-d396d49623a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7af78be5-4e55-4733-ad6f-d396d49623a5?resizing_type=fit)

To learn more about how to create a persistent local leaderboard, check out [Make Your Own In-Game Leaderboard](https://dev.epicgames.com/documentation/fortnite/make-your-own-ingame-leaderboard-in-verse).

## Racer Order at the Start Line

The converted template replaces the random order of racers at the starting line from the original project, to an order that’s based on how well the racers did in the previous round. This encourages players to finish the race quickly even when they aren’t in first place.

For the first round, racers are placed in a random order, but after the first round racers are ordered by the position they finished in the previous round. This information needs to be stored between rounds but does not persist after the game ends. You can use it to determine the start order by sorting the players based on their previous finish order. To learn how to store round information and sort data, check out the following tutorials:

- [Custom Round Logic](https://dev.epicgames.com/documentation/fortnite/custom-round-logic-using-verse)
- [Sorting Algorithms](https://dev.epicgames.com/documentation/fortnite/sorting-algorithms-in-verse)

[![](https://dev.epicgames.com/community/api/documentation/image/3d5e6485-eefe-47c1-a800-549d712ac344?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d5e6485-eefe-47c1-a800-549d712ac344?resizing_type=fit)

Verse

```
# Orders and returns players by their finish order in the previous round.
# During the first round, players are given random starting placements.
GetPlayerStartOrder<public>(Players:[]player):[]player=
    var OrderedPlayers:[]player = Players

    if:
        IsFirstRound[GetRound[]]
    then:
        # Randomize player order because it's first round.
        set OrderedPlayers = Shuffle(OrderedPlayers)
```

When assigning players to vehicles and setting them up at the start line, you want to make sure that the players are actually the ones that are active and going to race. You can create a function named `GetAllValidPlayers()` that goes through all the players and returns the ones that are still active (haven’t left the game yet) and aren’t spectators (will actually be racing).

Verse

```
# Get all players that are able to race.
GetAllValidPlayers(Players:[]player):[]player=
    # Valid players are ones that are active and not spectating.
    for:
        Player : Players
        Player.IsActive[]
        not Player.IsSpectator[]
    do:
        Player
```

# Get all players that are able to race.
GetAllValidPlayers(Players:[]player):[]player=
# Valid players are ones that are active and not spectating.
for:
Player : Players
Player.IsActive[]
not Player.IsSpectator[]
do:
Player

With all this, the project uses the `starting_game_sequence` device to set up the leaderboard lobby on the first round, and then assign players to start positions and vehicles before starting the race.

Verse

```
# This file handles the logic for the pregame lobby and the cinematics that play at the beginning of a race.
# It controls the length of the starting lineup based on the number of players, and plays an intro for each
# player by displaying their stats.

using { /Fortnite.com/Characters }
using { /Fortnite.com/Devices }
using { /Fortnite.com/FortPlayerUtilities }
using { /Verse.org/Native }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
```

## Starting Line Cinematic with Player Stats

The original version of the Creative Designing a Speedway Race template used the Pulse Trigger device to orchestrate the **ready-set-go** introduction to the race. The Pulse Trigger played a sequence of events over a set period of time by activating triggers to display text and enable lights on the starting line.

[![](https://dev.epicgames.com/community/api/documentation/image/8faf7edf-3a0e-4908-9d12-b6e5d49823bd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8faf7edf-3a0e-4908-9d12-b6e5d49823bd?resizing_type=fit)

With the converted template, the Pulse Trigger device was replaced with UEFN’s [Cinematic Sequence device](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) to achieve a grand opening cinematic. Using Sequencer, you can add different cameras, Heads Up Display (HUD) elements, and a dynamic lineup view that adjusts based on the amount of active players. Similar to how the Pulse Trigger device was previously set up, the Level Sequence activates the devices at important moments, allowing you to determine when to display the next player’s score or when to cut the intro.

[![](https://dev.epicgames.com/community/api/documentation/image/a59ecf70-4c2b-49f5-877d-5f8f84b709cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a59ecf70-4c2b-49f5-877d-5f8f84b709cd?resizing_type=fit)

Specifically, the Level Sequence activates the [Trigger device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-trigger-devices-in-fortnite-creative) named **StartPlayerIntroEvent** whenever a player intro starts, and activates the Trigger device named **EndPlayerIntroEvent** whenever a player intro ends. The Verse code uses this information to determine how many player intros have been shown already and stops playing the cinematic if it's the same as the number of players in the game. If the cinematic finishes first, it will also cancel waiting for player intros because it’s in the `race` expression.

The Verse code calls `WaitForPlayerIntro()` for each player, which starts a loop for each player and waits for the **StartPlayerIntroEvent** Trigger device to activate as many times as the starting position order of the player to know when to display the player’s stats in the HUD. Each of these `WaitForPlayerIntro()` loops is called in the [`ArraySync()` function](https://dev.epicgames.com/community/snippets/oYRX/fortnite-generic-sync-and-race-across-elements-in-an-array), which uses a divide-and-conquer concurrency algorithm to `sync` across multiple async functions and array elements.

Verse

```
# A Verse-authored creative device that can be placed in a level
starting_game_sequence := class(creative_device):

    # The cinematic that intros the players and their stats.
    @editable
    StartingLineupCinematic:cinematic_sequence_device = cinematic_sequence_device{}

    # The cinematic that we cut to after the lineup and before the race starts.
    @editable
    RaceStartCinematic:cinematic_sequence_device = cinematic_sequence_device{}
```

The project uses a [Pop-Up Dialog device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-popup-dialog-devices-in-fortnite-creative) to design the widgets in the [Widget Editor](https://dev.epicgames.com/documentation/fortnite/ui-widget-editor-in-unreal-editor-for-fortnite) and swap out the information using Verse. It does this by setting the text on buttons in the Pop-Up Dialog device.

Verse

```
# Updates the Popup UI to display the lifetime stats of the given player during the
# race starting sequence.
UpdatePopupUI<public>(Player:agent, PopupDialogUI:popup_dialog_device):void=
    if:
        CurrentPlayerStats := GetPlayerStats[Player]
    then:
        PopupDialogUI.SetButtonText(PlayerText(Player), 0)
        PopupDialogUI.SetButtonText(PointsText(CurrentPlayerStats.Points), 1)
        PopupDialogUI.SetButtonText(PodiumsText(CurrentPlayerStats.Podiums), 2)
        BestLapText:message = if(IsValidBestLapTime[CurrentPlayerStats.BestLapTime]):
```

## Level Design

In this update, we used Landscape mode to create an off-road track. We saved memory by making use of fewer assets, and the mountains that now surround the track have more depth. We also used water volumes and the waterfall to create a new type of terrain and draw your eye forward to the next part of the race track.

We upgraded from the legacy day/night cycle of our original project to the advanced Fortnite Chapter 4 lighting. This new cycle enabled us to use [Lumen](https://dev.epicgames.com/documentation/en-us/uefn/UE/building-virtual-worlds/lighting-and-shadows/global-illumination/lumen?application_version=1.0), creating softer shadows and realistic global illumination.

[![](https://dev.epicgames.com/community/api/documentation/image/dca98b3f-b424-461a-adcb-c5c3a09762bd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dca98b3f-b424-461a-adcb-c5c3a09762bd?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/428ad9dc-7839-4dec-bd37-b4b71833f9da?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/428ad9dc-7839-4dec-bd37-b4b71833f9da?resizing_type=fit)

Did you know there are over 120 barriers in the original race track template? Barriers were used to keep players on the track and to ensure cars never went out of bounds. In the update, you’ll see that barriers are only used to keep players in their spot before a race starts and not all around the track. Race checkpoints, collectibles, and some environment pieces were used to encourage players to stay on track:

In the end, the intentionally placed race checkpoints are the final way to require players to follow the track, as each one is necessary to progress through the race.
