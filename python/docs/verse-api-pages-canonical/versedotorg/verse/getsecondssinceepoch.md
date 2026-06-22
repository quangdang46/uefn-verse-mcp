## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/getsecondssinceepoch

# GetSecondsSinceEpoch function

Learn technical details about the GetSecondsSinceEpoch function.

Returns the number of seconds since January 1, 1970 UTC, ignoring leap seconds. I.e, this function implements Unix time. This function always returns the same value within the same transaction.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`GetSecondsSinceEpoch<public><native>():float`

## Parameters

`GetSecondsSinceEpoch` does not take any parameters.

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `GetSecondsSinceEpoch` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
