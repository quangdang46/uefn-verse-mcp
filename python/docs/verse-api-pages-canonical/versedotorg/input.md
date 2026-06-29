## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/input

# Input module

Learn technical details about the Input module.

Module import path: /Verse.org/Input

- [`Verse.org`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg)
- **`Input`**

  - [`Gameplay`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/gameplay)
  - [`UI`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/ui)

## Classes and Structs

| Name | Description |
| --- | --- |
| [`input_events(t)`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/input_events/input_events(t)) | Input_events is a container for user input events which can be subscribed to.   - Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player. - Low-level notifications of current user input: BeginDetectEvent, DetectionOngoingEvent, and EndDetectEvent. - High-level notifications of triggered events: TriggerActivationEvent and CancelActivationEvent.  /—----------<-------\   BeginDetectEvent -> DetectionOngoingEvent -> TriggerActivationEvent -> EndDetectEvent   /\ /\ /   ---------------------> CancelActivationEvent ----------------------/ |
| [`player_input`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/player_input) | The per-player input manager. Get one for a player with 'GetPlayerInput', then use it to:  *Turn input mappings on or off for that player with 'AddInputMapping' / 'RemoveInputMapping'.*  Get the 'input_events' object for an 'input_action' with 'GetInputEvents', and subscribe to its events to react to that input. An input_action only generates events for a player while at least one input_mapping that references it is active on that player. |
| [`deproject_results`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/deproject_results) | Holds the world-space ray produced by deprojecting a viewport coordinate. |

## Functions

| Name | Description |
| --- | --- |
| [`GetPlayerInput`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/getplayerinput) | Access input-related data and settings for a player. |
| [`input_events`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/input_events) | Input_events is a container for user input events which can be subscribed to.   - Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player. - Low-level notifications of current user input: BeginDetectEvent, DetectionOngoingEvent, and EndDetectEvent. - High-level notifications of triggered events: TriggerActivationEvent and CancelActivationEvent.  /—----------<-------\   BeginDetectEvent -> DetectionOngoingEvent -> TriggerActivationEvent -> EndDetectEvent   /\ /\ /   ---------------------> CancelActivationEvent ----------------------/ |

## Enumerations

| Name | Description |
| --- | --- |
| [`input_method`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/input_method) | Represents the player's current preferred input method. |
