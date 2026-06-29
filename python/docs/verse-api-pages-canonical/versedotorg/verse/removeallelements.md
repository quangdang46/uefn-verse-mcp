## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/removeallelements

# (Input:[]t).RemoveAllElements extension

Learn technical details about the (Input:[]t).RemoveAllElements extension.

Makes an `array` by removing all elements that equal `ElementToRemove` from `Input`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).RemoveAllElements<public>(ElementToRemove:t where t:comparable):[]t`

## Parameters

`RemoveAllElements` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `ElementToRemove` | `t` |  |
| `t` | `comparable` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `RemoveAllElements` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
