## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/spatialmath/fromscalarvector3-1

# FromScalarVector3 function

Learn technical details about the FromScalarVector3 function.

Util function for converting a scalar `vector3` from /Verse.org/SpatialMath to a `vector3` from /UnrealEngine.com/Temporary/SpatialMath.
Use this function when your vector indicates a magnitude on each axis but not a direction, such as when you convert a scale measurement rather than a translation or position.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /UnrealEngine.com/Temporary/SpatialMath }` |

`FromScalarVector3<public>(InVector3:vector3):`[`vector3`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/spatialmath/vector3)

## Parameters

`FromScalarVector3` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `InVector3` | `vector3` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `FromScalarVector3` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
