## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/err

# Err function

Learn technical details about the Err function.

Halts the Verse runtime with error `Message`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Err<public><native>(Message:[]char):false`

## Parameters

`Err` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Message` | `[]char` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Err` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
