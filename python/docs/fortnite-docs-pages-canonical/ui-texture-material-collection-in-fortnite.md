## https://dev.epicgames.com/documentation/en-us/fortnite/ui-texture-material-collection-in-fortnite

# UI Texture Material Collection

Use customizable textures to create custom icons or avatar images.

Customizing UI textures is time consuming and requires deep knowledge of [material functions](https://dev.epicgames.com/documentation/fortnite/material-functions-in-unreal-editor-for-fortnite) and setup. To make custom UI textures more accessible, Unreal Editor for Fortnite (UEFN) has a series of highly customizable [textures](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#texture).

## UI Material Folders

The UI Materials folder is in the content browser under **Fortnite** > **UI** > **Materials**.

The **Materials folder** contains two types of UI materials:

- **Meter materials**: Typically used for measuring health and shields. (See UI Materials Collections for more information.)
- **Textures**: Typically used as a background image or in UI animations.

Textures belong to the following parameter categories:

|  |  |  |
| --- | --- | --- |
| **SDF Texture** | **Texture Effects** | **Texture Mask** |
| A texture shape with a fuzzy outline. You can set parameters that customize:   - Color - Shape - Stroke - Shadow   You can also rotate and feather the textures. | A texture with 9 different customizable special effects.  All effects are driven by [material functions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#material-function) that you customize using parameter inputs. | A texture mask hides portions of the texture based on your inputs. You can set parameters that provide a way to customize:   - Color - Shape - Stroke |
|  |  |  |

## Create a Material Instance

To use a texture from the UI folder, you must first turn it into a **material instance**. Material instances use less memory than materials or textures, and are much more customizable in UMG due to the parameters available.

Parameters are manipulated in the View Model where they are bound with a device function or Verse code that manipulates the material into behaving a certain way.

To create a material instance from a material, follow these steps:

A material instance automatically generates in the main project folder.

## SDF Texture

The [SDF](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#sdf) texture can override the player’s default avatar icon image, or be used for iconography. An SDF texture has a number of customizable parameters that you use to determine the appearance of the icon, make the icon fuzzy or sharp, create a glow effect to make the icon look like a neon sign and more.

All of a texture’s parameters can be used with the [View Model](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#view-model) in UMG and in Verse code through Verse fields. Use the table below to learn more about using the different parameters.

### Base

The basic parameters for the SDF texture.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Texture** | Select an SDF texture from the dropdown menu. |  |
| **Color** | Select a color for the texture. |  |
| **Glow Max** | Increases and decreases the glow of the shape’s edge.  Values closer to **0** solidify the outline of the shape.  Values closer to **1** increase the shape’s outline glow.  Additional GlowMax parameters are dependent on the **GlowMax** value. |  |
| **Rotation** | Rotates the texture from the center.  A value of **0.25** rotates the texture 90 degrees to the left. A value of **-0.25** rotates **90 degrees t**o the right. |  |
| **Texture Feather Amount** | Determines how much feathering to enforce on the SDF texture's edges when GlowMax parameters are in use.  High values increase the amount of feathering and lower values decrease the amount of feathering. |  |

### Shadow Color

Determines the color of the texture shadow.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Shadow Glow Max** | Determines how much glow the texture shadow has.  Values closer to s**0** solidify the outline of the shape.  Values closer to 1 increase the shape’s outline glow. |  |
| **Shadow Offset X** | Determines the offset amount of the texture shadow along the **X-axis**.  Higher values move the shadow away from the texture.  Lower values move the shadow closer to the texture. |  |
| **Shadow Offset Y** | Determines the offset amount of the texture shadow along the **Y-axis**.  Higher values move the shadow away from the texture.  Lower values move the shadow closer to the texture. |  |
| **Shadow Opacity** | Determines the opacity of the texture shadow.  Values closer to **1** increase the opacity of the selected color.  Values closer to **0** decrease the opacity of the color. |  |
| **Shadow Rotation** | Rotate the texture shadow from the center.  A value of **0.25** rotates the texture shadow **90 degrees** to the left. |  |
| **Shadow Thickness** | Determines the thickness of the texture shadow.  Higher values increase the size of the shadowthickness.  Lower values decrease the thickness. |  |

### Stroke

Parameters that affect the appearance of the texture’s stroke.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Inner Stroke Color** | Determines the color of the texture’s inner stroke. |  |
| **Inner Stroke Glow Max** | Determines the maximum glow amount of the texture’s inner stroke.  InnerStrokeGlowMax is dependent on the **GlowMax** value. The maximum GlowMax value set determines the maximum glow value for InnerStrokeGlowMax and OuterStrokeGlowMax. |  |
| **Inner Stroke Thickness** | Determines the thickness of the inner stroke.  Higher values increase the thickness of the stroke and lower values reduce it. |  |
| **Inner Stroke Thickness Glow Max** | Determines the glow thickness of the texture’s inner stroke.  Higher values increase the glow thickness of the stroke and lower values reduce the glow thickness of the texture’s inner stroke.  InnerStrokeThicknessGlowMax is dependent on the **GlowMax** value. The maximum GlowMax value set determines the maximum glow value for InnerStrokeGlowMax, InnerStrokeThicknessGlowMax, and OuterStrokeGlowMax. |  |
| **Outer Stroke Color** | Determines the color of the outer stroke. |  |
| **Outer Stroke Glow Max** | Determines the glow amount of the texture’s outer stroke.  Values closer to **0** solidify the outline of the shape.  Values closer to **1** increase the shape’s outline glow.  OuterStrokeGlowMax is dependent on the **GlowMax** value. The maximum GlowMax value set determines the maximum glow value for InnerStrokeGlowMax, InnerStrokeThicknessGlowMax, and OuterStrokeGlowMax. |  |
| **Outer Stroke Thickness** | Determines the thickness of the texture’s outer stroke.  Higher values increase the thickness of the stroke and lower values reduce the thickness. |  |
| **Outer Stroke Thickness Glow Max** | Determines the glow thickness of the texture’s outer stroke.  Higher values increase the glow thickness of the stroke and lower values reduce it. |  |

## Texture Effects

Texture Effects has a number of customizable effects that can transform the appearance of the texture:

- Tile
- Warp
- Pixelate
- Bounce
- Halftone
- Stepped Gradient
- And more…

The parameters can be mixed and targeted with the [View Model](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#view-model) in [UMG](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/UMG?application_version=5.7) and in Verse code through Verse fields. Use the table below to learn more about the different parameters.

### Basic Texture

The basic parameters for the texture. Select a texture from the dropdown menu.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Texture** | Select a texture from the dropdown menu. |  |
| **Tiling X** | Tiles the texture along the **X-axis**.  A value of **1** does not tile the texture.  Values above **1** add tiles along the **X-axis**.  It’s best to use whole numbers for this parameter to have complete images. |  |
| **Tiling Y** | Tiles the texture along the **Y-axis**.  A value of **1** does not tile the texture.  Values above **1** add tiles to the texture along the **Y-axis**.  It’s best to use whole numbers for this parameter to have complete images |  |
| **Translate X** | Moves the texture along the **X-axis**.  You can animate the texture by targeting the **Translate X parameter** with Sequencer inside UMG. |  |
| **Translate Y** | Moves the texture along the **Y-axis**.  You can animate the texture by targeting the **Translate Y parameter** with Sequencer inside UMG. |  |
| **Translate Speed X** | Determines the speed of translation across the **X-axis**. |  |
| **Translate Speed Y** | Determines the speed of translation across the **Y-axis**. |  |

### Scaling

Parameters that provide a way to change the scale and size of the texture. Creates a pounding effect on the texture.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Is Scaling** | Determines the scaling effect on the texture.  This option is only visible when the other Scaling parameters are also in use. |  |
| **Scaling Maximum Speed** | Determines the maximum speed of the scaling effect on the texture. |  |
| **Scaling Minimum Speed** | Determines the minimum speed of the scaling effect on the texture. |  |
| **Start Size** | The texture’s size at the beginning of the animation. |  |
| **Middle Size** | The texture’s size in the middle of the animation. |  |
| **End Size** | The texture’s size at the end of the animation. |  |

### Warping

Parameters that provide a way to add a warping effect to the texture.

To alter the appearance of an icon, additional Warping parameters must be used along with the **IsWarping** parameter.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Is Warping** | Determines the amount of warping effect on the texture. |  |
| **Amplitude X** | Applies a stretching effect along the **X-axis**. |  |
| **Amplitude Y** | Applies a stretching effect along the **Y-axis**. |  |
| **Frequency X** | Applies a **Sine Wave** effect to the texture along the **X-axis**. |  |
| **Frequency Y** | Applies a **Sine Wave** effect to the texture along the **Y-axis**. |  |
| **Warp Speed** | Determines how fast the warp effect is on the texture. |  |

### Pixelate

Parameters that provide a way to pixelate the appearance of the texture.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Is Pixelated** | Adds a pixel effect to the texture.  A value of **0** does not apply the pixel effect to the texture.  A value of **1** completely pixelates the texture. |  |
| **Number of Pixels** | Determines the number of pixels the texture has.  A value of **1** turns the texture into a square. Adding more pixels creates a pixelated shape. |  |

### Bounce

Parameters that provide a way to add a bouncing effect to the texture.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Is Bouncing** | Determines the bounce rate of the effect.  This option is only visible when the other Bounce parameters are also in use. |  |
| **Bounce Speed** | Determines how fast the texture bounces. |  |
| **Bounce X** | Determines the amount of bounce effect to apply along the **X-axis**. |  |
| **Bounce Y** | Determines the amount of bounce effect to apply along the **Y-axis**. |  |

### Halftone

Parameters that produce a comic ink dot effect on the texture.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Is Halftone** | Determines whether the effect is in use and the opacity of the halftone effect.  Higher values increase the opacity of the effect, while lower values decrease the opacity of the effect. |  |
| **Dot Density** | Increases the density of dots in the effect.  Higher values increase the number of dots and reduces the size of the dots.  Lower values decrease the number of dots and increase the size of the dots. |  |
| **Dot Glow Max** | Determines the maximum amount of glow applied around the dots.  Positive values cause the dots to appear like stars, negative values cause the dots to appear as circles. |  |
| **Dot Glow Min** | Determines the minimum amount of glow around the dots.  The values can be used to switch the color of the background and dots. Values of **5 and higher** cause the effect to fade into one color. Similarly, values below **-7** cause the effect to fade into one color. |  |
| **Dot Max Size** | Determines the maximum size of the dots. |  |
| **Dot Min Size** | Determines the minimum size of the dots. |  |
| **Gradient Color 1** | Determines the primary color of the halftone effect. |  |
| **Gradient Color 2** | Determines the secondary color of the halftone effect. |  |
| **Halftone Pan Speed X** | Determines the speed the dots travel across the **X-axis**. |  |
| **Halftone Pan Speed Y** | Determines the speed the dots travel across the **Y-axis**. |  |
| **Halftone Rotation** | Rotates the direction the dots travel. |  |

### Stepped Gradient

Parameters that provide a way to add a stepped gradient to the texture.

These parameters are dependent upon the **Tint Color** parameters.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Is Stepped Gradient** | Determines if the stepped gradient effect is applied to the texture. |  |
| **Stepped Gradient Amount** | Determines the amount of stepped gradient to apply to the texture.  **IsSteppedGradient** must be enabled with a value below **1.0** for this parameter to work. |  |

### Tint Color

These parameters provide a way to add colors to the texture to create a gradient effect on the texture.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Tint Gradient Opacity** | Determines the opacity of the colors in the gradient.  Lower values decrease the texture’s opacity and higher values increase the material’s opacity. |  |
| **Tint Color 1** | Determines the first color in the gradient. |  |
| **Tint Color 1 Position** | Determines the position for the first color in the gradient.  This option only works when the **TintGradientOn** option is selected and a value set. |  |
| **Tint Color 2** | Determines the second color in the gradient. |  |
| **Tint Color 2 Position** | Determines the position for the second color in the gradient.  Higher values shift the gradient to start on the opposite side.  Lower values increase the appearance of the second color selection.  This option only works when the **Tint GradientOn** option is selected and a value set. |  |
| **Tint Color 3** | Determines the third color in the gradient. |  |
| **Tint Color 3 Position** | Determines the position for the second color in the gradient.  Higher values shift the gradient to start on the opposite side.  Lower values increase the appearance of the second color selection.  This option only works when the **TintGradientOn** option is selected and a value set. |  |
| **Tint Gradient On** | Determines whether the gradient effect is applied to the texture. |  |
| **Tint Gradient Rotation** | Rotates the direction of the gradient. |  |
| **Tint Radial Gradient** | Changes the gradient into a radial gradient. |  |
| **Tint Radial Gradient Size** | Determines the radial gradient size. |  |

### Alpha Color

Parameters that provide a way to add transparency, color, and gradient to a texture that has Alpha and .

These parameters work best on textures that have color, like a character picture, or a black and white texture.

[![An illustration that shows where the Alpha parameters have influence over the image or shape in the texture.](https://dev.epicgames.com/community/api/documentation/image/410f4fcf-ccf2-4b68-b2b7-f31aa6934344?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/410f4fcf-ccf2-4b68-b2b7-f31aa6934344?resizing_type=fit)

Alpha example

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Alpha Opacity** | Determines the opacity of the Alpha colors on the texture.  Lower values decrease the texture’s opacity and higher values increase the material’s opacity. |  |
| **Alpha Color 1** | Determines the first color in the gradient. |  |
| **Alpha Color 1 Position** | Determines the position for the first color in the gradient.  This option only works when the **AlphaGradientOn** option is selected and a value set. |  |
| **Alpha Color 2** | Determines the second color in the gradient. |  |
| **Alpha Color 2 Position** | Determines the position for the second color in the gradient.  Higher values shift the gradient to start on the opposite side.  Lower values increase the appearance of the second color selection.  This option only works when the **AlphaGradientOn** option is selected and a value set. |  |
| **Alpha Color 3** | Determines the third color in the gradient. |  |
| **Alpha Color 3 Position** | Determines the position for the third color in the gradient.  Higher values shift the gradient to start on the opposite side.  Lower values increase the appearance of the third color selection.  This option only works when the **AlphaGradientOn** option is selected and a value set. |  |
| **Alpha Gradient On** | Determines whether the gradient is applied to the texture. |  |
| **Alpha Gradient Rotation** | Rotates the direction of the gradient. |  |
| **Alpha Radial Gradient** | Turns the gradient into a radial gradient. |  |
| **Alpha Radial Gradient Size** | Determines the radial gradient size. |  |

## Texture Mask

Texture Mask uses parameters that can mask the icon or  player avatar and add outline elements to the icon or avatar image.

The Texture Mask material has a number of customizable parameters that you use with the View Model in UMG and in Verse code through Verse Fields. Use the table below to learn more about using the different parameters.

### Texture

Parameters that determine the appearance of the texture.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Texture** | Select a texture from the dropdown menu. |  |
| **Texture Alpha** | Determines the Alpha color of the texture.  The **1** value is white. Values **below 1** decrease the white value and blend with the background color. |  |
| **Texture Position X** | Positions the texture along the **X-axis**. |  |
| **Texture Position Y** | Positions the texture along the **Y-axis**. |  |
| **Texture Scale X** | Scales the texture along the **X-axis**. |  |
| **Texture Scale Y** | Scales the texture along the **Y-axis**. |  |

### Fill

Parameters that determine the look of the gradient applied to the background.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Custom Fill Texture** | Select a Fill Texture from the dropdown menu. |  |
| **Fill Alpha** | Determines the Alpha color of the mask.  The **1** value is white, values **below 1** decrease the white value and blend with the background color. |  |
| **Fill Color 1** | Determines the first color in the gradient. |  |
| **Fill Color 1 Gradient Position** | Determines the position for the first color in the gradient. |  |
| **Fill Color 2** | Determines the second color in the gradient. |  |
| **Fill Color 2 Gradient Position** | Determines the position for the second color in the gradient.  Higher values shift the gradient to start on the opposite side.  Lower values increase the appearance of the second color selection. |  |
| **Fill Color 3** | Determines the third color in the gradient. |  |
| **Fill Color 3 Gradient Position** | Determines the position for the third color in the gradient.  Higher values shift the gradient to start on the opposite side.  Lower values increase the appearance of the third color selection. |  |
| **Fill Color Radial Gradient Size** | Determines the size of the gradient on the background. |  |
| **Fill Gradient Type** | Changes the gradient type from radial to linear. |  |
| **Glow** | Determines the glow amount of the background. |  |
| **Linear Gradient Fill Rotation** | Rotates the gradient around a circle.  The LinearGradientFillRotation option is dependent on values set in the **FillGradientType** option. |  |
| **Shape** | Determines the shape of the mask around the texture. |  |
| **Shape Rotation** | Rotates the mask shape around the texture. |  |
| **Shape Size** | Determines the size of the mask shape around the texture. |  |
| **Bottom Left Corner Radius** | Changing this parameter adds a rounded corner to the bottom left corner based on the value used. |  |
| **Bottom Right Corner Radius** | Changing this parameter adds a rounded corner to the bottom right corner based on the value used. |  |
| **Top Left Corner Radius** | Changing this parameter adds a rounded corner to the top left corner based on the value used. |  |
| **Top Right Corner Radius** | Changing this parameter adds a rounded corner to the top right corner based on the value used. |  |

### Outline

Parameters that determine the appearance of the outline around the mask.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Gap Thickness** | Determines the gap size between the outline and the texture.  The GapThickness option is dependent on the **OutlineAlpha** option having a value set over **0.40**. |  |
| **Outline Alpha** | Determines the Alpha color of the outline.  The **1** value is the full alpha color, values **below 1** decrease the color value and blend into the background. |  |
| **Outline Color 1** | Determines the first color in the outline gradient. |  |
| **Outline Color 1 Position** | Determines the position for the first color in the outline gradient. |  |
| **Outline Color 2** | Determines the second color in the outline gradient. |  |
| **Outline Color 2 Position** | Determines the position for the second color in the outline gradient. |  |
| **Outline Color 3** | Determines the third color in the outline gradient. |  |
| **Outline Color 3 Position** | Determines the position for the third color in the outline gradient. |  |
| **Outline Thickness** | Determines the thickness of the outline. |  |

### Texture Mask

Parameters to change the appearance of the texture mask.

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Description** | **GIF** |
| **Show Mask Preview** | Determines the opacity of the mask preview.  A value of **0** means the preview is invisible, a value of **1** means the mask is completely visible.  This parameter is only visible when the **MaskWidth** and **MaskHeight** options have values higher than **0.0**. |  |
| **Mask Position X** | Position the mask along the **X-axis**. |  |
| **Mask Position Y** | Position the mask along the **Y-axis**. |  |
| **Mask Height** | Determines the height of the mask. |  |
| **Mask Width** | Determines the width of the mask. |  |

### Slant

Parameters that determine the degree of slant to apply to the background and mask outline.

|  |  |  |
| --- | --- | --- |
| **Parameter** | Description | **GIF** |
| **Slant X** | Slants the background and mask outline along the **X-axis**. |  |
| **Slant Y** | Slants the background and mask outline along the **Y-axis**. |  |
