## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/todiagnostic

# ToDiagnostic function

Learn technical details about the ToDiagnostic function.

Converts any Verse value into an opaque diagnostic message.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`ToDiagnostic<public><native>(Value:any):`[`diagnostic`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/diagnostic)

## Parameters

`ToDiagnostic` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Value` | `any` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `ToDiagnostic` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
