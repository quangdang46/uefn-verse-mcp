## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/clamp

# Clamp function

Learn technical details about the Clamp function.

Constrains the value of `Val` between `A` and `B`. Robustly handles different argument orderings.
Returns the median of `Val`, `A`, and `B`, such that comparisons with `NaN` operate as if `NaN > +Inf`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Clamp<public>(Val:float, A:float, B:float):float`

## Parameters

`Clamp` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Val` | `float` |  |
| `A` | `float` |  |
| `B` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Clamp` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
