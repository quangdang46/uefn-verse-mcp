## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/makeerror

# MakeError function

Learn technical details about the MakeError function.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/Verse }` |

`MakeError<public>(Result:error_type where error_type:any)<computes>:`[`result(success_type,error_type)`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/result/result(success_type,error_type))

## Parameters

`MakeError` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Result` | `error_type` |  |
| `error_type` | `any` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `MakeError` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |

### Effects

The following effects determine how `MakeError` behaves in your programs. For the complete list of effects, see the Effect Specifers section of the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Effect | Meaning |
| --- | --- |
| `computes` | This effect requires that the function has no side effects, and is not guaranteed to complete. There’s an unchecked requirement that the function, when provided with the same arguments, produces the same result. Any function that doesn’t have the `native` specifier that would otherwise have the `converges` effect is a good example of using the `computes` effect. |
