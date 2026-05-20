## https://dev.epicgames.com/documentation/en-us/fortnite/lighting-starter-island-template-in-unreal-editor-for-fortnite

# Lighting Starter Island Template

Learn how to effectively use basic lighting and lighting concepts on your island.

![Lighting Starter Island Template](https://dev.epicgames.com/community/api/documentation/image/8c9ccbd7-c53c-464f-b67d-4bd38b174b31?resizing_type=fill&width=1920&height=335)

The **Lighting Starter Island template** shows how to use interior and exterior lighting as part of your level design to create a look and feel that is distinct from classic Fortnite.

This companion tutorial is designed to get you familiar with the different lighting actors and devices available in Unreal Editor for Fortnite (UEFN), as well as lighting concepts in general. All of the lighting techniques in this template take into consideration how to design lighting for multiple platforms.

Low-end platforms have different capabilities for lighting and do not use [Lumen](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#lumen) when rendering.

All lighting is packaged in the [Outliner](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#outliner-panel) so you can easily search and filter lights and [geometry](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#geometry) elements by room number. Each room has a complementary folder where you’ll find the lights, geometry, and other devices that populate the room.

Walk through the template building to see the most basic lighting elements available in UEFN, then learn how to use and implement lighting with a few basic examples designed to show how you can scale the complexity of your lighting as you move forward in your project.

[![The tutorial level in UEFN.](https://dev.epicgames.com/community/api/documentation/image/378969ac-25e1-4ecc-8153-d57fce90735d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/378969ac-25e1-4ecc-8153-d57fce90735d?resizing_type=fit)

You can find this template in the **Project Templates** section of the **Feature Examples** of the **Project Browser**.

Each room has bookmarks set up for you to view examples of what you can expect to learn. Press these keys to move throughout the island template:

- **1** - Room 1
- **2** - Room 2
- **3** - Room 3
- **4** - Room 4
- **5** - Room 5
- **6** - Room 5
- **7** - Room 5

Get started by pressing the 1 key to go to Room 1 and begin with the different lighting actors and their uses.

## Room 1 - The Basics

**Room 1** focuses on your [key lighting](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#key-light) first. Key lighting is the main source of light for your level or individual scene, which means you’re either starting with interior lighting or exterior lighting. There is no right answer, just personal preference.

**Interior Lighting:**

- If there are dark spaces, like Interior rooms or night scenes, start with artificial lighting. Think of it as your key light.

**Exterior Lighting:**

- Start with natural light as your key light if you’re working on exteriors or interior spaces with large windows that will be illuminated with sun and sky, then create your secondary lighting with artificial lights as needed.

Room 1 uses the three basic light actors, [Point Lights](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#point-light), Spot Lights, and [RectLights](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#rectangle-light) and demonstrates some of the ways they can be used.

The lighting in this room sets a Base Scale by focusing on:

### Lighting Actor - Rectangular Light

A **Rectangular light** (RectLight) provides a way to light a large area evenly and generate [diffuse shadows](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#diffuse-shadows) based on the area it covers. RectLights are great for imitating fluorescent ceiling lights and for studio lighting setups.

Select the light and take a look at the modified settings by clicking the Details panel settings (gear icon) and checking **Show Only Modified Properties**.

[![The rectangle light is selected in the scene.](https://dev.epicgames.com/community/api/documentation/image/f6565aac-0526-4da0-a0e1-ff4aa5895f84?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f6565aac-0526-4da0-a0e1-ff4aa5895f84?resizing_type=fit)

*Click image to enlarge.*

Note that not many settings were adjusted. The focus was to set a base lighting intensity in a completely dark room with the following setting adjustments:

- **Intensity** - 0.5.
- **Source** - Width and Height. (The light’s size dictates how sharp or smooth the shadows are.) Remember, this setting will also affect the [specular reflection](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#specular) and highlights like shown below.
- **Barn Door Angle and Length** - The barn door function is useful if you want to limit the direction of the light as though you were working with studio lights.
- **Temperature** - This controls the [color](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#color-temperature) of your light.

  Try changing the temperature to **3000** K. Notice how it becomes warmer (more yellow), then change it to **8000** K and notice how it becomes cooler (more blue).
- **Volumetric Shadow** is enabled to stop the light volume effect from leaking outside of the room and shining through the walls. This also enables the volumetric effect to be occluded by objects that cast shadows.

### Lighting Actor - SpotLight

A spotlight focuses light to a specific area or spot. In this room there are two spotlights. One points to a few colored static spheres and the other to a rotating mesh so you can see how the shadows interact with the lighting actor.

[![The spot light uses slightly more settings to control the light.](https://dev.epicgames.com/community/api/documentation/image/9e4068cf-0eb4-4958-a1a8-4871522ec3e1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e4068cf-0eb4-4958-a1a8-4871522ec3e1?resizing_type=fit)

Select the spotlight over the colored spheres, then check **Show only Modified Properties** from the Details panel to view only the adjusted settings.

- **Intensity** - Notice how these lights require more intensity than the area light (rectangle light). This is based on the light size. Since this is a smaller light, it requires more intensity to light the scene.
- **Inner Cone Angle and Outer Cone Angle** - These settings allow you to decide how wide and focused the illuminated area will be. Adjust the outer cone first, then the inner cone.

  Start with **60** for the Outer Cone Angle and **30** for Inner Cone Angle, then try different cone angles to see how the light changes.
- **Source Radius** - This is the size of the light. A larger radius means softer shadows, but this also means larger specular reflections. Use a size that is consistent with the mesh used as the light source, like with the Rectangular Light Area.
- **Temperature** - The light is warmer than the RectLight at **3800** K.
- **Volumetric Shadows** - This setting is enabled to show a bit of atmosphere inside the room.

  [![Volumetric Shadows are enabled to show how the spotlight creates an effect of fog or atmosphere.](https://dev.epicgames.com/community/api/documentation/image/1db8967b-e931-4637-acfd-083cd5fbde14?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1db8967b-e931-4637-acfd-083cd5fbde14?resizing_type=fit)

Select **SpotLight6**. Notice how the **Temperature** is set to **5500,** making it appear white. It also shows a lot more fog because the **Volumetric Scattering Intensity** is increased to **4** from the default value of **1**.

### Lighting Actor - Point Light

[Point lights](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#point-light) emit light from a single point in all directions, like a lightbulb would. In this case, a point light act like the light source of a table lamp with a shade. The point light glows from inside like a lightbulb in a large light fixture.

[![Like the spotlight, a point light uses slightly more settings to control the light.](https://dev.epicgames.com/community/api/documentation/image/1d598498-426d-47e3-92b1-395a7583fe9f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d598498-426d-47e3-92b1-395a7583fe9f?resizing_type=fit)

Select the lights and play with the modified settings.

- **Intensity** - This setting is the same as in the spotlight, we made the two match to establish our base lighting intensity.
- **Attenuation** - Use this setting to limit the distance the light reaches in all directions. While not physically accurate, it's very useful to achieve a specific look.

Both Spotlight and PointLight have a setting called **Inverse Square**, enabled by default. This means the light will decay with distance as it does in real life. Start with the default Inverse Square setting and then play with the Attenuation to see how the light changes.

- **Source Radius** - This setting dictates the actual size of the light source — the larger the size, the softer the shadows, and vice versa. Keep the setting relative to the size of the fixture you create.

  Remember that this light shows in specular reflections, so if you have a larger than necessary radius, it will look weird in the reflections because there will be a discrepancy between the light fixture and the light itself.

The last example is a point light with a self-illuminating sphere. While this is a bit unnecessary with high-end hardware, you’ll need a light source and the sphere in lower-end platforms to fake the glow of the sphere. Also, the self-illuminating material on its own with Lumen will not generate sharp shadows if that’s the look you’re trying to achieve.

[![The high-end looking glowing sphere.](https://dev.epicgames.com/community/api/documentation/image/ff950fad-d1ad-4310-b2dc-efeb2e27aaa9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff950fad-d1ad-4310-b2dc-efeb2e27aaa9?resizing_type=fit)

*This sphere works with high-end platforms. Note how it produces a warm glow and deep shadows.*

[![The high-end looking glowing sphere.](https://dev.epicgames.com/community/api/documentation/image/4d6d30df-8172-4ae2-bdab-9a800c218ba2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d6d30df-8172-4ae2-bdab-9a800c218ba2?resizing_type=fit)

*This sphere works with low-end platforms. Note how it produces a cool glow and softer shadows.*

Select **PointLight** and hide it so you can see how the shadows and light effect changes. This is important to the success of your lighting if you’re planning lighting across multiple platforms.

If you have a light fixture that needs to cast light and shadow, then you’ll need the two elements — a fixture with a self-illuminating material and the light itself.

Consider everything covered in these three examples so that you don't stumble upon issues down the road once your map lighting gets more complex.

Remember that the goal is to establish a starting point for base lighting using a simple combination of settings that you can repeat in your scenes as they get more complex. The fewer settings you modify, the easier it will be later to adjust them.

Following this philosophy, everything in this small room was reused and multiplied in subsequent rooms, from geometry and materials, to lights. Small incremental steps are essential to success.

Press the **2 key** to go to Room 2. Here you will learn how to implement the lighting actors.

## Room 2 - Implementing the Basics

You should now understand how to set up basic lighting using the three lighting actors (spot, point, and rectangle) to establish a base for light Intensities, Temperature, and Reach with each one.

In the second room, all the lessons learned in Room 1 are applied to light a long corridor scene.

[![The corridor expands upon the lighting actors from Room 2by introducing lighting concepts to the scene.](https://dev.epicgames.com/community/api/documentation/image/8be42694-ac9b-44d6-8ae9-71c85b7bfb76?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8be42694-ac9b-44d6-8ae9-71c85b7bfb76?resizing_type=fit)

The goal in lighting the corridor is to create a lighting scenario that looks like something from real life. To accomplish this, you’ll use what you learned in Room 1 and add:

Look for a folder called **Sequences** and select **LS_OpenDoor**.

### The Corridor

Position the camera in front of the doors and play the sequence.

The corridor reuses the same lights and principles from Room 1 to achieve a more realistic look in a simple, [custom modeled corridor](https://dev.epicgames.com/documentation/fortnite/architectural-modeling-guidelines-in-unreal-editor-for-fortnite). The lighting adds a layer of realism to the environment using the lights to add Hierarchy, Rhythm, Light and Shadow to the scene.

### Hierarchy

Spotlights are the [key lights](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#key-light) here. For this particular scene, spotlights have the strongest intensity and are meant to light characters as they walk down the hall.

[RectLights](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#rectangle-light) are secondary lights, and are meant to [fill](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#fill-light) only, meaning that these lights support the spot lights by softening shadows created by the spotlights. Note how the rectangle lights are a cooler temperature compared to the spotlights (this is an artistic choice) but an important distinction.

[Point lights](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#point-light) are tertiary and used as accent lighting with a green colored light to draw your attention to the door at the end of the corridor.

Notice how Hierarchy is also used to assign materials to the architectural assets. The lighter material of the walls counters the weight of the darker floor material.

The materials also take into consideration that all lights are pointing down, the cove lighting and light fixtures on the ceiling balance the room with more geometric complexity and light fixtures at the top.

### Rhythm

There is already a certain scale and rhythm to the corridor due to the nature of the paneling and scale of these architectural assets.

See how the [scalloping](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#scalloping) created by the spotlights on the walls adds an extra dimension to the otherwise simple, flat material. Add a bit of reflection to the walls and you have a space that looks more "finished", when in reality each wall panel is a box with a chamfered edge and basic material applied to it.

[![An example of light scalloping on the wall.](https://dev.epicgames.com/community/api/documentation/image/a54718c5-2474-4b35-89ac-3d783ad0a1e1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a54718c5-2474-4b35-89ac-3d783ad0a1e1?resizing_type=fit)

### Light and Shadow

Always have both light and shadow in your project. Without shadows, you’ll have a flat-looking scene. Make sure your scene works with your key lights only. This way, the rest of the lights are just accents that add more dimension to the scene.

[![An example of shadow lighting.](https://dev.epicgames.com/community/api/documentation/image/a5d909a7-1ae6-4cbd-a5e9-ccd6f72f25b9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a5d909a7-1ae6-4cbd-a5e9-ccd6f72f25b9?resizing_type=fit)

In the slider image below, the image on the left uses only the spotlights to create light in the scene, while in the image on the right, accent lighting is added with RectLights. The difference is small but effective.

![Only the SpotLights are turned on.](https://dev.epicgames.com/community/api/documentation/image/eae62654-c4e1-4247-b65f-44995880e96e?resizing_type=fit&width=1920&height=1080)

![The RectLights are turned on and used as accent lighting.](https://dev.epicgames.com/community/api/documentation/image/282dc9fa-f2e0-4395-98ea-72ccf42d3fc7?resizing_type=fit&width=1920&height=1080)

Don't try to overfill your scene with light. Doing so causes a flat scene that loses depth which in turn causes flat characters.

All geometry in Room 2 was generated using [modeling tools](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite) in UEFN. All [materials](https://dev.epicgames.com/documentation/fortnite/material-library-in-unreal-editor-for-fortnite) are Material Instances of some basic Fortnite materials that you can customize.

Hierarchy, rhythm, light and shadow are basic lighting principles to keep in mind when starting to create lighting for your game. In the next room you’ll learn more about the Customizable Light device in UEFN and how to use this device in your project.

Press the **3 key** to go to Room 3. In this room you will learn how to use the Customizable Light device.

## Room 3 - Customizable Light Devices

The [**Customizable Light** device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-customizable-light-devices-in-fortnite-creative) is a light source that can be turned on or off by player interaction, or by signals sent from devices. You can choose to use the device as a point light or a spot light. With the Customizable Light, there is no associated prop (like a street lamp or overhead light) that represents the source of the light.

In this room prop lights are used alongside the Customizable Light device to show the two options side-by-side. Here, the light device demonstrates one of the features it’s capable of, color switching. Select any of the Customizable Lights in Room 3 and experiment with the adjusted settings.

You’ll notice that adjusting this device means you can use it as either a **Point Light** or a **Spot Light**. Both lighting types have the same capabilities and functionality with the only difference being the light’s effect on the scene.

Since this device does not have a light fixture, you’ll have to create your own or use one of the Fortnite props that doesn’t have a light actor attached.

Some lights in the Fortnite prop gallery have an attached light actor, while others do not. In the image below, light props from the **Alternate Lights Prop Gallery** show a series of the same light with and without a light actor attached.

[![Shelters Light prop from Fortnite Creative.](https://dev.epicgames.com/community/api/documentation/image/33469b0f-66a8-4816-b2c0-48004a03a4e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/33469b0f-66a8-4816-b2c0-48004a03a4e0?resizing_type=fit)

The Details panel is different for the Customizable Light from traditional lighting actors. This is because devices are designed and optimized to make them ready to work with the [Direct Event Binding system](https://dev.epicgames.com/documentation/fortnite/direct-event-binding-in-unreal-editor-for-fortnite), which interacts with other devices in your game.

Intensity, Color, Attenuation, and Source Radius will behave the same way as with the light actors used in Rooms 1 and 2.

The reflection intensity demonstrated in this example is one of the many advantages of light devices. These devices simplify light control and its interaction with the game. In this example, notice how easily the light reflection or [specular reflection](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#specular) can be adjusted.

In Room 1, you were advised to make the light area size relative to the actual fixture since the light size shows up in reflections and specular highlights. In this case, you can completely disable reflection settings and use the light just for the effect of lighting if you want to use a fixture for reflections.

In the advanced panel, you’ll find presets for the light behavior. There are three Customizable Lights acting as point lights with their initial state as **enabled**. These lights can be dimmed and undimmed by pressing the buttons labeled for each light type.

Two Customizable Lights acting as spot lights with **Party** and **Flicker** modes are connected to a simple On/Off **Button** device.

[![Two Customizable Lights acting as spot lights with **Party** and **Flicker** modes are connected to a simple On/Off **Button **device.](https://dev.epicgames.com/community/api/documentation/image/8637f185-88a3-4110-a957-8261c909015a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8637f185-88a3-4110-a957-8261c909015a?resizing_type=fit)

At this point, you should be familiar with the Customizable Light device, lighting hierarchy, and how to establish base lighting. The lighting in Rooms 1 and 2 address interior artificial lighting. In the next section, you’ll learn how to add natural light to the mix with the [Environment Light Rig](https://dev.epicgames.com/documentation/fortnite/environment-light-rig-device-in-unreal-editor-for-fortnite).

Press the **4 key** to move to the next room. Discover how to effectively use the Environment Light Rig device to create indoor and outdoor lighting, as well as use the light actors to create ambient lighting.

## Room 4 - Environment Light Rig

The [Environment Light Rig](https://dev.epicgames.com/documentation/fortnite/environment-light-rig-device-in-unreal-editor-for-fortnite) is a powerful device that is heavily customizable.

This device allows you to design your exterior lighting. Like all Fortnite devices, the Environment Light Rig makes your life easier by combining multiple individual components and [direct event binding](https://dev.epicgames.com/documentation/fortnite/direct-event-binding-in-unreal-editor-for-fortnite) options to make the device work in your project.

[![An example of exterior lighting.](https://dev.epicgames.com/community/api/documentation/image/81f1cb5a-0ceb-4f4e-af2d-7f5f9382abff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81f1cb5a-0ceb-4f4e-af2d-7f5f9382abff?resizing_type=fit)

Select the Environment Light Rig, you’ll see it has options for:

- **Directional Light** (SunLight)
- **Skylight** (SkyLight)
- **SkyAtmosphere** (The actual sky you see rendered)
- **Exponential Height Fog** (Fog)
- **Post Processing for Lumen** and **Non-Lumen**
- **Color Grading**

To adjust the device, all you need to do is rotate the gizmo and see how the lighting changes in the room.

### Directional Light (SunLight)

With these settings, you’re able to control color, intensity, shadow smoothness, and temperature just like you can with most lights. In this template, most settings were left at their defaults as the default settings already work efficiently.

[![An example of Directional Lighting in exteriors.](https://dev.epicgames.com/community/api/documentation/image/7ecb5e96-49ab-4c1a-b909-191f66875d2b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ecb5e96-49ab-4c1a-b909-191f66875d2b?resizing_type=fit)

### Skylight (SkyLight)

You can think of your skylight as the [fill light](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#fill-light) for the environment. For high-end PCs or consoles, the Environmental Light Rig can be used with **Real Time Capture** enabled because these machines can render the environment lighting without any issues. In lower-end consoles, it’s recommended to use a [cubemap](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#cubemap), as real-time capture can be resource-intensive.

If you enable **Show Only Modified Properties** in the Details panel, you’ll see that the intensity of the sky is decreased from the default setting (1) to **.2**. This achieves a good middle ground for this particular scene and at this intensity it works for Lumen and Non Lumen capable devices.

Turn off **Show Only Modified Properties** and you’ll see that a cubemap is loaded even though Real-Time Capture is enabled. A cubemap needs to be loaded so that the Environment Light Rig can automatically switch to it in a low end device.

You can further customize the Skylight intensity to work across platforms using **Engine Scalability Settings**. Use the scalability settings to get a sense of what the scene will look like on low-end devices, this will allow you to further adjust the cubemap intensity or colors if needed for your ambient lighting.

[![The engine scalability settings help set a performance baseline for different platforms.](https://dev.epicgames.com/community/api/documentation/image/bab5928d-18da-4829-bdb4-d66a0181eb9c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bab5928d-18da-4829-bdb4-d66a0181eb9c?resizing_type=fit)

If you aren’t using a cubemap, interiors seem darker and ceilings appear black.

For this particular scene, the artistic choice was to create a good middle ground to show off the Environment Light Rig Skylight capability — enough to work well with high-end and low-end hardware.

### SkyAtmosphere (The actual sky you see rendered)

Many SkyAtmosphere settings are designed to modify the time of day, which affects how the scene looks, but be aware that there will be more inconsistencies between console scalability.

The colors of this component are driven by many factors and are based on how the atmosphere reacts to direct light and skylight. So, while you can adjust these settings for art direction purposes, be mindful that the more settings you adjust the more complex your lighting across devices will be.

Once you get familiar with the tools of this setting, you can experiment with different settings.

[![An example of Skylight being used as fil lighting.](https://dev.epicgames.com/community/api/documentation/image/51f0cb4e-fd33-4b64-9580-f2efe558a642?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51f0cb4e-fd33-4b64-9580-f2efe558a642?resizing_type=fit)

### Exponential Height Fog (Fog)

The only setting modified was **Intensity**. The setting was adjusted slightly higher than the default of **.01** to **.03**. This slight adjustment means you can see more of the environment fog and atmosphere in the scene.

Again, there are many settings on this component that can drastically change the look of your scene, like the **Fog Inscattering Color**, **Sky Atmosphere Ambient Color**, and **Opacity**.

Achieve the look you’re going for by changing as few variables and settings as possible with the light colors and temperatures. Only if necessary should you push the settings a bit further.

The less you adjust, the easier it will be to troubleshoot the look of your scene down the road.

### Post Processing Volumes

The Environment Light Rig has three Post Processing Volumes inside its component list. These are crucial to your look on lower-end scalability devices or consoles.

**Color Grading** - This affects your scene in any scalability mode — you can focus your color grading or look with this setting. Use Color Grading if you have certain effects shared throughout your different scalability, such as Chromatic Aberration, Vignetting, Sharpness, and Contrast.

**LumenExposure** - This setting works automatically on **High** and **Epic** Scalabilities.

**BasicExposure** - This setting works automatically on **Low** and **Medium** Scalabilities.

In this room, the Lumen Exposure and Basic Exposure settings were used to control the [white balance](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#white-balance) in Low and Medium scalability for a similar overall effect. Since Low and Medium don’t have Lumen Global Illumination, no light bounces around the scene, and looks different even with the same settings.

See the white balance examples below based on scalability below.

[![Medium Scalability with Default White balance](https://dev.epicgames.com/community/api/documentation/image/27c8ba22-a8c5-431b-832d-6d7f2c9d8686?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27c8ba22-a8c5-431b-832d-6d7f2c9d8686?resizing_type=fit)

*Medium Scalability with Default White balance*

[![High Scalability with Default White balance](https://dev.epicgames.com/community/api/documentation/image/dc54514e-b657-4363-a7ca-ef70ea1c9011?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc54514e-b657-4363-a7ca-ef70ea1c9011?resizing_type=fit)

*High Scalability with Default White balance*

[![Medium Scalability with Adjusted White Balance](https://dev.epicgames.com/community/api/documentation/image/ef1063e4-96b1-42e7-8b40-63954d2fa1f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef1063e4-96b1-42e7-8b40-63954d2fa1f8?resizing_type=fit)

*High Scalability with adjusted White balance*

As you develop the lighting for your scene, you’ll be able to use these three post-process volumes inside the Environment Light Rig to compensate for inconsistencies between low-end and high-end devices.

Remember to start small. Go for the general settings first, and keep adjusting as necessary when there are drastic changes in look and feel.

Press the **5 key** to go to Room 5. In the last room you will learn how to combine your knowledge of the Environment Light Rig with the Customizable Light device to create unique exterior lighting.

## Room 5 - Exterior Customizable Light Device

In this outside area, the balanced light actors are applied to the scene as accent lighting and natural lighting and atmosphere are introduced to the room. In the GIF below, the natural light filters in through the trellis above.

Compare how all of these lighting elements look in a more open space. The last two spaces in this room are semi-open spaces with reflective surfaces, and an open space at a larger scale.

[![An example of using different lighting sources outside.](https://dev.epicgames.com/community/api/documentation/image/7288ea32-2254-4f20-bedf-319316f71c82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7288ea32-2254-4f20-bedf-319316f71c82?resizing_type=fit)

Select one of the Customizable Light devices that are blowing in the wind. As you learned in [Room 3](https://dev.epicgames.com/documentation/fortnite/lighting-starter-island-template-in-unreal-editor-for-fortnite), these lights have numerous options that readily give your project a fixed starting point.

One of the options is **Windy**, but this is just a light device without a mesh, so when you playtest the level, all you see is a light that moves but with no light source.

Using the UEFN [modeling tools](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite), a rudimentary lantern was made by creating a cylinder and modeling more details around the base shape. Afterward, two materials were applied to the lanterns that were already in use throughout all rooms.

Last, the UVW mapping tools were used to adjust the gradient used to fake the light brightness at the edges of the lantern. The same principle used here was that used on the sphere in Room 1, but more complexity and detail were added to the lanterns than the spheres.

[![An example of how all the different lighting looks together.](https://dev.epicgames.com/community/api/documentation/image/4973dcb1-c798-432d-898a-e10d92363edb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4973dcb1-c798-432d-898a-e10d92363edb?resizing_type=fit)

Once you have your custom light fixture, you can add it as a component to the hierarchy on the Customizable Light device so that it animates the same way the light is being animated in the Windy mode.

## Exterior - Lighting Scalability Manager

**Lighting Scalability Manager** is the last step to this tutorial. You’ll learn how to use the Light Scalability Manager to spawn a custom skysphere for lower-end hardware that can't render all the same effects for the sky that the Environmental Light Rig is capable of on its own.

[![Control how your lighting looks on low-end platforms with the Light Scalability manager.](https://dev.epicgames.com/community/api/documentation/image/0d46765d-fbba-42a1-9502-e835ef96ef5d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d46765d-fbba-42a1-9502-e835ef96ef5d?resizing_type=fit)

A special material was created to capture the sky colors as the sun moves.

[![An example of a custom sky material.](https://dev.epicgames.com/community/api/documentation/image/40f45d2a-db87-4309-a244-00aa193fdbef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40f45d2a-db87-4309-a244-00aa193fdbef?resizing_type=fit)

The Lighting Scalability Manager was used to enable or disable specific geometry, lights, or materials that work within lower-end platforms. This is particularly useful if you want to have a completely separate set of lights to light your scene for low-end platforms.

[![A view of the gardens with the environmental lighting rig lighting the entire project exterior.](https://dev.epicgames.com/community/api/documentation/image/75b40725-3b86-4a55-849e-f996d6b70b1d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75b40725-3b86-4a55-849e-f996d6b70b1d?resizing_type=fit)

## Things to Keep in Mind

- Think about light and shadow first. Ask yourself where the direct lighting comes from.
- Think about color and temperature second. Literally think about the exterior and interior scene temperature and what it should feel like; cold, warm, hot, or humid. This will help you decide which colors to use.
- Consider what complmentary environmental details you need for your scene, like Fog, Clouds, and Sky.
- You can use subtle post effects like chromatic aberration, vignetting, and bloom to effectively add depth and dimension to your lighting and scene.
- Pay close attention to the important priorities of your Environmental Light Rig device, Post process volumes, or Lumen Exposure Manager Post Process Volumes.
- Always check how your project looks in all scalabilities to make sure you aren’t diverting too much from the high-end look.
- Be bold with your changes, if you design your project with small linear increments you won’t notice the differences between settings and will most likely end up with a flat looking scene that you won't know how to fix. A drastic change allows you to find your limits then find that middle ground that works for your project. Use this approach to get faster results with the fewest changes to settings.
