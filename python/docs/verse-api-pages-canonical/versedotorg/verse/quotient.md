## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/quotient

# Quotient function

Learn technical details about the Quotient function.

Returns the quotient `X/Y` as defined by Euclidean division, i.e.:

- `Quotient[X/Y] = Floor[X/Y]` when `Y > 0`
- `Quotient[X/Y] = Ceil[X/Y]` when `Y < 0`
- `Quotient[X/Y] * Y + Mod[X,Y] = X`
  Fails if `Y = 0`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Quotient<public><native>(X:int, Y:int):int`

## Parameters

`Quotient` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `X` | `int` |  |
| `Y` | `int` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Quotient` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
