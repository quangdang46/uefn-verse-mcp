## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/clamp-1

# Clamp function

Learn technical details about the Clamp function.

Constrains the value of `Val` between `A` and `B`. Robustly handles different argument orderings.
Returns the median of `Val`, `A`, and `B`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Clamp<public><native>(Val:int, A:int, B:int):int`

## Parameters

`Clamp` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Val` | `int` |  |
| `A` | `int` |  |
| `B` | `int` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Clamp` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
