## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/guard_spawner_visibility_range_restriction

# guard_spawner_visibility_range_restriction enumeration

Learn technical details about the guard_spawner_visibility_range_restriction enumeration.

Used with `guard_spawner_device.VisibilityRangeRestriction` to define how the guard uses `guard_spawner_device.VisibilityRange`

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Enumerators

The `guard_spawner_visibility_range_restriction` enumeration includes the following enumerators:

| Name | Description |
| --- | --- |
| `OnlyWhenUnaware` | The NPC only uses its `VisibilityRange` when it does not have a target. Otherwise, the guard has an infinite range. |
| `Always` | The NPC uses its `VisibilityRange` both when it is unaware and when it has a target. |
