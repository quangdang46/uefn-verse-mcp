## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/scenegraph/findsweephits-2

# (Entity:entity).FindSweepHits extension

Learn technical details about the (Entity:entity).FindSweepHits extension.

Find all objects in the scene that would intersect Volume if they were swept from GlobalTransform along the Displacement vector Hits are sorted by hit distance. NOTE: This entity defines the context(scene) for the query but does not otherwise take part in the sweep.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SceneGraph }` |

`(Entity:entity).FindSweepHits<public>(Displacement:vector3, StartGlobalTransform:transform, Volume:collision_volume)<transacts>:generator(sweep_hit)`

## Parameters

`FindSweepHits` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Entity` | `entity` |  |
| `Displacement` | `vector3` |  |
| `StartGlobalTransform` | `transform` |  |
| `Volume` | `collision_volume` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `FindSweepHits` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |

### Effects

| Effect | Meaning |
| --- | --- |
| `transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You’ll be notified when you compile your code if the `transacts` effect was added to a function that can’t be rolled back. Note that this check is not done for functions with the `native` specifier. |
