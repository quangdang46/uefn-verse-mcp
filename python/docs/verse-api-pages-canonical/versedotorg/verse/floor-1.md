## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/floor-1

# Floor function

Learn technical details about the Floor function.

Returns the largest `int` that is less than or equal to `Val`.
Fails if `not IsFinite(Val)`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Floor<public><native>(Val:float):int`

## Parameters

`Floor` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Val` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Floor` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
