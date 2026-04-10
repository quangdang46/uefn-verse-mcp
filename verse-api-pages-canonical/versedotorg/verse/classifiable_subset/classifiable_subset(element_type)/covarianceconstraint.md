## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/classifiable_subset/classifiable_subset(element_type)/covarianceconstraint

# CovarianceConstraint function
Learn technical details about the CovarianceConstraint function.
Temporary function for constraining variance correctly.
|
---|---
Verse `using` statement | `using { /Verse.org/Verse }`
`CovarianceConstraint<protected>()<transacts><no_rollback>:?`
## Parameters
`CovarianceConstraint` does not take any parameters.
## Attributes, Specifiers, and Effects
### Specifiers
The following specifiers determine how you can interact with `CovarianceConstraint` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/en-us/fortnite/specifiers-and-attributes-in-verse).
Specifier | Meaning
---|---
`protected` | The identifier is only accessible in the current class and any subtypes. You can use this on classes, interfaces, structs, enums, non-module methods, and data.
### Effects
The following effects determine how `CovarianceConstraint` behaves in your programs. For the complete list of effects, see the Effect Specifers section of the [Specifiers Page](https://dev.epicgames.com/documentation/en-us/fortnite/specifiers-and-attributes-in-verse).
Effect | Meaning
---|---
`transacts` | This effect indicates that any actions performed by the function can be rolled back. The transacts effect is required any time a mutable variable (`var`) is written. You'll be notified when you compile your code if the `transacts` effect was added to a function that can't be rolled back. Note that this check is not done for functions with the `native` specifier.
`no_rollback` | This is the default effect when no exclusive effect is specified. The `no_rollback` effect indicates that any actions performed by the function cannot be undone and so the function cannot be used in a failure context. This effect cannot be manually specified.
