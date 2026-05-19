## https://dev.epicgames.com/documentation/en-us/fortnite/verse-fields-examples-in-fortnite

# Scene Events
Learn about creating Scene Events to change your component's behavior and add interesting events to your scene.
![Scene Events](https://dev.epicgames.com/community/api/documentation/image/486e8235-4da1-4f19-a154-79513638f7a2?resizing_type=fill&width=1920&height=335)
Scene events provide a way to send signals up or down the scene graph. They are all about decoupling parts of the scene graph from each other, allowing them to communicate through messages instead of directly binding to each other.
You define a custom event, send it from an entity, and any component along the way responds by overriding `OnReceive`.
  * `SendDown` sends the event from an entity downward through its children, grandchildren, and so on (depth-first).
  * `SendUp` sends the event upward through its parent, grandparent, and so on toward the root.

Multiple components can respond to a scene event. Every component in an entity’s hierarchy gets its `OnReceive` called. A component can consume the event (return `true`) to stop propagation, or pass through (return `false`) to let it keep traveling.
The three things you need:
  * **A custom event** : A class that inherits from `scene_event`.
  * **A responding component** : Overrides `OnReceive`, casts the event, and reacts.
  * **A send call** : `Entity.SendDown(Event)` or `Entity.SendUp(Event)`.

Scene events can be reused across your projects, you can expand upon scene events by adding additional events or tweaking the behavior of entities and components in a chain of events to do something slightly different.
##  Cast Pattern
The `OnReceive` call provides a way to create a generic `scene_event`. To find out what specific type was sent, use a failable cast:
Verse
```

```

if (SpecificEvent := my_event[E]): # Cast succeeded — access SpecificEvent.Amount, etc.
Copy full snippet(2 lines long)
If the event isn't that type, the cast fails and the `if` block is skipped. This filters for only the events you need. The `OnReceive` gets called for every scene event passing through the hierarchy, so the cast is essential.
##  Event Propagation
The `SendDown` event traverses depth-first, it calls `OnReceive` on each component of the starting entity, then recurses into the first child (and its children) before moving to the next sibling.
The `SendUp` event traverses in the opposite direction from `SendDown`, it starts entity first, then parent, then grandparent, up to the root.
Both event types stop immediately if any component consumes the event (returns `true` from `OnReceive`). Both return `logic — true` if the event was consumed somewhere, or `false` if it traveled the entire path without being consumed.
###  Consumed Events
  * Return `true` from `OnReceive` — propagation stops, no further entities react to the event.

This is useful when a component fully handles the event and no additional components in the hierarchy respond to the event. For example, a shield absorbing damage before it reaches the entity underneath.
Verse
```
damage_event<public> := class(scene_event):
    Amount<public>:int

# A shield that absorbs all damage and stops it from reaching children.
shield_component := class(component):
    var ShieldHP:int = 100

    OnReceive<override>(E:scene_event):logic =
        if (Dmg := damage_event[E]):
            set ShieldHP -= Dmg.Amount

```

Copy full snippet(22 lines long)
If the shield entity is an ancestor of the health entity, `SendDown` hits the shield first. Because the shield returns `true`, the health component is not affected by the event.
###  Pass Through Events
  * Return `false` (the default) — the event keeps traveling through the hierarchy.

The base `OnReceive` on `component` returns `false`, which is why calling `(super:)OnReceive(E)` at the end of your override is the standard pattern for passing an event onward.
##  Scene Events Examples
Following are code examples of basic scene events behavior.
###  Define an Event
Verse
```

```

my_event<public> := class(scene_event): Amount<public>:int
Copy full snippet(2 lines long)
###  Respond to an Event in a Component
Verse
```

```

my_responder := class(component): var Score:int = 0 OnReceive<override>(E:scene_event):logic = if (Event := my_event[E]): set Score += Event.Amount (super:)OnReceive(E)
Copy full snippet(7 lines long)
###  Send Event
Verse
```

```

Event := my_event{Amount := 10} MyEntity.SendDown(Event)
Copy full snippet(2 lines long)
###  Handle Multiple Event Types
Verse
```

```

OnReceive<override>(E:scene_event):logic = if (DmgEvent := damage_event[E]): # Handle damage... else if (HealEvent := heal_event[E]): # Handle healing... (super:)OnReceive(E)
Copy full snippet(6 lines long)
###  Use var Fields to Collect Information from Responders
Verse
```
my_event<public> := class(scene_event):
    I<public>:int
    var Activations:int = 0      # Responders can increment this

# In the responder:
OnReceive<override>(E:scene_event):logic =
    if (CE := my_event[E]):
        set CE.Activations += 1
    (super:)OnReceive(E)

```

Copy full snippet(14 lines long)
##  Things to Watch Out For
  * Always call `(super:)OnReceive(E)` to ensure superclasses get their `OnReceive` invoked.
For classes that inherit directly from components, this is less important. In those cases, returning `false` to continue propagation at the end of the function is reasonable.
  * Always cast before accessing fields. The parameter type is `scene_event`, not your specific event class.
  * Don't consume accidentally. Returning `true` silently hides the event from the rest of the hierarchy.
  * The entity must be in the scene for `SendUp/SendDown` to work. This restriction might be lifted in the future.

##  API Quick Reference
|
---|---
**API** |  **What it does**
`scene_event` |  Interface. Inherit from this to make your own event type.
`Entity.SendDown(E)` |  Send event to this entity and all descendants.
`Entity.SendUp(E)` |  Send event to this entity and all ancestors.
`Component.SendDown(E)` |  Send event from this component's entity downward. (prefer `Entity.SendDown/Up` whenever possible to improve compatibility)
`OnReceive(E):logic` |  Override to respond. Return `true` to consume, false to pass through.
