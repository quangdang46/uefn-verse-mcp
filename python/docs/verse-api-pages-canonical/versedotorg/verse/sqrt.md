## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/sqrt

# Sqrt function

Learn technical details about the Sqrt function.

Returns the square root of `X` if `X >= 0.0`.
Returns `NaN` if `X < 0.0`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Sqrt<public><native>(X:float):float`

## Parameters

`Sqrt` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `X` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Sqrt` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
