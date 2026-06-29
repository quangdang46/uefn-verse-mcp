## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/find

# (Input:[]t).Find extension

Learn technical details about the (Input:[]t).Find extension.

Returns the first index whose element in `Input` equals `ElementToFind`.
Fails if ElementToFind does not exist in the array.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).Find<public>(ElementToFind:t where t:comparable):int`

## Parameters

`Find` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `ElementToFind` | `t` |  |
| `t` | `comparable` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `Find` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
