## https://dev.epicgames.com/documentation/en-us/fortnite/custom-round-logic-using-verse

# Custom Round Logic

Learn how to save information that persists across rounds and reset the persistent data when the multi-round game ends or a player leaves the session.

![Custom Round Logic](https://dev.epicgames.com/community/api/documentation/image/6feea1b9-bf7a-41ef-a934-f7f66a25137d?resizing_type=fill&width=1920&height=335)

In racing games, it's common for players to have a different start position based on how well they performed in a previous round. It encourages players to finish the race quickly even when they aren’t in first place so they start ahead of the other players.

[![](https://dev.epicgames.com/community/api/documentation/image/d935ffbb-dacf-4c7b-8fc4-796132f566a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d935ffbb-dacf-4c7b-8fc4-796132f566a9?resizing_type=fit)

To accomplish this, the game needs to know what round the players are currently in and the racer finish order must persist across all the rounds – but not across all game sessions. A session weak map variable in Verse resets its data every round, so this round information has to be stored with each player, using a [player weak map variable](https://dev.epicgames.com/documentation/fortnite/using-persistable-data-in-verse), and reset after the game ends.

Currently, a project can only have up to two player weak map variables. If your project already has a player weak map variable, it’s a good idea to have the second one record the round information to differentiate the data that should always persist from the data that you’ll reset after the game ends or a player leaves the session.

It's also important to know what round the players are currently on to apply round-specific logic and reset the round info on the last round. There’s currently no API for getting the current round, so this information needs to be recorded in the persistable data for each player as well.

In summary, you will need a player weak map variable that has at least the following information:

- Finish order
- Last completed round

The following sections show you how to set up this data and round-logic. You can find the complete code at the end of the page.

## Record Last Completed Round

Follow these steps to set up the persistable data for each player and record the last completed round.

1. Create a persistable class named `player_circuit_info` to store player info across rounds. This class should have the fields to represent the player’s last finish order, `LastRoundFinishOrder`, and their last completed round, `LastCompletedRound`. These fields are initialized with `-1` to represent invalid values, so you know when these fields actually contain useful information.

   Verse

   ```
        # Tracks the number of and in what order a player finished the previous round.
        player_circuit_info<public> := class<final><persistable>:
            Version:int = 0
            LastRoundFinishOrder:int = -1
            LastCompletedRound<public>:int = -1
   ```

    # Tracks the number of and in what order a player finished the previous round.
   player_circuit_info&lt;public&gt; := class&lt;final&gt;&lt;persistable&gt;:
   Version:int = 0
   LastRoundFinishOrder:int = -1
   LastCompletedRound&lt;public&gt;:int = -1
2. Create a player weak map variable using the `player_circuit_info` class to persist the round info with players.

   Verse

   ```
        # A persistable map that maps each player to
        # what order they finished the previous round.
        var CircuitInfo<public>:weak_map(player, player_circuit_info) = map{}
   ```

    # A persistable map that maps each player to
   # what order they finished the previous round.
   var CircuitInfo&lt;public&gt;:weak_map(player, player_circuit_info) = map{}
3. As a best practice for working with persistable data, create a constructor for the persistable class to be able to update the info for each player easily. For more details, see [using constructors for partial updates](https://dev.epicgames.com/documentation/fortnite/using-persistable-data-in-verse).

   Verse

   ```
        # Creates a new player_circuit_info from the given older player_circuit_info.
        MakePlayerCircuitInfo<constructor>(OldPlayerCircuitInfo:player_circuit_info)<transacts> := player_circuit_info:
            Version := OldPlayerCircuitInfo.Version
            LastRoundFinishOrder := OldPlayerCircuitInfo.LastRoundFinishOrder
            LastCompletedRound := OldPlayerCircuitInfo.LastCompletedRound
   ```

    # Creates a new player_circuit_info from the given older player_circuit_info.
   MakePlayerCircuitInfo&lt;constructor&gt;(OldPlayerCircuitInfo:player_circuit_info)&lt;transacts&gt; := player_circuit_info:
   Version := OldPlayerCircuitInfo.Version
   LastRoundFinishOrder := OldPlayerCircuitInfo.LastRoundFinishOrder
   LastCompletedRound := OldPlayerCircuitInfo.LastCompletedRound
4. Now that you’ve defined structures for this data, add a function to record a player’s finish order and update their persistent data. This function uses the constructor made in the previous step to partially update the data for the only information you’re concerned with: the finish order.

   Verse

   ```
        # Creates a new player_circuit_info for the given player with the order they finished the round in.
        RecordPlayerFinishOrder<public>(Agent:agent, FinishOrder:int)<decides><transacts>:void=
            Player := player[Agent]
            Player.IsActive[]
            PlayerCircuitInfo:player_circuit_info = if:
                Info := CircuitInfo[Player]
            then:
                Info
            else:
                player_circuit_info{}
   ```
5. Create another function to update only the last completed round for the player.

   Verse

   ```
        # Updates a player's player_circuit_info with their last completed round.
        UpdateRound<public>(Agent:agent, CompletedRound:int)<decides><transacts>:void=
            Player := player[Agent]
            Player.IsActive[]
            PlayerCircuitInfo := CircuitInfo[Player]
            set CircuitInfo[Player] = player_circuit_info:
                MakePlayerCircuitInfo<constructor>(PlayerCircuitInfo)
                LastCompletedRound := CompletedRound
   ```

    # Updates a player&#39;s player_circuit_info with their last completed round.
   UpdateRound&lt;public&gt;(Agent:agent, CompletedRound:int)&lt;decides&gt;&lt;transacts&gt;:void=
   Player := player[Agent]
   Player.IsActive[]
   PlayerCircuitInfo := CircuitInfo[Player]
   set CircuitInfo[Player] = player_circuit_info:
   MakePlayerCircuitInfo&lt;constructor&gt;(PlayerCircuitInfo)
   LastCompletedRound := CompletedRound
6. Now that you can record the last completed round for the player, create a function to calculate the last completed round for the game by checking which players have the latest recorded round. You need to check all players to account for players that may have joined the session in progress. The last completed round variable is initialized with `-1` to represent invalid data. If any players have a value greater than `-1` then a round has already finished.

   Verse

   ```
        # Returns the highest last completed round among all players.
        GetLastCompletedRound<public>(Players:[]player, TotalRounds:int)<transacts>:int=
            var LastCompletedRound:int = -1
            for:
                Player : Players
                Player.IsActive[]
                PlayerCircuitInfo := CircuitInfo[Player]
            do:
                # Update LastCompletedRound if this player has the highest last completed round.
                else if:
   ```
7. Create a Verse device to test that the round and player finish order is working as expected. Make sure your project is set up for multiple rounds, by setting the Total Rounds property in [Island Settings](https://dev.epicgames.com/documentation/fortnite/island-settings-in-unreal-editor-for-fortnite).

   Verse

   ```
        # A Verse-authored creative device that can be placed in a level
        test_round_info_device := class(creative_device):

            # Runs when the device is started in a running game
            OnBegin<override>()<suspends>:void=
                Players := GetPlayspace().GetPlayers()
                CurrentRound := GetLastCompletedRound(Players) + 1
                Print("Current round is {CurrentRound}")

                for:
   ```

## Reset Round Info on Player Leaving

The player's persistent data for round information should be reset when a player leaves during the game. You can subscribe to the playspace’s PlayerRemovedEvent to know when they leave.

Follow these steps to reset round information when a player leaves:

## Reset Round Info on Game End

The `OnBegin` function for a Verse device runs at the start of every round. This is a good time to determine if a player has unexpected persistent data, such as if their last completed round is the same as the total number of rounds. If so, you need to reset the data for the player. There is currently no API for knowing the total number of rounds in a game. Instead, you’ll need to add an editable property to the Verse device for the total rounds in the Verse code and make sure it matches the Total Rounds property in [Island Settings](https://dev.epicgames.com/documentation/fortnite/island-settings-in-unreal-editor-for-fortnite).

Follow these steps to reset the round info when the game has ended:

## Adding Logic Based on Current Round

Now, you can use this information to have custom logic depending on which round the players are in. For example, you could show a [local leaderboard](https://dev.epicgames.com/documentation/fortnite/make-your-own-ingame-leaderboard-in-verse) for the first round of a game.

Calling `GetLastCompletedRound()` every time you need to know which round is being played isn’t ideal. Instead, you can do this once per round and record the round info in a session weak map variable so all Verse code in the project can access this value at any time without needing to recompute it every time.

This is a great example to show the differences and reasoning for using the session weak map variable and player weak map variable in your code:

- **Session weak map variables** are useful for singletons and storing data for the current round that you don’t want to recompute every time.
- The **player weak map variables** are designed for information that needs to persist across multiple rounds and game sessions but must be associated with individual players.

Follow these steps to set up a session weak map variable for storing the current round.

Now that this info is stored in a session weak map variable, you can easily add custom logic for rounds. For example, you can check if it’s the first round and set up a lobby and leaderboard viewing area for the players.

Verse

```
# Returns true if this is the first round of the game.
IsFirstRound<public>(RoundToCheck:int)<decides><transacts>:void=
    RoundToCheck <= 0
```

# Returns true if this is the first round of the game.
IsFirstRound<public>(RoundToCheck:int)<decides><transacts>:void=
RoundToCheck <= 0

## On Your Own

Check out [Speedway Race with Verse Persistence](speedway-race-with-verse-persistence-in-unreal-editor-for-fortnite) for how to use this code in a racing game for determining the start order of players.

After checking out the template, try the following:

- Add additional round information, for example which vehicle is assigned to the player.
- Teleport players to different areas of the map at the beginning of each round.

What other games can you think of that use round-specific logic?

## Complete Code

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

# A persistable map that maps each player to
# what order they finished the previous round.
var CircuitInfo<public>:weak_map(player, player_circuit_info) = map{}

# Maps the current session to its associated round info.
var RoundInfo:weak_map(session, round_info) = map{}
```
