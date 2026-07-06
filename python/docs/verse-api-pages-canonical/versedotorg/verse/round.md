## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/round

# Round function

Learn technical details about the Round function.

Returns `Val` rounded to the nearest `int`. When the fractional part of `Val` is `0.5`, rounds to the nearest *even* `int` (per the IEEE-754 default rounding mode).
Fails if `not IsFinite(Val)`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Round<public><native>(Val:float):int`

## Parameters

`Round` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Val` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Round` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
