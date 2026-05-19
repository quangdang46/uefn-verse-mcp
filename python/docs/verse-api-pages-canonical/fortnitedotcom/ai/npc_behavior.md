## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ai/npc_behavior

# npc_behavior class
Learn technical details about the npc_behavior class.
Inherit from this to create a custom NPC behavior. The npc_behavior can be defined for a character in a CharacterDefinition asset, or in a npc_spawner_device.
|
---|---
Verse `using` statement | `using { /Fortnite.com/AI }`
## Members
This class has functions, but no data members.
### Functions
Function Name | Description
---|---
[`OnBegin`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ai/npc_behavior/onbegin) |  This function is called when the NPC is added to the simulation.
[`OnEnd`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ai/npc_behavior/onend) |  This function is called when the NPC is removed from the simulation.
[`GetAgent`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ai/npc_behavior/getagent) |  Returns the agent associated with this behavior.
[`GetEntity`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ai/npc_behavior/getentity) |  Returns the entity associated with this behavior.
