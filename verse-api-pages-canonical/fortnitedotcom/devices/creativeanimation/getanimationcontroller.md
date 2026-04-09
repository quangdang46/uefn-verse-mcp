## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/getanimationcontroller

# GetItemGrantCountAtIndex function
Learn technical details about the GetItemGrantCountAtIndex function.
Returns the number of items this Item Granter will award for the item at the specified `Index`. This will return 0 if `Index` is invalid. If _Cycle Behavior_ is _Stop_ , `Index` is clamped to the number of items in the Item Granter. If _Cycle Behavior_ is _Wrap_ , `Index` is modulo'd to the number of items in the Item Granter.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
`GetItemGrantCountAtIndex<public>(Index:int)<transacts>:int`
## Parameters
`GetItemGrantCountAtIndex` takes the following parameters:
Name | Type | Description
---|---|---
`Index` | `int` |
## Attributes, Specifiers, and Effects
### Specifiers
The following specifiers determine how you can interact with `GetItemGrantCountAtIndex` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).
Specifier | Meaning
---|---
`public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data.
### Effects
The following effects determine how `GetItemGrantCountAtIndex` behaves in your programs. For the complete list of effects, see the Effect Specifers section of the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).
Effect | Meaning
---|---
`transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You’ll be notified when you compile your code if the `transacts` effect was added to a function that can’t be rolled back. Note that this check is not done for functions with the `native` specifier.
