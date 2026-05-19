## https://dev.epicgames.com/documentation/en-us/fortnite/sports-galleries-in-fortnite-creative

# City Starter Visual Styles
Learn visual techniques to create a stylized island using the City Starter template.
![City Starter Visual Styles](https://dev.epicgames.com/community/api/documentation/image/c8d94dfb-494d-496a-b272-3043a4c8986d?resizing_type=fill&width=1920&height=335)
The **City Starter** template highlights the process and techniques you can use to design the look of a city within Unreal Editor for Fortnite (UEFN).
This island contains a little slice of New York City, lit and stylized to make the Teenage Mutant Ninja Turtles (TMNT) feel right at home! Play through the template to experience a low and high viewpoint of the city.
This guide reviews the steps the team took to conceptualize and build the look of the template. It covers the following areas:
  * Designing visuals from concept
  * Approaches to asset layout
  * Post-processing techniques
  * Additional style techniques: custom skybox, lighting, and windows
  * Ideas to expand the experience

Check out the post-processing, skybox, and custom lighting, and to learn how to create awesome stylized visuals.
This is not a game play tutorial. The map does not include barriers in the level. You can add them as you build for your own experience with assets like the [Barrier device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-barrier-devices-in-fortnite-creative). To learn how to build an arcade game mode, including a side scroller camera and custom user interface (UI), see the [TMNT Arcade Template](https://dev.epicgames.com/documentation/fortnite/tmnt-arcade-template-in-unreal-editor-for-fortnite).
To access the template, follow these steps:
  1. Open UEFN.
  2. Go to **Brand Templates > City Starter**.
  3. Create a new project.

[![Brand Templates Browser](https://dev.epicgames.com/community/api/documentation/image/4def7566-65aa-41d5-8047-63117a06edd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4def7566-65aa-41d5-8047-63117a06edd3?resizing_type=fit)
If you don't see the project in Brand Templates, ensure you have properly signed up. For more information, see [TMNT Brand Rules](https://dev.epicgames.com/documentation/fortnite/tmnt-brand-and-creator-rules-in-unreal-editor-for-fortnite).
##  Visual Styles
The City Starter template features two prominent aesthetic styles: **cartoon** and **comic**. These visual styles were designed to fit the TMNT gameplay and themes. The two styles are available in the UEFN template through the post-process volumes, and in Creative islands with the [Post-Processing device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-post-process-devices-in-fortnite-creative). These styles are not exclusive to the TMNT developer tools. Use the techniques in the template to further customize your islands or to build on this template.
|
---|---
[![Cartoon Style Filter](https://dev.epicgames.com/community/api/documentation/image/f8a75781-85fd-4c46-bc3e-6e6894a34449?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f8a75781-85fd-4c46-bc3e-6e6894a34449?resizing_type=fit) |  [![Comic Style Filter](https://dev.epicgames.com/community/api/documentation/image/0ed51ad5-111b-42c4-9fe4-3101c250e02e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ed51ad5-111b-42c4-9fe4-3101c250e02e?resizing_type=fit)
Cartoon Style Filter |  Comic Style Filter
These styles were curated by reviewing the TMNT experiences from cartoons to 3D-animated style. The team worked with Paramount to establish iconic elements that capture the TMNT world. From concept art and other reference pieces, the team noted elements like cel shading, rooftop scenes with the moon overlooking, and color schemes.
[![Concept References](https://dev.epicgames.com/community/api/documentation/image/87ab5b4a-4486-4606-8858-e30416afcce4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87ab5b4a-4486-4606-8858-e30416afcce4?resizing_type=fit)
_Concept References_
Aesthetics act as a game design element that fits with the mechanics and narrative of the experience. These aesthetics range from color, lightning, assets, and the layout of the scene. They help create the feel of the experience for players.
###  Switch the Styles
From the editor, you can toggle between the styles using the **Outliner**. In the Outliner, search for "postproccess" to view both the **PostProcessVolume_Cartoon** and **PostProcessVolume_Comic** volumes.
[![Post-process Volume](https://dev.epicgames.com/community/api/documentation/image/c51b2cbf-7682-4e8c-b522-e269e0a18fb9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c51b2cbf-7682-4e8c-b522-e269e0a18fb9?resizing_type=fit)
_Style switcher in sewer lair._
The cartoon style is active by default. To enable the comic style, follow these steps:
  1. In the Outliner, toggle the eyeball icon for **PostProcessVolume_Cartoon** to off.
  2. Select **PostProcessVolume_Comic** and in the Details panel, search "blendweight".
  3. Set the **Blend Weight** value to 1.

Before running the template, make sure you revert the changes above.
In the template game play, you can choose the visual mode in the sewer lair from the switch devices on the wall. Toggle the styles, then explore the street and roof level to view the TMNT assets that create the city. Use the template as a foundation to build your own TMNT experience or pull the visual techniques into another project.
[![Style Mode Switcher](https://dev.epicgames.com/community/api/documentation/image/5d8ee1f8-241b-4c52-a912-f79f03554d98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d8ee1f8-241b-4c52-a912-f79f03554d98?resizing_type=fit)
To learn how to adjust these styles further, see the [Post-Process Techniques](https://dev.epicgames.com/documentation/fortnite/tmnt-city-starter-visual-styles-in-unreal-editor-for-fortnite) section on this page.
##  Level Design
The Cartoon and Comic filters are both striking visual styles, but the city is what brings the template together. The artists laid out assets in a way that creates an authentic city for TMNT. The use of TMNT and Fortnite assets add layers to the city. The arrangement of assets to define a space and path for players to travel is called **level design**.
[![Level Design in City Starter Template](https://dev.epicgames.com/community/api/documentation/image/422eb94a-0a2a-494c-9886-e219711f843e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/422eb94a-0a2a-494c-9886-e219711f843e?resizing_type=fit)
_TMNT city, with a silhouette skyline in the background to add depth and encircle the player._
###  Center the City
The template was designed from choices that define the city. Although the template is not a full game example, to help design the layout, the template has a [platformer](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#platformer) theme. This game genre helps define the playable space. Within the playable space, artists placed unique, detailed assets, primarily TMNT assets. The idea is that players can enter and explore these assets.
These assets support the theme. When thinking of style, you have to keep assets in mind. They can aid or break the visual look of the experience. The arrangement of these assets in the level and how a player navigates the scene also plays an important role. The template uses additional assets like posters, neon signs, graffiti, and props to bring character to the world and further establish the theme. For the full list of assets, see [Working with TMNT Islands](https://dev.epicgames.com/documentation/fortnite/working-with-tmnt-islands-in-fortnite).
[![Channel 6 Assets in Comic Style](https://dev.epicgames.com/community/api/documentation/image/568892c9-8ec9-4c6e-8fc4-a40423c47bb7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/568892c9-8ec9-4c6e-8fc4-a40423c47bb7?resizing_type=fit)
_Channel 6 assets in the comic style mode._
With the playable space set, the team has an idea of how to build out the rest of the map to fill the space.
The map consists of a foreground, middle ground, and background. Buildings and windows simplify the further they are from the center. The skyline acts as the backdrop for the map, enclosing the player in the city. For the sewer lair, highly detailed assets are placed because the intention is for the player to explore every part of the area.
|
---|---
[![City Level Asset Layout](https://dev.epicgames.com/community/api/documentation/image/c6dde424-40b4-4c70-881a-ff64a24cf53e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c6dde424-40b4-4c70-881a-ff64a24cf53e?resizing_type=fit) |  [![Sewer Lair Asset Layout](https://dev.epicgames.com/community/api/documentation/image/6f34f7a5-5e5e-4d9f-a6ae-5e41fc36beda?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6f34f7a5-5e5e-4d9f-a6ae-5e41fc36beda?resizing_type=fit)
City Level Asset Layout |  Sewer Lair Asset Layout
Finally, accent elements like the moon, windows, lighting, and a visual filter are used to capture the feel of the city nightlife.
##  Post-Process Techniques
What emphasizes the city feel are the various techniques used to create the visual styles. Post-process volumes are the prominent feature used to create the styles.
Post-processing is a visual overlay that affects the aesthetics of your island as a whole or select parts. Each filter has standard post-process settings adjusted, along with custom materials that drive the look. To learn more about post-processing and its standard settings, see [Intro to Post-Processing](https://dev.epicgames.com/documentation/fortnite/intro-to-postprocessing-in-unreal-editor-for-fortnite).
###  Cartoon Post-Process Filter
####  Depth Fog
The template uses a custom atmospheric-fog effect through materials. The fog adds color and helps establish depth to the city. You can use the material settings to artistically control the silhouettes of the buildings and the color of the scene.
To learn more about the controls to make adjustments, see the [Custom Fog Material](https://dev.epicgames.com/documentation/fortnite/tmnt-city-starter-visual-styles-in-unreal-editor-for-fortnite) section on the page.
|
---|---
[![City Skyline in Foreground](https://dev.epicgames.com/community/api/documentation/image/37ba351b-729a-4aca-b6cd-1cea8a8a97ed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/37ba351b-729a-4aca-b6cd-1cea8a8a97ed?resizing_type=fit) |  [![City Skyline Pushed Back](https://dev.epicgames.com/community/api/documentation/image/e3fde803-9871-423b-9699-4897f4a2c0b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e3fde803-9871-423b-9699-4897f4a2c0b5?resizing_type=fit)
City Skyline in Foreground |  City Skyline Pushed Back
####  Cel Shader
The cel shader material flattens the lighting and introduces some light posterization and thresholds. This helps the scene look more cartoony.
In the template, the effect is masked to the foreground to keep the distance from appearing jarring. Since reference cartoons and anime often have softer painted backgrounds, the masking keeps to the look.
|
---|---
[![No Cel Shader](https://dev.epicgames.com/community/api/documentation/image/e3354372-6c78-4df8-9f2f-b90b5db346b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e3354372-6c78-4df8-9f2f-b90b5db346b4?resizing_type=fit) |  [![With Cel Shader](https://dev.epicgames.com/community/api/documentation/image/46eea855-0e6b-4bcf-97c7-e59612196e9b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46eea855-0e6b-4bcf-97c7-e59612196e9b?resizing_type=fit)
Cel Shader Value 0 |  Cel Shader Value 1
####  Outlines
The outlines help further stylize the scene to create the cartoon feel. The material includes options to control the thickness, color and opacity through depth. With these settings, artists strengthened the lines in the foreground and created complimentary outlines for the buildings as they recede into the distance.
![Outline Value 0](https://dev.epicgames.com/community/api/documentation/image/f7bbfa2a-51a1-444f-b22f-567e58467b50?resizing_type=fit&width=1920&height=1080)
![Outline Value 1](https://dev.epicgames.com/community/api/documentation/image/f4b55783-0f3c-454b-b248-721fd701a2b2?resizing_type=fit&width=1920&height=1080)
Outline Value 0
Outline Value 1
###  Comic Post-Process Filter
The Comic (Noir) filter uses some standard post-process settings and similar cel shader and outline materials as the Cartoon filter. The outline material was adjusted to compliment the tonal grayscale range. The filter's unique custom materials include posterization, comic tone, and a frame. The outcome is a highly graphic style reminiscent of a comic or graphic novel.
####  Comic Tone and Frame
The comic tone material desaturates and applies luminance thresholds to give the scene a printed tonal range. The frame material is then applied to complete the look.
|
---|---
[![No Comic Tone and Frame](https://dev.epicgames.com/community/api/documentation/image/75cbbd39-9faa-4082-9225-e38688bc81f6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75cbbd39-9faa-4082-9225-e38688bc81f6?resizing_type=fit) |  [![With Comic Tone and Frame](https://dev.epicgames.com/community/api/documentation/image/2527445b-813c-4a23-9176-5ee873f71987?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2527445b-813c-4a23-9176-5ee873f71987?resizing_type=fit)
Comic Tone and Frame Value 0 |  Comic Tone and Frame Value 1
####  Posterization
To make the comic effect even more convincing, the image is posterized with solid bands of gray converted to various sizes of dots. The darker the tone, the larger the dot, until they merge to form pure black. The dots are then merged into the grayscale image to the desired amount. The material is used at 25% of its value to reduce eye strain during game play.
|
---|---
[![No Posterization](https://dev.epicgames.com/community/api/documentation/image/3ba3c623-e7c2-4e9c-bf29-04203dfb7b57?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ba3c623-e7c2-4e9c-bf29-04203dfb7b57?resizing_type=fit) |  [![With Comic Tone and Frame](https://dev.epicgames.com/community/api/documentation/image/841e78db-6395-4bee-b344-b4f895526277?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/841e78db-6395-4bee-b344-b4f895526277?resizing_type=fit)
Posterization Value 0 |  Posterization Value 1
###  Editing the Post-Process Materials
Materials drive the post-process effect you see in both stylized modes. You can explore the build of each material and make adjustments to fit your project. You can also swap out materials in the post-process volumes to quickly alter the style.
To view the custom materials for each post-process volume:
  1. In the **Outliner** , click the post-process volume.
  2. Go to the **Details panel > Rendering Features > Post Process Materials > Array**.

|
---|---
[![Cartoon Post Process Materials](https://dev.epicgames.com/community/api/documentation/image/0f1fa2dc-cc8a-409a-bf2e-db57a1a22bda?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f1fa2dc-cc8a-409a-bf2e-db57a1a22bda?resizing_type=fit) |  [![Comic Post Process Materials](https://dev.epicgames.com/community/api/documentation/image/c928b0ba-cbfd-44a6-be0c-4498f24915c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c928b0ba-cbfd-44a6-be0c-4498f24915c0?resizing_type=fit)
Cartoon Post Process Materials |  Comic Post Process Materials
You can adjust each array value between 0 and 1 to examine the effect of each material. To open the location of each material, click the folder icon. Next, click the material you want to examine to open the Material Editor. The Material Editor has some artist settings in the Details panel, while others have parameters in the Material Graph. Artist-friendly settings are parameters from the Material Graph that are exposed as public variables. To learn more about materials, including the editor, functions, and expressions, see [Material Nodes and Settings](https://dev.epicgames.com/documentation/fortnite/material-nodes-and-settings-in-unreal-editor-for-fortnite).
####  Custom Fog Material
An example of artist settings in a material are the parameters set up for the depth fog material. The fog's color values are set by curve ramps, which provide a flexible way to adjust fog values precisely across the scene depth. This method gives more control to create a stylized look over the editor's built-in atmospheric fog system.
_Controls for the depth fog material._
The material consists of the following core parameters, designed for artists to quickly make adjustments. You can access these values in the Details panel of the material, or go into the Material Graph and adjust the default values.
Fog Parameter  |  Description
---|---
Curve Far and Near Point |  Sets the Near and Far distance that the curve asset ramp is mapped to. The ramp colors on the left correspond to the Near Point and the right side of the ramp correspond to the Far point.
Curve Input |  Provides a color curve to adjust the gradient colors of the fog. To open the curve, double-click the icon. To learn more, see the Unreal Engine documentation [Curve Atlases in Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/curve-atlases-in-unreal-engine-materials).
Global Amount |  Sets the percentage of visibility for the fog ramp.
Range Cutoff |  Sets the threshold of the scene depth. You can use the range values to control whether fog is applied to the skybox.
The fog material is an example of how you can open each material to make adjustments. The remaining materials have the same principles. To practice creating a new post-processing material and learn about the Material Graph, see [Using a Post Process Material](https://dev.epicgames.com/documentation/fortnite/intro-to-postprocessing-in-unreal-editor-for-fortnite).
##  Additional Visual Techniques
This section covers some techniques used with lighting and windows to further push the mood and stylization.
###  Adjusting the Procedural Skybox
Another material-based technique is the skybox, which is separate from the post-process volume. Both filters use the custom procedural skybox to create a stylized atmosphere. The material is attached to a static mesh sphere that encompasses the map. Artist-friendly parameters are exposed in the Details panel of the material for quick adjustments.
You can access the Skybox tool from one of the following:
  * **Outliner > SkySphere > MI_ProceduralSkybox**
  * **Content Drawer > Project Name > Materials > MI_ProceduralSkybox**

Double-click the material to open the Material Editor. The **Parameter Groups** category houses the settings for adjusting the stylization of the sky, described in the table below. The category includes a **Global Static Switch Parameter Values** to toggle the sharpness of the horizon and moon.
_Controls for the skybox material._
Skybox Parameter  |  Description  |  Example
---|---|---
Global Scalar Parameter Values |  Adjusts the moon and atmosphere attributes. The controls provide artists the means to stylize the moon as a centerpiece. The technique fulfills the concept of the TMNT turtles running across the building tops in silhouette against the moon. |  [![Skybox Moon Value](https://dev.epicgames.com/community/api/documentation/image/ece7f339-5292-4a8c-82a6-53fb862cf64f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ece7f339-5292-4a8c-82a6-53fb862cf64f?resizing_type=fit)
Global Vector Parameter Values |  Adjusts the color of the sky attributes. The custom skybox provides more control over sky gradient colors and blending biases. This color control is essential to improving the skyline values against the skyscrapers. The extra color controls are designed to tweak the sky carefully beyond realistic values to fit more in line with the stylized color palette. |  [![Skybox Sky Value](https://dev.epicgames.com/community/api/documentation/image/f1d93d51-8dfc-4fda-b26f-d9c9e0266c3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1d93d51-8dfc-4fda-b26f-d9c9e0266c3d?resizing_type=fit)
Stars |  Adjusts the transform, color, tiling, and brightness of the stars. |  [![Skybox Stars Value](https://dev.epicgames.com/community/api/documentation/image/0f47c1d9-bf8b-4b88-8823-fff9c77e9924?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f47c1d9-bf8b-4b88-8823-fff9c77e9924?resizing_type=fit)
Clouds |  Adjusts the cloud texture map, cloud coverage, edge softness, light and dark colors, rim light, opacity, and cloud motion direction. This provides a way for the artist to dial in a more dynamic sky with more visual interest. |
With the custom sky and lighting setup, the **World Time of Day Manager** is toggled off in **World Settings**.
You can further examine the material from the Material Graph. To open the Material Graph, in the Material Editor toolbar, click **Hierarchy > M_ProceduralSkybox**. The graph opens with groups of nodes categorized into comment boxes to show which parameters they affect. You can adjust the nodes to redefine parameters.
[![Procedural Skybox Material Graph](https://dev.epicgames.com/community/api/documentation/image/50f1e523-5323-4cc2-923d-f0a8ea8f7b96?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50f1e523-5323-4cc2-923d-f0a8ea8f7b96?resizing_type=fit)
_Material Graph for the Procedural Skybox._
###  Custom Lighting
The lighting for the template is integrated with the post-processing volumes to ensure proper aesthetics. Lighting helps set the mood and provide direction to players. It also helps define attributes of the post-process filters. General lights were placed to illuminate the city, then specific lights were added to highlight buildings and props.
[![Mood Lighting Compostion](https://dev.epicgames.com/community/api/documentation/image/fa7a1f54-46eb-48e6-b730-b3fc47d04ab0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa7a1f54-46eb-48e6-b730-b3fc47d04ab0?resizing_type=fit)
####  Mood Lighting
Mood lighting is the process of precisely placing lights that are intended to set a particular feeling for the experience.
During the conceptualization phase, artists review the reference material (often called mood boards) to establish the emotion and lighting direction. This process is used in other story forms like live action films, animations, and live theater.
Most of the mood lighting in the scene is set up by one of the following:
  * **Skylight:** Drives the scene ambient color and controls the darkest illumination in the shadows.
  * **Directional light:** Controls the moon position and illumination from the moon.
  * **Point lights:** Placed to add pops of cartoon color in areas that might otherwise be less interesting. (Specular is disabled to remove bright spots created by these lights.)
  * Light components attached to an actor.
  * Emissive materials.

The mood lights also help keep the visual quality when you optimize your project. The stylization of the lights and assets maintains the visual interest on lower-end devices.
|  |
---|---|---
[![Classic Fornite BR Style](https://dev.epicgames.com/community/api/documentation/image/8fceb109-8c22-455b-86c9-86abfe225a9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8fceb109-8c22-455b-86c9-86abfe225a9a?resizing_type=fit) |  [![Cartoon Style](https://dev.epicgames.com/community/api/documentation/image/bcdd8e50-6eed-45a2-84dd-18a5713b935f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bcdd8e50-6eed-45a2-84dd-18a5713b935f?resizing_type=fit) |  [![Comic Style](https://dev.epicgames.com/community/api/documentation/image/b2aad751-1d8c-4c43-9cca-21ed13df1c01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2aad751-1d8c-4c43-9cca-21ed13df1c01?resizing_type=fit)
Classic Fornite BR Style |  Cartoon Style |  Comic Style
To learn more about artistic light practices, see [Lighting and Color](https://dev.epicgames.com/documentation/fortnite/making-cinematics-2-lighting-and-color-in-unreal-editor-for-fortnite).
###  Windows
The further you get from the center of the city, the more the windows in the scene simplify. As noted in level design, simplification adds depth and helps optimize the scene. The windows also make use of materials to emit light and further support the stylized look. The table below describes the various techniques used for the windows.
A [Day Sequence device](https://dev.epicgames.com/documentation/fortnite/using-day-sequence-devices-in-unreal-editor-for-fortnite) is used to control the background building material-based lights to be off.
In this example, the color and style of these material lights did not fit the city aesthetic, so a decision was made to turn them off and create custom window lights.
Technique  |  Description  |  Example
---|---|---
Interior Cubemap |  A material method to give the appearance of a 3D space. The method is used to fill buildings that players aren't expected to enter but can see in passing. You can access the material from **Content Drawer > Project Name > Materials > M_Windows_Interior**. |  [![Cartoon Sheen Material](https://dev.epicgames.com/community/api/documentation/image/5d57007a-64dd-4501-a53a-5b53c657ce1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d57007a-64dd-4501-a53a-5b53c657ce1a?resizing_type=fit)
Window Mask |  Material that randomizes the positions of windows to give the background buildings variety. You can access the material from **Content Drawer > Project Name > Materials > M_WindowMask**. |  [![Window Mask](https://dev.epicgames.com/community/api/documentation/image/4cc67987-ad64-4b8b-9997-cbdd5ecbc2cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4cc67987-ad64-4b8b-9997-cbdd5ecbc2cf?resizing_type=fit)
Random Value from World Position |  The look of a room, lit or unlit, is determined by the position of the window in the world. Each window material has a world position offset applied to the color of the material. The offset creates a random brightness factor to add life to the city. This method reduces the use of unique materials and memory. |
Cartoon Sheen Material |  Diagonal lines applied to windows to mimic a stylized sheen effect. **Content Drawer > Project Name > Materials > M_Windows_Channel6**. |  [![Cartoon Sheen Material](https://dev.epicgames.com/community/api/documentation/image/627139e5-a5ed-4acb-b64c-c23a3fb4a359?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/627139e5-a5ed-4acb-b64c-c23a3fb4a359?resizing_type=fit)
##  Expanding the Experience
After learning the approaches and techniques used to create the key aesthetics of the template, you can begin to elevate the map into your own TMNT experience!
Run through the template and switch between the styles to imagine what gameplay elements and narratives fit with the filter and city.
Here are some ideas to get you started:
  * Build on the platformer base and add enemy encounters throughout. To learn how to add encounters, see [TMNT Enemy Encounters and Obstacles](https://dev.epicgames.com/documentation/fortnite/tmnt-arcade-template-in-unreal-editor-for-fortnite#tmntenemyencountersandobstacles).
  * Use the newsroom assets as narrative cut scenes with the comic style. To learn more, see [Making Cinematics and Cutscenes](https://dev.epicgames.com/documentation/fortnite/making-cinematics-and-cutscenes-in-unreal-editor-for-fortnite).
  * Enhance the effect with comic starburst materials as dialog boxes that appear using Sequencer. To learn more, see [Gameplay Events in Sequencer](https://dev.epicgames.com/documentation/fortnite/gameplay-events-in-sequencer-in-unreal-editor-for-fortnite).

###  Create a Sunny Style
As you build on the template or pull assets into other projects, start from a conceptual base of what narrative and gameplay fits the city scene and TMNT assets. Think of the mood you want to set and how the lighting would look. Consider the parts of the map you intend the player to explore.
[![Sunny Style Concept](https://dev.epicgames.com/community/api/documentation/image/81aa4df2-cdda-44b1-9312-9efe29b7eac9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81aa4df2-cdda-44b1-9312-9efe29b7eac9?resizing_type=fit)
_Concept reference for a sunny style map with NPC encounter on the roof._
With the post-process volumes and additional visual techniques you can take this concept of a sunny style city and bring it to life.
####  Skybox Adjustments
First, brighten the atmosphere with the procedural skybox. To create blue skies, follow these steps:
  1. In the **Content Drawer** , search **MI_ProceduralSkybox** and double-click to open the Material Editor.
  2. In the Details panel, adjust the following values:
    1. **Cloud Dark and Light:** RGB 1.0, 1.0, 1.0
    2. **Horizon Colour:** RGB 0.0619, 0.970, 1.0
    3. **Colour Top:** RGB 0.038, 0.119, 0.838
    4. **Star Brightness:** 0 (to turn off stars)
    5. **Moon Brightness:** 9.5 (to mimic the sun)

Alternatively, instead of the moon brightness adjustment, you can swap the moon texture in the Material Graph with your own image of the sun.
[![Moon Texture in Material Graph](https://dev.epicgames.com/community/api/documentation/image/063db12c-139e-4614-bca1-59d483f18bdc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/063db12c-139e-4614-bca1-59d483f18bdc?resizing_type=fit)
####  Light Adjustments
With the blue skies, the sun and its light direction must match better. To adjust the position of the sun and light direction, follow these steps:
  1. In the **Outliner,** search and select **DirectionalLight_Index1**.
  2. Rotate the light to the left to set a higher position.
  3. In the**Details** panel, increase the light intensity to 6.

Next, to turn off the midground and foreground window lights, follow these steps:
  1. Click a midground window.
  2. In the Menu bar click **Select > Select All With Same Material**.
  3. Delete the window set.
  4. Repeat the steps for the foreground windows.

Removing the windows when they are not needed helps optimize the scene.
####  Fog Adjustments
For the sunny mode, use **PostProcessVolume_Cartoon** as the base. To adjust the fog depth and color, follow these steps:
  1. In the Content Drawer, search **PP_DepthFog_Inst** then double-click the material to open the Material Editor.
  2. In the Details panel, double-click the **Curve Input** color curve.
  3. Adjust the top color key values:
    1. Far right color key: RGB 0.022, 0.979, 0.629
    2. Middle color key: RGB 0.0, 0.140, 0.307
    3. Far left color key: RGB 0.208, 0.059, 0.117

[![Color Ramp Adjustments](https://dev.epicgames.com/community/api/documentation/image/74a94824-9bc3-4bf2-95a3-98cc56603ff4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/74a94824-9bc3-4bf2-95a3-98cc56603ff4?resizing_type=fit)
In the **Details** panel of **PP_DepthFog_Inst** , adjust the depth of the color ramp with the following values:
  * **Curve Far Point:** 93511
  * **Curve Near Point:** 14887

####  Posterization Adjustments
Finally, add the posterization to create a similar dotted effect as the Comic-Noir mode.
  1. In the Details panel, under the Post Process Materials, add a material array element by clicking the plus icon.
  2. From the dropdown of the new array, choose **Asset reference** , then search and select **PP_Posterize**.
  3. To adjust the amount, browse to the material and double-click to open the Material Editor.
  4. In the Parameters panel, set **Posterize Amount** to 0.05.

[![Posterize Adjustment](https://dev.epicgames.com/community/api/documentation/image/0410e468-452f-404b-956e-029cc6e63d40?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0410e468-452f-404b-956e-029cc6e63d40?resizing_type=fit)
With some adjustments to materials and lights you woke up the city to blue skies! Now get those turtles to their lair quickly.
[![Sunny Style Mode](https://dev.epicgames.com/community/api/documentation/image/9594f774-657b-4c80-a207-f5c897ce1f3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9594f774-657b-4c80-a207-f5c897ce1f3d?resizing_type=fit)
