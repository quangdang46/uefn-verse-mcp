## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/concurrency/awaitable

# awaitable function

Learn technical details about the awaitable function.

A parametric interface implemented by events with a `payload` that can be waited on. Matched with `signalable.`

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Concurrency }` |

`awaitable<public>(payload:any):awaitable(payload)`

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.

## Parameters

`awaitable` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `payload` | `any` |  |

### Generated Interface

`awaitable` returns the parametric interface [`awaitable(payload)`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/concurrency/awaitable/awaitable(payload)).

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `awaitable` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
