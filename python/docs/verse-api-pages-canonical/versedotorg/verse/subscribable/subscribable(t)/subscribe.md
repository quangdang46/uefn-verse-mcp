## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/subscribable/subscribable(t)/subscribe

# Subscribe function
Learn technical details about the Subscribe function.
Registers `Callback` to be invoked on matching calls to `signable.Signal`. Returns an unsubscriber object. Call `cancelable.Cancel` on the unsubscriber to unregister `Callback`.
|
---|---
Verse `using` statement | `using { /Verse.org/Verse }`
`Subscribe<public>(Callback:`(), :`void)<transacts>:`[`cancelable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/cancelable)
## Parameters
`Subscribe` takes the following parameters:
Name | Type | Description
---|---|---
`Callback` | (), :`void` |
## Attributes, Specifiers, and Effects
### Specifiers
The following specifiers determine how you can interact with `Subscribe` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/en-us/fortnite/specifiers-and-attributes-in-verse).
Specifier | Meaning
---|---
`public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data.
### Effects
The following effects determine how `Subscribe` behaves in your programs. For the complete list of effects, see the Effect Specifers section of the [Specifiers Page](https://dev.epicgames.com/documentation/en-us/fortnite/specifiers-and-attributes-in-verse).
Effect | Meaning
---|---
`transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You'll be notified when you compile your code if the `transacts` effect was added to a function that can't be rolled back. Note that this check is not done for functions with the `native` specifier.
