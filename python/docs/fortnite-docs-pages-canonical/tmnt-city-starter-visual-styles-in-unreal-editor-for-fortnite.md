## https://dev.epicgames.com/documentation/en-us/fortnite/tmnt-city-starter-visual-styles-in-unreal-editor-for-fortnite

# City Starter Visual Styles

Learn visual techniques to create a stylized island using the City Starter template.

![City Starter Visual Styles](https://dev.epicgames.com/community/api/documentation/image/c8d94dfb-494d-496a-b272-3043a4c8986d?resizing_type=fill&width=1920&height=335)

The **City Starter** template highlights the process and techniques you can use to design the look of a city within Unreal Editor for Fortnite (UEFN).

This island contains a little slice of New York City, lit and stylized to make the Teenage Mutant Ninja Turtles (TMNT) feel right at home! Play through the template to experience a low and high viewpoint of the city.

This guide reviews the steps the team took to conceptualize and build the look of the template. It covers the following areas:

- Designing visuals from concept
- Approaches to asset layout
- Post-processing techniques
- Additional style techniques: custom skybox, lighting, and windows
- Ideas to expand the experience

Check out the post-processing, skybox, and custom lighting, and to learn how to create awesome stylized visuals.

This is not a game play tutorial. The map does not include barriers in the level. You can add them as you build for your own experience with assets like the [Barrier device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-barrier-devices-in-fortnite-creative). To learn how to build an arcade game mode, including a side scroller camera and custom user interface (UI), see the [TMNT Arcade Template](tmnt-arcade-template-in-unreal-editor-for-fortnite).

To access the template, follow these steps:

[![Brand Templates Browser](https://dev.epicgames.com/community/api/documentation/image/8e702f27-29dc-402a-97a2-40b954973cd6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e702f27-29dc-402a-97a2-40b954973cd6?resizing_type=fit)

## Visual Styles

The City Starter template features two prominent aesthetic styles: **cartoon** and **comic**. These visual styles were designed to fit the TMNT gameplay and themes. The two styles are available in the UEFN template through the post-process volumes, and in Creative islands with the [Post-Processing device](https://dev.epicgames.com/documentation/fortnite/using-post-processing-devices-in-fortnite-creative). These styles are not exclusive to the TMNT developer tools. Use the techniques in the template to further customize your islands or to build on this template.

|  |  |
| --- | --- |
| [Cartoon Style Filter](https://dev.epicgames.com/community/api/documentation/image/01fcfcf6-c6fb-4a29-989b-2880772c98c9?resizing_type=fit) | [Comic Style Filter](https://dev.epicgames.com/community/api/documentation/image/5607195c-d515-4f14-ac1a-f4d8831f30ae?resizing_type=fit) |
| Cartoon Style Filter | Comic Style Filter |

These styles were curated by reviewing the TMNT experiences from cartoons to 3D-animated style. The team worked with Paramount to establish iconic elements that capture the TMNT world. From concept art and other reference pieces, the team noted elements like cel shading, rooftop scenes with the moon overlooking, and color schemes.

[![Concept References](https://dev.epicgames.com/community/api/documentation/image/94f8506e-35a4-431c-8af5-c8f92f8601e1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94f8506e-35a4-431c-8af5-c8f92f8601e1?resizing_type=fit)

*Concept References*

Aesthetics act as a game design element that fits with the mechanics and narrative of the experience. These aesthetics range from color, lightning, assets, and the layout of the scene. They help create the feel of the experience for players.

### Switch the Styles

From the editor, you can toggle between the styles using the **Outliner**. In the Outliner, search for "postproccess" to view both the **PostProcessVolume_Cartoon** and **PostProcessVolume_Comic** volumes.

[![Post-process Volume](https://dev.epicgames.com/community/api/documentation/image/3e5395b7-a6b3-4e05-aeb0-df5f56bb5379?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e5395b7-a6b3-4e05-aeb0-df5f56bb5379?resizing_type=fit)

*Style switcher in sewer lair.*

The cartoon style is active by default. To enable the comic style, follow these steps:

Before running the template, make sure you revert the changes above.

In the template game play, you can choose the visual mode in the sewer lair from the switch devices on the wall. Toggle the styles, then explore the street and roof level to view the TMNT assets that create the city. Use the template as a foundation to build your own TMNT experience or pull the visual techniques into another project.

[![Style Mode Switcher](https://dev.epicgames.com/community/api/documentation/image/b5de5d2c-1bac-4569-b147-2bf12d4c954b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b5de5d2c-1bac-4569-b147-2bf12d4c954b?resizing_type=fit)

To learn how to adjust these styles further, see the [Post-Process Techniques](https://dev.epicgames.com/documentation/fortnite/tmnt-city-starter-visual-styles-in-unreal-editor-for-fortnite) section on this page.

## Level Design

The Cartoon and Comic filters are both striking visual styles, but the city is what brings the template together. The artists laid out assets in a way that creates an authentic city for TMNT. The use of TMNT and Fortnite assets add layers to the city. The arrangement of assets to define a space and path for players to travel is called **level design**.

[![Level Design in City Starter Template](https://dev.epicgames.com/community/api/documentation/image/2ecb144b-c2a5-4e49-bfa8-622142e22143?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2ecb144b-c2a5-4e49-bfa8-622142e22143?resizing_type=fit)

*TMNT city, with a silhouette skyline in the background to add depth and encircle the player.*

### Center the City

The template was designed from choices that define the city. Although the template is not a full game example, to help design the layout, the template has a [platformer](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#platformer) theme. This game genre helps define the playable space. Within the playable space, artists placed unique, detailed assets, primarily TMNT assets. The idea is that players can enter and explore these assets.

These assets support the theme. When thinking of style, you have to keep assets in mind. They can aid or break the visual look of the experience. The arrangement of these assets in the level and how a player navigates the scene also plays an important role. The template uses additional assets like posters, neon signs, graffiti, and props to bring character to the world and further establish the theme. For the full list of assets, see [Working with TMNT Islands](https://dev.epicgames.com/documentation/fortnite/working-with-tmnt-islands-in-fortnite).

[![Channel 6 Assets in Comic Style](https://dev.epicgames.com/community/api/documentation/image/1ac379b9-30f9-428a-84a8-1c7aa75075e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ac379b9-30f9-428a-84a8-1c7aa75075e0?resizing_type=fit)

*Channel 6 assets in the comic style mode.*

With the playable space set, the team has an idea of how to build out the rest of the map to fill the space.

The map consists of a foreground, middle ground, and background. Buildings and windows simplify the further they are from the center. The skyline acts as the backdrop for the map, enclosing the player in the city. For the sewer lair, highly detailed assets are placed because the intention is for the player to explore every part of the area.

|  |  |
| --- | --- |
| [City Level Asset Layout](https://dev.epicgames.com/community/api/documentation/image/7694cab8-580d-4473-bd2f-8591a035db24?resizing_type=fit) | [Sewer Lair Asset Layout](https://dev.epicgames.com/community/api/documentation/image/e890e6a1-acb0-4978-8581-5087cf000268?resizing_type=fit) |
| City Level Asset Layout | Sewer Lair Asset Layout |

Finally, accent elements like the moon, windows, lighting, and a visual filter are used to capture the feel of the city nightlife.

## Post-Process Techniques

What emphasizes the city feel are the various techniques used to create the visual styles. Post-process volumes are the prominent feature used to create the styles.

Post-processing is a visual overlay that affects the aesthetics of your island as a whole or select parts. Each filter has standard post-process settings adjusted, along with custom materials that drive the look. To learn more about post-processing and its standard settings, see [Intro to Post-Processing](https://dev.epicgames.com/documentation/fortnite/intro-to-postprocessing-in-unreal-editor-for-fortnite).

### Cartoon Post-Process Filter

#### Depth Fog

The template uses a custom atmospheric-fog effect through materials. The fog adds color and helps establish depth to the city. You can use the material settings to artistically control the silhouettes of the buildings and the color of the scene.

To learn more about the controls to make adjustments, see the [Custom Fog Material](https://dev.epicgames.com/documentation/fortnite/tmnt-city-starter-visual-styles-in-unreal-editor-for-fortnite) section on the page.

|  |  |
| --- | --- |
| [City Skyline in Foreground](https://dev.epicgames.com/community/api/documentation/image/17329174-9add-4081-a955-3892323ac0c2?resizing_type=fit) | [City Skyline Pushed Back](https://dev.epicgames.com/community/api/documentation/image/6c3a0805-a697-4495-84e5-9a5a5250981a?resizing_type=fit) |
| City Skyline in Foreground | City Skyline Pushed Back |

#### Cel Shader

The cel shader material flattens the lighting and introduces some light posterization and thresholds. This helps the scene look more cartoony.

In the template, the effect is masked to the foreground to keep the distance from appearing jarring. Since reference cartoons and anime often have softer painted backgrounds, the masking keeps to the look.

|  |  |
| --- | --- |
| [No Cel Shader](https://dev.epicgames.com/community/api/documentation/image/e722b6da-561c-43f5-bb10-8606fb28d8a9?resizing_type=fit) | [With Cel Shader](https://dev.epicgames.com/community/api/documentation/image/dc8ef359-3d34-4fe5-9ab9-51f4b76a4147?resizing_type=fit) |
| Cel Shader Value 0 | Cel Shader Value 1 |

#### Outlines

The outlines help further stylize the scene to create the cartoon feel. The material includes options to control the thickness, color and opacity through depth. With these settings, artists strengthened the lines in the foreground and created complimentary outlines for the buildings as they recede into the distance.

![Outline Value 0](https://dev.epicgames.com/community/api/documentation/image/91e8af07-1446-46b2-bf42-40e214b0ce6c?resizing_type=fit&width=1920&height=1080)

![Outline Value 1](https://dev.epicgames.com/community/api/documentation/image/91c34d92-595c-419c-aa5f-d0c9fea6b55f?resizing_type=fit&width=1920&height=1080)

### Comic Post-Process Filter

The Comic (Noir) filter uses some standard post-process settings and similar cel shader and outline materials as the Cartoon filter. The outline material was adjusted to compliment the tonal grayscale range. The filter's unique custom materials include posterization, comic tone, and a frame. The outcome is a highly graphic style reminiscent of a comic or graphic novel.

#### Comic Tone and Frame

The comic tone material desaturates and applies luminance thresholds to give the scene a printed tonal range. The frame material is then applied to complete the look.

|  |  |
| --- | --- |
| [No Comic Tone and Frame](https://dev.epicgames.com/community/api/documentation/image/969eaa0f-43a3-4b5b-8ad6-39501c4f924c?resizing_type=fit) | [With Comic Tone and Frame](https://dev.epicgames.com/community/api/documentation/image/cb9bd1cf-5c69-4456-b4a4-8d69f71e97ac?resizing_type=fit) |
| Comic Tone and Frame Value 0 | Comic Tone and Frame Value 1 |

#### Posterization

To make the comic effect even more convincing, the image is posterized with solid bands of gray converted to various sizes of dots. The darker the tone, the larger the dot, until they merge to form pure black. The dots are then merged into the grayscale image to the desired amount. The material is used at 25% of its value to reduce eye strain during game play.

|  |  |
| --- | --- |
| [No Posterization](https://dev.epicgames.com/community/api/documentation/image/b92e7a48-d166-4436-8d1f-ce841acec24c?resizing_type=fit) | [With Comic Tone and Frame](https://dev.epicgames.com/community/api/documentation/image/3b5fc51d-4242-472d-9e4d-95d0a8260eb5?resizing_type=fit) |
| Posterization Value 0 | Posterization Value 1 |

### Editing the Post-Process Materials

Materials drive the post-process effect you see in both stylized modes. You can explore the build of each material and make adjustments to fit your project. You can also swap out materials in the post-process volumes to quickly alter the style.

To view the custom materials for each post-process volume:

|  |  |
| --- | --- |
| [Cartoon Post Process Materials](https://dev.epicgames.com/community/api/documentation/image/a87d1f3a-efc6-4990-b72f-f047727316f7?resizing_type=fit) | [Comic Post Process Materials](https://dev.epicgames.com/community/api/documentation/image/4dd6feac-6bd3-4bc0-9bac-2930685bef7e?resizing_type=fit) |
| Cartoon Post Process Materials | Comic Post Process Materials |

You can adjust each array value between 0 and 1 to examine the effect of each material. To open the location of each material, click the folder icon. Next, click the material you want to examine to open the Material Editor. The Material Editor has some artist settings in the Details panel, while others have parameters in the Material Graph. Artist-friendly settings are parameters from the Material Graph that are exposed as public variables. To learn more about materials, including the editor, functions, and expressions, see [Material Nodes and Settings](https://dev.epicgames.com/documentation/fortnite/material-nodes-and-settings-in-unreal-editor-for-fortnite).

#### Custom Fog Material

An example of artist settings in a material are the parameters set up for the depth fog material. The fog's color values are set by curve ramps, which provide a flexible way to adjust fog values precisely across the scene depth. This method gives more control to create a stylized look over the editor's built-in atmospheric fog system.

*Controls for the depth fog material.*

The material consists of the following core parameters, designed for artists to quickly make adjustments. You can access these values in the Details panel of the material, or go into the Material Graph and adjust the default values.

| Fog Parameter | Description |
| --- | --- |
| Curve Far and Near Point | Sets the Near and Far distance that the curve asset ramp is mapped to. The ramp colors on the left correspond to the Near Point and the right side of the ramp correspond to the Far point. |
| Curve Input | Provides a color curve to adjust the gradient colors of the fog. To open the curve, double-click the icon. To learn more, see the Unreal Engine documentation [Curve Atlases in Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/curve-atlases-in-unreal-engine-materials). |
| Global Amount | Sets the percentage of visibility for the fog ramp. |
| Range Cutoff | Sets the threshold of the scene depth. You can use the range values to control whether fog is applied to the skybox. |

The fog material is an example of how you can open each material to make adjustments. The remaining materials have the same principles. To practice creating a new post-processing material and learn about the Material Graph, see [Using a Post Process Material](https://dev.epicgames.com/documentation/fortnite/intro-to-postprocessing-in-unreal-editor-for-fortnite).

## Additional Visual Techniques

This section covers some techniques used with lighting and windows to further push the mood and stylization.

### Adjusting the Procedural Skybox

Another material-based technique is the skybox, which is separate from the post-process volume. Both filters use the custom procedural skybox to create a stylized atmosphere. The material is attached to a static mesh sphere that encompasses the map. Artist-friendly parameters are exposed in the Details panel of the material for quick adjustments.

You can access the Skybox tool from one of the following:

- **Outliner > SkySphere > MI_ProceduralSkybox**
- **Content Drawer > Project Name > Materials > MI_ProceduralSkybox**

Double-click the material to open the Material Editor. The **Parameter Groups** category houses the settings for adjusting the stylization of the sky, described in the table below. The category includes a **Global Static Switch Parameter Values** to toggle the sharpness of the horizon and moon.

*Controls for the skybox material.*

| Skybox Parameter | Description | Example |
| --- | --- | --- |
| Global Scalar Parameter Values | Adjusts the moon and atmosphere attributes.  The controls provide artists the means to stylize the moon as a centerpiece. The technique fulfills the concept of the TMNT turtles running across the building tops in silhouette against the moon. | [Skybox Moon Value](https://dev.epicgames.com/community/api/documentation/image/5a62a439-ecfb-4506-899a-a2d30de4706f?resizing_type=fit) |
| Global Vector Parameter Values | Adjusts the color of the sky attributes. The custom skybox provides more control over sky gradient colors and blending biases.  This color control is essential to improving the skyline values against the skyscrapers. The extra color controls are designed to tweak the sky carefully beyond realistic values to fit more in line with the stylized color palette. | [Skybox Sky Value](https://dev.epicgames.com/community/api/documentation/image/d1f22082-b2f4-44db-b680-251d7b210d73?resizing_type=fit) |
| Stars | Adjusts the transform, color, tiling, and brightness of the stars. | [Skybox Stars Value](https://dev.epicgames.com/community/api/documentation/image/6b06a2dc-16f8-4f17-9f6d-8fb76730aab3?resizing_type=fit) |
| Clouds | Adjusts the cloud texture map, cloud coverage, edge softness, light and dark colors, rim light, opacity, and cloud motion direction. This provides a way for the artist to dial in a more dynamic sky with more visual interest. |  |

With the custom sky and lighting setup, the **World Time of Day Manager** is toggled off in **World Settings**.

You can further examine the material from the Material Graph. To open the Material Graph, in the Material Editor toolbar, click **Hierarchy > M_ProceduralSkybox**. The graph opens with groups of nodes categorized into comment boxes to show which parameters they affect. You can adjust the nodes to redefine parameters.

[![Procedural Skybox Material Graph](https://dev.epicgames.com/community/api/documentation/image/21ce11db-46b3-4912-89ce-5ae03ce669c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21ce11db-46b3-4912-89ce-5ae03ce669c5?resizing_type=fit)

*Material Graph for the Procedural Skybox.*

### Custom Lighting

The lighting for the template is integrated with the post-processing volumes to ensure proper aesthetics. Lighting helps set the mood and provide direction to players. It also helps define attributes of the post-process filters. General lights were placed to illuminate the city, then specific lights were added to highlight buildings and props.

[![Mood Lighting Compostion](https://dev.epicgames.com/community/api/documentation/image/7ce7dd59-e8b1-466f-a7d5-4c2a4b2f7083?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ce7dd59-e8b1-466f-a7d5-4c2a4b2f7083?resizing_type=fit)

#### Mood Lighting

Mood lighting is the process of precisely placing lights that are intended to set a particular feeling for the experience.

During the conceptualization phase, artists review the reference material (often called mood boards) to establish the emotion and lighting direction. This process is used in other story forms like live action films, animations, and live theater.

Most of the mood lighting in the scene is set up by one of the following:

- **Skylight:** Drives the scene ambient color and controls the darkest illumination in the shadows.
- **Directional light:** Controls the moon position and illumination from the moon.
- **Point lights:** Placed to add pops of cartoon color in areas that might otherwise be less interesting. (Specular is disabled to remove bright spots created by these lights.)
- Light components attached to an actor.
- Emissive materials.

The mood lights also help keep the visual quality when you optimize your project. The stylization of the lights and assets maintains the visual interest on lower-end devices.

|  |  |  |
| --- | --- | --- |
| [Classic Fornite BR Style](https://dev.epicgames.com/community/api/documentation/image/53a6e1dc-424e-40fa-8ac9-1dc0670f3d49?resizing_type=fit) | [Cartoon Style](https://dev.epicgames.com/community/api/documentation/image/5d3f77e3-6b66-4140-9ef1-744a6e8df1f7?resizing_type=fit) | [Comic Style](https://dev.epicgames.com/community/api/documentation/image/cfcee3d6-7a23-4359-bb9c-9dfc5e35047f?resizing_type=fit) |
| Classic Fornite BR Style | Cartoon Style | Comic Style |

To learn more about artistic light practices, see [Lighting and Color](https://dev.epicgames.com/documentation/fortnite/making-cinematics-2-lighting-and-color-in-unreal-editor-for-fortnite).

### Windows

The further you get from the center of the city, the more the windows in the scene simplify. As noted in level design, simplification adds depth and helps optimize the scene. The windows also make use of materials to emit light and further support the stylized look. The table below describes the various techniques used for the windows.

A [Day Sequence device](https://dev.epicgames.com/documentation/fortnite/using-day-sequence-devices-in-unreal-editor-for-fortnite) is used to control the background building material-based lights to be off.

In this example, the color and style of these material lights did not fit the city aesthetic, so a decision was made to turn them off and create custom window lights.

| Technique | Description | Example |
| --- | --- | --- |
| Interior Cubemap | A material method to give the appearance of a 3D space. The method is used to fill buildings that players aren't expected to enter but can see in passing.  You can access the material from **Content Drawer > Project Name > Materials > M_Windows_Interior**. | [Cartoon Sheen Material](https://dev.epicgames.com/community/api/documentation/image/e75c8b1c-8f87-4d17-bb49-643cb1305595?resizing_type=fit) |
| Window Mask | Material that randomizes the positions of windows to give the background buildings variety.  You can access the material from **Content Drawer > Project Name > Materials > M_WindowMask**. | [Window Mask](https://dev.epicgames.com/community/api/documentation/image/a38cb03d-84e5-48c3-8d6d-c10d0ec4ca79?resizing_type=fit) |
| Random Value from World Position | The look of a room, lit or unlit, is determined by the position of the window in the world. Each window material has a world position offset applied to the color of the material. The offset creates a random brightness factor to add life to the city. This method reduces the use of unique materials and memory. |  |
| Cartoon Sheen Material | Diagonal lines applied to windows to mimic a stylized sheen effect.  **Content Drawer > Project Name > Materials > M_Windows_Channel6**. | [Cartoon Sheen Material](https://dev.epicgames.com/community/api/documentation/image/4d841253-bfde-4f94-a43e-eba38ace0139?resizing_type=fit) |

## Expanding the Experience

After learning the approaches and techniques used to create the key aesthetics of the template, you can begin to elevate the map into your own TMNT experience!

Run through the template and switch between the styles to imagine what gameplay elements and narratives fit with the filter and city.

Here are some ideas to get you started:

- Build on the platformer base and add enemy encounters throughout. To learn how to add encounters, see [TMNT Enemy Encounters and Obstacles](tmnt-arcade-template-in-unreal-editor-for-fortnite#tmntenemyencountersandobstacles).
- Use the newsroom assets as narrative cut scenes with the comic style. To learn more, see [Making Cinematics and Cutscenes](https://dev.epicgames.com/documentation/fortnite/making-cinematics-and-cutscenes-in-unreal-editor-for-fortnite).
- Enhance the effect with comic starburst materials as dialog boxes that appear using Sequencer. To learn more, see [Gameplay Events in Sequencer](https://dev.epicgames.com/documentation/fortnite/gameplay-events-in-sequencer-in-unreal-editor-for-fortnite).

### Create a Sunny Style

As you build on the template or pull assets into other projects, start from a conceptual base of what narrative and gameplay fits the city scene and TMNT assets. Think of the mood you want to set and how the lighting would look. Consider the parts of the map you intend the player to explore.

[![Sunny Style Concept](https://dev.epicgames.com/community/api/documentation/image/ec8c551e-71b6-4610-9a52-7f9cbe1c53cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec8c551e-71b6-4610-9a52-7f9cbe1c53cf?resizing_type=fit)

*Concept reference for a sunny style map with NPC encounter on the roof.*

With the post-process volumes and additional visual techniques you can take this concept of a sunny style city and bring it to life.

#### Skybox Adjustments

First, brighten the atmosphere with the procedural skybox. To create blue skies, follow these steps:

1. In the **Content Drawer**, search **MI_ProceduralSkybox** and double-click to open the Material Editor.
2. In the Details panel, adjust the following values:

Alternatively, instead of the moon brightness adjustment, you can swap the moon texture in the Material Graph with your own image of the sun.

[![Moon Texture in Material Graph](https://dev.epicgames.com/community/api/documentation/image/bc1940c1-3f9d-4538-accb-5bcf74f5de6d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc1940c1-3f9d-4538-accb-5bcf74f5de6d?resizing_type=fit)

#### Light Adjustments

With the blue skies, the sun and its light direction must match better. To adjust the position of the sun and light direction, follow these steps:

Next, to turn off the midground and foreground window lights, follow these steps:

Removing the windows when they are not needed helps optimize the scene.

#### Fog Adjustments

For the sunny mode, use **PostProcessVolume_Cartoon** as the base. To adjust the fog depth and color, follow these steps:

[![Color Ramp Adjustments](https://dev.epicgames.com/community/api/documentation/image/af64186b-f9f5-4739-9170-7f3bb5504941?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af64186b-f9f5-4739-9170-7f3bb5504941?resizing_type=fit)

In the **Details** panel of **PP_DepthFog_Inst**, adjust the depth of the color ramp with the following values:

- **Curve Far Point:** 93511
- **Curve Near Point:** 14887

#### Posterization Adjustments

Finally, add the posterization to create a similar dotted effect as the Comic-Noir mode.

[![Posterize Adjustment](https://dev.epicgames.com/community/api/documentation/image/07d83040-c79d-45b9-8e20-80ceb75abfe9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07d83040-c79d-45b9-8e20-80ceb75abfe9?resizing_type=fit)

With some adjustments to materials and lights you woke up the city to blue skies! Now get those turtles to their lair quickly.

[![Sunny Style Mode](https://dev.epicgames.com/community/api/documentation/image/21729529-405f-4928-8e8c-04d6214ad2d1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21729529-405f-4928-8e8c-04d6214ad2d1?resizing_type=fit)
