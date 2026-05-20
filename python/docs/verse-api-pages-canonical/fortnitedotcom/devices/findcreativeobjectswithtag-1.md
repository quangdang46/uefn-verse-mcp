## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/findcreativeobjectswithtag-1

# (InCreativeDevice:creative_device_base).FindCreativeObjectsWithTag extension

Learn technical details about the (InCreativeDevice:creative_device_base).FindCreativeObjectsWithTag extension.

Generates a `creative_object_interface` for every creative object that has any tag of type `tag_type`. Will not find anything if called on a default constructed object.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

`(InCreativeDevice:creative_device_base).FindCreativeObjectsWithTag<public>(tag_type:castable_subtype(tag))<transacts>:generator(creative_object_interface)`

## Parameters

`FindCreativeObjectsWithTag` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `InCreativeDevice` | `creative_device_base` |  |
| `tag_type` | `castable_subtype(tag)` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `FindCreativeObjectsWithTag` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |

### Effects

| Effect | Meaning |
| --- | --- |
| `transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You’ll be notified when you compile your code if the `transacts` effect was added to a function that can’t be rolled back. Note that this check is not done for functions with the `native` specifier. |
