## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/remove

# (Input:[]t).Remove extension

Learn technical details about the (Input:[]t).Remove extension.

Makes an `array` by removing `Input`'s elements from `StartIndex` to `StopIndex-1`.
Succeeds if `0 <= StartIndex <= StopIndex <= Input.Length`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).Remove<public>(StartIndex:int, StopIndex:int where t:any):[]t`

## Parameters

`Remove` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `StartIndex` | `int` |  |
| `StopIndex` | `int` |  |
| `t` | `any` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `Remove` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
