## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/tostring

# ToString function

Learn technical details about the ToString function.

Makes a `string` representation of `rotation` in axis/degrees format with a right-handed sign convention.
`ToString(MakeRotationRadians(vector3{Left:=0.0, Up:=0.0, Forward:=1.0}, PiFloat/2.0))` produces the string: `"{Axis = {Left=0.000000, Up=0.000000, Forward=1.000000}, Angle = 90.000000}"`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SpatialMath }` |

`ToString<public>(Rotation:rotation):[]char`

## Parameters

`ToString` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Rotation` | `rotation` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `ToString` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
