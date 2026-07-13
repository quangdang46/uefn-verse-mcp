## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/spatialmath/makeunitvector

# (V:vector2).MakeUnitVector extension

Learn technical details about the (V:vector2).MakeUnitVector extension.

Makes a unit length `vector2` pointing in the same direction of `V`.
Fails if `V.IsAlmostZero[] or not V.IsFinite[]`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /UnrealEngine.com/Temporary/SpatialMath }` |

`(V:vector2).MakeUnitVector<public>():`[`vector2`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/spatialmath/vector2)

## Parameters

`MakeUnitVector` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `V` | `vector2` |  |

## Attributes, Specifiers, and Effects

The following attributes, specifiers, and effects determine how you can interact with `MakeUnitVector` in your programs, as well as how it behaves in your programs and UEFN. For the complete list of attributes, specifiers, and effects; see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

### Specifiers

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
