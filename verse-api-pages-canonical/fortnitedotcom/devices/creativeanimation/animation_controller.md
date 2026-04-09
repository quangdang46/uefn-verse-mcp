## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/animation_controller

# GrantItemIndex function
Learn technical details about the GrantItemIndex function.
Grants an item at a specific `ItemIndex` to an `Agent`. `Index` should be between `0` and the available item count - 1. If Value is out of bounds, which item is granted is determined by _Cycle Behavior_.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
`GrantItemIndex<public>(Agent:agent, ItemIndex:int)<transacts><no_rollback>:void`
## Parameters
`GrantItemIndex` takes the following parameters:
Name | Type | Description
---|---|---
`Agent` | `agent` |
`ItemIndex` | `int` |
## Attributes, Specifiers, and Effects
### Specifiers
The following specifiers determine how you can interact with `GrantItemIndex` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).
Specifier | Meaning
---|---
`public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data.
### Effects
The following effects determine how `GrantItemIndex` behaves in your programs. For the complete list of effects, see the Effect Specifers section of the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).
Effect | Meaning
---|---
`transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You’ll be notified when you compile your code if the `transacts` effect was added to a function that can’t be rolled back. Note that this check is not done for functions with the `native` specifier.
`no_rollback` | This is the default effect when no exclusive effect is specified. The `no_rollback` effect indicates that any actions performed by the function cannot be undone and so the function cannot be used in a failure context. This effect cannot be manually specified.
