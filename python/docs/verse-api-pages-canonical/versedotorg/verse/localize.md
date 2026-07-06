## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/localize

# Localize function

Learn technical details about the Localize function.

Makes a `string` by localizing `Message` based on the current `locale`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Localize<public><native>(Message:message):[]char`

## Parameters

`Localize` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Message` | `message` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Localize` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
