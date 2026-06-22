## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ai/guard_awareness_component/getalertlevel

# GetAlertLevel function

Learn technical details about the GetAlertLevel function.

Get the current alert level for a specific target.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/AI }` |

`GetAlertLevel<public><native>(Target:entity):`[`guard_alert_level`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/guard_alert_level)

## Parameters

`GetAlertLevel` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Target` | `entity` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `GetAlertLevel` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
