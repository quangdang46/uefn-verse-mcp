## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/fort_round_manager

# fort_round_manager interface
Learn technical details about the fort_round_manager interface.
This interface is implemented by the round manager living on the simulation entity.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Game }`
## Members
This interface has functions, but no data members.
### Functions
Function Name | Description
---|---
[`SubscribeRoundStarted`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/fort_round_manager/subscriberoundstarted) |  Subscribed callbacks will be invoked in two scenarios:
  * When a new Fortnite round starts
  * If a round is ongoing, your callback will be invoked immediately Upon the round ending, all callbacks will be canceled

[`SubscribeRoundEnded`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/fort_round_manager/subscriberoundended) |  Subscribed callbacks will be invoked when a Fortnite round ends
