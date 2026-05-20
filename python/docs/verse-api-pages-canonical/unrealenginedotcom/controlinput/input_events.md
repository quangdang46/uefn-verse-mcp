## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/controlinput/input_events

# input_events function

Learn technical details about the input_events function.

Input_events is a container for user input events which can be subscribed to.

- Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player.
- Low-level notifications of current user input: DetectionBeginEvent, DetectionOngoingEvent, and DetectionEndEvent.
- High-level notifications of triggered events: ActivationTriggeredEvent and ActivationCanceledEvent.

  /—----------<-------\
  DetectionBeginEvent -> DetectionOngoingEvent -> ActivationTriggeredEvent -> DetectionEndEvent
  /\ /\ /
  ---------------------> ActivationCanceledEvent ----------------------/

|  |  |
| --- | --- |
| Verse `using` statement | `using { /UnrealEngine.com/ControlInput }` |

`input_events<public>(t:any):input_events(t)`

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.

## Parameters

`input_events` takes the following parameters:

| Name | Type | Description |
| --- | --- | --- |
| `t` | `any` |  |

### Generated Class

`input_events` returns the parametric class [`input_events(t)`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/controlinput/input_events/input_events(t)).

## Attributes, Specifiers, and Effects

### Specifiers

The following specifiers determine how you can interact with `input_events` in your programs. For the complete list of specifiers, see the [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse).

| Specifier | Meaning |
| --- | --- |
| `public` | The identifier is universally accessible. You can use this on modules, classes, interfaces, structs, enums, methods, and data. |
