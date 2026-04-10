## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/input

# Input module
Learn technical details about the Input module.
Module import path: /Verse.org/Input
  * [`Verse.org`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg)
  * **`Input`**
    * [`UI`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/ui)

## Classes and Structs
Name | Description
---|---
[`input_events(t)`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/input_events/input_events\(t\)) |  Input_events is a container for user input events which can be subscribed to.
  * Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player.
  * Low-level notifications of current user input: BeginDetectEvent, DetectionOngoingEvent, and EndDetectEvent.
  * High-level notifications of triggered events: TriggerActivationEvent and CancelActivationEvent. /—----------<-------\ BeginDetectEvent -> DetectionOngoingEvent -> TriggerActivationEvent -> EndDetectEvent /\ /\ / ---------------------> CancelActivationEvent ----------------------/

[`player_input`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/player_input) |  This is the main manager class for input-related settings and functions for a player.
## Functions
Name | Description
---|---
[`GetPlayerInput`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/getplayerinput) |  Access input-related data and settings for a player.
[`input_events`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/input_events) |  Input_events is a container for user input events which can be subscribed to.
  * Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player.
  * Low-level notifications of current user input: BeginDetectEvent, DetectionOngoingEvent, and EndDetectEvent.
  * High-level notifications of triggered events: TriggerActivationEvent and CancelActivationEvent. /—----------<-------\ BeginDetectEvent -> DetectionOngoingEvent -> TriggerActivationEvent -> EndDetectEvent /\ /\ / ---------------------> CancelActivationEvent ----------------------/
