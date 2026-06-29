## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/lerp

# Lerp function

Learn technical details about the Lerp function.

Used to linearly interpolate/extrapolate between `From` (when `Parameter = 0.0`) and `To` (when `Parameter = 1.0`). Expects that all arguments are finite.
Returns `From*(1 - Parameter) + To*Parameter`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SpatialMath }` |

`Lerp<public>(From:vector3, To:vector3, Parameter:float):`[`vector3`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/vector3)

## Parameters

`Lerp` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `From` | `vector3` |  |
| `To` | `vector3` |  |
| `Parameter` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Lerp` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
