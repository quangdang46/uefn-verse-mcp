## https://dev.epicgames.com/documentation/en-us/fortnite/change-a-players-point-of-view-with-cameras-in-unreal-editor-for-fortnite

# Transitioning Player Point of View with Cameras

Learn how to change the camera when a player opens a door to create a transition between areas.

![Transitioning Player Point of View with Cameras](https://dev.epicgames.com/community/api/documentation/image/b9c5bef4-e2b2-41f9-971e-8e813ca727df?resizing_type=fill&width=1920&height=335)

Cameras play a key role in the look and feel of a game. Third-person cameras can give players a greater sense of space, while first-person cameras give players a closer look at their game world. Switching cameras during gameplay can evoke different feelings, and transitioning between multiple cameras can add significant variety to your experience. For example, you could create a fun platforming challenge using a fixed camera to create a side-scrolling section.

In UEFN, you can use Verse to handle camera changes. By using devices to listen for events, you can add a camera to a player to change their view when the event triggers. In this example, you'll add an [Orbit Camera](https://dev.epicgames.com/documentation/fortnite/using-orbit-camera-devices-in-fortnite-creative) device to a player at the end of a cinematic. You can modify the settings on an orbit camera to simulate a first-person view, and by adding the camera at the end of a cinematic you can create a smooth transition from third to first-person. For added gameplay, this example has the player grab a weapon and swing it at the door to trigger the cinematic. You can tailor this example to fit the needs of your experience, such as a player swinging a wrench to fix a faulty ship door, or swinging a hammer to smash a boulder and reveal a secret area. You can also more broadly apply these concepts to create cool gameplay moments, like a wide shot when entering a new zone, switching to a top-down view when the player needs to solve a puzzle, or a first-person view in a spooky horror experience.

Follow this tutorial to learn how to create a Verse device that transitions a player from third to first-person using a cinematic sequence when they open a door.

This example uses the following language features:

- Class: This example creates a Verse class that activates a cinematic when a player opens a door.
- Option: You can store subscribable events in option variables, and cancel subscriptions to those events later.

This example uses the following APIs:

- [Subscribable](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/subscribable): You'll subscribe to events to know when a player enters a volume next to the door, and grant players an item when they interact with a button.

## Setting Up the Level

This example uses the following devices:

- 1 x [Button](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative) device: When the player interacts with the button, they'll receive a sword from an item granter device.
- 1 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/item-granter) device: The item granter grants the player the sword they need to progress through the door.
- 1 x [Conditional Button](https://dev.epicgames.com/documentation/fortnite/conditional-button) device: The required weapon is set as the **Key Item** of the conditional button so that the player can't progress through the door unless they have the required sword.
- 1 x [Input Trigger](https://dev.epicgames.com/documentation/fortnite/using-input-trigger-devices-in-fortnite-creative) device: This opens the door when the player attacks by listening for the fire input action. This only happens when the player is inside the volume device, if the player has the sword, and the door isn't already open.
- 1 x [Volume](https://dev.epicgames.com/documentation/fortnite/using-volume-devices-in-fortnite-creative) device: Since you don't want just any attack trigger with the sword to open the door, the volume device makes sure the player needs to be right next to the door to open it.
- 1 x [Cinematic Sequence](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) devices: To create a smooth transition from third- to first-person, you'll play a cinematic that shows the door opening and reposition the camera to line up with the player's viewpoint in first-person.
- 1 x [Orbit Camera](https://dev.epicgames.com/documentation/fortnite/using-orbit-camera-devices-in-fortnite-creative) device: To create a first-person view for the player, you'll use an orbit camera positioned inside the character's chest to mimic a first-person viewpoint. This view change only happens after the cinematic players when the player opens the door.
- 1 x [Lock](https://dev.epicgames.com/documentation/fortnite/using-lock-devices-in-fortnite-creative) device: This keeps the door locked to prevent the player from opening it before they have the required weapon.
- 1 x [Map Indicator](https://dev.epicgames.com/documentation/fortnite/map-indicator) device: This displays the location of the door on the minimap when the player picks up the weapon.

To set up your level, follow these steps:

### Item Granter and Button

To grant the player the weapon they need to open the door, you'll use an item granter and a button device. When the player interacts with the button, the item granter grants them the weapon. To add these elements, follow these steps:

### Input Trigger

To know when a player swings a weapon, you can use an input trigger that listens for a particular action. When a player swings the weapon, the input trigger activates. To add an input trigger, follow these steps:

### Volume

To make sure a player has to be next to the door to open it, you can use a volume device near the door to check if a player is inside it. To add a volume device, follow these steps.

### Lock

To make sure a player can't open the door before they get the weapon, you can lock the door using a lock device. To add a lock device, follow these steps:

### Map Indicator

When the place a player needs to reach is far away from where they get the weapon, it's helpful to show players where to go using a map indicator. This displays an image on their map and minimap and can activate an objective pulse that points players directly to the door. To add a map indicator, follow these steps:

### Conditional Item Button

To know that a player is swinging the correct weapon they need to open the door, you can use a conditional item button to check the weapon they're holding when they swing it. To add a conditional item button, follow these steps:

### Orbit Camera

To simulate a first-person view, you can use an orbit camera to change the player's perspective. To add an orbit camera, follow these steps:

### Cinematic Sequence

To trigger a cinematic when opening the door, you need a cinematic sequence device to play it. To add a cinematic sequence, follow these steps:

## Door Opening Cinematic using Verse

To handle the logic for playing a cinematic and opening the door, you'll use a [Verse device](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite). The device listens for a player swinging their weapon inside the volume device, then plays a cinematic sequence, opens the door, and transitions the player into first-person.

### Setting Up Fields

To create your Verse device:

1. Create a new Verse device using [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite), and name it `door_open_cinematic_manager`.
2. Above the `door_open_cinematic_manager` class definition, add a log channel to print messages specific to this device. Then add a logger to the class definition to use with the log channel.

   Verse

   ```
   door_open_channel := class(log_channel){}
   		
        # A Verse-authored creative device that can be placed in a level
        door_open_cinematic_manager := class(creative_device):
            Logger:log = log{Channel := door_open_channel}
   ```

   door_open_channel := class(log_channel){}
   # A Verse-authored creative device that can be placed in a level
   door_open_cinematic_manager := class(creative_device):
   Logger:log = log{Channel := door_open_channel}
3. Add the following fields to the `door_open_cinematic_manager` class definition:

   - An editable Volume device named `DoorVolume`. This is the volume the player needs to be inside to open the door.

     Verse

     ```
     # The volume the player needs to be inside of to open the door.
       @editable
       DoorVolume:volume_device = volume_device{}
     ```

     # The volume the player needs to be inside of to open the door.
     @editable
     DoorVolume:volume_device = volume_device{}
   - An editable Input Trigger device named `FireTrigger`. This listens for the player using their weapon while inside the `DoorVolume`.

     Verse

     ```
     # The input trigger that listens for the player swinging their weapon
       # when inside the DoorVolume.
       @editable
       FireTrigger:input_trigger_device = input_trigger_device{}
     ```

     # The input trigger that listens for the player swinging their weapon
     # when inside the DoorVolume.
     @editable
     FireTrigger:input_trigger_device = input_trigger_device{}
   - An editable Conditional Button device named `ConditionalButton`. This checks that the player has the correct weapon equipped when inside the volume device.

     Verse

     ```
     # The Conditional Item Button that checks that the player has the correct weapon.
       @editable
       ConditionalButton:conditional_button_device = conditional_button_device{}
     ```

     # The Conditional Item Button that checks that the player has the correct weapon.
     @editable
     ConditionalButton:conditional_button_device = conditional_button_device{}
   - An editable Lock Device named `DoorLock`. This keeps the door locked if the player doesn't have the correct weapon.

     Verse

     ```
     # The lock device that prevents the door from being opened.
       @editable
       Door:lock_device = lock_device{}
     ```

     # The lock device that prevents the door from being opened.
     @editable
     Door:lock_device = lock_device{}
   - An editable Cinematic Sequence device named `CinematicSequence`. This plays the cinematic leading into the camera transition when opening the door.

     Verse

     ```
     # The cinematic sequence device that plays the cinematic when opening the door.
       @editable
       CinematicSequence:cinematic_sequence_device = cinematic_sequence_device{}
     ```

     # The cinematic sequence device that plays the cinematic when opening the door.
     @editable
     CinematicSequence:cinematic_sequence_device = cinematic_sequence_device{}
   - An editable Map Indicator device named `ObjectiveMarker`. This shows the location of the door on the minimap after picking up the weapon.

     Verse

     ```
     # The map indicator device that shows the location of the door.
       @editable
       ObjectiveMarker:map_indicator_device = map_indicator_device{}
     ```

     # The map indicator device that shows the location of the door.
     @editable
     ObjectiveMarker:map_indicator_device = map_indicator_device{}
   - An editable Item Granter device named `ItemGranter`. This grants the player the weapon they need to progress.

     Verse

     ```
     # The item granter device that grants the player the weapon they need.
       @editable
       ItemGranter:item_granter_device = item_granter_device{}
     ```

     # The item granter device that grants the player the weapon they need.
     @editable
     ItemGranter:item_granter_device = item_granter_device{}
   - An editable Button device named `ItemGrantButton`. This activates the `ItemGranter` to grant the player the weapon they need.

     Verse

     ```
     # The button that activates the ItemGranter granter.
       @editable
       ItemGrantButton:button_device = button_device{}
     ```

     # The button that activates the ItemGranter granter.
     @editable
     ItemGrantButton:button_device = button_device{}
   - An editable Orbit Camera device named `FPSCamera`. This simulates a first-person view and is added to the player after the cinematic ends.

     Verse

     ```
     # The orbit camera that simulates a first-person view.
       @editable
       FPSCamera:gameplay_camera_orbit_device = gameplay_camera_orbit_device{}
     ```

     # The orbit camera that simulates a first-person view.
     @editable
     FPSCamera:gameplay_camera_orbit_device = gameplay_camera_orbit_device{}
   - A [`logic`](logic-in-verse) variable named `IsDoorOpen`. This field tracks whether the door is already open, so the sequence doesn't play if it is.

     Verse

     ```
     # A variable that tracks whether the door is already open.
       var IsDoorOpen:logic = false
     ```

     # A variable that tracks whether the door is already open.
     var IsDoorOpen:logic = false
   - An [`option`](option-in-verse) `cancelable` variable named `FireSubscription`. This stores the subscription to the `FireTrigger` `PressedEvent`. The cinematic sequence should only trigger when the player is right next to the door. This cancelable subscription makes sure to `Unregister` the player from the `FireTrigger`, if they get too far away.

     Verse

     ```
     # A cancelable subscription to the FireTrigger device.
       var FireSubscription:?cancelable = false
     ```

     # A cancelable subscription to the FireTrigger device.
     var FireSubscription:?cancelable = false

### Playing the Cinematic

When the door opens, a cinematic occurs that shows the door opening and transitions the players' view from third to first person. Follow the steps below to activate your cinematic when a player opens the door.

### Tracking the Player and Granting Items

Since the player needs to swing their weapon while inside the `DoorVolume` to open the door, the input trigger device needs to be listening for that event. Follow the steps below to get your input trigger to listen for when your player swings a weapon.

### Linking it All Together

You can now subscribe each event to its associated function and test out your code in-game.

## Complete Code

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# See https://dev.epicgames.com/documentation/en-us/uefn/create-your-own-device-in-verse for how to create a verse device.
door_open_log := class(log_channel){}

door_open_cinematic_manager := class(creative_device):

    Logger:log = log{Channel := door_open_log}
```

## On Your Own

By completing this guide, you've learned how to use Verse to play a cinematic when a player opens a door, and how to transition from third to first-person camera.

Using what you've learned, try the following:

- Can you do other types of camera transitions, such as a transition to a side-scroller view?
- How about a dedicated button to change the camera angle, or designing a level that requires multiple camera angles to progress?
- Can you use input triggers for negative penalties, such as challenging players to get through a section without jumping, and play a cinematic if they fail?
