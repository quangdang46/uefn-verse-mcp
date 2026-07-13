## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/scenegraph/component/isinscene

# IsInScene function

Learn technical details about the IsInScene function.

Succeeds if the component is currently in the scene.

- After `OnAddedToScene` is called this call succeeds.
- After `OnRemovingFromScene` is called this call fails.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SceneGraph }` |

`IsInScene<public><native><final>():void`

## Parameters

`IsInScene` does not take any parameters.

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `IsInScene` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
| `final` | You can only use the final specifier on classes and members of classes. When a class has the final specifier, you cannot create a subclass of the class. When a field has the final specifier, you cannot override the field in a subclass. When a method has the final specifier, you cannot override the method in a subclass. |
