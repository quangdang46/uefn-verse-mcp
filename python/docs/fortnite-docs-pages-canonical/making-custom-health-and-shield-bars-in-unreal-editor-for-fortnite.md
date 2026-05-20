## https://dev.epicgames.com/documentation/en-us/fortnite/making-custom-health-and-shield-bars-in-unreal-editor-for-fortnite

# Making Custom Health and Shield Bars

Create custom Health and Shield Bars for your custom HUD.

![Making Custom Health and Shield Bars](https://dev.epicgames.com/community/api/documentation/image/e7b92c7f-6ce4-4cfc-95b4-db8762640ac0?resizing_type=fill&width=1920&height=335)

Create custom Health and Shield bars in Unreal Motion Graphics (UMG) using UI materials, UI textures, and various widgets in the palette to replace the default Fortnite user interface (UI). Health and Shield bars can be added to a nameplate or placed separately in the HUD.

The design and placement of Health and Shield bars are unique to each game and take into consideration the game type (fighting game, multiplayer cooperative, role playing, and so on).

[![Example of custom Halth and Shield bars.](https://dev.epicgames.com/community/api/documentation/image/0bfdc441-59ba-4c6a-ae42-34fb5ae0db50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0bfdc441-59ba-4c6a-ae42-34fb5ae0db50?resizing_type=fit)

## Set Up Material Instances Without Modifying Materials

In this example, you’ll use a variety of materials that were created in UEFN. They include a progress bar in the shape of a rectangle (box) and circle. The rectangle progress bar also has an option to turn the progress bar into sections.

[![A progress bar in the shape of a rectangle (box) and circle.](https://dev.epicgames.com/community/api/documentation/image/84770e99-0495-4366-b48b-81d2ec3aba3b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/84770e99-0495-4366-b48b-81d2ec3aba3b?resizing_type=fit)

Materials were set up using a combination of Material Functions from the UI Material Lab, parameters that are exposed to the Material Instance, and some math to get it all working.

It's best practice to use materials for widgets. Materials update dynamically based on gameplay data, which helps in optimizing UI and provides a way to add special effects. Textures are only used for a more complicated design that can’t easily be achieved with math functions.

For more information on using materials as part of your UI design and implementation, see [**UI Useful Materials**](https://dev.epicgames.com/community/learning/tutorials/6GjP/unreal-engine-ui-useful-materials#progressbars-sdfshapes). The tutorial has more information on using **Signed Distance Fields** (SDFs) for creating dynamic progress bar Materials in UEFN and UE.

A Material Instance creates instances of a material with parameters that can easily tweak the appearance of that material without recompiling it. To create an instance of a material, right-click on a **Material** and select **Create Material Instance**.

[![To create an instance of a material, right click on a Material and select Create Material Instance.](https://dev.epicgames.com/community/api/documentation/image/4db04098-8169-494f-b0be-ffdd36ff43f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4db04098-8169-494f-b0be-ffdd36ff43f8?resizing_type=fit)

More info about Material Instances, refer to [**Creating and using Material Instances**](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-material-instances-in-unreal-engine) in Unreal engine documentation.

There are a few parameters exposed in UEFN. In the example material, the Progress parameter changes how much the bar is filled up. The range is normalized to **0-100** using the **ConstantBiasScale** node in the **M_CircleProgressBar** so it fits into the Fortnite HP range.

You can change the **Background Color** (BGColor) and the **Liquid Color** which are gradients. Afterward, preview your changes in the preview viewport on the left.

[![You can change the Background Color (BGColor) and the Liquid Color which is a gradient.](https://dev.epicgames.com/community/api/documentation/image/d56c05d1-a586-40c0-bd51-93860e15defa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d56c05d1-a586-40c0-bd51-93860e15defa?resizing_type=fit)

You can make as many Material Instances you need for various purposes. In this example, two materials are used, one for HP and another for Shield.

## Widget Layout Best Practices

In UMG only, use the Canvas panel if you need an absolute position on the screen or need to finely manipulate where various widgets are placed.

For smaller widgets use:

- **Overlay**
- **Stack Boxes**
- **Size Boxes** (if you need to constrain your widget to a specific size)
- **Grid Panel** (if you want to maintain sizing of your container but want to manipulate position of child widgets)

Once the materials are ready, create a **Widget Blueprint** in the Content Browser, then double-click the widget thumbnail to open the UMG Editor.

[![Create a Widget Blueprint in the Content Browser.](https://dev.epicgames.com/community/api/documentation/image/1603bcc7-0e42-48d9-afe1-21f8ad10d538?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1603bcc7-0e42-48d9-afe1-21f8ad10d538?resizing_type=fit)

### Using a Canvas Panel

In this example, the Canvas panel is used to place the Health and Shield bars in an absolute position on the HUD by anchoring the widgets to certain parts of the screen.

For individual HUD elements, it’s best practice to use a combination of the following widgets:

- **Overlay** - If you need to overlay a widget on top of one another
- **Stack Boxes** - If you need to lay your widgets out horizontally or vertically
- **Size Boxes** - If you need to constrain your widget to a specific size
- **Grid Panel** - if you want to maintain sizing of your container but want to manipulate position of child widgets inside it

With this in mind, start laying out the Health and Shield widgets.

### Setting up the HP Bar and Text

Now that the Health and Shields container is ready, set up the Health and Shields widget.

1. Nest an **Overlay** under the **Stack Box** and rename it **HPOverlay**. This causes the HP Text to overlay the round HP bar.

   [![Nest an Overlay under the HPShieldContainer.](https://dev.epicgames.com/community/api/documentation/image/c293e854-f728-4718-8722-4740cb6e93f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c293e854-f728-4718-8722-4740cb6e93f5?resizing_type=fit)
2. Nest an **Image** under **HPOverlay** and rename it **HPBar**. This provides a way to add the Material Instance you made above to your widget.

   [![Nest an Image under the Overlay.](https://dev.epicgames.com/community/api/documentation/image/39698918-ddee-4528-ae5c-b2949048c107?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/39698918-ddee-4528-ae5c-b2949048c107?resizing_type=fit)
3. Select **HPBar** in the Hierarchy, in Details under **Brush**> **Image** select your custom Health bar Material Instance.

   [![Add your custom material to the Brush setting.](https://dev.epicgames.com/community/api/documentation/image/efec2014-e094-48db-8713-05229901ed4e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efec2014-e094-48db-8713-05229901ed4e?resizing_type=fit)

   To change the size of the Material Instance, you can customize the Image Size property below.
4. Nest a **Text Block** under **HPOverlay** and rename it **HPText**. This provides a way to add text on top of the circle Health bar.

   [![Nest a Text Box under the HPOverlay.](https://dev.epicgames.com/community/api/documentation/image/4e525085-5ddb-423e-8660-054f1681f3b9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e525085-5ddb-423e-8660-054f1681f3b9?resizing_type=fit)
5. Select the **Text Block** and in Details set the **Horizontal and Vertical** alignment to **Centre**. This ensures the text is always center-aligned to **HPBar**.

   [![Set the HPBar to center alignment.](https://dev.epicgames.com/community/api/documentation/image/015fc9b2-5c68-4796-a95a-0157b29efd5f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/015fc9b2-5c68-4796-a95a-0157b29efd5f?resizing_type=fit)

   *Click to enlarge image.*
6. Change the **font size** under **Appearance** > **Font** > **Size** so it fits into the HP Bar.

   [![Adjust the font size to fit the HPBar.](https://dev.epicgames.com/community/api/documentation/image/88bfaa59-e575-412a-83e5-49f672f5a0f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/88bfaa59-e575-412a-83e5-49f672f5a0f8?resizing_type=fit)

   *Click to enlarge image.*
7. Click **Compile**. Now you have a HP Bar and HP Text ready!

   [![Final HPBar design](https://dev.epicgames.com/community/api/documentation/image/798170b0-498c-4712-a023-8a6c790db23f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/798170b0-498c-4712-a023-8a6c790db23f?resizing_type=fit)

### Setting Up the Shield Bar and Text

To set up your Shield Bar and Text, repeat the same steps above. This time add a space between the HP Bar and Shield Bar. Since HPShieldsContainer is a Stack Box, it automatically lays out child widgets horizontally.

Use an Image widget inside the Stack Box to add a space between your Health and Shield bars. Set up the blank Image widget by doing the following:

This means that nothing will show up in your widget but the Image widget still takes up space in your layout! This allows you to easily manage spacing between elements in a Stack Box without needing to rely on padding.

[![Example of added space after the HP Bar.](https://dev.epicgames.com/community/api/documentation/image/bb191bb4-8b6d-4303-8c92-cd43e6cc9ca5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb191bb4-8b6d-4303-8c92-cd43e6cc9ca5?resizing_type=fit)

Now you’re ready to create the bindings that add functionality to the Health and Shield progress bars.

## View Bindings

### Adding a Viewmodel

A viewmodel provides a way for you to add device functionality to a Widget Blueprint. The viewmodel uses View Bindings to identify widgets in the blueprint and graph device functionality to that widget.

The HUD Controller Player Info Viewmodel provides a way to replace parts of your HUD with a custom widget.

Now it’s time to set up the bindings that bind data from the viewmodel to your widget!

### Set Up ToText View Bindings

1. Select **Window** > **View Bindings** to open the **View Bindings** window.

   [![Select View Bindings from the Windows menu to bind the HUD Controller device to the Widget Blueprint.](https://dev.epicgames.com/community/api/documentation/image/ff81a916-9150-4a9f-9330-35172c8eb44d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff81a916-9150-4a9f-9330-35172c8eb44d?resizing_type=fit)
2. Select **HPText** in your **Hierarchy** and select **Add Widget** in **View Bindings** to bind **HPText** to show your current **Health number**. An empty binding appears.

   [![Select HPText in your Hierarchy and click on Add Widget in View Bindings.](https://dev.epicgames.com/community/api/documentation/image/76c1c57f-6648-4139-b9f6-07f8ef87118c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76c1c57f-6648-4139-b9f6-07f8ef87118c?resizing_type=fit)
3. The left box is the **Widget Property** and the right box is the data you want to bind to the Widget Property. Click the **left box**, and a list of properties for the **HPText Text Block** will appear. Select the **Text** property to pass the HP numbers into this property.

   [![Select the Text property.](https://dev.epicgames.com/community/api/documentation/image/0dfa4b0f-ac92-4772-9274-1f7cdf492eaf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0dfa4b0f-ac92-4772-9274-1f7cdf492eaf?resizing_type=fit)
4. The right box is the data you want to pass into the selected widget property. However, the Text property only accepts data of the Text type. Since the Fortnite HP number comes in a Float (i.e. Double) type, you need to convert it into the appropriate Text type. Click the **right box** and select **Conversion Functions** > **To Text (Double)**.

   [![Select Conversion Functions, and select To Text (Double).](https://dev.epicgames.com/community/api/documentation/image/19e2e976-621d-4087-b7de-3750c487c45a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19e2e976-621d-4087-b7de-3750c487c45a?resizing_type=fit)

   A large list of options appear. The most important settings are typically at the top, while the rest of the settings provide a way for you to format the final value that gets passed into your Text property.

   [![Text properties](https://dev.epicgames.com/community/api/documentation/image/7e3dd964-ce50-47e8-b93b-e8741b6b7149?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e3dd964-ce50-47e8-b93b-e8741b6b7149?resizing_type=fit)

   *Click image to enlarge.*
5. Select the **Link icon** next to **Value**, then select your **Health value** from the **HUD Controller Viewmodel**.

   [![Select your Health value from the HUD Controller Viewmodel.](https://dev.epicgames.com/community/api/documentation/image/335e0bbd-b4d1-4f13-bdcc-01b157e700bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/335e0bbd-b4d1-4f13-bdcc-01b157e700bc?resizing_type=fit)
6. Click the empty field and select **HUDPlayerInfoListViewmodel** in the left column, expand **Controlling Player Info** on the right, and select **Health**.

   [![Click on the empty field and select HUDPlayerInfoListViewmodel in the left column, expand Controlling Player Info on the right, and select Health.](https://dev.epicgames.com/community/api/documentation/image/fec325e6-2c77-4b2b-b969-5deac2295a6b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fec325e6-2c77-4b2b-b969-5deac2295a6b?resizing_type=fit)

   This passes the Health property–a Float (i.e. Double) type, through the To Text (Double) Conversion Function. To Text (Double) converts Health into a Text type so it displays on the widget. The converted Health is then passed into the Text property of your HPText widget.

   [![The converted Health is then passed into the Text property of your HPText widget.](https://dev.epicgames.com/community/api/documentation/image/0c468f98-bd8f-4fa6-bcfc-37622f27d651?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c468f98-bd8f-4fa6-bcfc-37622f27d651?resizing_type=fit)
7. Repeat the steps above to set up the ShieldText widget. The same bindings will show the Shield numbers as well.

   [![Repeat the steps above to set up the ShieldText widget.](https://dev.epicgames.com/community/api/documentation/image/80850ec0-922c-4b27-803f-6264571525ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/80850ec0-922c-4b27-803f-6264571525ad?resizing_type=fit)

### Set Material Parameter

For more details on how Set Material Parameter works, refer to [**Set Material Parameter**](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-material-parameter-collections-in-unreal-engine) in Unreal Engine documentation.

Now it’s time to set up the Circle progress bar. The progress changes based on player Health and Shield levels.

This is the final result of binding the Health and Shield stats in the viewmodel. Now, whenever the player’s health changes, it will pass the Health property into the HP bar Material Instance and update the Progress scalar parameter.

[![Final result](https://dev.epicgames.com/community/api/documentation/image/926065f6-e8b5-4199-95fa-2ed2608c27c1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/926065f6-e8b5-4199-95fa-2ed2608c27c1?resizing_type=fit)

Repeat the same for your ShieldBar. Instead of binding it to the Health property, it should be binded to the **Shield property**.

[![Shield property](https://dev.epicgames.com/community/api/documentation/image/bc25ba21-d275-406d-980f-f468442129ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc25ba21-d275-406d-980f-f468442129ba?resizing_type=fit)

Now your HP and Shields bindings are set up! It’s time to display your widget on your HUD.

## HUD Controller Device Setup

## Other Examples of Progress Bars

The **Rectangle material** can be found under **Fortnite** > **UI** > **Material**, you can customize the basic box to use as background in many forms, for any widget!

[![Material UI Shape used to create UI elements.](https://dev.epicgames.com/community/api/documentation/image/3d3c780f-e050-4c22-b9ff-bc051f94dc7a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d3c780f-e050-4c22-b9ff-bc051f94dc7a?resizing_type=fit)

Create a Material Instance from this and start using it with UMG!

[![Settings for the Material UI Shape.](https://dev.epicgames.com/community/api/documentation/image/16effff5-c7a7-42db-9aff-d28d239e87ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16effff5-c7a7-42db-9aff-d28d239e87ba?resizing_type=fit)

Using the information here and the Materials we provide you with, try making these Progress Bars:

- Using a texture as a background to frame your Player Avatar, Display Name, and HP Bar.

  [![Example of custom nameplate with Health and Shield bars.](https://dev.epicgames.com/community/api/documentation/image/a5d13adc-735d-44dd-ace3-ceae85bc3ae8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a5d13adc-735d-44dd-ace3-ceae85bc3ae8?resizing_type=fit)
- Using a combination of textures, icons, progress bar Materials, and the Rectangle material under Fortnite > UI > Material to stylize basic progress bars.

  [![Example of custom Health and Shield bars.](https://dev.epicgames.com/community/api/documentation/image/d81d7aac-f892-4b17-a625-36ca6c1c9298?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d81d7aac-f892-4b17-a625-36ca6c1c9298?resizing_type=fit)
- Sectioned HP and Shield Bar along with the Player Avatar and Display Name.

  [![Example of custom Health and Shield bars.](https://dev.epicgames.com/community/api/documentation/image/ae372ee6-9c9c-448e-b6f3-126392f8b080?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae372ee6-9c9c-448e-b6f3-126392f8b080?resizing_type=fit)

### Next Up

- [![Making a Custom Squad View](https://dev.epicgames.com/community/api/documentation/image/ef2ad1eb-1150-45f5-ae98-e4a8b57a1a57?resizing_type=fit&width=640&height=640)

  Making a Custom Squad View

  Expand on the custom backplate knowledge to create a custom squad view for your project.](https://dev.epicgames.com/documentation/fortnite/making-a-custom-squad-view-in-unreal-editor-for-fortnite)
