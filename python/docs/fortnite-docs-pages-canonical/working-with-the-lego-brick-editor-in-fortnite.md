## https://dev.epicgames.com/documentation/en-us/fortnite/working-with-the-lego-brick-editor-in-fortnite

# Working with the LEGO® Brick Editor

Learn about the LEGO® Brick Editor and how to use all its tools to build custom assets brick-by-brick.

![Working with the LEGO® Brick Editor](https://dev.epicgames.com/community/api/documentation/image/c0b56727-d260-4d68-8ae4-43a65ee458f8?resizing_type=fill&width=1920&height=335)

You can use the LEGO® Brick Editor to create uniquely built experiences on your islands like you would in your living room - brick by brick! The LEGO Brick Editor has numerous LEGO bricks available, in bright and authentic, opaque LEGO colors. Whether you’re building custom LEGO assets or your own brick-built town, the LEGO Brick Editor makes it possible.

There is no wrong way to start building your own LEGO creations; you can pull out all the bricks you need from the gallery in one go, or pull the bricks out one by one. Or pull a few bricks out and see where your instincts take you. Whatever building style suits you best is the right one!

Get started by opening the **LEGO Brick Editor**:

- In the toolbar, navigate to the **Selection Mode** dropdown, and select **LEGO**®**Brick Editor**.

  [![Open the LEGO Brick Editor form the Selection dropdown menu.](https://dev.epicgames.com/community/api/documentation/image/1888a3f8-49f2-4815-b58c-e7b15d534057?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1888a3f8-49f2-4815-b58c-e7b15d534057?resizing_type=fit)

  Click to enlarge image.

You can also switch to the LEGO Brick Editor using the keyboard short cut, **Shift+6**.

The LEGO Brick Editor is a tool you use for brick building your own LEGO static meshes that you can use as props, and more. It is a gallery that includes a fixed amount of LEGO Bricks, which you can apply the provided set of original LEGO colors to. You cannot use the LEGO Brick Editor to create your own bricks, nor scales the bricks up and down. You must work with the default stud size of the bricks. For more information about LEGO bricks, see the **[LEGO® Brand Rules](https://dev.epicgames.com/documentation/fortnite/lego-brand-rules-in-fortnite)** and **[Working with LEGO Islands](https://dev.epicgames.com/documentation/fortnite/working-with-lego-islands-in-fortnite-creative)**.

## LEGO Brick Editor Overview

The LEGO Brick Editor adds a UI panel to the left of the viewport containing all the functionality and tools you need to build your own unique brick-built assets. From this panel you’ll select bricks and the brick color, Kragle the bricks together when you’re ready, and separate the bricks when you want to edit your Kragled creation.

The LEGO Brick Editor uses the regular editor features of UEFN such as the Outliner, Details panel, and Content Browser. The LEGO Brick Editor also works with all islands that are based on a LEGO template in the Brand Templates tab in the Project Browser.

[![LEGO template islands can be found in the Project Browser under the Brand Template tile.](https://dev.epicgames.com/community/api/documentation/image/551f8d3a-7c0d-4110-a78e-a87289bcf6f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/551f8d3a-7c0d-4110-a78e-a87289bcf6f9?resizing_type=fit)

The LEGO Brick Editor panel has three major sections:

- **LEGO Brick Editor Tools**
- **Brick Color**
- **Brick Search and Index**

[![The LEGO Brick Editor panel appears on the left hand side of the screen when you change the mode to LEGO Brick Editor.](https://dev.epicgames.com/community/api/documentation/image/c36dc7e5-c5d5-4e43-904e-65ed82de8ee9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c36dc7e5-c5d5-4e43-904e-65ed82de8ee9?resizing_type=fit)

Click to enlarge image.

### LEGO Brick Editor Tools

The LEGO Brick Editor tools have three main functions:

For more information on Kragle, see the Kragle section below.

### Brick Color

[![Brick Color has tools that provide a way for you to change the color of bricks already in the viewport, or the bricks you drag out of the brick index.](https://dev.epicgames.com/community/api/documentation/image/5ff65ee5-53f6-4495-bed7-fbaf5ce7dab5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5ff65ee5-53f6-4495-bed7-fbaf5ce7dab5?resizing_type=fit)

Brick Color includes the following features:

After placing a brick, you can change its color from the **Details** panel.

[![Brick color can be changed through the Details panel as well. Select the Static Mesh from the Details panel breakdown window, then change the brick color from the section entitled Color.](https://dev.epicgames.com/community/api/documentation/image/d7b9ac25-940e-4370-9322-a613c0781d21?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7b9ac25-940e-4370-9322-a613c0781d21?resizing_type=fit)

Click to enlarge image.

### LEGO Brick Search and Index

The LEGO Brick Editor index lists all available bricks. Scroll through the index to find just the right brick or narrow down your search by typing the name of the brick in the search bar.

[![The brick index has a search bar feature and scrollable window that contains all the available bricks.](https://dev.epicgames.com/community/api/documentation/image/f62ea93d-8273-4b5b-82f3-80b4dbe9dd86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f62ea93d-8273-4b5b-82f3-80b4dbe9dd86?resizing_type=fit)

Click to enlarge image.

LEGO bricks have a two conditions:

- Bricks in the index have a fixed set of colors. In order to maintain authenticity of the LEGO bricks in UEFN, you aren’t allowed to change their Material.
- Bricks from the index cannot be scaled in your projects. This feature is disabled while in the LEGO Brick Editor mode. Project validators ensure that this rule is followed.

Why can’t you scale the bricks, you ask? LEGO bricks must maintain a uniform scale across the project, in order for the studs and tubes to be able to connect. To learn more about LEGO brick dimensions, see **[Working With LEGO Islands](https://dev.epicgames.com/documentation/fortnite/working-with-lego-islands-in-fortnite-creative)**.

As you build, you may want to duplicate the brick or set of bricks you have selected. To do so, press **Ctrl+D** on the keyboard and a copy will spawn adjacent to your selection. You’ll end up using this shortcut a lot as you build.

### The LEGO Brick Index

Below is an overview of all available LEGO bricks in the editor.

| Available LEGO Bricks |  |  |  |  |
| --- | --- | --- | --- | --- |
| [An example of a 1 x 1 brick.](https://dev.epicgames.com/community/api/documentation/image/5c17e117-3330-4ea9-98fe-4117808db632?resizing_type=fit)  Brick 1 x 1 | [An example of a 1 x 2 brick.](https://dev.epicgames.com/community/api/documentation/image/31162b05-343d-4690-bd78-122a455fab27?resizing_type=fit)  Brick 1 x 2 | [An example of a 1 x 3 brick.](https://dev.epicgames.com/community/api/documentation/image/52115714-934c-4d5a-84eb-8d8ad2512b14?resizing_type=fit)  Brick 1 x 3 | [An example of a 1 x 4 brick.](https://dev.epicgames.com/community/api/documentation/image/ca262cd9-656e-4d5e-b144-03e69ba43c87?resizing_type=fit)  Brick 1 x 4 | [An example of a 2 x 2 brick.](https://dev.epicgames.com/community/api/documentation/image/0a744883-6f62-4592-b7d5-fbb9062c5073?resizing_type=fit)  Brick 2 x 2 |
| [An example of a 2 x 3 brick.](https://dev.epicgames.com/community/api/documentation/image/c4aaf3c3-be0e-4124-8c34-44aafd492c47?resizing_type=fit)  Brick 2 x 3 | [An example of a 2 x 4 brick.](https://dev.epicgames.com/community/api/documentation/image/3346a7ac-ffea-4195-ba79-2ccc0a746fdc?resizing_type=fit)  Brick 2 x 4 | [An exampleof a 1 x 4 brick with a bow.](https://dev.epicgames.com/community/api/documentation/image/a65456f3-1c11-4ebd-a8c9-5c847610cb06?resizing_type=fit)  Brick with Bow   1 x 4 | [An example of a 1 x 2 x 1 brick with bow and cutout.](https://dev.epicgames.com/community/api/documentation/image/0fa2bd2e-deb0-4c75-9620-6fd0baa1f86f?resizing_type=fit)  Brick  1 x 2 x 1 Bow, with Cutout | [An example of a small 1 x 1 Nose Cone.](https://dev.epicgames.com/community/api/documentation/image/efb5bb43-584f-4ee7-bcd4-a295389679a9?resizing_type=fit)  Nose Cone Small 1 x 1 |
| [An example of a 1 x 1 round brick.](https://dev.epicgames.com/community/api/documentation/image/ab5c31b9-aec3-4dab-8858-2a0016598946?resizing_type=fit)  Round Brick  1 x 1 | [An example of a 16 with Cross](https://dev.epicgames.com/community/api/documentation/image/3add9d2c-14a5-433d-b61d-95cd6793dda8?resizing_type=fit)  Brick 16 with Cross | [An example of a 2 x 2 x 2 Nose Cone.](https://dev.epicgames.com/community/api/documentation/image/258dc970-6e3c-4330-9708-3e6c52f7fd5f?resizing_type=fit)  Nose Cone  2 x 2 x 2 | [An example of a 1 x 1 plate.](https://dev.epicgames.com/community/api/documentation/image/bdb89641-41f5-4215-a0a5-776cd7dc6c4c?resizing_type=fit)  Plate 1 x 1 | [An example of a 1 x 2 plate.](https://dev.epicgames.com/community/api/documentation/image/68ed2448-cc3e-4a20-a0fb-f8757b3691ea?resizing_type=fit)  Plate 1 x 2 |
| [An example of a 1 x 3 plate.](https://dev.epicgames.com/community/api/documentation/image/daa47af8-fc46-435d-a530-b203c1654bb7?resizing_type=fit)  Plate 1 x 3 | [An example of a 1 x 4 plate.](https://dev.epicgames.com/community/api/documentation/image/05273a15-8071-423f-bb84-51046b7f7c6e?resizing_type=fit)  Plate 1 x 4 | [An example of a 1 x 8 plate.](https://dev.epicgames.com/community/api/documentation/image/4870b5ee-3cc1-4701-84c9-d6e03ba5569e?resizing_type=fit)  Plate 1 x 8 | [An example of a 2 x 2 plate.](https://dev.epicgames.com/community/api/documentation/image/ef5abce0-6c32-4017-8171-4f7aee407efe?resizing_type=fit)  Plate 2 x 2 | [An example of a 2 x 3 plate.](https://dev.epicgames.com/community/api/documentation/image/4fb8cf47-e305-4152-aca1-082efc155415?resizing_type=fit)  Plate 2 x 3 |
| [An example of a 2 x 4 plate.](https://dev.epicgames.com/community/api/documentation/image/ec280dc8-5bfd-494c-907b-ae7748856451?resizing_type=fit)  Plate 2 x 4 | [An example of a 2 x 8 plate.](https://dev.epicgames.com/community/api/documentation/image/a96d95ce-840e-4bf1-aedc-195859b063d2?resizing_type=fit)  Plate 2 x 8 | [An example of a 4 x 6 plate.](https://dev.epicgames.com/community/api/documentation/image/4d58204e-0cff-4983-8961-0c806f5c0dfc?resizing_type=fit)  Plate 4 x 6 | [An example of a n 8 x 8 plate.](https://dev.epicgames.com/community/api/documentation/image/55ceef0a-aede-4730-a801-d3a93f43b52b?resizing_type=fit)  Plate 8 x 8 | [An example of a 1 x 2 x 2 corner plate.](https://dev.epicgames.com/community/api/documentation/image/8cd282c6-963b-4d47-8ac1-01128ba5321d?resizing_type=fit)  Corner Plate  1 x 2 x 2 |
| [An example of a 2 x 2 45 degree angle Corner Plate.](https://dev.epicgames.com/community/api/documentation/image/49540983-8c32-41db-b84a-07ac7dc717bf?resizing_type=fit)  Corner Plate  2 x 2 45° Angle | [An example of a 3 x 3 corner plate with a 45 degree angle.](https://dev.epicgames.com/community/api/documentation/image/e7832ae3-c214-4737-8613-431307c5e588?resizing_type=fit)  Corner Plate  3 x 3 45° Angle | [An example of a 1 x 1 round brick.](https://dev.epicgames.com/community/api/documentation/image/4607e353-53bd-4aea-9ef9-74ed19d99338?resizing_type=fit)  Round Brick  1 x 1 | [An example of a 2 x 2 round plate.](https://dev.epicgames.com/community/api/documentation/image/c424afbe-6a2e-4b38-b1fd-1dd9ba0954cc?resizing_type=fit)  Round Brick  2 x 2 | [An example of a 1 x 1 plate with tooth.](https://dev.epicgames.com/community/api/documentation/image/f8fb3c9e-25ab-456e-ab3f-fe3156fe25e1?resizing_type=fit)  Plate 1 x 1 with Tooth |
| [An example of a 1 x 2 plate with one knob.](https://dev.epicgames.com/community/api/documentation/image/9119bbad-6d2a-47b4-b499-95f599f016e2?resizing_type=fit)  Plate 1 x 2  with 1 Knob | [An example of a 2 x 2 plate with one knob.](https://dev.epicgames.com/community/api/documentation/image/73f8f2f2-7f02-4c2b-be05-f89b17457508?resizing_type=fit)  Plate 2 x 2 with 1 Knob | [An example of a 16 satellite dish](https://dev.epicgames.com/community/api/documentation/image/4bfe594b-0ea5-4f18-9d6e-7e32ccae3781?resizing_type=fit)  Satellite Dish 16 | [An example fo a 1 x 1 flat tile.](https://dev.epicgames.com/community/api/documentation/image/b1c99ff3-4cdb-4fe1-b2dd-379dc1a521b2?resizing_type=fit)  Flat Tile 1 x 1 | [An example of a 1 x 1 flat tile.](https://dev.epicgames.com/community/api/documentation/image/4d01da49-2b04-4da8-9416-1b4d5d638be5?resizing_type=fit)  Flat Tile 1 x 2 |
| [An example of a 1 x 3 flat tile.](https://dev.epicgames.com/community/api/documentation/image/24b1fbee-f3ee-494e-a615-d8f933f5438e?resizing_type=fit)  Flat Tile 1 x 3 | [An example of a 1 x 4 flat tile.](https://dev.epicgames.com/community/api/documentation/image/262b97a9-9c32-4171-9e60-7ff5b59feea1?resizing_type=fit)  Flat Tile 1 x 4 | [An example of a 2 x 2 flat tile.](https://dev.epicgames.com/community/api/documentation/image/882b9365-c5f1-4a84-91d5-1643e8c65018?resizing_type=fit)  Flat Tile 2 x 2 | [An example of a 1 x 2 radiator grille.](https://dev.epicgames.com/community/api/documentation/image/3dc27623-eb43-4388-b088-4f59096fcf41?resizing_type=fit)  Radiator Grille  1 x 2 | [An example of a 1 x 1 flat round tile.](https://dev.epicgames.com/community/api/documentation/image/fcd355d4-f78d-4027-92c2-ac06333dfa53?resizing_type=fit)  Flat Tile 1 x 1 Round |
| [An example of a 2 x 2 falt round tile.](https://dev.epicgames.com/community/api/documentation/image/74d9c910-4978-4f1f-b037-ca1c38b3722b?resizing_type=fit)  Flat Tile 2 x 2 Round | [An example of a quarter 1 x 1 circle tile.](https://dev.epicgames.com/community/api/documentation/image/7fcd02b4-a1c3-4ba9-b8d3-803f79b0a210?resizing_type=fit)  ¼ Circle Tile 1X1 | [An example of a 2 x 2 tile with bow.](https://dev.epicgames.com/community/api/documentation/image/fb9724aa-f7a4-4a81-b6d4-da7053b853db?resizing_type=fit)  Tile 2 x 2 with Bow | [An example of 2 x 3 flat tile with angle.](https://dev.epicgames.com/community/api/documentation/image/c37e6bb5-11a1-4f78-a9e7-2a8640c0a158?resizing_type=fit)  Flat Tile 2X3 with Angle | [An example of a 1 x 1 x](https://dev.epicgames.com/community/api/documentation/image/d2e327ba-d8c0-4c19-a8f0-7ab46cc0f117?resizing_type=fit)  Roof Tile  1 x 1 x ⅔ |
| [An example of a 1 x 1 x ⅔ roof tile.](https://dev.epicgames.com/community/api/documentation/image/3bcd33cd-14b0-4279-802c-3b2717c50d83?resizing_type=fit)  Roof Tile  1 x 2 x ⅔ | [An example of a 1 x 2 45 degree angle roof tile.](https://dev.epicgames.com/community/api/documentation/image/4ff2fe8f-b690-4d8a-866b-2d53d9bd8b21?resizing_type=fit)  Roof Tile 1 x 2 with 45° Angle | [An example of a 1 x 3 roof tile with a 45 degree angle.](https://dev.epicgames.com/community/api/documentation/image/3018c3a0-e55f-471a-8899-174a54f9ed87?resizing_type=fit)  Roof Tile 1 x 3 with 45° Angle | [An example of an 1 x 2 inverted roof tile.](https://dev.epicgames.com/community/api/documentation/image/e1776761-5fc5-4c15-953e-489cc3a45227?resizing_type=fit)  Roof Tile 1 x 2 Inverted | [An example of a 1 x 3 inverted roof tile with 25 degree angle.](https://dev.epicgames.com/community/api/documentation/image/5337ae3a-ab62-40fe-948f-3d96b96ca19c?resizing_type=fit)  Roof Tile 1 x 3 Inverted with 25° Angle |
| Profile Brick 1 x 2 | Profile Brick 1 x 2 Single Gro. | Palisade Brick  1 x 2 | Column 1 x 1 x 6 | Double Sphere 2 x 2 x 1 2/3, with Knob |
| Pyramid Ridged Tile 1 x 1 x 2/3 | Roof Tile with Lattice  1 x 2 x 2/3 | Roof Tile 1 x 2 45° Angle, without Knobs | Roof Tile 1 x 2 Inverted, 45° Angle, with Cut | Plate 2 x 2 x 2/3 Bow, Inverted Bow |
| Brick 1 x 3 x 3 Inside Arch, with Cutout, Knob | Brick 1 x 3 Outside Half Arch | Brick 1 x 3 x 2 with Inside Bow | Brick with Bow  1 x 5 x 4 Inv. | Brick with Bow  1 x 3 x 3 |
| Brick with Bow  1 x 4 x 3 | Brick with Bow  1 x 5 x 4 | Window Arch | Window Arch Corner | Fence 1 x 4 x 2 with 4 Knobs |
| Fence 1 x 4 x 2 with Shaft | Vegetable | Kitchen Equipment |  |  |

## Brick Building

Ready to start building like a Master Builder? Here are the basic steps to get you started:

To practice using the Lego Brick Editor, open the **[LEGO Brick Editor Template](https://dev.epicgames.com/documentation/fortnite/lego-brick-editor-template-in-fortnite)** island and follow the LEGO Brick Editor Template document to learn more about working with the LEGO Brick Editor tools.

To disassemble bricks, select the Kragled bricks, then select **Separate** from the LEGO Brick Editor tools. The bricks become instantly unglued, but don’t fall apart.

## Brick Rotation

Bricks rotate with the standard rotation gizmo. In Rotate Mode when a brick is selected, a diamond shape appears inside the brick. The diamond rotates with the LEGO brick by the gizmo to give you an idea of the 3D view of the brick. Each stud and connection point is a different pivot point on all bricks, so you can set the rotation gizmo to a top pivot point and a bottom pivot point.

By default, bricks snap at a 90 degree angle around each axis. You can use your keyboard to rotate your bricks.

When you click on a brick, a yellow diamond appears. The editor finds the closest connectivity field to your cursor and uses that as the pivot for rotation. The connectivity field acts like a sensor and a magnet. It senses when another brick is close and then guides the brick towards the closest stud on the brick or plate for connectivity.

When working with LEGO bricks, it’s important to do so in the LEGO Brick Editor tool. When this tool is active, it overrides the toolbar with its own selection, translation, and rotation gizmos. Using these gizmos outside of the tool will not preserve LEGO connectivity.

## Snapping Bricks Together

In the LEGO Brick Editor mode, the bricks snap together automatically when they are within proximity to one another. For optimal brick snapping, ensure that your **UEFN Snapping Location** settings are set to **16** when you’re working with the LEGO Brick Editor.

LEGO bricks use multiples of 16 to snap to the Stud Region on the grid. For more information about LEGO studs, brick sizes, snapping, and more, see [Working With LEGO Islands](https://dev.epicgames.com/documentation/fortnite/working-with-lego-islands-in-fortnite-creative).

LEGO® Brick snapping is only in effect when using the LEGO Brick Editor mode. The LEGO Brick Editor snap settings use different snap size dimensions from the default UEFN Editor. When using LEGO Brick Editor Mode the following Fortnite snap settings are unavailable:

- Snapping Toggle
- Snap to Grid
- Snap to Present Angle
- Scaling Resize Ratios

![Default UEFN Editor](https://dev.epicgames.com/community/api/documentation/image/4348a0bd-5b27-40f8-b5fd-0ea3278a58f6?resizing_type=fit&width=1920&height=1080)

![LEGO Brick Editor](https://dev.epicgames.com/community/api/documentation/image/f8ac4bdb-44bf-49d1-ae21-7e953152bdf9?resizing_type=fit&width=1920&height=1080)

### Advanced Snapping Settings

You can find the advanced snapping settings in the **Mesh Element Selection** settings in the viewport toolbar.

[![Advanced snap settings can be found in the viewport toolbar under the Snap dropdown menu.](https://dev.epicgames.com/community/api/documentation/image/1c3b0a37-8171-42f7-a60f-357388bd67c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c3b0a37-8171-42f7-a60f-357388bd67c6?resizing_type=fit)

| Setting | Function |
| --- | --- |
| **Click to End Drag** | The brick follows the mouse movement until clicked into place on another brick or onto the grid.  This setting is off be default, select an unkragled brick in the viewport to engage this setting. |
| **Enable Edge Snapping** | Makes bricks attempt to snap together when they are placed adjacent to each other. |
| **Max Snapping Distance** | The maximum distance to move the selection to complete a snap when you’re using a gizmo. |
| **Single Field Placement** | Determines if a single stud or tube should connect another single stud or tube when you’re dragging bricks. |

You can customize snapping by configuring a way to select snapping according to the brick’s Surface, Rotation, and more. Click the **Magnet** icon from the viewport toolbar to select new **Snapping** settings.

In the LEGO Brick Editor, bricks snap together like they would in the real world. They can only snap together on top of each other, and cannot intersect each other. If you’re unable to snap something together, check to see if there’s anything obstructing the brick from being targeted in the viewport. You can also exit and then return to the LEGO Brick Editor, to see if a soft reset helps.

## Kragling Your LEGO Creation

Much like in The LEGO Movie, your LEGO bricks can be “glued” together into one optimized static mesh, without worrying about getting Kragle on your hands. The Kragle tool works like a digital content creation tool. You can use it to build modular pieces you can use multiple times in your project.

Break a large object into multiple smaller subsets and kragle them individually.

For example, when creating a building, you can kragle the different wall pieces together as one reusable piece. Continue to kragle the different parts of the building together; floors, roofs, and more.

For creating items for your experience, kragle the basic structure together, then add different bricks to embellish and distinguish one item from another.

[![An example of a complete structure made of kragled parts.](https://dev.epicgames.com/community/api/documentation/image/1ee2b0a8-22e9-4eca-bbab-b5f81a956876?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ee2b0a8-22e9-4eca-bbab-b5f81a956876?resizing_type=fit)

When you kragle assets, all your kragled meshes collect in the Content Browser.

When in selection mode, double-clicking on a LEGO brick or mesh selects that item and all other items that are connected to that object via studs. The process automatically continues until all the connected ancestors and descendants are selected. This is handy when you want to select your set of bricks to kragle.

Kragling has a few restrictions and tips to keep in mind as you build:

- Once a structure has been kragled, you can’t apply a new color to the kragled bricks. To add a new color, you’ll have to separate the bricks and then kragle them again.
- Kragling works on the selected bricks. It does not matter if they are physically snapped together or just nearby each other. Kragling can take some time, so please be patient.
- Undoing a Kragle operation will return the originating bricks, but will not undo changes to the kragled mesh. This is done for memory purposes, as it is not feasible to keep entire meshes in the undo history.
- If you kragle on top of an existing kragled Mesh, all instances of that mesh in the scene will be updated. Be careful doing this, as you might adjust the shape too much and accidentally make interpenetrations or break existing connectivity.
- Kragled meshes have their pivot in the bottom center of the generated mesh. If this is not to your liking, you can edit it after generation using the **Modeling Mode**/**Edit Pivot** tool. Changed pivots are not preserved if re-kragling.
- You may also wish to fine-tune the generated collision volume. This is acceptable as long as you preserve the LEGO/LEGO interpenetration detection. Changes are not preserved if re-kragling.
- In order to optimize meshes, kragling will attempt to determine if there is any way to see a given triangle from the outside. If there isn’t a path, those triangles are removed. This greatly reduces the final triangle count, but it also impacts how you model. Don’t make really complex spaces that you intend to walk in as one kragled mesh. Break it up into constituent pieces.

### Memory Management When Kragling

Kragled bricks are considered custom built assets by the editor. Depending on the size of the LEGO structure you build, it could be quite memory intensive. This is where kragling key pieces together comes in handy, since it’s an effective way to work within the memory limit.

A kragled model has a larger imprint than a model that isn’t kragled. The un-kragled model instances the repeated parts, even at the brick level. When a model is kragled into one object, it’s no longer able to instance the individual bricks, so it uses more memory.

![No Kragle](https://dev.epicgames.com/community/api/documentation/image/3f1f9694-d89b-42a6-a8cc-b4f13267fe00?resizing_type=fit&width=1920&height=1080)

![With Kragle](https://dev.epicgames.com/community/api/documentation/image/b8f709db-1970-4227-8c31-04ae35c1c162?resizing_type=fit&width=1920&height=1080)

So why would you want to kragle your brick-built assets? Kragling makes the building process faster! When you kragle key pieces of your design together you create a repeating pattern that can be joined together to make a larger object. You also avoid dragging each individual brick into place in the viewport when you want to move the structure you built.

When an asset is kragled, it becomes a [static mesh](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#static-mesh). This static mesh is highly optimized and runs more efficiently than individual bricks. The same static mesh can be used multiple times in a project without increasing the memory requirements, because the duplicates reference the original static mesh instance and its information with no additional memory cost.

The LEGO Brick Editor also works with UEFN’s memory management tools. To optimize your project, see the documents in the **[Memory and Optimization](https://dev.epicgames.com/documentation/fortnite/memory-and-optimization-in-unreal-editor-for-fortnite)** section.

You can add new LEGO bricks to meshes that have already been kragled to continue building your beautiful creation.

## Frequently Asked Questions

### Does the LEGO Brick Editor work with the LEGO Assembly Device?

No, items created with the LEGO Brick Editor cannot be used with the Assembly Device. The Assembly device uses LEGO assets that are geometry collections, whereas the LEGO Brick Editor uses static meshes. Because the LEGO Brick Editor exports a static mesh, the Assembly device does not identify it as an object that can be assembled

### How do individual bricks and kragled meshes interact with assets from the existing LEGO content gallery?

For the first version, we’re keeping them apart with respect to the editor mode. You can’t select anything but the individual bricks or kragled meshes in the editor mode and the connectivity rules do not take the gallery items into account.

### How can I get more bricks and brick colors?

This initial release was kept small to introduce this editor to the community and see what features are needed to be valuable to developers. You cannot create new bricks or apply other colors than the presets available. New bricks and colors may be added to the LEGO Brick Editor. For more information on what you can and cannot do with LEGO bricks, see the **[LEGO® Brand Rules](https://dev.epicgames.com/documentation/fortnite/lego-brand-rules-in-fortnite)**.

### The editor is missing a key feature, when is it coming?

This initial release was kept small to introduce this editor to the community and see what features are needed to be valuable to developers. Please give feedback in the [forums](https://forums.unrealengine.com/categories?tag=fortnite) about what you’d like to see.

### Can I use LEGO Brick Editor and BuildingProp together?

Yes, you can use the kragled static meshes in your Fortnite Building Prop and Building Static Mesh actors.

### Can I use LEGO Brick Editor and Scene Graph together?

Yes, once you create a static mesh through kragling, the generated mesh can be referenced with a Mesh Component. Note that the same rules apply to Scene Graph, the materials must not be changed, the scale must not change, and avoid LEGO/LEGO interpenetrations. The first two are protected by validation, but we do not yet validate object overlap for Mesh Components. This will change in a future release.

### Will the bricks fall apart when hit?

For the first version, we are not adding support for Geometry Collections, which is the underlying object format for destructible LEGO content gallery items. Similarly, the Assembly Device requires Geometry Collections to function, so it is unsupported in this first version. For now it is suggested you use the techniques from the Adventure Template to have your BuildingProps disappear on death and spawn the individual currency studs.
