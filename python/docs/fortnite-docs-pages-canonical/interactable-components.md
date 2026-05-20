## https://dev.epicgames.com/documentation/en-us/fortnite/interactable-components

# Interactable Components

Components that enable interactions using Scene Graph.

![Interactable Components](https://dev.epicgames.com/community/api/documentation/image/be0fdbf6-26d9-4b4d-a37c-c6abc810b8a2?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

**Interactable components** are **Scene Graph components** designed to simplify basic player interactions in UEFN.

These components enable agents to interact with the entity that the components are attached to.

**Interaction** is defined by the agent attempting to start, and being signaled on, the success of the interaction — for instance, pressing the **E** key on PC. The component doesn’t dictate what an interaction does, but only handles the handshake between the interacting agent and the interactable component.

## interactable_component

The **interactable_component** is the basis for granting players the ability to interact with objects in a game.

[![](https://dev.epicgames.com/community/api/documentation/image/7bb20cd5-3dd6-4af0-898f-3fa799f7ee07?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7bb20cd5-3dd6-4af0-898f-3fa799f7ee07?resizing_type=fit)

interactable component

Interactions typically happen when a player presses **the interact button** next to an object. This base component enables the minimal required interactivity to trigger a game event.

The **interactable_component** needs to be attached to a **mesh_component** to work.

Using Verse, you can override the default behavior of the component to create custom interactions. Consult the [interactable_component class API reference](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_component) for more details.

### Verse Class

The interactable_component class can start an interaction and manage cooldowns for both the component and for each agent that interacts with it.

Verse

```
# An interactable component allows an agent to start and succeed at an interaction.
# The functionality of what happens on success should be implemented by overriding the success event.
interactable_component<public> := class(component, enableable):
    # Set the enable/disable for interaction of the component.
    Enable<override>()<transacts> : void
    Disable<override>()<transacts> : void
    IsEnabled<override>()<decides><reads> : void

    # Event fires when an interaction starts. Sends the interacting agent.
```

### Examples

In this first example, the user can interact with a mesh that modifies the state from Enabled to Disabled. The entity is composed of a **mesh_component** of a computer and the customized **interactable_enableable_component**.

interactable button

Below is the code used for the interactable_enableable_component:

Verse

interactable_enableable_component

```
using { /Verse.org }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }
using { /Fortnite.com/Game }

# Allows a Enable/Disable state on the interactable_component
interactable_enableable_component<public> := class<final_super>(interactable_component):

    # Default text to show on the UI
    EnabledText<localizes> : message = "Enabled"
```

In this second example, the interaction triggers the light turning on inside the lantern. The entity is made of a **lamp mesh component** and the interactable_enableable_light_component.

interactable lamp

Below is the code used for the interactable_enableable_light_component:

Verse

interactable_enableable_light_component

```
using { /Verse.org }
using { /Verse.org/Native }
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }

# Will turn on/off a light after interacting with the entity
interactable_enableable_light_component<public> := class<final_super>(interactable_enableable_component):

    # Entity who has the light_component attached
    @editable
```

## basic_interactable_component

The **basic_interactable_component** gives more control over the interaction parameters.

[![](https://dev.epicgames.com/community/api/documentation/image/c0b97f25-c6ea-4de9-9fbb-53176ced6407?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0b97f25-c6ea-4de9-9fbb-53176ced6407?resizing_type=fit)

basic_interactable component

The basic interactable component allows for interactions to have a duration that must elapse before the interaction succeeds, and it handles the complexity around this potentially by allowing multiple interactions simultaneously.

It also allows a way to manage the cooldown time between each interaction, which can vary based on the interacting agent.

Interactions are governed by the basic_interactable_component Verse class.

### Verse Class

Verse

```
# An interactable component with a composable feature set.
basic_interactable_component<public> := class(interactable_component):
    # Cooldowns begin elapsing on successful interactions. A cooldown which applies for all attempts to interact on this component.
    @editable
    Cooldown<public> : ?interactable_cooldown = false

    # Cooldowns begin elapsing on successful interactions. A cooldown which applies for future attempts to interact on this component by the agent which succeeded.
    @editable
    CooldownPerAgent<public> : ?interactable_cooldown_per_agent = false
```
