## https://dev.epicgames.com/documentation/en-us/fortnite/using-hud-message-devices-in-fortnite-creative

# Configuring Collision for a Static Mesh
Players can interact with their environment when you add collision to your props.
![Configuring Collision for a Static Mesh](https://dev.epicgames.com/community/api/documentation/image/c0ed26c8-95ed-4e73-87a8-5601bd0d2c0a?resizing_type=fill&width=1920&height=335)
[](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#collision)[Collision](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#collision) is what prevents objects in your world from intersecting. Without collision, the player would be able to walk through the mesh. The collision box is also the first step to creating a [hitbox](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#hitbox) around an asset you want to enable players to gather resources from.
##  Existing Collision
Double-click your mesh in the **Content Browser** to open the **Edit** window.
If your mesh already has collision, you can view it by toggling **Simple Collision** in the **Show** menu of the static mesh editor.
[![show collision](https://dev.epicgames.com/community/api/documentation/image/1b127ee1-a3d4-46dc-8112-8fe053f00200?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b127ee1-a3d4-46dc-8112-8fe053f00200?resizing_type=fit)
If you want to delete the current collision, you can do this by going to **Collision** > **Remove Collision**.
[![remove collision](https://dev.epicgames.com/community/api/documentation/image/3a1b35cb-b385-45a5-a4f9-a4b3c66494c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a1b35cb-b385-45a5-a4f9-a4b3c66494c6?resizing_type=fit)
##  Static Mesh Set Up
Some meshes you import might have collision already set, using the [Static Mesh Editor](https://dev.epicgames.com/documentation/unreal-engine/static-mesh-editor-ui-in-unreal-engine?application_version=5.5) you can tailor the existing collision settings or create a new collision box on a static mesh. This ensures players can interact with the mesh in the ways you intend, otherwise players could get caught on pieces of geometry as they move around.
You can add collision to static meshes you import whether you created the mesh in external modeling software or you purchased the mesh. To add customized collision to static meshes you purchased from Fab, select the **Add as modifiable Unreal Engine asset**. Without this setting you’ll have to use the default collision that comes with the asset.
Setting collision can also reduce the memory impact of the mesh by reducing the number of polygons the collision box covers. There are two basic types of collision you can set in Unreal Editor for Fortnite (UEFN), simple and complex.
**Simple collision** is used for player movement, convex pieces, and simple 3D shapes. Simple collision reduces the number of polygons affected by the collision box. It’s best to use simple collision on objects you don’t intend players to interact with.
In the image below, the simplified collision is visualized with a green collision box around the sphere. Inside the sphere is a series of purple polygons that make up the shape.
[![](https://dev.epicgames.com/community/api/documentation/image/8804f134-6468-4606-9f76-ccb20956dd25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8804f134-6468-4606-9f76-ccb20956dd25?resizing_type=fit) Click image to enlarge.
**Complex collision** is used on weapons and assets that require player interaction. Without complex collision a player wouldn’t be able to sit in a chair, pick up an object, or easily climb on or travel through an asset.
In the image below the tree trunk is using complex collision, notice the yellow polygons that make up the complex collision box. The complex collision box allows a player to run up to the trunk and step on the roots. If the trunk was in a simplified collision box, the player wouldn't get near the tree trunk.
[![](https://dev.epicgames.com/community/api/documentation/image/9bb6bb22-8c49-4125-99d4-6891ce637db0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9bb6bb22-8c49-4125-99d4-6891ce637db0?resizing_type=fit) Click image to enlarge.
###  Reduce Memory Impact
There are a few ways to reduce the memory impact of a mesh when using complex collision:
  * Turn off complex collision **per section** on a static mesh. This is useful for assets such as trees. Players don't interact with the trunk, but can move around in the leaves at the top.
  * Set **per mesh** basis to use the polygons of a mesh for collision. This setting is best used with complicated meshes.
  * Set **Use Simple as Complex** to save memory for tiny objects.
  * Use the **Nanite Fallback** setting to reduce the number of triangles that count toward memory. This setting doesn’t count the Nanite triangles towards the total memory count.
  * Set collision by using **LOD for Collision** to tailor the collision box size to the LOD of the object. This saves memory for lower performing consoles and mobile.
You can only use LOD for Collision when you turn on the **Nanite Fallback** setting. This option can only be used with complex collision.

##  Adding Simplified Collision
If your mesh does not have collision configured, you can easily add a simple shape around it.
  1. Double-click the **static mesh thumbnail** in the **Content Browser** to open the editor.
  2. In the **Static Mesh Editor** , expand the **Collision** dropdown menu and choose one of the top three options.
[![simplified collision](https://dev.epicgames.com/community/api/documentation/image/275463a1-40ba-4fc6-b744-737d8f6afdcc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/275463a1-40ba-4fc6-b744-737d8f6afdcc?resizing_type=fit)
  3. The newly-created collision has a widget that you can use to translate, rotate, and scale your collision shape.

If you already have a collision on a mesh and you add another collision, the new one will not replace the previous collision, but add to it. Make sure to **Remove Collision** if you want to replace the previous collision.
##  Adding More Complex Collision
If you want your mesh to have more accurate collision, you can use the other options in the **Collision** dropdown menu.
###  K-DOP
These options are called the **K-DOP** simple collision generators. K-DOP is a type of bounding volume where **K** is the number of axis-aligned planes and **DOP** stands for **discrete oriented polytope**. It takes K axis-aligned planes and pushes them as close to the mesh as it can.
In the Static Mesh Editor K can be:
  * 10 - Box with 4 edges beveled - you can choose X- Y- or Z-aligned edges.
  * 18 - Box with all edges beveled.
  * 26 - Box with all edges and corners beveled.

Here is what the mesh looks like with 10-DOP, 18-DOP, and 26-DOP respectively.
[![Kitty DOP](https://dev.epicgames.com/community/api/documentation/image/bb1b4ca3-2142-4ba4-829f-796ad8cc2e82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb1b4ca3-2142-4ba4-829f-796ad8cc2e82?resizing_type=fit)
###  Auto Convex Collision
When you select **Auto Convex Collision** from the **Collision** dropdown menu, you will see a **Convex Decomposition** panel appear on the bottom right corner of the editor.
[![CDP](https://dev.epicgames.com/community/api/documentation/image/4eb201ed-12bc-4783-9366-8b0e13c77414?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4eb201ed-12bc-4783-9366-8b0e13c77414?resizing_type=fit)
**Hull Count** will generate as few primitives as possible to represent the collision mesh. **Max Hull Verts** increases or decreases the number of vertices your collision mesh has. The higher these values, the more precise your collision will be, but also the more complex and memory-hungry. Click **Apply** to apply changes.
Below is the result of having applied the values shown in the previous image.
[![Kitty CDP](https://dev.epicgames.com/community/api/documentation/image/f4d68c32-bdd3-458b-9381-2e54e1b84d5b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f4d68c32-bdd3-458b-9381-2e54e1b84d5b?resizing_type=fit)
###  Combining Simple Shapes
Another simple way to set up complex collisions is by using multiple simple shape collision meshes to create the collision for your mesh.
Add various **Simplified Collision** meshes and use the widget to **translate** ,**rotate** ,**scale** the simple shapes into place.
[Toon Cat FREE](https://sketchfab.com/3d-models/toon-cat-free-b2bd1ee7858444bda366110a2d960386) by [Omabuarts Studio](https://sketchfab.com/omabuarts) licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
