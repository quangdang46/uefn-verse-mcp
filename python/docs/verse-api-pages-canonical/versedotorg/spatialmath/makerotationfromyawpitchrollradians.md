## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makerotationfromyawpitchrollradians

# MakeRotationFromYawPitchRollRadians function

Learn technical details about the MakeRotationFromYawPitchRollRadians function.

Makes a `rotation` by applying a pre-rotation of `YawAngle` followed by `PitchAngle` and then `RollAngle`, in that order:

- *yaw* is right-handed rotation about the Down axis,
- *pitch* is right-handed rotation about the Right axis,
- *roll* is right-handed rotation about the Forward axis.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SpatialMath }` |

`MakeRotationFromYawPitchRollRadians<public>(YawAngle:float, PitchAngle:float, RollAngle:float):`[`rotation`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/rotation)

## Parameters

`MakeRotationFromYawPitchRollRadians` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `YawAngle` | `float` |  |
| `PitchAngle` | `float` |  |
| `RollAngle` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `MakeRotationFromYawPitchRollRadians` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
