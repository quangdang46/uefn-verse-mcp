## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/fortplayerutilities/getspectatedagent

# (InAgent:agent).GetSpectatedAgent extension

Learn technical details about the (InAgent:agent).GetSpectatedAgent extension.

Returns the agent a spectator is currently spectating, fails if the spectator isn't spectating or isn't spectating an agent.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/FortPlayerUtilities }` |

`(InAgent:agent).GetSpectatedAgent<public><native>():`[`agent`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/agent)

## Parameters

`GetSpectatedAgent` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `InAgent` | `agent` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `GetSpectatedAgent` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
