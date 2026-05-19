## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/damage_args

# damage_args struct
Learn technical details about the damage_args struct.
Parameters for common damage functions on Fortnite objects.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Game }`
## Members
This struct has data members, but no functions.
### Data
Data Member Name | Type | Description
---|---|---
`Instigator` | `?game_action_instigator` |  Player, agent, etc. that instigated the damage to the object.
`Source` | `?game_action_causer` |  Player, weapon, vehicle, etc. that damaged the object.
`Amount` | `float` |  Amount of damage to apply to the object.
