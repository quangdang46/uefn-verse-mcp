## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/findcreativeobjectswithtag-2

# (InNPCBehavior:npc_behavior).FindCreativeObjectsWithTag extension
Learn technical details about the (InNPCBehavior:npc_behavior).FindCreativeObjectsWithTag extension.
Generates a `creative_object_interface` for every creative object that has any tag of type `tag_type`. Will not find anything if called on an `npc_behavior` that is not simulating.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
`(InNPCBehavior:npc_behavior).FindCreativeObjectsWithTag<public><native>(tag_type:castable_subtype(tag))<transacts>:generator(creative_object_interface)`
## Parameters
`FindCreativeObjectsWithTag` takes the following parameters:
Name | Type | Description
---|---|---
`InNPCBehavior` | `npc_behavior` |
`tag_type` | `castable_subtype(tag)` |
## Attributes, Specifiers, and Effects
The following attributes, specifiers, and effects determine how you can interact with `FindCreativeObjectsWithTag` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/en-us/fortnite/specifiers-and-attributes-in-verse).
### Attributes
Attribute | Arguments | Meaning
---|---|---
`available` | `MinUploadedAtFNVersion := 3200` | This feature is available beginning with the UEFN version specified by `MinUploadedAtFNVersion` and unavailable prior to that version.
### Specifiers
Specifier | Meaning
---|---
`public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data.
`native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data.
### Effects
Effect | Meaning
---|---
`transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You'll be notified when you compile your code if the `transacts` effect was added to a function that can't be rolled back. Note that this check is not done for functions with the `native` specifier.
