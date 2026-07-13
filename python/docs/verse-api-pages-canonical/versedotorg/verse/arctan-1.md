## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/arctan-1

# ArcTan function

Learn technical details about the ArcTan function.

Returns the angle in radians at the origin between a ray pointing to `(X, Y)` and the positive `X` axis such that `-PiFloat < ArcTan(Y, X) <= PiFloat`.
Returns `0.0` if `X=0.0 and Y=0.0`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`ArcTan<public><native>(Y:float, X:float):float`

## Parameters

`ArcTan` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Y` | `float` |  |
| `X` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `ArcTan` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
