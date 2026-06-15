## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/replaceelement

# (Input:[]t).ReplaceElement extension

Learn technical details about the (Input:[]t).ReplaceElement extension.

Makes an `array` by replacing the element at `IndexToReplace` with `ElementToReplaceWith` in `Input`.
Succeeds if `0 <= IndexToReplace <= Input.Length-1`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).ReplaceElement<public>(IndexToReplace:int, ElementToReplaceWith:t where t:any):[]t`

## Parameters

`ReplaceElement` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `IndexToReplace` | `int` |  |
| `ElementToReplaceWith` | `t` |  |
| `t` | `any` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `ReplaceElement` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
