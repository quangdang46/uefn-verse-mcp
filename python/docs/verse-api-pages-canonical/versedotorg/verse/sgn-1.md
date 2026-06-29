## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/sgn-1

# Sgn function

Learn technical details about the Sgn function.

Returns the sign of `Val`:

- `1.0` if `Val > 0.0`
- `0.0` if `Val = 0.0`
- `-1.0` if `Val < 0.0`
- `NaN` if `Val = NaN`

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Sgn<public>(Val:float):float`

## Parameters

`Sgn` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Val` | `float` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Sgn` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
