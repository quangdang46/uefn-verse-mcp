## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/replacefirstelement

# (Input:[]t).ReplaceFirstElement extension

Learn technical details about the (Input:[]t).ReplaceFirstElement extension.

Makes an `array` by replacing the element at the lowest index that equals `ElementToReplace` with `ElementToReplaceWith` in `Input`.
Fails if `Input` did not contain any instances of `ElementToReplace`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).ReplaceFirstElement<public>(ElementToReplace:t, ElementToReplaceWith:t where t:comparable):[]t`

## Parameters

`ReplaceFirstElement` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `ElementToReplace` | `t` |  |
| `ElementToReplaceWith` | `t` |  |
| `t` | `comparable` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `ReplaceFirstElement` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
