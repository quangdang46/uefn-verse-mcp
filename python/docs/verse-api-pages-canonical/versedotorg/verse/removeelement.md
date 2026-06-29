## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/removeelement

# (Input:[]t).RemoveElement extension

Learn technical details about the (Input:[]t).RemoveElement extension.

Makes an `array` by removing the element at `IndexToRemove` from `Input`.
Succeeds if `0 <= IndexToRemove <= Input.Length-1`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).RemoveElement<public>(IndexToRemove:int where t:any):[]t`

## Parameters

`RemoveElement` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `IndexToRemove` | `int` |  |
| `t` | `any` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `RemoveElement` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
