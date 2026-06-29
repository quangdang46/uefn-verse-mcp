## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/slice-1

# (Input:[]t).Slice extension

Learn technical details about the (Input:[]t).Slice extension.

Makes an `array` containing `Input`'s elements from `StartIndex` to `Input.Length-1`.
Succeeds if `0 <= StartIndex <= Input.Length`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).Slice<public>(StartIndex:int where t:any):[]t`

## Parameters

`Slice` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `StartIndex` | `int` |  |
| `t` | `any` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `Slice` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
