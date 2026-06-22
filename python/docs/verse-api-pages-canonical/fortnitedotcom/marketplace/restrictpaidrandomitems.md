## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/marketplace/restrictpaidrandomitems

# RestrictPaidRandomItems function

Learn technical details about the RestrictPaidRandomItems function.

Informs if usage of paid random items is restricted for `Player`
due to platform, territory, age, or user configuration restrictions.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Marketplace }` |

`RestrictPaidRandomItems<public><native>(Player:player):void`

## Parameters

`RestrictPaidRandomItems` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Player` | `player` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `RestrictPaidRandomItems` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
