## https://dev.epicgames.com/documentation/en-us/fortnite/working-with-the-lego-brick-editor-in-fortnite

# Working with the LEGO® Brick Editor

Learn about the LEGO® Brick Editor and how to use all its tools to build custom assets brick-by-brick.

![Working with the LEGO® Brick Editor](https://dev.epicgames.com/community/api/documentation/image/c0b56727-d260-4d68-8ae4-43a65ee458f8?resizing_type=fill&width=1920&height=335)

You can use the LEGO® Brick Editor to create uniquely built experiences on your islands like you would in your living room - brick by brick! The LEGO Brick Editor has numerous LEGO bricks available, in bright and authentic, opaque LEGO colors. Whether you’re building custom LEGO assets or your own brick-built town, the LEGO Brick Editor makes it possible.

There is no wrong way to start building your own LEGO creations; you can pull out all the bricks you need from the gallery in one go, or pull the bricks out one by one. Or pull a few bricks out and see where your instincts take you. Whatever building style suits you best is the right one!

Get started by opening the **LEGO Brick Editor**:

- In the toolbar, navigate to the **Selection Mode** dropdown, and select **LEGO**®**Brick Editor**.

  [![Open the LEGO Brick Editor form the Selection dropdown menu.](https://dev.epicgames.com/community/api/documentation/image/aa36cd37-f5cb-4f76-8ab7-ca57e8e61fe3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa36cd37-f5cb-4f76-8ab7-ca57e8e61fe3?resizing_type=fit)

  Click to enlarge image.

You can also switch to the LEGO Brick Editor using the keyboard short cut, **Shift+6**.

The LEGO Brick Editor is a tool you use for brick building your own LEGO static meshes that you can use as props, and more. It is a gallery that includes a fixed amount of LEGO Bricks, which you can apply the provided set of original LEGO colors to. You cannot use the LEGO Brick Editor to create your own bricks, nor scales the bricks up and down. You must work with the default stud size of the bricks. For more information about LEGO bricks, see the **[LEGO® Brand Rules](https://dev.epicgames.com/documentation/fortnite/lego-brand-rules-in-fortnite)** and **[Working with LEGO Islands](https://dev.epicgames.com/documentation/fortnite/working-with-lego-islands-in-fortnite-creative)**.

## LEGO Brick Editor Overview

The LEGO Brick Editor adds a UI panel to the left of the viewport containing all the functionality and tools you need to build your own unique brick-built assets. From this panel you’ll select bricks and the brick color, Kragle the bricks together when you’re ready, and separate the bricks when you want to edit your Kragled creation.

The LEGO Brick Editor uses the regular editor features of UEFN such as the Outliner, Details panel, and Content Browser. The LEGO Brick Editor also works with all islands that are based on a LEGO template in the Brand Templates tab in the Project Browser.

[![LEGO template islands can be found in the Project Browser under the Brand Template tile.](https://dev.epicgames.com/community/api/documentation/image/044f4352-f4dd-45a6-8353-94c7d7350077?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/044f4352-f4dd-45a6-8353-94c7d7350077?resizing_type=fit)

The LEGO Brick Editor panel has three major sections:

- **LEGO Brick Editor Tools**
- **Brick Color**
- **Brick Search and Index**

[![The LEGO Brick Editor panel appears on the left hand side of the screen when you change the mode to LEGO Brick Editor.](https://dev.epicgames.com/community/api/documentation/image/b664a1cc-6fb8-4dbc-a840-3ff79b57c28d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b664a1cc-6fb8-4dbc-a840-3ff79b57c28d?resizing_type=fit)

Click to enlarge image.

### LEGO Brick Editor Tools

The LEGO Brick Editor tools have three main functions:

For more information on Kragle, see the Kragle section below.

### Brick Color

[![Brick Color has tools that provide a way for you to change the color of bricks already in the viewport, or the bricks you drag out of the brick index.](https://dev.epicgames.com/community/api/documentation/image/0d0dead0-5d1a-4b24-9804-a35ac524fd96?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d0dead0-5d1a-4b24-9804-a35ac524fd96?resizing_type=fit)

Brick Color includes the following features:

After placing a brick, you can change its color from the **Details** panel.

[![Brick color can be changed through the Details panel as well. Select the Static Mesh from the Details panel breakdown window, then change the brick color from the section entitled Color.](https://dev.epicgames.com/community/api/documentation/image/78cd7e87-c619-477a-86e9-364ed7a1ed9e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/78cd7e87-c619-477a-86e9-364ed7a1ed9e?resizing_type=fit)

Click to enlarge image.

### LEGO Brick Search and Index

The LEGO Brick Editor index lists all available bricks. Scroll through the index to find just the right brick or narrow down your search by typing the name of the brick in the search bar.

[![The brick index has a search bar feature and scrollable window that contains all the available bricks.](https://dev.epicgames.com/community/api/documentation/image/336b9057-f7f9-4722-b641-32871f2a9c73?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/336b9057-f7f9-4722-b641-32871f2a9c73?resizing_type=fit)

Click to enlarge image.

LEGO bricks have a two conditions:

- Bricks in the index have a fixed set of colors. In order to maintain authenticity of the LEGO bricks in UEFN, you aren’t allowed to change their Material.
- Bricks from the index cannot be scaled in your projects. This feature is disabled while in the LEGO Brick Editor mode. Project validators ensure that this rule is followed.

Why can’t you scale the bricks, you ask? LEGO bricks must maintain a uniform scale across the project, in order for the studs and tubes to be able to connect. To learn more about LEGO brick dimensions, see **[Working With LEGO Islands](https://dev.epicgames.com/documentation/fortnite/working-with-lego-islands-in-fortnite-creative)**.

As you build, you may want to duplicate the brick or set of bricks you have selected. To do so, press **Ctrl+D** on the keyboard and a copy will spawn adjacent to your selection. You’ll end up using this shortcut a lot as you build.

To discover all the bricks available in the Brick Editor, see **[LEGO® Brick Index](https://dev.epicgames.com/documentation/fortnite/lego-brick-index-in-fortnite)**.

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

![Default UEFN Editor](https://dev.epicgames.com/community/api/documentation/image/333835f1-7c3c-47b9-988a-7ee9137bfef6?resizing_type=fit&width=1920&height=1080)

![LEGO Brick Editor](https://dev.epicgames.com/community/api/documentation/image/52eac276-6607-4c13-ba64-2e9797f9e279?resizing_type=fit&width=1920&height=1080)

### Advanced Snapping Settings

You can find the advanced snapping settings in the **Mesh Element Selection** settings in the viewport toolbar.

[![Advanced snap settings can be found in the viewport toolbar under the Snap dropdown menu.](https://dev.epicgames.com/community/api/documentation/image/9e728729-f4fc-44fb-8bc1-59b2183d8534?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e728729-f4fc-44fb-8bc1-59b2183d8534?resizing_type=fit)

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

[![An example of a complete structure made of kragled parts.](https://dev.epicgames.com/community/api/documentation/image/438d1e21-723a-4ed0-a578-1b205ec67dc5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/438d1e21-723a-4ed0-a578-1b205ec67dc5?resizing_type=fit)

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

![No Kragle](https://dev.epicgames.com/community/api/documentation/image/8a3129f2-ad7c-4086-94cd-7ccbd56d94c6?resizing_type=fit&width=1920&height=1080)

![With Kragle](https://dev.epicgames.com/community/api/documentation/image/618309d0-9ada-4f39-b959-f9417570caac?resizing_type=fit&width=1920&height=1080)

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
