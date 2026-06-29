## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/getupaxis

# (Rotation:rotation).GetUpAxis extension

Learn technical details about the (Rotation:rotation).GetUpAxis extension.

Makes a unit `vector3` pointing in the *up* rotated direction.
This is equivalent to: `vector3{Forward:=0.0, Left:=0.0, Up:=1.0} * Rotation`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SpatialMath }` |

`(Rotation:rotation).GetUpAxis<public>():`[`vector3`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/vector3)

## Parameters

`GetUpAxis` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Rotation` | `rotation` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `GetUpAxis` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
