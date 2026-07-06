## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/sortby

# SortBy function

Learn technical details about the SortBy function.

Stably sort `Array` using `Less` where `Less` succeeding indicates `Left` should precede `Right`

|  |  |
| --- | --- |
| Verse `using` statement | `using { /UnrealEngine.com/Temporary }` |

`SortBy<public><native>(Array:[]t, Less:`(`(t, t)`):`void where t:any):[]t`

## Parameters

`SortBy` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `Array` | `[]t` |  |
| `Less` | (`(t, t)`):`void` |  |
| `t` | `any` |  |

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `SortBy` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
| `native` | Indicates that the definition details of the element are implemented in C++. Verse definitions with the `native` specifier auto-generate C++ definitions that a developer can then fill out its implementation. You can use this specifier on classes, interfaces, enums, methods, and data. |
