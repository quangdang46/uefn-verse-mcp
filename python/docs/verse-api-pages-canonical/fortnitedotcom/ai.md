## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ai

# AI module

Learn technical details about the AI module.

Module import path: /Fortnite.com/AI

- [`Fortnite.com`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom)
- **`AI`**

  - [`movement_types`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/movement_types)

## Classes and Structs

| Name | Description |
| --- | --- |
| [`equipped_sidekick_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/equipped_sidekick_component) | Component to manage functionality specifically for an agent's equipped Sidekick. |
| [`spark_mode_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/spark_mode_component) | component to manage an entity that supports a Spark mode. Spark mode will transform the entity into a floating spark. The entity will enter `spark mode` whenever it enters impassable terrain or to reduce visual clutter. |
| [`guard_actions_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/guard_actions_component) | Fortnite Guards AI actions management |
| [`guard_awareness_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/guard_awareness_component) | Fortnite Guard perception management |
| [`navigation_target`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/navigation_target) |  |
| [`npc_actions_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_actions_component) | Fortnite NPC AI actions management |
| [`npc_awareness_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_awareness_component) | Fortnite NPC perception management |
| [`npc_behavior`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_behavior) | Inherit from this to create a custom NPC behavior. The npc_behavior can be defined for a character in a CharacterDefinition asset, or in a npc_spawner_device. |
| [`npc_target_info`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_target_info) | Information about a perceived target. |
| [`sidekick_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/sidekick_component) | Component to manage functionality shared by all Sidekick types. |
| [`npc_sidekick_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_sidekick_component) | Component to manage functionality specifically for an NPC Sidekick. |

## Interfaces

| Name | Description |
| --- | --- |
| [`focus_interface`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/focus_interface) |  |
| [`fort_leashable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/fort_leashable) |  |
| [`navigatable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/navigatable) |  |

## Functions

| Name | Description |
| --- | --- |
| [`MakeNavigationTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/makenavigationtarget) | Generate a navigation_target from any position. |
| [`MakeNavigationTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/makenavigationtarget-1) | Generate a navigation_target from any position. |
| [`MakeNavigationTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/makenavigationtarget-2) | Generate a navigation_target from an agent. |

## Enumerations

| Name | Description |
| --- | --- |
| [`ai_action_error_type`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/ai_action_error_type) | Result of a failed AI action |

|  |  |
| --- | --- |
| [`navigation_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/navigation_result) | Result of a navigation request |

|  |  |
| --- | --- |
| [`navigation_action_error_type`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/navigation_action_error_type) |  |

|  |  |
| --- | --- |
| [`navigation_action_success_type`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/navigation_action_success_type) |  |

|  |  |
| --- | --- |
| [`movement_type`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/movement_type) |  |

|  |  |
| --- | --- |
| [`guard_alert_level`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/guard_alert_level) | The different alert levels of a Fortnite Guard. |

|  |  |
| --- | --- |
| [`sidekick_mood`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/sidekick_mood) | Sidekicks have a mood that modifies their animations to suit that mood. This is the list of currently supported moods. |

|  |  |
| --- | --- |
| [`sidekick_reaction`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/sidekick_reaction) | The set of available reactions that can be played on the Sidekick |
