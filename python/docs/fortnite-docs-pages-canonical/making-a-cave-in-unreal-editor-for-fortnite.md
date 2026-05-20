## https://dev.epicgames.com/documentation/en-us/fortnite/making-a-cave-in-unreal-editor-for-fortnite

# Making a Cave

Create a cave inside your custom terrain.

![Making a Cave](https://dev.epicgames.com/community/api/documentation/image/570f2dfc-3013-4939-bf5b-e0d677879ad6?resizing_type=fill&width=1920&height=335)

Tunnels or caves that players can drive or walk through can also contain spaces where players can explore and find hidden treasures.

Plan where you'll place the cave entrance on your mountain. It should be a place players can easily access. The best place is on ground level or at the lowest level of a mountain so you have the space to create the type of cave you want.

To create the cave or tunnel, you’ll need the **Landscape Visibility** tool and the **Fort Underground Volume**. Without the [volume](unreal-editor-for-fortnite-glossary#volume), players despawn from the world after entering the cave, and vehicles teleport to the terrain above the cave.

When you’ve decided where to start the cave, switch to the **Sculpt** tools and select **Visibility**.

[![](https://dev.epicgames.com/community/api/documentation/image/0985cab1-0707-419f-9ba1-3ee117bee60c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0985cab1-0707-419f-9ba1-3ee117bee60c?resizing_type=fit)

Use the following Visibility settings:

Get the initial volume set inside the cave or tunnel, then form the walls of the cave and floor using gallery props or custom imported assets to build out the cave walls and floor. The Gray Cliff Grass Gallery works well with the base terrain that spawns. You can find it in the Content Browser under **Fortnite** > **Galleries** > **Terrain**.

If you use the Gray Cliff Grass Gallery, drag either the **Cave Tunnel Straight** prop or the **Cave Tunnel Straight X2 New** prop into the viewport, placing it close to the entrance of the cave. Scale the tunnel piece in the **Details** panel.

If you don’t intend to create a tunnel, drag the **Cave Tunnel End** into the viewport and scale to align with the straight tunnel piece.

Once the cave is accessible, you can add boulders to the scene to hide any portion of the cave props that stick out of the ground. This will make the cave entrance look and feel more rugged.

To find all the boulder and rock types, click the Gallery folder in the Content Browser and type **rock mountain** in the search bar. All the rock types will populate in the Content Browser.

[![Add boulder props to make things look more natural around the cave entrance.](https://dev.epicgames.com/community/api/documentation/image/c471e825-4c65-4dca-9cb3-cd056832d04c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c471e825-4c65-4dca-9cb3-cd056832d04c?resizing_type=fit)

Once the cave and props are set up, [playtest](playtesting-your-island-unreal-editor-for-fortnite) to make sure that everything works as intended. After playtesting, type **rock** into the Content Browser and select rocks of different sizes to place around your mountain and riverbed to make the terrain look natural.

[![Adding boulders and rocks to the terrain to make it look natural.](https://dev.epicgames.com/community/api/documentation/image/d1e320c4-8533-4b5c-bf94-68e5d753df20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1e320c4-8533-4b5c-bf94-68e5d753df20?resizing_type=fit)

Use images of real mountain landscapes for inspiration.

Playtest by walking through your cave. Make sure players can traverse through the entire cave easily. Experiment with props from the Nature gallery to hide seams, create the walls of your cave, and add visual interest in the terrain around the mouth of the cave.

Once you’re happy with how the terrain looks, you’re ready to move on to creating roads and pathways.

## Next Section

- [![Creating Roads and Pathways](https://dev.epicgames.com/community/api/documentation/image/0b8ed9b1-3f4c-4722-9a1e-2da213a996f7?resizing_type=fit&width=640&height=640)

  Creating Roads and Pathways

  Learn how to create roads and pathways for your custom terrain.](https://dev.epicgames.com/documentation/fortnite/creating-roads-and-pathways-in-unreal-editor-for-fortnite)
