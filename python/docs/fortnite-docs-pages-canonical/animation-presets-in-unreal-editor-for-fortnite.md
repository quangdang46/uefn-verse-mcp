## https://dev.epicgames.com/documentation/en-us/fortnite/animation-presets-in-unreal-editor-for-fortnite

# Animation Presets

Learn about Animation Presets, and how to set them up on NPCs.

![Animation Presets](https://dev.epicgames.com/community/api/documentation/image/d35cd318-874f-4287-9886-376270d7160d?resizing_type=fill&width=1920&height=335)

**Animation Presets** are a collection of customizable animation behaviors. They can currently only be applied to NPC characters using the [NPC Spawner](https://dev.epicgames.com/documentation/en-us/uefn/using-npc-spawner-devices-in-unreal-editor-for-fortnite). Each preset comes with a set of customizable properties that you can tweak to suit a character.

Animation Presets control how your character animates. If you want to extend this functionality, you can create your own Verse script and play one-time animations using the [PlayAnimation API](https://dev.epicgames.com/documentation/en-us/uefn/verse-api/fortnitedotcom/animation/playanimation).

If you want to learn more about importing a custom character, see [Importing Assets](https://dev.epicgames.com/documentation/fortnite/importing-assets-in-unreal-editor-for-fortnite).

This tutorial walks you through:

- [Creating an Actor Blueprint Class from a custom skeletal mesh](https://dev.epicgames.com/documentation/fortnite/animation-presets-in-unreal-editor-for-fortnite),
- [More details about the two preset types available](https://dev.epicgames.com/documentation/fortnite/animation-presets-in-unreal-editor-for-fortnite),
- [Creating an Animation Preset for the actor using imported animations](https://dev.epicgames.com/documentation/fortnite/animation-presets-in-unreal-editor-for-fortnite), and
- [Creating an NPC Character definition for the actor](https://dev.epicgames.com/documentation/fortnite/animation-presets-in-unreal-editor-for-fortnite).

## Create an Actor Blueprint Class

To use Animation Presets on your character:

## Animation Preset Types

### Basic Locomotion

[![Basic Locomotion](https://dev.epicgames.com/community/api/documentation/image/fab4034f-f86d-473c-8f35-80338b961570?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fab4034f-f86d-473c-8f35-80338b961570?resizing_type=fit)

The Basic Locomotion preset is great for a wide range of characters, and is quick and easy to set up. This preset requires five animations:

- Idle
- Move Forward
- Move Backward
- Move Left
- Move Right

Each animation has an associated **play rate** value, which controls the speed at which the animation plays out.

Only the **Idle** animation is required to get your preset to work. This can be useful if you plan on your NPC remaining stationary.

### Biped Locomotion

[![Biped locomotion](https://dev.epicgames.com/community/api/documentation/image/6bd8c410-c505-49df-ba48-1ac51fda0492?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6bd8c410-c505-49df-ba48-1ac51fda0492?resizing_type=fit)

As the name implies, the Biped Locomotion preset is ideal for biped characters. This preset offers a lot more control over the animation behavior than the Basic Locomotion preset, and can accommodate more animations.

This preset offers separate animations for walking and running, and breaks animations down even further. For example, the walking animation is composed of **Walk Start**, **Walk Loop** and **Walk Stop**, which gives you the ability to tweak every detail of the locomotion.

**F, B, L** and **R** stand for Forward, Backward, Left and Right, respectively.

## Create an Animation Preset

When your animations need tweaking, you can edit them with Control Rig.

Making your animations transition well requires synchronization. You can add Sync Markers to synchronize points in the animation. For locomotion animations, marking when each foot contacts the ground will improve the blending. The video below illustrates how this is done.

## Create an NPC Character Definition

Animation Presets are normally used for Custom character types. To animate Fortnite Characters using Animation Presets, use the FN_Mannequin skeletal mesh available in the [Animation 101 Template](animation-101-template-in-unreal-editor-for-fortnite) and [retarget the animations](https://dev.epicgames.com/documentation/fortnite/transfer-character-animations-in-unreal-editor-for-fortnite) to the Fortnite skeletal mesh.

You’re now ready to test out the NPC. Drag the NPC Character Definition asset into your level and start your UEFN session.

[![NPC in Editor](https://dev.epicgames.com/community/api/documentation/image/369ddec2-dbbd-47d9-ace5-cbc193a167cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/369ddec2-dbbd-47d9-ace5-cbc193a167cf?resizing_type=fit)

In-game, you’ll see your NPC Spawner device with your NPC. Start the game and you can see your NPC idling, using the animation you provided.

[![NPC in Editor](https://dev.epicgames.com/community/api/documentation/image/3bb291d9-0262-41f7-b558-41412458c276?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3bb291d9-0262-41f7-b558-41412458c276?resizing_type=fit)

For more information on setting up NPC behavior, see the [AI and NPCs](ai-and-npcs-in-unreal-editor-for-fortnite) section in the UEFN documentation.
