## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/insert

# (Input:[]t).Insert extension

Learn technical details about the (Input:[]t).Insert extension.

Makes an `array` by inserting `ElementsToInsert` into `Input` such that the first element of `ElementsToInsert` is at `InsertionIndex`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(Input:[]t).Insert<public>(InsertionIndex:int, ElementsToInsert:[]t where t:any):[]t`

## Parameters

`Insert` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Input` | `[]t` |  |
| `InsertionIndex` | `int` |  |
| `ElementsToInsert` | `[]t` |  |
| `t` | `any` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `Insert` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
