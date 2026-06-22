## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/tostring-1

# ToString function

Learn technical details about the ToString function.

Makes a `string` representation of `InTransform` where the result is on the form.
`"{Translation = {ToString(`InTransform.Translation`)}, Rotation = {ToString(`InTransform.Rotation`)}, Scale = {ToString(`InTransform.Scale`)}}".

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SpatialMath }` |

`ToString<public>(InTransform:transform):[]char`

## Parameters

`ToString` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `InTransform` | `transform` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `ToString` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
