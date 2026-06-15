## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/containsany

# (InSet:classifiable_subset(element_type)).ContainsAny extension

Learn technical details about the (InSet:classifiable_subset(element_type)).ContainsAny extension.

Succeeds if any of the `element_types` are present in `InSet`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`(InSet:classifiable_subset(element_type)).ContainsAny<public>(element_types:[]castable_subtype(k) where t:castable_subtype(k), k:any):void`

## Parameters

`ContainsAny` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `InSet` | `classifiable_subset(element_type)` |  |
| `element_types` | `[]castable_subtype(k)` |  |
| `t` | `castable_subtype(k)` |  |
| `k` | `any` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `ContainsAny` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Attributes

| Attribute | Arguments | Meaning |
| --- | --- | --- |
| `available` | `MinUploadedAtFNVersion := 3800` |  |
| `experimental` |  | This feature is in an experimental state, and you cannot publish projects implmenting it. The API for this feature is subject to change and backward compatibility is not guaranteed. |

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
