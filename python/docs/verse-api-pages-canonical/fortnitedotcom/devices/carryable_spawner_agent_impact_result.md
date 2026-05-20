## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/carryable_spawner_agent_impact_result

# carryable_spawner_agent_impact_result struct

Learn technical details about the carryable_spawner_agent_impact_result struct.

Payload of `device_event_carryable_spawner_agent_impact`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Members

This struct has data members, but no functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `Target` | `?agent` | Agent impacted by the carryable. |
| `Source` | `?agent` | The agent responsible for the impact. Either the thrower, or if none exists, the agent who instigated the carryable to spawn. |
| `Damage` | `float` | Damage applied by the impact. |
| `ImpactedFromThrow` | `logic` | Whether the impact was a direct result of being thrown (as opposed to an indirect hit from bouncing or rolling). |
