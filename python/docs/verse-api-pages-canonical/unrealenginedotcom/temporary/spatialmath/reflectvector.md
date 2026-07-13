## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/spatialmath/reflectvector

# ReflectVector function

Learn technical details about the ReflectVector function.

Makes a `vector2` by inverting the `SurfaceNormal` component of `Direction`.
Fails if `not SurfaceNormal.MakeUnitVector[]`.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /UnrealEngine.com/Temporary/SpatialMath }` |

`ReflectVector<public>(Direction:vector2, SurfaceNormal:vector2):`[`vector2`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/spatialmath/vector2)

## Parameters

`ReflectVector` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Direction` | `vector2` |  |
| `SurfaceNormal` | `vector2` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `ReflectVector` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
