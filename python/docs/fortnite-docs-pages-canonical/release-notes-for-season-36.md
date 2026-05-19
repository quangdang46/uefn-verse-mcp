## https://dev.epicgames.com/documentation/en-us/fortnite/release-notes-for-season-36

# UI Texture Material Collection
Use customizable textures to create custom icons or avatar images.
Customizing UI textures is time consuming and requires deep knowledge of [material functions](https://dev.epicgames.com/documentation/fortnite/material-functions-in-unreal-editor-for-fortnite) and setup. To make custom UI textures more accessible, Unreal Editor for Fortnite (UEFN) has a series of highly customizable [textures](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#texture).
##  UI Material Folders
The UI Materials folder is in the content browser under **Fortnite** > **UI** > **Materials**.
The **Materials folder** contains two types of UI materials:
  * **Meter materials** : Typically used for measuring health and shields. (See UI Materials Collections for more information.)
  * **Textures** : Typically used as a background image or in UI animations.

Textures belong to the following parameter categories:
|  |
---|---|---
**SDF Texture** |  **Texture Effects** |  **Texture Mask**
A texture shape with a fuzzy outline. You can set parameters that customize:
  * Color
  * Shape
  * Stroke
  * Shadow

You can also rotate and feather the textures. |  A texture with 9 different customizable special effects. All effects are driven by [material functions](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#material-function) that you customize using parameter inputs. |  A texture mask hides portions of the texture based on your inputs. You can set parameters that provide a way to customize:
  * Color
  * Shape
  * Stroke

[![](https://dev.epicgames.com/community/api/documentation/image/60d6eaa6-e917-4beb-826c-2831cacc0061?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60d6eaa6-e917-4beb-826c-2831cacc0061?resizing_type=fit) |  [![](https://dev.epicgames.com/community/api/documentation/image/f4ad6bf1-f91f-4a0b-8d9b-5df1106c6c57?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f4ad6bf1-f91f-4a0b-8d9b-5df1106c6c57?resizing_type=fit) |  [![](https://dev.epicgames.com/community/api/documentation/image/3ee6cb05-c3f5-46c8-b504-81b124f248cb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ee6cb05-c3f5-46c8-b504-81b124f248cb?resizing_type=fit)
##  Create a Material Instance
To use a texture from the UI folder, you must first turn it into a **material instance**. Material instances use less memory than materials or textures, and are much more customizable in UMG due to the parameters available.
Parameters are manipulated in the View Model where they are bound with a device function or Verse code that manipulates the material into behaving a certain way.
To create a material instance from a material, follow these steps:
  1. Open the **Project** > **Fortnite** > **UI** > **Materials** folders.
[![The UI Materials are found under Fortnite in the UI folder.](https://dev.epicgames.com/community/api/documentation/image/bec15382-7ad1-4458-b25d-cebfcc36af5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bec15382-7ad1-4458-b25d-cebfcc36af5a?resizing_type=fit) Click image to enlarge.
  2. **Right-click** a material to open the dropdown context menu.
  3. Select **Create Material Instance** from the dropdown menu.
[![Right-click on a material thumbnail to open the context menu. Select Material Instance from the dropdown menu to create a modifiable material instance.](https://dev.epicgames.com/community/api/documentation/image/4e1e9459-28be-4f5d-b1ec-bd5f23bc6ad2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e1e9459-28be-4f5d-b1ec-bd5f23bc6ad2?resizing_type=fit) Click image to enlarge.

A material instance automatically generates in the main project folder.
##  SDF Texture
The [SDF](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#sdf) texture can override the player’s default avatar icon image, or be used for iconography. An SDF texture has a number of customizable parameters that you use to determine the appearance of the icon, make the icon fuzzy or sharp, create a glow effect to make the icon look like a neon sign and more.
All of a texture’s parameters can be used with the [View Model](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#view-model) in UMG and in Verse code through Verse fields. Use the table below to learn more about using the different parameters.
###  Base
The basic parameters for the SDF texture.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Texture** |  Select an SDF texture from the dropdown menu. |
**Color** |  Select a color for the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/023f6e10-51f1-4f97-81ca-5e182ac2bf3c?resizing_type=fit)
**Glow Max** |  Increases and decreases the glow of the shape’s edge. Values closer to **0** solidify the outline of the shape. Values closer to **1** increase the shape’s outline glow. Additional GlowMax parameters are dependent on the **GlowMax** value. |  ![](https://dev.epicgames.com/community/api/documentation/image/80285c8a-6768-40a9-8ee7-2dcf7ce2af88?resizing_type=fit)
**Rotation** |  Rotates the texture from the center. A value of **0.25** rotates the texture 90 degrees to the left. A value of **-0.25** rotates **90 degrees t** o the right. |  ![](https://dev.epicgames.com/community/api/documentation/image/ccdbd3e5-68d8-4802-afda-532e8af27f31?resizing_type=fit)
**Texture Feather Amount** |  Determines how much feathering to enforce on the SDF texture's edges when GlowMax parameters are in use. High values increase the amount of feathering and lower values decrease the amount of feathering. |  ![](https://dev.epicgames.com/community/api/documentation/image/129105d9-4e3b-439a-afd3-e973edd1ddb1?resizing_type=fit)
###  Shadow Color
Determines the color of the texture shadow.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Shadow Glow Max** |  Determines how much glow the texture shadow has. Values closer to s**0** solidify the outline of the shape. Values closer to 1 increase the shape’s outline glow. |  ![](https://dev.epicgames.com/community/api/documentation/image/66a6799c-0dba-4a29-9bd1-d89afac2e285?resizing_type=fit)
**Shadow Offset X** |  Determines the offset amount of the texture shadow along the **X-axis**. Higher values move the shadow away from the texture. Lower values move the shadow closer to the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/536dd72e-03ff-4c76-80e3-af54e6090552?resizing_type=fit)
**Shadow Offset Y** |  Determines the offset amount of the texture shadow along the **Y-axis**. Higher values move the shadow away from the texture. Lower values move the shadow closer to the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/87dec5fc-d9f9-4166-84d5-4427097f3054?resizing_type=fit)
**Shadow Opacity** |  Determines the opacity of the texture shadow. Values closer to **1** increase the opacity of the selected color. Values closer to **0** decrease the opacity of the color. |  ![](https://dev.epicgames.com/community/api/documentation/image/c8b05ab1-08a9-4db9-bfce-c7cae7a86562?resizing_type=fit)
**Shadow Rotation** |  Rotate the texture shadow from the center. A value of **0.25** rotates the texture shadow **90 degrees** to the left. |  ![](https://dev.epicgames.com/community/api/documentation/image/58996ced-c3d7-4854-b8ac-fb7d2b38c9c0?resizing_type=fit)
**Shadow Thickness** |  Determines the thickness of the texture shadow. Higher values increase the size of the shadowthickness. Lower values decrease the thickness. |  ![](https://dev.epicgames.com/community/api/documentation/image/15a98b25-b0d2-4318-85bb-05628963a56d?resizing_type=fit)
###  Stroke
Parameters that affect the appearance of the texture’s stroke.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Inner Stroke Color** |  Determines the color of the texture’s inner stroke. |  ![](https://dev.epicgames.com/community/api/documentation/image/de97b7f4-e18d-4d05-aaca-4bc6785c0f4c?resizing_type=fit)
**Inner Stroke Glow Max** |  Determines the maximum glow amount of the texture’s inner stroke. InnerStrokeGlowMax is dependent on the **GlowMax** value. The maximum GlowMax value set determines the maximum glow value for InnerStrokeGlowMax and OuterStrokeGlowMax. |  [![](https://dev.epicgames.com/community/api/documentation/image/6905f04d-e326-4052-aeff-638a27c8e785?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6905f04d-e326-4052-aeff-638a27c8e785?resizing_type=fit)
**Inner Stroke Thickness** |  Determines the thickness of the inner stroke. Higher values increase the thickness of the stroke and lower values reduce it. |  ![](https://dev.epicgames.com/community/api/documentation/image/5be482ec-2283-48b7-9db4-2b8f03c7db52?resizing_type=fit)
**Inner Stroke Thickness Glow Max** |  Determines the glow thickness of the texture’s inner stroke. Higher values increase the glow thickness of the stroke and lower values reduce the glow thickness of the texture’s inner stroke. InnerStrokeThicknessGlowMax is dependent on the **GlowMax** value. The maximum GlowMax value set determines the maximum glow value for InnerStrokeGlowMax, InnerStrokeThicknessGlowMax, and OuterStrokeGlowMax. |  ![](https://dev.epicgames.com/community/api/documentation/image/dfd47971-0c9c-4520-8c84-00229807e549?resizing_type=fit)
**Outer Stroke Color** |  Determines the color of the outer stroke. |  ![](https://dev.epicgames.com/community/api/documentation/image/6e30ab18-39de-4175-9d34-2088bc9879bd?resizing_type=fit)
**Outer Stroke Glow Max** |  Determines the glow amount of the texture’s outer stroke. Values closer to **0** solidify the outline of the shape. Values closer to **1** increase the shape’s outline glow. OuterStrokeGlowMax is dependent on the **GlowMax** value. The maximum GlowMax value set determines the maximum glow value for InnerStrokeGlowMax, InnerStrokeThicknessGlowMax, and OuterStrokeGlowMax. |  [![](https://dev.epicgames.com/community/api/documentation/image/2e1b4503-6079-436a-b1b8-3cea9a9407c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e1b4503-6079-436a-b1b8-3cea9a9407c3?resizing_type=fit)
**Outer Stroke Thickness** |  Determines the thickness of the texture’s outer stroke. Higher values increase the thickness of the stroke and lower values reduce the thickness. |  ![](https://dev.epicgames.com/community/api/documentation/image/6d6a3147-e4d4-47eb-b0e1-b43f72cdc4ed?resizing_type=fit)
**Outer Stroke Thickness Glow Max** |  Determines the glow thickness of the texture’s outer stroke. Higher values increase the glow thickness of the stroke and lower values reduce it. |  ![](https://dev.epicgames.com/community/api/documentation/image/6ddf9c52-4812-47ac-9e9f-ff7085db79ce?resizing_type=fit)
##  Texture Effects
Texture Effects has a number of customizable effects that can transform the appearance of the texture:
  * Tile
  * Warp
  * Pixelate
  * Bounce
  * Halftone
  * Stepped Gradient
  * And more…

The parameters can be mixed and targeted with the [View Model](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#view-model) in [UMG](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/UMG) and in Verse code through Verse fields. Use the table below to learn more about the different parameters.
###  Basic Texture
The basic parameters for the texture. Select a texture from the dropdown menu.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Texture** |  Select a texture from the dropdown menu. |  ![](https://dev.epicgames.com/community/api/documentation/image/48d014d3-e74f-437c-9309-e2561e91a859?resizing_type=fit)
**Tiling X** |  Tiles the texture along the **X-axis**. A value of **1** does not tile the texture. Values above**1** add tiles along the **X-axis**. It’s best to use whole numbers for this parameter to have complete images. |  ![](https://dev.epicgames.com/community/api/documentation/image/2219592b-0ab5-4f43-b646-f1ece538c336?resizing_type=fit)
**Tiling Y** |  Tiles the texture along the **Y-axis**.  A value of **1** does not tile the texture.  Values above**1** add tiles to the texture along the **Y-axis**. It’s best to use whole numbers for this parameter to have complete images |  ![](https://dev.epicgames.com/community/api/documentation/image/7e96ee9b-ae14-4e00-a0bb-6bc05f2f8e4d?resizing_type=fit)
**Translate X** |  Moves the texture along the **X-axis**. You can animate the texture by targeting the **Translate X parameter** with Sequencer inside UMG. |  ![](https://dev.epicgames.com/community/api/documentation/image/d21e2c3d-8a28-4039-8d6e-63581c6c4741?resizing_type=fit)
**Translate Y** |  Moves the texture along the **Y-axis**. You can animate the texture by targeting the **Translate Y parameter** with Sequencer inside UMG. |  ![](https://dev.epicgames.com/community/api/documentation/image/531428b0-c9fd-47a0-a40a-41956be0f15f?resizing_type=fit)
**Translate Speed X** |  Determines the speed of translation across the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/9e8ad122-6be5-43cf-8608-9bb8a7b62d57?resizing_type=fit)
**Translate Speed Y** |  Determines the speed of translation across the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/91023a0f-651a-48bf-a911-39e84b226010?resizing_type=fit)
###  Scaling
Parameters that provide a way to change the scale and size of the texture. Creates a pounding effect on the texture.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Is Scaling** |  Determines the scaling effect on the texture. This option is only visible when the other Scaling parameters are also in use. |  ![](https://dev.epicgames.com/community/api/documentation/image/312c8863-b6e1-4d22-ae9b-75b6e673abe9?resizing_type=fit)
**Scaling Maximum Speed** |  Determines the maximum speed of the scaling effect on the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/8f5c8b35-2d17-4f92-8fc3-4341dc5bb594?resizing_type=fit)
**Scaling Minimum Speed** |  Determines the minimum speed of the scaling effect on the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/b11128b2-46a0-4602-bf45-147f5642e020?resizing_type=fit)
**Start Size** |  The texture’s size at the beginning of the animation. |  ![](https://dev.epicgames.com/community/api/documentation/image/91868d58-f700-4f81-b0a4-5f63d6b23c70?resizing_type=fit)
**Middle Size** |  The texture’s size in the middle of the animation. |  ![](https://dev.epicgames.com/community/api/documentation/image/28b3bafe-54b5-4d61-a50b-285cb701379d?resizing_type=fit)
**End Size** |  The texture’s size at the end of the animation. |  ![](https://dev.epicgames.com/community/api/documentation/image/e5ff008c-0383-4863-aef0-eb80c0d0f468?resizing_type=fit)
###  Warping
Parameters that provide a way to add a warping effect to the texture.
To alter the appearance of an icon, additional Warping parameters must be used along with the **IsWarping** parameter.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Is Warping** |  Determines the amount of warping effect on the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/c2cb0a83-d68c-4953-9063-c58af2edd670?resizing_type=fit)
**Amplitude X** |  Applies a stretching effect along the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/4788af76-34b4-488f-bb0e-38c88babd334?resizing_type=fit)
**Amplitude Y** |  Applies a stretching effect along the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/d316c7fb-80fd-45bb-89d1-36cac8149f5a?resizing_type=fit)
**Frequency X** |  Applies a **Sine Wave** effect to the texture along the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/b41e0b32-1f7b-4688-ab70-86ebee565715?resizing_type=fit)
**Frequency Y** |  Applies a **Sine Wave** effect to the texture along the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/cbbf6771-5143-4795-8bd9-4ffa7ee9d843?resizing_type=fit)
**Warp Speed** |  Determines how fast the warp effect is on the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/f6c1644e-7b34-4659-b4ce-8d2d660c3074?resizing_type=fit)
###  Pixelate
Parameters that provide a way to pixelate the appearance of the texture.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Is Pixelated** |  Adds a pixel effect to the texture. A value of **0** does not apply the pixel effect to the texture. A value of **1** completely pixelates the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/9589d84a-f68c-4411-b439-5ea9a0e9466c?resizing_type=fit)
**Number of Pixels** |  Determines the number of pixels the texture has. A value of **1** turns the texture into a square. Adding more pixels creates a pixelated shape. |  ![](https://dev.epicgames.com/community/api/documentation/image/4f44a5ba-a134-496f-82b2-fb84dcdcea12?resizing_type=fit)
###  Bounce
Parameters that provide a way to add a bouncing effect to the texture.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Is Bouncing** |  Determines the bounce rate of the effect. This option is only visible when the other Bounce parameters are also in use. |  ![](https://dev.epicgames.com/community/api/documentation/image/22bfd64d-8ae6-4309-83ae-650e7e9ec101?resizing_type=fit)
**Bounce Speed** |  Determines how fast the texture bounces. |  ![](https://dev.epicgames.com/community/api/documentation/image/943681c4-a8fd-448a-8ff0-5b7ad8be5e31?resizing_type=fit)
**Bounce X** |  Determines the amount of bounce effect to apply along the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/01f848cd-0eb5-4ccb-a7a9-9681437d0642?resizing_type=fit)
**Bounce Y** |  Determines the amount of bounce effect to apply along the**Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/b9c0baee-d7ef-4864-82bc-2bc657201cd3?resizing_type=fit)
###  Halftone
Parameters that produce a comic ink dot effect on the texture.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Is Halftone** |  Determines whether the effect is in use and the opacity of the halftone effect. Higher values increase the opacity of the effect, while lower values decrease the opacity of the effect. |  ![](https://dev.epicgames.com/community/api/documentation/image/c0fca930-f5c5-48c5-9fc5-6bfe374b3239?resizing_type=fit)
**Dot Density** |  Increases the density of dots in the effect. Higher values increase the number of dots and reduces the size of the dots. Lower values decrease the number of dots and increase the size of the dots. |  ![](https://dev.epicgames.com/community/api/documentation/image/4d8ee350-3cb2-442c-b90c-23f21d8c71cf?resizing_type=fit)
**Dot Glow Max** |  Determines the maximum amount of glow applied around the dots. Positive values cause the dots to appear like stars, negative values cause the dots to appear as circles. |  ![](https://dev.epicgames.com/community/api/documentation/image/7ee9cfac-394a-4cbc-9b35-7d7c9dfac2f9?resizing_type=fit)
**Dot Glow Min** |  Determines the minimum amount of glow around the dots. The values can be used to switch the color of the background and dots. Values of **5 and higher** cause the effect to fade into one color. Similarly, values below **-7** cause the effect to fade into one color. |  ![](https://dev.epicgames.com/community/api/documentation/image/92c79328-1be8-462d-b990-4ab6dfb2ec14?resizing_type=fit)
**Dot Max Size** |  Determines the maximum size of the dots. |  ![](https://dev.epicgames.com/community/api/documentation/image/ae096d1c-8654-428d-b5ae-929d7efa972c?resizing_type=fit)
**Dot Min Size** |  Determines the minimum size of the dots. |  ![](https://dev.epicgames.com/community/api/documentation/image/ee932438-89f0-4fa4-8b23-5a651728fe8e?resizing_type=fit)
**Gradient Color 1** |  Determines the primary color of the halftone effect. |  ![](https://dev.epicgames.com/community/api/documentation/image/f5805608-e195-4ee7-b26b-e8347148ca67?resizing_type=fit)
**Gradient Color 2** |  Determines the secondary color of the halftone effect. |  ![](https://dev.epicgames.com/community/api/documentation/image/29d96908-7895-46c3-b534-06127d05daab?resizing_type=fit)
**Halftone Pan Speed X** |  Determines the speed the dots travel across the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/da47f7a7-5522-4bb8-84a0-2e24996d1b03?resizing_type=fit)
**Halftone Pan Speed Y** |  Determines the speed the dots travel across the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/1c2a2569-3c7f-454e-ba5c-fa2ef5c9dd6e?resizing_type=fit)
**Halftone Rotation** |  Rotates the direction the dots travel. |  ![](https://dev.epicgames.com/community/api/documentation/image/867ad00f-00ee-42a3-81b5-f419f705fd2d?resizing_type=fit)
###  Stepped Gradient
Parameters that provide a way to add a stepped gradient to the texture.
These parameters are dependent upon the **Tint Color** parameters.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Is Stepped Gradient** |  Determines if the stepped gradient effect is applied to the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/791b360a-5b3a-4831-a9ec-19d83ea0106b?resizing_type=fit)
**Stepped Gradient Amount** |  Determines the amount of stepped gradient to apply to the texture. **IsSteppedGradient** must be enabled with a value below **1.0** for this parameter to work. |  ![](https://dev.epicgames.com/community/api/documentation/image/90520219-cb78-4338-ba3d-ac14f1e4ea4d?resizing_type=fit)
###  Tint Color
These parameters provide a way to add colors to the texture to create a gradient effect on the texture.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Tint Gradient Opacity** |  Determines the opacity of the colors in the gradient. Lower values decrease the texture’s opacity and higher values increase the material’s opacity. |  ![](https://dev.epicgames.com/community/api/documentation/image/abefe039-549b-434a-bc65-ee8ea7931af1?resizing_type=fit)
**Tint Color 1** |  Determines the first color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/3b989ed5-cf9a-407b-9bef-9504c388183f?resizing_type=fit)
**Tint Color 1 Position** |  Determines the position for the first color in the gradient. This option only works when the **TintGradientOn** option is selected and a value set. |  ![](https://dev.epicgames.com/community/api/documentation/image/e291256e-da12-4d4e-b28a-530c0df8efbf?resizing_type=fit)
**Tint Color 2** |  Determines the second color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/058263b4-baa0-4a53-9d68-5f00ae454a67?resizing_type=fit)
**Tint Color 2 Position** |  Determines the position for the second color in the gradient. Higher values shift the gradient to start on the opposite side. Lower values increase the appearance of the second color selection. This option only works when the **Tint GradientOn** option is selected and a value set. |
**Tint Color 3** |  Determines the third color in the gradient. |
**Tint Color 3 Position** |  Determines the position for the second color in the gradient. Higher values shift the gradient to start on the opposite side. Lower values increase the appearance of the second color selection. This option only works when the **TintGradientOn** option is selected and a value set. |
**Tint Gradient On** |  Determines whether the gradient effect is applied to the texture. |
**Tint Gradient Rotation** |  Rotates the direction of the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/fec4b4d3-7853-4a4d-9b3b-c58c8695fc31?resizing_type=fit)
**Tint Radial Gradient** |  Changes the gradient into a radial gradient. |
**Tint Radial Gradient Size** |  Determines the radial gradient size. |
###  Alpha Color
Parameters that provide a way to add transparency, color, and gradient to a texture that has Alpha and .
These parameters work best on textures that have color, like a character picture, or a black and white texture.
[![An illustration that shows where the Alpha parameters have influence over the image or shape in the texture.](https://dev.epicgames.com/community/api/documentation/image/410f4fcf-ccf2-4b68-b2b7-f31aa6934344?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/410f4fcf-ccf2-4b68-b2b7-f31aa6934344?resizing_type=fit) Alpha example
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Alpha Opacity** |  Determines the opacity of the Alpha colors on the texture. Lower values decrease the texture’s opacity and higher values increase the material’s opacity. |  ![](https://dev.epicgames.com/community/api/documentation/image/dd6a906c-fab1-4587-8d07-c94d3c980f43?resizing_type=fit)
**Alpha Color 1** |  Determines the first color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/1280d0a5-dd11-4961-b4d5-ab22f8db73fc?resizing_type=fit)
**Alpha Color 1 Position** |  Determines the position for the first color in the gradient. This option only works when the **AlphaGradientOn** option is selected and a value set. |  ![](https://dev.epicgames.com/community/api/documentation/image/1279cccf-0035-40bb-b0b0-4f728412d4ec?resizing_type=fit)
**Alpha Color 2** |  Determines the second color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/8264ff8a-884f-4e81-a5ec-e20c06d65e64?resizing_type=fit)
**Alpha Color 2 Position** |  Determines the position for the second color in the gradient. Higher values shift the gradient to start on the opposite side. Lower values increase the appearance of the second color selection. This option only works when the **AlphaGradientOn** option is selected and a value set. |  ![](https://dev.epicgames.com/community/api/documentation/image/c6ed21a5-90e3-4d0d-a21c-9d35118fb27d?resizing_type=fit)
**Alpha Color 3** |  Determines the third color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/080338ac-cd4a-465f-bd57-d03268d22167?resizing_type=fit)
**Alpha Color 3 Position** |  Determines the position for the third color in the gradient. Higher values shift the gradient to start on the opposite side. Lower values increase the appearance of the third color selection. This option only works when the **AlphaGradientOn** option is selected and a value set. |  ![](https://dev.epicgames.com/community/api/documentation/image/d698eb63-81a7-42d4-8757-cc0fe2b31b40?resizing_type=fit)
**Alpha Gradient On** |  Determines whether the gradient is applied to the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/3de2749a-2cf1-4193-af7d-9a6af8f45b8a?resizing_type=fit)
**Alpha Gradient Rotation** |  Rotates the direction of the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/d84d9b98-2c64-4426-af2b-2e50e6d4c4eb?resizing_type=fit)
**Alpha Radial Gradient** |  Turns the gradient into a radial gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/53af2e2e-b061-450e-adfa-6cdd6e175524?resizing_type=fit)
**Alpha Radial Gradient Size** |  Determines the radial gradient size. |  ![](https://dev.epicgames.com/community/api/documentation/image/a5242c15-b8b7-4f48-8b82-3a77fa98ab17?resizing_type=fit)
##  Texture Mask
Texture Mask uses parameters that can mask the icon or player avatar and add outline elements to the icon or avatar image.
The Texture Mask material has a number of customizable parameters that you use with the View Model in UMG and in Verse code through Verse Fields. Use the table below to learn more about using the different parameters.
###  Texture
Parameters that determine the appearance of the texture.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Texture** |  Select a texture from the dropdown menu. |  ![](https://dev.epicgames.com/community/api/documentation/image/1d68f074-19df-4a4c-b943-61577e33ce91?resizing_type=fit)
**Texture Alpha** |  Determines the Alpha color of the texture. The **1** value is white. Values **below 1** decrease the white value and blend with the background color. |  ![](https://dev.epicgames.com/community/api/documentation/image/60ea9e5e-0a16-423f-98f3-825a1936c5f6?resizing_type=fit)
**Texture Position X** |  Positions the texture along the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/8e3ad22a-70c6-4b67-af59-193e545bf225?resizing_type=fit)
**Texture Position Y** |  Positions the texture along the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/4f91e7f2-d625-4c3d-a773-e0efd00b15a5?resizing_type=fit)
**Texture Scale X** |  Scales the texture along the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/1a9826ec-6701-42d3-bdb2-44d2b974c41a?resizing_type=fit)
**Texture Scale Y** |  Scales the texture along the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/013da100-b247-4004-bc5e-8ac0c0469274?resizing_type=fit)
###  Fill
Parameters that determine the look of the gradient applied to the background.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Custom Fill Texture** |  Select a Fill Texture from the dropdown menu. |
**Fill Alpha** |  Determines the Alpha color of the mask. The**1** value is white, values**below 1** decrease the white value and blend with the background color. |  ![](https://dev.epicgames.com/community/api/documentation/image/8b4caff0-cd2b-427f-8322-96f5bef3430d?resizing_type=fit)
**Fill Color 1** |  Determines the first color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/c42965c5-4636-4ddb-90a7-f85d1794aa0e?resizing_type=fit)
**Fill Color 1 Gradient Position** |  Determines the position for the first color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/e326e158-9080-469a-8156-c933f9cf03d6?resizing_type=fit)
**Fill Color 2** |  Determines the second color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/341b9eb5-6f25-456e-a94d-6c89e0de34d9?resizing_type=fit)
**Fill Color 2 Gradient Position** |  Determines the position for the second color in the gradient. Higher values shift the gradient to start on the opposite side. Lower values increase the appearance of the second color selection. |  ![](https://dev.epicgames.com/community/api/documentation/image/278567ca-ab3f-4f9e-8bbe-ba8380f29365?resizing_type=fit)
**Fill Color 3** |  Determines the third color in the gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/15cc6341-268e-4206-93cc-f023f90b0955?resizing_type=fit)
**Fill Color 3 Gradient Position** |  Determines the position for the third color in the gradient. Higher values shift the gradient to start on the opposite side. Lower values increase the appearance of the third color selection. |  ![](https://dev.epicgames.com/community/api/documentation/image/52c29064-febd-4918-933d-5364652305aa?resizing_type=fit)
**Fill Color Radial Gradient Size** |  Determines the size of the gradient on the background. |  ![](https://dev.epicgames.com/community/api/documentation/image/affc750b-49a8-40fe-9031-b22906c2bf74?resizing_type=fit)
**Fill Gradient Type** |  Changes the gradient type from radial to linear. |  ![](https://dev.epicgames.com/community/api/documentation/image/4aa788e8-a8f3-4617-b5de-617bde8167c1?resizing_type=fit)
**Glow** |  Determines the glow amount of the background. |
**Linear Gradient Fill Rotation** |  Rotates the gradient around a circle. The LinearGradientFillRotation option is dependent on values set in the **FillGradientType** option. |  ![](https://dev.epicgames.com/community/api/documentation/image/9f3997f8-91b7-4c60-91ef-80049ff8d847?resizing_type=fit)
**Shape** |  Determines the shape of the mask around the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/656d27f1-ee99-41ce-bc6e-df2e1719414b?resizing_type=fit)
**Shape Rotation** |  Rotates the mask shape around the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/beddab2d-99c3-4a4c-a45a-28352f95ed3d?resizing_type=fit)
**Shape Size** |  Determines the size of the mask shape around the texture. |  ![](https://dev.epicgames.com/community/api/documentation/image/98fba951-a7e4-4dcb-9420-401b80875978?resizing_type=fit)
**Bottom Left Corner Radius** |  Changing this parameter adds a rounded corner to the bottom left corner based on the value used. |  ![](https://dev.epicgames.com/community/api/documentation/image/3d3bfff6-831d-49dc-8677-5883a1dd9208?resizing_type=fit)
**Bottom Right Corner Radius** |  Changing this parameter adds a rounded corner to the bottom right corner based on the value used. |  ![](https://dev.epicgames.com/community/api/documentation/image/0873e977-84b7-4df1-b241-8c842edcb92c?resizing_type=fit)
**Top Left Corner Radius** |  Changing this parameter adds a rounded corner to the top left corner based on the value used. |  ![](https://dev.epicgames.com/community/api/documentation/image/8ab5a425-2505-4a7d-82a0-1676f3819179?resizing_type=fit)
**Top Right Corner Radius** |  Changing this parameter adds a rounded corner to the top right corner based on the value used. |  ![](https://dev.epicgames.com/community/api/documentation/image/d9ce887c-14b2-4b1d-9a90-3ab4361ffc4c?resizing_type=fit)
###  Outline
Parameters that determine the appearance of the outline around the mask.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Gap Thickness** |  Determines the gap size between the outline and the texture. The GapThickness option is dependent on the **OutlineAlpha** option having a value set over **0.40**. |  ![](https://dev.epicgames.com/community/api/documentation/image/4a59f087-2245-40f3-9136-c50cc5cb81fb?resizing_type=fit)
**Outline Alpha** |  Determines the Alpha color of the outline. The **1** value is the full alpha color, values **below 1** decrease the color value and blend into the background. |  ![](https://dev.epicgames.com/community/api/documentation/image/6762d7bb-f0d6-4191-bd9c-97848f8a38b0?resizing_type=fit)
**Outline Color 1** |  Determines the first color in the outline gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/695aa96f-af83-4f16-b0f1-a98f3a47d4b5?resizing_type=fit)
**Outline Color 1 Position** |  Determines the position for the first color in the outline gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/5df06816-c3f4-4b7d-832c-e8a458c5b6f2?resizing_type=fit)
**Outline Color 2** |  Determines the second color in the outline gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/8ea7e4a9-d084-447e-beb2-85d4ee9251d9?resizing_type=fit)
**Outline Color 2 Position** |  Determines the position for the second color in the outline gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/ca9db7f5-7a45-435e-bd3e-e36172942294?resizing_type=fit)
**Outline Color 3** |  Determines the third color in the outline gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/2ab9e7b2-27cf-4cda-9cbd-5ef68d1bf274?resizing_type=fit)
**Outline Color 3 Position** |  Determines the position for the third color in the outline gradient. |  ![](https://dev.epicgames.com/community/api/documentation/image/9e907f50-830f-4c2f-8f74-30ef17623114?resizing_type=fit)
**Outline Thickness** |  Determines the thickness of the outline. |  ![](https://dev.epicgames.com/community/api/documentation/image/8f17f740-2525-452a-bcd4-d635b2267ff9?resizing_type=fit)
###  Texture Mask
Parameters to change the appearance of the texture mask.
|  |
---|---|---
**Parameter** |  **Description** |  **GIF**
**Show Mask Preview** |  Determines the opacity of the mask preview. A value of **0** means the preview is invisible, a value of **1** means the mask is completely visible. This parameter is only visible when the **MaskWidth** and **MaskHeight** options have values higher than **0.0**. |  ![](https://dev.epicgames.com/community/api/documentation/image/83b257d4-e5a0-4dcb-bcca-7b1ddf0153be?resizing_type=fit)
**Mask Position X** |  Position the mask along the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/43e6c8b0-d902-4394-9c02-d6e5dc48ef36?resizing_type=fit)
**Mask Position Y** |  Position the mask along the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/1338b560-5b0a-4a54-aac6-491633f68831?resizing_type=fit)
**Mask Height** |  Determines the height of the mask. |  ![](https://dev.epicgames.com/community/api/documentation/image/3826e23f-84f4-4471-bd9e-efb032f4676a?resizing_type=fit)
**Mask Width** |  Determines the width of the mask. |  ![](https://dev.epicgames.com/community/api/documentation/image/39842ac4-a426-42eb-9089-776908c2cfd7?resizing_type=fit)
###  Slant
Parameters that determine the degree of slant to apply to the background and mask outline.
|  |
---|---|---
**Parameter** |  Description |  **GIF**
**Slant X** |  Slants the background and mask outline along the **X-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/30dc02aa-f9d6-41b7-a67e-133b6cd80031?resizing_type=fit)
**Slant Y** |  Slants the background and mask outline along the **Y-axis**. |  ![](https://dev.epicgames.com/community/api/documentation/image/d17933c7-8d34-4dcf-8e6d-3f5c79d48860?resizing_type=fit)
