## https://dev.epicgames.com/documentation/en-us/fortnite/make-your-own-ingame-leaderboard-in-verse

# Make Your Own In-Game Leaderboard in Verse

Create an in-game leaderboard that tracks player stats across games

![Make Your Own In-Game Leaderboard in Verse](https://dev.epicgames.com/community/api/documentation/image/be2f53ab-cd9c-4b86-9afc-83f7ea732640?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [Persistent Player Statistics](https://dev.epicgames.com/documentation/fortnite/persistent-player-statistics-in-unreal-editor-for-fortnite)

This tutorial builds on the concepts in [Persistent Player Statistics](https://dev.epicgames.com/documentation/fortnite/persistent-player-statistics-in-unreal-editor-for-fortnite), so go check that out first!

Leaderboards are a staple of competitive games, letting players show off their skills and make their name known. They help players develop a sense of progression and encourage players to keep coming back so they can see themselves rise to the top.

[Verse Persistence](https://dev.epicgames.com/documentation/fortnite/using-persistable-data-in-verse) provides the tool that lets you build these leaderboards and add that competitive edge to your experience. You’ve already seen how you can track persistable data between play sessions in the persistent player statistics tutorial, and how to modify and update that data based on different events. Now you’ll apply that knowledge to learn how to create full local leaderboards, sort player stats, and put it all together in a racing game!

## Verse Language Features Used

- Class: This example creates a persistable Verse class that tracks a group of stats for a per player.
- Constructor: A constructor is a special function that creates an instance of the class it is associated with.
- weak_map: A weak_map is a simple map that cannot be iterated over. Verse persistable data is required to be stored in a weak_map.

## Setting Up the Level

This example uses the following props and devices:

- 3 x [Billboard Device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-billboard-devices-in-fortnite-creative): These will display each player’s lifetime stats, and you’ll sort them based on lifetime points to show off the best players in the lobby.
- 3 x [Player Reference Device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-player-reference-devices-in-fortnite-creative): In combination with the billboards, player references will put a face to the name of your top performers so other players know who to look out for during the game.
- 3 x [Checkpoint Device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-race-checkpoint-devices-in-fortnite-creative): These are the checkpoints players race through to complete the race.
- 1 x [Race Manager Device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-race-manager-devices-in-fortnite-creative): This tracks when players start and end the race, and awards them points based on their finish placement.
- 1 x [Pickup Truck Spawner Device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-pickup-truck-spawner-devices-in-fortnite-creative): This spawns the vehicle you’ll use during the race, but you can change this to any vehicle to suit your experience.

To set up your level, follow these steps:

### Billboards and Player References

To display player stats, you’ll use a combination of billboards and player references. Each billboard will display a player’s lifetime stats, while the player reference will show a visual representation of that player. To add these elements, follow these steps:

### Checkpoints, Pickup Truck, and Race Manager

Since this is a race, you’ll need something to race with! You’ll also need checkpoints to race through, and a race manager to direct the race during the game. To add these elements, follow these steps:

## Modifying your Stats Table

This example uses a modified version of the `player_stats_table` file from [Persistent Player Statistics](https://dev.epicgames.com/documentation/fortnite/persistent-player-statistics-in-unreal-editor-for-fortnite). This one will look similar to the file from that example, with some important differences that change the implementation.

Follow the steps below to create your player stats table:

## Managing Stats

Just like in [Persistent Player Statistics](https://dev.epicgames.com/documentation/fortnite/persistent-player-statistics-in-unreal-editor-for-fortnite), you’re going to use a manager file to handle managing and recording stat changes for players.

Follow the steps below to build your modified `player_stats_manager` file.

## Building Player Leaderboards

To display player data on your leaderboards, you’re going to need a few things. You need a way to update the text on the billboards and the players on the player reference devices. You also need a way to sort these devices, since you want the top players to be most prominent on your leaderboard. Because these functions have a similar goal of modifying devices in the level, it’s a good idea to group the functions in a common file.

Follow the steps below to create functions that update your devices in-level:

### Sorting and Displaying the Best Player

Before continuing, it’s important to consider how you want to sort these billboards. Do you want the player with the most points to be on top, or the player with the most wins? What if you want to sort by different stats? You need a method to handle all of these, and a [sorting algorithm](https://dev.epicgames.com/documentation/fortnite/sorting-algorithms-in-verse) is the answer. By using a sorting algorithm and a comparison function, you can specify what criteria you want to sort by. You can then sort your billboards and player references to display the top players in your experience. This example uses the [Merge Sort](https://dev.epicgames.com/documentation/fortnite/sorting-algorithms-in-verse) algorithm, but you are free to implement your own.

Follow the steps below to add comparison and sorting to your billboards, and finish updating devices in your level.

1. Back in your `player_stats_table` file, you’re going to define comparison functions for each of your stats. Each of these takes a `Left` and `Right` `player_and_stats` struct, and compares them based on a particular stat. These functions have the `<decides><transacts>` modifiers, so if the comparison fails the function will also fail. For example, letting you know that `Left` is less than `Right`. Add a new function named `MorePointsComparison()` to your **player_stats_table.verse** `file. This function checks if` Left.Points `is greater than` Right.Points`, and fails if not. If it succeeds, it returns` Left`.

   Verse

   ```
        # Returns Left if Left has greater Points than Right.
        MorePointsComparison<public>(Left:player_and_stats, Right:player_and_stats)<decides><transacts>:Left=
            Left.StatsTable.Points > Right.StatsTable.Points
            Left
   ```

    # Returns Left if Left has greater Points than Right.
   MorePointsComparison&lt;public&gt;(Left:player_and_stats, Right:player_and_stats)&lt;decides&gt;&lt;transacts&gt;:Left=
   Left.StatsTable.Points &gt; Right.StatsTable.Points
   Left
2. Copy this function three times, one for a less points comparison and two for comparing wins. Your comparison functions should look like the following:

   Verse

   ```
        # Returns Left if Left has greater Points than Right.
        MorePointsComparison<public>(Left:player_and_stats, Right:player_and_stats)<decides><transacts>:player_and_stats=
            Left.StatsTable.Points > Right.StatsTable.Points
            Left

        # Returns Left if Left has less Points than Right.
        LessPointsComparison<public>(Left:player_and_stats, Right:player_and_stats)<decides><transacts>:player_and_stats=
            Left.StatsTable.Points < Right.StatsTable.Points
            Left
   ```
3. Add the [Merge Sort](https://dev.epicgames.com/documentation/fortnite/sorting-algorithms-in-verse) algorithm. You can place this in a separate file or module and test the algorithm on the provided test file.
4. Back in `player_leaderboards`, add a new function `UpdateStatsBillboards()`. This function takes an array of agents and an array of billboards, sorts them, and calls `UpdateStatsBillboard()` to update each billboard in the level.

   Verse

   ```
        # Update the stats billboards by sorting them based on the amount of lifetime points
        # each player has.
        UpdateStatsBillboards<public>(Players:[]agent, StatsBillboards:[]billboard_device):void=
   ```

    # Update the stats billboards by sorting them based on the amount of lifetime points
   # each player has.
   UpdateStatsBillboards&lt;public&gt;(Players:[]agent, StatsBillboards:[]billboard_device):void=
5. In `UpdateStatsBillboards()`, initialize a new array variable of `player_and_stats` named `PlayerAndStatsArray`. Set this equal to the result of a `for` expression. In that `for` expression, for each `agent`, get the `player` for that `agent`, and retrieve their `player_stats_table` using `GetPlayerStats[]`. Then return a `player_and_stats` struct constructed from the `player` and their stats table.

   Verse

   ```
        UpdateStatsBillboards<public>(Players:[]agent, StatsBillboards:[]billboard_device):void=
            var PlayerAndStatsArray:[]player_and_stats =
                for:
                    Agent:Players
                    Player := player[Agent]
                    PlayerStats := GetPlayerStats[Player]
                do:
                    player_and_stats:
                        Player := Player
                        StatsTable := PlayerStats
   ```

    UpdateStatsBillboards&lt;public&gt;(Players:[]agent, StatsBillboards:[]billboard_device):void=
   var PlayerAndStatsArray:[]player_and_stats =
   for:
   Agent:Players
   Player := player[Agent]
   PlayerStats := GetPlayerStats[Player]
   do:
   player_and_stats:
   Player := Player
   StatsTable := PlayerStats
6. To sort your `PlayerAndStatsArray`, initialize a new variable `SortedPlayersAndStats` to the result of calling `MergeSort()`, passing the array and the `MorePointsComparison`. After sorting in a `for` expression, iterate through each element in `SortedPlayerAndStats`, storing the element index in a variable `PlayerIndex`. Use `PlayerIndex` to index into the `StatsBillboards` array, then call `UpdateStatsBillboard` passing the player and the billboard to update. Your complete `UpdateStatsBillboards()` function should look like this:

   Verse

   ```
        # Update the stats billboards by sorting them based on the amount of lifetime points
        # each player has.
        UpdateStatsBillboards<public>(Players:[]agent, StatsBillboards:[]billboard_device):void=
            var PlayerAndStatsArray:[]player_and_stats =
                for:
                    Agent:Players
                    Player := player[Agent]
                    PlayerStats := GetPlayerStats[Player]
                do:
                    player_and_stats:
   ```
7. To update your player references, you’re going to use a very similar function named `UpdatePlayerReferences()`. This function takes an array of `player_reference_device` instead of billboards, and instead of calling `UpdateStatsBillboard()` at the end, it calls `Register()` on the player reference device for each player. Copy your `UpdateStatsBillboard()` code into a new function `UpdatePlayerReferences()` with the above changes. Your complete `UpdatePlayerReferences()` function should look like this:

   Verse

   ```
        # Update the player references devices by sorting them based on the amount
        # of lifetime points each player has.
        UpdatePlayerReferences<public>(Players:[]player, PlayerReferences:[]player_reference_device):void=
            var PlayerAndStatsArray:[]player_and_stats =
                for:
                    Agent:Players
                    Player := player[Agent]
                    PlayerStats := GetPlayerStats[Player]
                do:
                    player_and_stats:
   ```

## Player Leaderboards in your Level

With everything set up, it’s time to show off your players! You’ll create a device to award points to players when they interact with the button, and sort player references and billboards so that the best players are front and center. Follow the steps below to create a Verse device to test leaderboards in your level:

1. Create a new Verse device named **player_leaderboards_example**. See [Create Your Own Device Using Verse](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite) for steps.
2. At the top of the `player_leaderboards_example class` definition, add the following fields:

   - An editable array of Player Reference devices named `PlayerReferences`. These provide visual representations of each player in the race.

     Verse

     ```
       # Visual representations of each player.
       @editable
       PlayerReferences:[]player_reference_device = array{}
     ```

      # Visual representations of each player.
     @editable
     PlayerReferences:[]player_reference_device = array{}
   - An editable array of Billboard devices named `Leaderboards`. These display each player’s stats on a billboard in the level.

     Verse

     ```
       # Billboards that display each player's stats.
       @editable
       Leaderboards:[]billboard_device = array{}
     ```

      # Billboards that display each player&#39;s stats.
     @editable
     Leaderboards:[]billboard_device = array{}
   - An editable Race Manager device named `RaceManager`. You’ll subscribe to events from the Race Manager to know when a player finishes the race.

     Verse

     ```
       # Tracks when players complete a race, with the players in the first spot being awarded a win.
       @editable
       RaceManager:race_manager_device = race_manager_device{}
     ```

      # Tracks when players complete a race, with the players in the first spot being awarded a win.
     @editable
     RaceManager:race_manager_device = race_manager_device{}
   - An editable integer named `PlacementRequiredForWin`. This is the placement a player needs to make to be awarded a win.

     Verse

     ```
       # The placement of a player must be at or below to award a win.
       @editable
       PlacementRequiredForWin:int = 1
     ```

      # The placement of a player must be at or below to award a win.
     @editable
     PlacementRequiredForWin:int = 1
   - An editable array of integers named `PointsPerPlace`. These are the number of points each player earns based on their placement.

     Verse

     ```
       # The number of points a player in each place earns.
       # Adjust this to award your players the desired amount of score
       # based on their placement.
       @editable
       PointsPerPlace:[]int = array{5, 3, 1}
     ```

      # The number of points a player in each place earns.
     # Adjust this to award your players the desired amount of score
     # based on their placement.
     @editable
     PointsPerPlace:[]int = array{5, 3, 1}
   - An integer variable named `CurrentFinishOrder`. This is the placement of the player who most recently completed the race.

     Verse

     ```
       # The spot of the player who just finished the race.
       # The first three players to finish the race will be awarded a win.
       var CurrentFinishOrder:int = 0
     ```

      # The spot of the player who just finished the race.
     # The first three players to finish the race will be awarded a win.
     var CurrentFinishOrder:int = 0

### Awarding Stats Based on Placement

When a player finishes the race, you want to update their stats based on their placement. Players who place well should receive a greater number of points, and players who had the best placements should receive a win.

Follow these steps to awards stats to players when they finish the race:

### Waiting for Players to Finish the Race

Now that you’ve got stat recording ready, you need to know when a player finishes the race to update their stats. To do this, you’ll listen for the race manager’s `RaceCompletedEvent()`. This event fires whenever any player finishes the race, so you’ll have to listen for it continuously in an async function.

### Linking it all Together

With your functions set up, it’s time to link them to your devices and get racing!

Follow these steps to link your logic to your devices:

Drag the **player_leaderboards_example** device into your level. Assign your player references to the **PlayerReferences** array, keeping note of the order. The device in the first index should correspond to the player reference for the top player, the second index for the second-best player, and so on. Do the same for leaderboards, making sure to keep them aligned with the player reference devices. Don’t forget to assign your Race Manager device as well!

[![Player Leaderboards Device Settings](https://dev.epicgames.com/community/api/documentation/image/3e0a49ec-bac6-42a2-95ae-975fe9f1b310?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e0a49ec-bac6-42a2-95ae-975fe9f1b310?resizing_type=fit)

## Testing Your Persistable Leaderboards

You can test your persistent data in an edit session, but this data will be reset when you exit and relaunch the session. To have your data persist across sessions, you’ll have to launch a [playtest session](https://dev.epicgames.com/documentation/en-us/fortnite-creative/adding-playtesters-in-fortnite-creative) and change certain settings in your [Island Settings](https://dev.epicgames.com/documentation/fortnite/island-settings-in-unreal-editor-for-fortnite). For info on setting up your island to test persistable data both in edit and playtest sessions, see [Testing with Persistent Data](https://dev.epicgames.com/documentation/fortnite/using-persistable-data-in-verse) and change certain settings in your Island Settings. For info on setting up your island to test persistable data both in edit and playtest sessions, see [Testing with Persistent Data](https://dev.epicgames.com/documentation/en-us/uefn/persistent-player-statistics-in-unreal-editor-for-fortnite).

After setting up your session, when you playtest your level, players finishing the race should be awarded points based on their placement. They should be awarded a win if their placement is high enough, and these stats should persist across play sessions. Players and their stats should be sorted, with the player who has the most points appearing in first place.

[![Leaderboards in lobby](https://dev.epicgames.com/community/api/documentation/image/5ff78378-73ec-4681-9279-14e36f883877?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5ff78378-73ec-4681-9279-14e36f883877?resizing_type=fit)

## On Your Own

By completing this guide, you’ve learned how to create leaderboards that display persistent player statistics in your level. You’ve also learned how to sort and update these leaderboards, making sure everyone knows who the best players are. Try to adapt this tutorial to your own experiences, and go show off the best of the best!

## Complete Code

### player_stats_table.verse

Verse

```
    # This file defines a player_stats_table, a collection of persistable player statistics.
    # It also contains functions to compare stats tables by each of the stats to order players
    # when sorting.

    using { /Fortnite.com/Devices }
    using { /Verse.org/Simulation }
    using { /UnrealEngine.com/Temporary/Diagnostics }

    # Structure for passing a player and their stats as arguments.
    player_and_stats<public> := struct:
```

### player_leaderboards.verse

Verse

```
    # This file contains the code that updates the billboards, player references, and UI on the island
    # to display a player's stats from their player stats table. It also handles adding wins and points to a
    # player's stats table.

    using { /Fortnite.com/Devices }
    using { /Verse.org/Simulation}

    # The message to display on the stats billboard.
    StatsMessage<localizes>(CurrentPlayer:message, Points:message, Wins:message):message=
        "{CurrentPlayer}:\n{Points}\n{Wins}"
```

### player_stats_manager.verse

Verse

```
    # This file handles the code for initializing, updating, and returning player_stats_tables
    # for each player. It also defines an abstract stat_type class to use for updating stats, and the
    # StatType module to use when displaying stats.

    using { /Fortnite.com/Devices }
    using { /Verse.org/Simulation }
    using { /UnrealEngine.com/Temporary/Diagnostics }

    # Return the player_stats_table for the provided Agent.
    GetPlayerStats<public>(Agent:agent)<decides><transacts>:player_stats_table=
```

### player_leaderboards_example.verse

Verse

```
    using { /Fortnite.com/Devices }
    using { /Verse.org/Simulation }
    using { /UnrealEngine.com/Temporary/Diagnostics }
    using { PlayerLeaderboard }

    # See https://dev.epicgames.com/documentation/en-us/uefn/create-your-own-device-in-verse for how to create a verse device.

    # A Verse-authored creative device that can be placed in a level
    player_leaderboards_example := class(creative_device):
        # Visual representations of each player.
```
