## https://dev.epicgames.com/documentation/en-us/fortnite/sculpting-the-terrain-in-unreal-editor-for-fortnite

# Sculpting the Terrain

Learn how to sculpt a custom terrain.

![Sculpting the Terrain](https://dev.epicgames.com/community/api/documentation/image/df800e68-bfa6-43ee-b15e-05b803572e10?resizing_type=fill&width=1920&height=335)

The [Sculpting toolset](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-sculpt-tool-in-unreal-engine) is a fast way to customize newly created terrain.

By playing around with the different sculpting tools and brush types, you’ll quickly determine how strong a sculpt brush needs to be, the [falloff](unreal-editor-for-fortnite-glossary#falloff) size of a sculpt brush, and which sculpting tools produce which effects on the terrain.

When you open the Sculpt tools in Landscape Mode, the **Sculpt** option is pre-selected. This tool raises or lowers the selected area of terrain, and is the main tool you’ll use to create mountains and hills.

[![The sculpt tool raises or lowers the terrain.](https://dev.epicgames.com/community/api/documentation/image/cad50234-4108-41f0-b9c0-6ae78f0ea009?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cad50234-4108-41f0-b9c0-6ae78f0ea009?resizing_type=fit)

Use the following settings for the Sculpt tool.

You’re ready to begin experimenting with sculpting your terrain. To create terrain that is easy for players to traverse, keep these best practices mind:

- Use big, broad strokes for mountains.
- Use smaller strokes for details.
- Experiment with the clay brush for different effects.

Practice moving your mouse and playing with the settings outlined above when you begin to sculpt the terrain. Experiment with different techniques for creating unique terrain with these tools.

You can lower the terrain while using the Sculpt tool with **Shift + Left Mouse**. Lowering the terrain provides a way to create paintable paths, undo an area that is raised too sharply, and soften raised portions of your terrain to create a gentle slope or cut off a portion of terrain to create a cliff with drop-off.

In the GIF below, the Tool Strength and Brush Falloff type and size settings were changed to create smaller hills.

The layout of the terrain you create should be able to support buildings, vehicles, and gameplay.

To create a mountain, you need to think about how much space you want the mountain to take up, and where you will place the mountain.

Move the viewport camera to where you want to build the mountain.

In the GIF below, the mouse is moving in a large circular motion to create the mountain base.

To create the middle of the mountain, the Sculpt tool settings for Tool Strength and Brush Falloff Type and Size were changed to build up the middle section of the mountain.

Once the middle layer is built, create cliffs in the center of the mountain.

Once you’ve built up the middle, play around with the brush styles, tool strength, and clay brush.

[![An example of a mountain range.](https://dev.epicgames.com/community/api/documentation/image/f815cd41-95c9-4fe4-bc6c-d3eeb460e055?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f815cd41-95c9-4fe4-bc6c-d3eeb460e055?resizing_type=fit)

Last, create plateaus on the mountain that players can access without falling off.

Change the Sculpt tool to **Smooth** and adjust the brush settings to:

Continue to move between the Sculpt and Smooth brushes to create a mountain that players can climb.

[![360 view of the mountain path.](https://dev.epicgames.com/community/api/documentation/image/11471b03-470e-4386-8332-23d1a9683595?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11471b03-470e-4386-8332-23d1a9683595?resizing_type=fit)

Once you’re happy with how your mountain looks, you’re ready to add a body of water using the [water tools](water-environment-tools-in-unreal-editor-for-fortnite).

## Next Section

- [![Painting the Terrain](https://dev.epicgames.com/community/api/documentation/image/8954e0d3-19fe-4349-856a-049939103597?resizing_type=fit&width=640&height=640)

  Painting the Terrain

  Paint your custom terrain to edit its appearance.](https://dev.epicgames.com/documentation/fortnite/painting-the-terrain-in-unreal-editor-for-fortnite)
