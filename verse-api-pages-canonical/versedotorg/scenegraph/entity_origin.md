## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/scenegraph/entity_origin

# interactable_success_limit class
Learn technical details about the interactable_success_limit class.
Used to set a limit of times to interact.
|
---|---
Verse `using` statement | `using { /Verse.org/SceneGraph }`
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`MaxSuccessfulInteractions` | `??int` |  The number of times the component can be successfully interacted with. A value of false is unlimited. When SuccessfulInteractionCount reaches MaxSuccessfulInteractions all active interactions are canceled, and the component cannot be interacted with.
`SuccessfulInteractionCount` | `?int` |  The number of times this component has had a successful interaction.
### Functions
Function Name | Description
---|---
[`ClearSuccessfulInteractionCount`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_success_limit/clearsuccessfulinteractioncount) |  Resets the counter for the times this component has had a successful interaction.
