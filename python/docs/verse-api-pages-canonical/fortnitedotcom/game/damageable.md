## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/damageable

# damageable interface

Learn technical details about the damageable interface.

Implemented by Fortnite objects that can be damaged.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Game }` |

## Members

This interface has functions, but no data members.

### Functions

| Function Name | Description |
| --- | --- |
| [`Damage`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/game/damageable/damage) | Damage the `damageable` object anonymously by `Amount`. Setting `Amount` to less than 0 will cause no damage. Use `Damage(:damage_args):void` when damage is being applied from a known instigator and source. |
| [`Damage`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/game/damageable/damage-1) | Damage the `damageable` object by `Args.Amount`. Setting `Amount` to less than 0 will cause no damage. |
| [`DamagedEvent`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/game/damageable/damagedevent) | Signaled when damage is applied to the `damageable` object. |
