## https://dev.epicgames.com/documentation/en-us/fortnite/making-a-custom-squad-view-in-unreal-editor-for-fortnite

# Making a Custom Squad View

Expand on the custom backplate knowledge to create a custom squad view for your project.

![Making a Custom Squad View](https://dev.epicgames.com/community/api/documentation/image/2b83da86-0572-481d-8cc5-b70cb21f94b8?resizing_type=fill&width=1920&height=335)

Creating a custom squad view builds on the [single player nameplate](https://dev.epicgames.com/documentation/fortnite/making-custom-backplates-in-unreal-editor-for-fortnite) widget design to create a squad view. The Stack Box widget transforms the player view from single player to squad by reproducing the single player info widget using the Viewmodel.

The Stack Box is a container that arranges the single player widget copies in a linear way, either left-to-right or top-to-bottom.This creates a consistent look for the squad.

[![The Stack Box is a container that arranges the single player widget copies in a linear way, either left-to-right or top-to-bottom.](https://dev.epicgames.com/community/api/documentation/image/9f0c741f-90df-4994-8472-0f3b5b3bcf4e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f0c741f-90df-4994-8472-0f3b5b3bcf4e?resizing_type=fit)

For this example, the squad view is stacked up and down.

To see an example of stacking a squad left to right, see **[Custom UI: Player Info](https://dev.epicgames.com/documentation/fortnite/tmnt-custom-ui-player-info-in-unreal-editor-for-fortnite)** in the Teenage Mutant Ninja Turtles documentation.

## Player Information Widget

To use the player information from team members during a game, the Player_Info widget must be set using the **Device - HUD Controller Player Info Viewmodel**. This setting creates separate widgets for the Controlling Player and their Squad/Team, using properties in Device - HUD Controller Player Info Viewmodel for each widget.

[![The Player_Info widget must be set using the Device - HUD Controller Player Info Viewmodel.](https://dev.epicgames.com/community/api/documentation/image/2d91a9f7-d5e6-41ca-8cbe-a2c8de4b4e0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d91a9f7-d5e6-41ca-8cbe-a2c8de4b4e0a?resizing_type=fit)

You can continue using the settings to set up the bindings from the [Backplate](https://dev.epicgames.com/documentation/fortnite/making-custom-backplates-in-unreal-editor-for-fortnite) and [Health and Shield](https://dev.epicgames.com/documentation/fortnite/making-custom-health-and-shield-bars-in-unreal-editor-for-fortnite) tutorials to bind the necessary pieces of player information.

Without the proper setup for the Player_Info widget, you will get error messages in the compiler.

[![Without the proper set up for the Player Info widget, you will get error messages in the compiler.](https://dev.epicgames.com/community/api/documentation/image/3a872942-4043-4331-becc-db2ab6639def?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a872942-4043-4331-becc-db2ab6639def?resizing_type=fit)

Below are the steps to create a Squad stack widget that binds the Team/Squad Player Info List viewmodels to Player Icon, Player Name, health, and shields.

## Create a User Widget

The Widget Editor is where you plan and layout your UI design for the squad view. Once you've decided on a layout, you can add materials to give your UI a custom look.

You should now have two user widgets in your Content Browser — one called **Player_Info** and a second called **Squad_View**.

[![](https://dev.epicgames.com/community/api/documentation/image/10c3854a-47ba-42e9-886f-988a63f4068f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10c3854a-47ba-42e9-886f-988a63f4068f?resizing_type=fit)

## Create the Squad Layout

It’s best practice to bring a fully functional single Player_Info widget into a Squad_View widget using a Stack Box as a container. This provides a consistent design by reproducing the single player design inside the Stack Box and repeating the design in a top-to-bottom direction or let-to-right direction.

You’ll add the single player widget to the viewmodel, then arrange the layout in the Event Graph through the Stack Box.

Do the following:

1. Drag an **Overlay** under the **Squad_Info** and name it **Container_Overlay**.
2. Resize **Container_Overlay** to **2560** x **1440**. This is the optimal size for all screens.

   [![Resize Container_Overlay to 2560 x 1440.](https://dev.epicgames.com/community/api/documentation/image/b9eba3cd-504e-4820-b8e7-5f4385ae73b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9eba3cd-504e-4820-b8e7-5f4385ae73b2?resizing_type=fit)
3. Nest a **Stack Box** under the **Container_Overlay**.
4. In the **Details** panel, change the following settings for the Stack box:

   [![In the Details panel set Padding to 25 and Orientation to Vertical.](https://dev.epicgames.com/community/api/documentation/image/9f9262cf-4603-46f1-8cb6-a31cb0a33938?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f9262cf-4603-46f1-8cb6-a31cb0a33938?resizing_type=fit)

   The Stack Box has 25 px of padding from the screen edge.
5. From the Main Menu Bar, select **Window** > **Viewmodels** to open the Viewmodel panel.

   [![From the Main Menu Bar select Window > Viewmodel to open the Viewmodel panel.](https://dev.epicgames.com/community/api/documentation/image/e5b00b8b-81df-4f62-8a37-a152d7ef469d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5b00b8b-81df-4f62-8a37-a152d7ef469d?resizing_type=fit)
6. Click **+Viewmodel**, then select **Device - HUD Controller Team/Squad Player Info List** > **Select**. This creates a viewmodel for the HUD Controller device.
7. From the Details panel, click **+Add Viewmodel Extension**. This opens options that provide a way to dynamically generate the squad widget inside the Squad_View widget based on the number of players in your team/squad.

   ![Before +Add Viewmodel Extension](https://dev.epicgames.com/community/api/documentation/image/cf282de1-c183-4270-9e6c-6b94a5721b83?resizing_type=fit&width=1920&height=1080)

   ![After +Add Viewmodel Extension](https://dev.epicgames.com/community/api/documentation/image/eb435175-912e-4189-8037-889280a98c21?resizing_type=fit&width=1920&height=1080)
8. From the **Entry Widget Class** setting, select your **Player_Info widget** from the dropdown and set **Entry ViewModel** to **HUDPlayerInfoListViewModel**.
9. Expand the **Slot Template** option and adjust the spacing between each player widget. Add or remove widgets, and change the alignment. Use these options to visualize how the widgets will look in-game.

   If your UI elements are too large for the available space, go back into the Player_Info widget and adjust the size of your Image widgets down to fit the Squad_View widget.

Next, you'll add bindings to make all the UI functional for squads.

## Squad Bindings

To bind a squad’s information to the Squad_View widget, you need to reference the squad member information through view bindings. The bindings tell the widget what information it needs to grab from the bound devices, and for which player. The information for each player is then populated in the UI through the HUD Controller device.

Add your widget to the HUD Controller and playtest your project.

## HUD Controller Device Setup

There are a few essential HUD Controller settings to change. You'll replace these default Fortnite HUD elements with your own widget design.

Playtest with two or more players to make sure the layout works and looks right for the island you created.

[![Playtest with two or more players to make sure the layout works and looks good with the island you created.](https://dev.epicgames.com/community/api/documentation/image/2857d23c-28c8-40fc-9f63-a797d5da597f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2857d23c-28c8-40fc-9f63-a797d5da597f?resizing_type=fit)
