## https://dev.epicgames.com/documentation/en-us/fortnite/sequencer-and-control-rig-in-unreal-editor-for-fortnite

# Sequencer and Control Rig

Film your skeletal mesh in action with Sequencer

![Sequencer and Control Rig](https://dev.epicgames.com/community/api/documentation/image/9d727faa-a7bc-40e7-9433-21a6fb4ae7a0?resizing_type=fill&width=1920&height=335)

In [**Sequencer**](unreal-editor-for-fortnite-glossary#sequencer), you can animate almost anything. It’s even possible to do a full [cinematic](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#cinematic-sequence) with camera animations! For more information, check out [Sequencer Basics in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine).

Do not confuse **Sequencer** with the **Cinematic Sequence** **device**! Once you record a level sequence, you then attach it to a Cinematic Sequence Device. For more information, see [Set Up the Cinematic Sequence Device](https://dev.epicgames.com/documentation/fortnite/sequencer-and-control-rig-in-unreal-editor-for-fortnite)

## Creating a Level Sequence

To create a level sequence and add a skeletal mesh to the sequence, do the following:

The next section covers the basics of creating an animated scene using **Sequencer**.

## Using Sequencer

This section of the tutorial walks you through some of the basic operations you can perform with Sequencer.

Before starting, it's a good idea to open the [Sequencer Editor Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine) and place it next to this page. The reference explains the Sequencer UI elements, and shows how to effectively navigate the editor.

For a more detailed explanation of animation sequences, check out [Animation Sequences in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine).

### Animate Using Translation and Rotation

The simplest kind of animation is changing the state of an asset by translating or rotating it. Try it out:

1. Open Sequencer by double-clicking your level sequence **"LS_Cine"**. This sequence should already be linked to a skeletal mesh in your level.
2. In your timeline, make sure the [playhead](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#playhead) is at **0000**, then press **Enter** or click the small **+** (depicted below) in the **Transform** row to set the first [keyframe](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#keyframe).

   [![keyframe selector](https://dev.epicgames.com/community/api/documentation/image/1681a52d-091e-4d46-b128-c7b01580b7d4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1681a52d-091e-4d46-b128-c7b01580b7d4?resizing_type=fit)
3. In the viewport, place your skeletal mesh where you want the animation to start.
4. Enable **Auto Key** so that keyframes are automatically created whenever a property or transform changes.

   [![auto key](https://dev.epicgames.com/community/api/documentation/image/06cf43af-6c48-46c8-8878-0563a40f907d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06cf43af-6c48-46c8-8878-0563a40f907d?resizing_type=fit)
5. Move the playhead forward a few frames.
6. Back in the viewport, move your skeletal mesh to the next location.
7. Playing the animation or moving the playhead between the two keyframes now shows your mesh moving from point A to point B.
8. Using the same method, try adding rotation to the mesh.
9. Add and link the **Cinematic Sequence** and **Trigger** devices, as shown in the previous section, to activate the animation in-game.

### Add Imported Animations

To make use of the animations that you imported earlier:

### Add a Camera

You can use a camera to create cutscenes, which can then be triggered inside your level. For a deeper dive, check out the Unreal Engine [Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine) page.

To add a camera:

1. Click the **Create Camera** button to add a camera track. This adds a **Camera Cuts** track as well as **CineCameraActor**, which also appears in the Outliner.

   [![Create Camera](https://dev.epicgames.com/community/api/documentation/image/afc66c1c-6594-48d9-bb2f-7d5bf8ae9827?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/afc66c1c-6594-48d9-bb2f-7d5bf8ae9827?resizing_type=fit)
2. Creating a camera switches your view to **Pilot Active**, which allows you to position the camera and frame your shot.
3. Key a camera just like you would a skeletal mesh by selecting the **Transform** row and adding keyframes as you move the camera.
4. Add a second camera and frame a close-up of your character.

Toggle between your camera actors and your regular viewport by clicking the **video camera icon** in the **Camera Cuts** row of Sequencer.

[![camera_cuts](https://dev.epicgames.com/community/api/documentation/image/e593e580-a681-4bd4-a30c-1e69b59e42f0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e593e580-a681-4bd4-a30c-1e69b59e42f0?resizing_type=fit)

You can also select the camera actor by toggling the **CineCameraActor** in the **Perspective** dropdown menu:

[![CineCameraActor](https://dev.epicgames.com/community/api/documentation/image/97543a0d-9e2f-4868-957f-55ab18291f24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97543a0d-9e2f-4868-957f-55ab18291f24?resizing_type=fit)

Return to the regular viewport by pressing the **eject key**.

[![Eject](https://dev.epicgames.com/community/api/documentation/image/029f4fae-5b18-4922-9824-37bda2b01b9f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/029f4fae-5b18-4922-9824-37bda2b01b9f?resizing_type=fit)

## Animate a Skeletal Mesh with FK Control Rig

Sequencer lets you animate your skeletal mesh using a procedurally-generated control rig called **FK Control Rig**. For a complete workflow, check out [FK Control Rig in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine).

Skeletal Meshes with few bones can be easily animated with FK Control Rig. Select the bone you want to animate and keyframe it by either pressing **S** (if your focus is in the viewport), or **Enter** (if your focus is in Sequencer).

Make a small change to your minion’s jogging animation:

## Set Up the Cinematic Sequence Device

Now that you have your sequence, you can add it to the Cinematic Sequence Device and use a trigger to play the cinematic. See [Cinematic Sequence Device](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) for more information specifically on the device.

To add a level sequence to the device:

You can trigger multiple sequences by chaining several Level Sequence devices and triggering them one after another to create more elaborate cutscenes.
