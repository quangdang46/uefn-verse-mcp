## https://dev.epicgames.com/documentation/en-us/fortnite/conversion-function-setting-material-parameters-in-umg-in-unreal-editor-for-fortnite

# Conversion Function: Setting Material Parameters in UMG

Use dynamic materials to create custom UI in UMG.

![Conversion Function: Setting Material Parameters in UMG](https://dev.epicgames.com/community/api/documentation/image/7140987a-4320-4ab7-a6b7-b5ad66e488a7?resizing_type=fill&width=1920&height=335)

Create dynamic UI with changing materials that update based on gameplay events and data. To make your UI dynamic, you need to use a combination of UI materials, View Bindings, and three of the **Set Material Parameter** conversion functions (Set Texture, Scalar, and Vector Parameter).

In **Unreal Editor for Fortnite** (UEFN) you’re given a basic Material with a number of Parameters. Use the **[Tracker device](https://dev.epicgames.com/documentation/fortnite/using-tracker-devices-in-fortnite-creative)** to track eliminations in a progress bar style widget as an example of a material that dynamically updates based on your progression in eliminating enemies.

## Create a Material Instance

For more information about material instances, refer to **[Creating and Using Material Instances](https://dev.epicgames.com/documentation/fortnite/creating-custom-ui-with-material-instances-in-unreal-editor-for-fortnite)** in Unreal Engine documentation.

All assets used to create these material instances can be found natively in UEFN. To learn how to make the material in this example, refer to **[Meter Material](https://dev.epicgames.com/documentation/fortnite/meter-material-in-unreal-editor-for-fortnite)** in the [Material tutorials](https://dev.epicgames.com/documentation/fortnite/ui-materials-in-unreal-editor-for-fortnite) section.

Icons can be found under the **Fortnite** folder in **Textures** > **Icons**.

## Setting Up the Tracker Widget

You'll create a custom Tracker widget in UMG that can be referenced in the Tracker device and track the players eliminations in the custom elimination UI.

1. Right-click in the **Content Browser** and select **User Interface** > **Widget Blueprint** > **User Widget**.

   [![Right-click in the Content Browser and select User Interface > Widget Blueprint > User Widget.](https://dev.epicgames.com/community/api/documentation/image/38137611-ce54-4d5b-9f62-81398e32cc1c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38137611-ce54-4d5b-9f62-81398e32cc1c?resizing_type=fit)
2. Make a simple Tracker widget that shows the Tracker Material and a Tracker title like in the example below.

   [![The Tracker widget shows the Tracker Material and a Tracker title.](https://dev.epicgames.com/community/api/documentation/image/6cb92886-4005-47ff-a59d-598473ae26fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cb92886-4005-47ff-a59d-598473ae26fa?resizing_type=fit)
3. Drag an **Overlay** into the widgetgraph. This layers all the pieces that make up the widget. It also provides a way for you to determine where on the screen this widget appears.

   [![](https://dev.epicgames.com/community/api/documentation/image/7871d5cd-3b56-4eb6-861b-6bb579615b90?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7871d5cd-3b56-4eb6-861b-6bb579615b90?resizing_type=fit)
4. Nest a **Stack Box** inside the **Overlay** so you can lay out the **Tracker Material** and Title left-to-right.

   [![Nest a Stack Box inside the Overlay.](https://dev.epicgames.com/community/api/documentation/image/ae5f7dff-dd89-49ce-a528-00bca3cebd77?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae5f7dff-dd89-49ce-a528-00bca3cebd77?resizing_type=fit)
5. Nest an **Overlay** inside the **Stack Box** so you can create a **Tracker Material** to overlay the Stack Box with a simple dark background.

   [![Nest an Overlay inside the Stack Box.](https://dev.epicgames.com/community/api/documentation/image/f83e673c-4b0e-4816-a91f-eba4c9f93ff5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f83e673c-4b0e-4816-a91f-eba4c9f93ff5?resizing_type=fit)
6. Inside the **Overlay**, nest two **Image** widgets. Press **F2** to rename them **TrackerBackground** and **TrackerMaterial**.

   [![Inside the Overlay, add two Image widgets.](https://dev.epicgames.com/community/api/documentation/image/042eb5b5-9f2a-45bf-9df0-badc6d26fcba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/042eb5b5-9f2a-45bf-9df0-badc6d26fcba?resizing_type=fit)
7. Select **TrackMaterial** to open its options in the **Details** panel. From the **Details** panel, select **Brush** > **Image** and look for the **MI_TrackerExample** material you created.

   [![Select TrackMaterial to open its options in the Details panel. From the Details panel, select Brush > Image and look for MI_TrackerExample you created.](https://dev.epicgames.com/community/api/documentation/image/b2c8e1e5-fc6e-4e44-a7cc-a2fc8fda2eb2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2c8e1e5-fc6e-4e44-a7cc-a2fc8fda2eb2?resizing_type=fit)
8. Set the **Image Size** below to **X=96.0**, **Y=96.0**. It should be large enough to be seen in-game.

   [![Set the Image Size below to X=96.0, Y=96.0. It should be large enough to be seen in-game.](https://dev.epicgames.com/community/api/documentation/image/099a5f5d-f35d-4daf-9a67-a36c6c12d5f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/099a5f5d-f35d-4daf-9a67-a36c6c12d5f3?resizing_type=fit)

   Now that the Tracker material is set up, you need to create the background for the material so the Track material is more readable.
9. Select **TrackerBacking**, and in the **Hierarchy**, then from the **Details** panel select **Brush** > **Draw As** > **Rounded Box**.

   [![Select TrackerBacking, and in the Hierarchy, then from the Details panel select Brush > Draw As > Rounded Box.](https://dev.epicgames.com/community/api/documentation/image/cb10b770-3568-44d9-a15f-6d80a82deee5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb10b770-3568-44d9-a15f-6d80a82deee5?resizing_type=fit)
10. Set the **Tint** option above to a neutral color for better readability. In this example, the tint was set to **3A3A3AFF** in the **Hex sRGB** field.

    [![Select a color for the Tinit option.](https://dev.epicgames.com/community/api/documentation/image/c2e9d692-8128-4500-bbad-c286ab0d1c9f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2e9d692-8128-4500-bbad-c286ab0d1c9f?resizing_type=fit)
11. Set the **Horizontal Alignment** and **Vertical Alignment** options to **Fill**. This ensures TrackerBacking fills the container that holds the TrackerMaterial.

    [![Set the Horizontal Alignment and Vertical Alignment options to Fill.](https://dev.epicgames.com/community/api/documentation/image/cac8c4e3-fdfb-4c64-884c-baa24c777fd7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cac8c4e3-fdfb-4c64-884c-baa24c777fd7?resizing_type=fit)

Now you have a background for your **TrackerMaterial** that looks easily readable on any in-game scene!

[![The background for the Trackermaterial is set up.](https://dev.epicgames.com/community/api/documentation/image/bf3736a9-486b-49ab-a610-fa89b4ddbf33?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf3736a9-486b-49ab-a610-fa89b4ddbf33?resizing_type=fit)

## Setting Up the Tracker Text

After the Tracker material is referenced in the Tracker widget, you'll set up text that informs the player what is being tracked in the UI.

Once all the final design touches are complete, you should have the **TrackerMaterial** and **TrackerTitle** set up.

[![Tracker Text is set.](https://dev.epicgames.com/community/api/documentation/image/20f5765b-212b-44ab-abee-53e1564e3fb1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20f5765b-212b-44ab-abee-53e1564e3fb1?resizing_type=fit)

To add some space between both items, add padding on the Right to the Overlay containing the TrackerMaterial:

Space is added between the image and the text.

[![Add some space between both items with padding.](https://dev.epicgames.com/community/api/documentation/image/8df372de-b9d3-4332-aeaa-6ddc4edf997a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8df372de-b9d3-4332-aeaa-6ddc4edf997a?resizing_type=fit)

If you want to easily modify spacing between multiple objects, you can insert an Image widget into the Stack Box that holds these objects, set the Image Size X to however much space you want, and set it to Draw As None. What happens is the Image doesn’t show up but it still takes up space in your Stack Box!

It makes it easier to manage spacing between objects and not hunt down Paddings in each widget.

[![](https://dev.epicgames.com/community/api/documentation/image/76977bb6-0c28-4d5b-be0e-02b4bb9c3054?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76977bb6-0c28-4d5b-be0e-02b4bb9c3054?resizing_type=fit)

## Setting up Set Material Parameters

Next you'll bind the values of the Tracker device to the material parameters in the Tracker widget.

### Adding a Viewmodel

You’re ready to start binding the data from the Tracker to manipulate your widget.

### Set Scalar Parameter

A **Scalar Parameter** takes in an **Int** or **Float** value. For example, the progress bar fills with the TrackerMaterial based on how many eliminations you have in the Tracker.

The Material is set up to convert the number of Eliminations from the Tracker device to fill up the TrackerMaterial. All you have to do is bind that data to the Progress material parameter in MI_TrackerExample.

![Early eliminations in the tracker](https://dev.epicgames.com/community/api/documentation/image/5d6b5f26-b121-4c96-86e6-0cec955e93e3?resizing_type=fit&width=1920&height=1080)

![Almost full elimination tracker](https://dev.epicgames.com/community/api/documentation/image/ac89ef9d-cc84-49f8-84f2-eaf68ee5f5b4?resizing_type=fit&width=1920&height=1080)

A Progress of 3.0 vs 8.0 in MI_TrackerExample. This is very handy!

You now have your current Tracker progress feeding directly into your material! The Tracker Material will slowly fill up when the player assigned to the Tracker gets an elimination!

[![](https://dev.epicgames.com/community/api/documentation/image/34cd07cd-c747-4097-a446-1ad7a9ebe9c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34cd07cd-c747-4097-a446-1ad7a9ebe9c3?resizing_type=fit)

### Set Vector Parameter

A Vector Parameter takes in a Vector4 value. Vectors are typically used for colors - RGBA (the four vectors), you’re going to use a Vector4 to change your icon color based on what is set up in the device.

For more information about Vectors, refer to **[Vector Material Expressions](https://dev.epicgames.com/documentation/unreal-engine/vector-material-expressions-in-unreal-engine?application_version=5.5)** in Unreal Engine documentation.

Whatever Icon Color that’s set on the Tracker device is passed to your material. If you want an orange icon, just set it on the device and it will color it for you! The material used in this example is already set up for that.

[![Whatever Icon Color that’s set on the Tracker device is passed to your material.](https://dev.epicgames.com/community/api/documentation/image/d6715fb1-9fbd-48db-92a4-99a6cf48eda0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6715fb1-9fbd-48db-92a4-99a6cf48eda0?resizing_type=fit)

### Set Texture Parameter

A Texture Parameter takes in a Texture2D value. Textures are typically used for images or icons, so we’re going to use it to change our icon based on what’s set up in the device!

For more information about Textures, refer to **[Textures](https://dev.epicgames.com/documentation/unreal-engine/textures-in-unreal-engine?application_version=5.5)** in Unreal Engine documentation.

The Texture Parameter is set. Now whatever icon is set in your Tracker device will pass it into the widget!

[![Whatever Icon Color that’s set on the Tracker device is passed to your material.](https://dev.epicgames.com/community/api/documentation/image/ca71b659-aff9-41e9-89b5-29046b90012e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca71b659-aff9-41e9-89b5-29046b90012e?resizing_type=fit)

## Bind Tracker Text to Tracker Name

Next you'll bind the Tracker title you created to the same setting in the Tracker device.

This binding passes the title of your Tracker to the Text Block.

[![This binding passes the title of your Tracker to the Text Block.](https://dev.epicgames.com/community/api/documentation/image/0af778e6-5b18-4c13-8c14-06a7e51dd15f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0af778e6-5b18-4c13-8c14-06a7e51dd15f?resizing_type=fit)

## Setting Up the Tracker Device

Next, you'll reference the widget you created in UMG in the Tracker device. This causes the elimination UI to display in the HUD.

## Final Result

Voila! You have the custom Tracker widget appearing on the top left. Whether you eliminate zombies or other players, the widget slowly fills up! That’s how you link gameplay data to your own custom widgets using Set Material Parameters.

[![](https://dev.epicgames.com/community/api/documentation/image/690d858d-a483-4828-85bd-d6829aee4c76?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/690d858d-a483-4828-85bd-d6829aee4c76?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/421a7e4a-d4c5-4b06-b082-52ab734c2a26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/421a7e4a-d4c5-4b06-b082-52ab734c2a26?resizing_type=fit)
