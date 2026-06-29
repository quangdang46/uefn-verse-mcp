## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/join

# Join function

Learn technical details about the Join function.

Makes a `message` by concatenating `Separator` between the elements of `Messages`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`Join<public><native>(Messages:[]message, Separator:message)<transacts>:`[`message`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/message)

## Parameters

`Join` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Messages` | `[]message` |  |
| `Separator` | `message` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `Join` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |

### Effects

The following effects determine how `Join` behaves in your programs. For the complete list of effects, see the Effect Specifers section of the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Effect | Meaning |
| --- | --- |
| `transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You’ll be notified when you compile your code if the `transacts` effect was added to a function that can’t be rolled back. Note that this check is not done for functions with the `native` specifier. |
