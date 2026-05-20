## https://dev.epicgames.com/documentation/en-us/fortnite/animation-101-template-in-unreal-editor-for-fortnite

# Animation 101 Template

Learn various ways to animate skeletal meshes.

![Animation 101 Template](https://dev.epicgames.com/community/api/documentation/image/c4e9a3fa-282e-4981-a358-41fda724c0b9?resizing_type=fill&width=1920&height=335)

The **Animation 101** template is a fast way to learn how to animate skeletal meshes.

This template showcases the current slate of animation devices, tools, assets, and workflows available in UEFN.

It also packages some of the assets you’ll need to plug into those devices and tools from the Content Browser.

This template takes you on an educational journey into a museum where you will learn about skeletal meshes and how to animate them, using either the [Animated Mesh](https://dev.epicgames.com/documentation/fortnite/using-animated-mesh-device-in-unreal-editor-for-fortnite) device or the **[Control Rig](https://dev.epicgames.com/documentation/fortnite/control-rig)** and [Sequencer](https://dev.epicgames.com/documentation/fortnite/sequencer-and-control-rig-in-unreal-editor-for-fortnite).

You can find this template in the **Project Templates** section of the **Project Browser**.

This tutorial will walk you through the template and explain its contents.

[![Launch Session](https://dev.epicgames.com/community/api/documentation/image/9109c054-b852-47eb-9fab-debd631df368?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9109c054-b852-47eb-9fab-debd631df368?resizing_type=fit)

## Skeletal Mesh

[![iSkeletal Mesh](https://dev.epicgames.com/community/api/documentation/image/98bc2e58-6c4d-41d1-84cf-d4970fd75ca2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98bc2e58-6c4d-41d1-84cf-d4970fd75ca2?resizing_type=fit)

When you load into the game, you will see a skeletal mesh of a Fortnite mannequin. Skeletal meshes are models that can be animated with the Animated Mesh device, or with the Control Rig in the Sequencer.

Skeletal meshes are the primary asset that animations are played on.

In the **Content Drawer**, under **Mannequin**, you have various assets that make up our mannequin.

When you drag the FN_Mannequin skeletal mesh into the island, it will look like the process shown above and create a FortSkeletalMeshActor.

[![Mannequin Details Panel](https://dev.epicgames.com/community/api/documentation/image/026c3b17-57b1-43ba-b014-57c98a1b1495?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/026c3b17-57b1-43ba-b014-57c98a1b1495?resizing_type=fit)

In the **Details** panel you can change the mannequin mesh to any other skeletal mesh. You can also change the material.

In the museum's hallway, you will see skeletal meshes with different animations.

You can instance animations, which creates a skeletal mesh actor and associates an animation to play on it. You can also change the skeletal mesh and animation.

When you drag an animation sequence from the Animations folder, it creates a FortSkeletalMesh with the FN_Mannequin skeletal mesh just as in the first example, but also associates an animation sequence to it.

The following settings will show in the **Details** panel when you apply an animation to a skeletal mesh.

[![Skeletal Mesh Details Panel](https://dev.epicgames.com/community/api/documentation/image/93850bae-fbe0-4287-8a8b-e917e2228629?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93850bae-fbe0-4287-8a8b-e917e2228629?resizing_type=fit)

- Looping: Determines whether the animation loops.
- Playing: Determines whether the animation plays in game /edit mode.
- Initial Position: Sets the animation frame to sit on if you’re not playing.
- Play Rate: Sets the animation speed. 1.0 = 100%

For consistency, you can determine whether instanced animation sequences play or not.

## Animated Mesh Device

[![Animated Mesh device](https://dev.epicgames.com/community/api/documentation/image/ded03b7d-9e5c-4f22-8cca-b96fe7788217?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ded03b7d-9e5c-4f22-8cca-b96fe7788217?resizing_type=fit)

Inside the theater are skeletal meshes paired with an Animated Mesh device.

Using the Animated Mesh device, you can set skeletal meshes to play many different animations that can be paused and reversed through triggers like the **[Button](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative)** device.

[![An example of the Animated Mesh details panel.](https://dev.epicgames.com/community/api/documentation/image/2694aef4-a566-4098-ba51-8831c654bd54?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2694aef4-a566-4098-ba51-8831c654bd54?resizing_type=fit)

Animated Mesh device user options and functions

The Animated Mesh device gives you the same controls that the base Skeletal Mesh actor gives you. You can also bind events to tell this device when to play, pause, or play in reverse during the game.

You can use the Button devices on the desk to trigger these events as a demo.

Skeletal Meshes without this device, like the ones at the entryway, will be unchangeable during gameplay. For more control on animations during gameplay, use the Animated Mesh device.

Skeletal Meshes don’t collide with the player, the world, or each other.

## Cinematic Sequence Device

[![Cinematic Sequence Device](https://dev.epicgames.com/community/api/documentation/image/7109ab1c-c30a-4758-b938-6e05935edd52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7109ab1c-c30a-4758-b938-6e05935edd52?resizing_type=fit)

Up the stairway is where you will find the [Cinematic Sequence](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) device along with a button that triggers a short cinematic.

You can watch this sequence in-game after interacting with the button, which activates the Play function of the Cinematic Sequence device.

[![Cinematic Sequence Details](https://dev.epicgames.com/community/api/documentation/image/aeb5b67e-6f83-48e3-ba06-92cc1ed1c53b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aeb5b67e-6f83-48e3-ba06-92cc1ed1c53b?resizing_type=fit)

You can use the Cinematic Sequence device to playback Level Sequences built in the Sequencer.

You must be in the project folder to add your own cinematics.

To make your own cinematics, locate the project folder in the **Content Drawer** then click **+Add**. Then, scroll to **Cinematics** and click **Level Sequence**.

You can double-click on your new Level Sequence to pull up the Sequencer.

The Sequencer is where you edit Level Sequences with control over what, when, where, and how long a cinematic will play. There are also many more features in the Sequencer.

[![Sequencer](https://dev.epicgames.com/community/api/documentation/image/3ab06827-0ec9-4fbf-b9b4-4aa5e4c0b8a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ab06827-0ec9-4fbf-b9b4-4aa5e4c0b8a5?resizing_type=fit)

To demo the Sequencer’s capabilities, navigate to the **Sequences** folder in the **Content Drawer** of UEFN. Then, select MuseumFlyThrough and double-click on it to open the Sequencer.

[![Sequencer](https://dev.epicgames.com/community/api/documentation/image/562cb6e4-8663-4df6-9544-ae751018e725?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/562cb6e4-8663-4df6-9544-ae751018e725?resizing_type=fit)

Alternatively, you can access the Sequencer through the **Cinematics** tab of the **Window** menu.

## Control Rig

The Control Rig can customize an animation as well as layer on props, visual effects, and more.

Double-click on the **MuseumFlyThrough sequence** thubmnail to open Sequencer, from here you can modify the sequence to make your own. This Sequencer includes:

- A camera cut track to animate and cut between cameras

  [![The Camera Cut tracks in Sequencer.](https://dev.epicgames.com/community/api/documentation/image/a643b3a1-1b7e-4868-85cf-b2ef5bd352b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a643b3a1-1b7e-4868-85cf-b2ef5bd352b3?resizing_type=fit)

  *Click image to enlarge.*

Double-click the **Control Rig** thumbnail to open the Control Rig Editor.

- Three [Control Rigs](https://docs.unrealengine.com/5.1/en-US/animation-editor-mode-in-unreal-engine/)

  [![The 3 Control Rigs assigned to the sequence.](https://dev.epicgames.com/community/api/documentation/image/271e1f2f-ca3a-4a7d-847a-9eaf7eb57e1c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/271e1f2f-ca3a-4a7d-847a-9eaf7eb57e1c?resizing_type=fit)

  *Click image to enlarge.*

Next, you can open the **Content Drawer** to the **Mannequin** folder and select the **Meshes** folder. Then, drag FN_Mannequin_ControlRig onto your island.

[![Animation Mode](https://dev.epicgames.com/community/api/documentation/image/df5ded80-e0f9-411a-9e38-7d2c7a8ca779?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df5ded80-e0f9-411a-9e38-7d2c7a8ca779?resizing_type=fit)

UEFN will then enter Animation Mode and automatically add this actor to your active sequence or make a new one.

With the Control Rig, you can animate in the Control Rig Editor by creating a new Control and animation.

[![Control Rig](https://dev.epicgames.com/community/api/documentation/image/93f03474-e50a-4643-bec0-bd84fb9fc012?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93f03474-e50a-4643-bec0-bd84fb9fc012?resizing_type=fit)

Double-clicking the **Control Rig** from the **Content Drawer** opens the Rig Graph, which allows you to add or change controls as you see fit.

You can also create manual animations with the Control Rig and Sequencer.

Follow these steps to make a new animation.

1. Drag the **Control Rig** from the **Mannequin** > **Meshes** folders and place it in your project. Sequencer opens and your character is selected in the viewport.
2. Add a **Transform Track**. Sequencer automatically applies a filter for **Control Rig Controls**.

   [![Transform Track](https://dev.epicgames.com/community/api/documentation/image/73e07ddd-0165-46e6-bca7-b83cada54fc6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/73e07ddd-0165-46e6-bca7-b83cada54fc6?resizing_type=fit)
3. Select a control from the panel and a pivot point appears on the limb.

   [![Select which controls you're using then move the mannequin.](https://dev.epicgames.com/community/api/documentation/image/c47cdf46-563d-4277-bbfa-01d5ed66c483?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c47cdf46-563d-4277-bbfa-01d5ed66c483?resizing_type=fit)
4. Make a key frame by hitting **Enter** or the key icon on the track.

   [![IKey Frame](https://dev.epicgames.com/community/api/documentation/image/ea25cbbb-bd5e-4937-beb1-66e9457cf9b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ea25cbbb-bd5e-4937-beb1-66e9457cf9b3?resizing_type=fit)
5. Move the limb into a new pose.
6. Scrub the play head forward, and repeat.
7. Save the animation as an animation sequence. Watch [this](https://www.youtube.com/watch?v=FgJ1stTScxI&t=1538s) YouTube video to find out more.

[![Bake to Control Rig](https://dev.epicgames.com/community/api/documentation/image/4983cb6d-a7c5-45bc-8603-be8df1bd69b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4983cb6d-a7c5-45bc-8603-be8df1bd69b5?resizing_type=fit)

To modify an existing animation, select **Bake To Control Rig** in the **Sequencer** then select your rig.

Use this section of Unreal Engine [Control Rig](https://dev.epicgames.com/documentation/unreal-engine/rigging-with-control-rig-in-unreal-engine?application_version=5.5) documentation to learn how to rig characters an create animations.

[![Mannequin Animation](https://dev.epicgames.com/community/api/documentation/image/c542b3f2-7b0f-4a4a-8a8b-adf2c5cf6778?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c542b3f2-7b0f-4a4a-8a8b-adf2c5cf6778?resizing_type=fit)

You can even attach props to animated meshes.

[![Mannequin Attachment](https://dev.epicgames.com/community/api/documentation/image/15fbce26-64e9-4a48-a9e4-a35ce8689fe0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/15fbce26-64e9-4a48-a9e4-a35ce8689fe0?resizing_type=fit)
