## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/getyawpitchrollradians

# (Rotation:rotation).GetYawPitchRollRadians extension

Learn technical details about the (Rotation:rotation).GetYawPitchRollRadians extension.

Makes a `tuple(float, float, float)` with three elements:

- *yaw* of `rotation` in radians
- *pitch* of `rotation` in radians
- *roll* of `rotation` in radians
  using the conventions of `MakeRotationFromYawPitchRollRadians`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SpatialMath }` |

`(Rotation:rotation).GetYawPitchRollRadians<public>():(float, float, float)`

## Parameters

`GetYawPitchRollRadians` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Rotation` | `rotation` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `GetYawPitchRollRadians` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
