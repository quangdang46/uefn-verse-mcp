## https://dev.epicgames.com/documentation/en-us/fortnite/using-the-conversation-device-in-unreal-editor-for-fortnite

# Conversation Devices

Create a custom conversation tree for NPCs on your island.

![Conversation Devices](https://dev.epicgames.com/community/api/documentation/image/89fcb2f0-8685-4998-8387-894908ccbcd2?resizing_type=fill&width=1920&height=335)

Want to create engaging dialogue where players make choices that have in-game consequences, purchase items, or receive rewards for completing NPC tasks? The **Conversation** device helps you create conversations that can be immersive, informative, and entertaining. You can drive the game’s story forward by providing players with much needed resources and information.

[![Conversation device icon](https://dev.epicgames.com/community/api/documentation/image/a7ac07da-a233-41fc-a087-26b207ddfd6f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7ac07da-a233-41fc-a087-26b207ddfd6f?resizing_type=fit)

The [Pop-Up Dialog](https://dev.epicgames.com/documentation/fortnite/using-popup-dialog-devices-in-fortnite-creative) device shares core functionality with the Conversation device. You can use both devices to:

- Display messages or instructions for the player.
- Display background information for objectives (when used with a [Tracker](https://dev.epicgames.com/documentation/fortnite/using-tracker-devices-in-fortnite-creative) device).
- Connect to invisible [Class Selector](https://dev.epicgames.com/documentation/fortnite/using-class-selector-devices-in-fortnite-creative) devices and allow players to choose their class.
- Create dialogues between the player and NPCs.

With the Conversation device, you can take the functionality further by adding branched conversations where players make choices that trigger events and change the outcomes of their game.

In Unreal Editor for Fortnite (UEFN), use this device to:

- Create a conversation tree.
- Make branching dialogues.
- Trigger other devices using events in conversation trees.

For an example of complex and dynamic NPC conversations, see the [Narrative and Roleplaying Template](https://dev.epicgames.com/documentation/fortnite/star-wars-narrative-and-roleplaying-in-fortnite) in the [STAR WARS™ Islands](https://dev.epicgames.com/documentation/fortnite/star-wars-islands-in-fortnite) game collection.

## Finding and Using the Device

The Conversation device can be found in the **Fortnite > Devices > UI** folder. Drag the device out of the Content Browser and place it in the viewport beside either an [NPC Spawner](https://dev.epicgames.com/documentation/fortnite/using-npc-spawner-devices-in-unreal-editor-for-fortnite) or [Character](https://dev.epicgames.com/documentation/fortnite/character-device) device.

The general workflow for this device is as follows:

## Setting Up the Device

For more detailed information on the Conversation Editor and its components, and how to create conversation graphs, see [Creating Conversations](https://dev.epicgames.com/documentation/fortnite/creating-conversations-in-unreal-editor-for-fortnite).

## Conversation Types

There are three types of conversation modals: **radial**, **box**, and **custom**. All conversation boxes display choices, and can trigger events.

Keep conversation modals consistent in your game. If you select radial for one, all conversation modals should also be radial throughout the project.

### Radial

The **radial** type displays the conversation UI and choices on a wheel. This style is used in Fortnite Battle Royale NPC interactions.

If your game doesn’t involve complex conversations or a complicated narrative, the radial type is a great way to offer items and make in-game transactions.

[![Conversation radial](https://dev.epicgames.com/community/api/documentation/image/13ed56ac-9a4b-45ed-9c82-c77e40fa52b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13ed56ac-9a4b-45ed-9c82-c77e40fa52b7?resizing_type=fit)

### Box

The **box** type provides ample space for more involved and complicated dialogues. Think about what players will be reading, and make the reading experience as pleasant as possible. Role playing games, visual novels, and many other game genres use a box UI for interactions.

The **box** type has three different **Conversation Type Box** styles:

- **Standard** - The default Box style.
- **Single Speaker** - A customizable box that shows an icon of the speaker.
- **Two Speakers** - A customizable box that shows an icon for both speakers.

#### Standard

The **Standard Box** displays NPC conversations in a speech box, with the player’s choices shown as buttons next to the speech box. This is the default style.

[![Conversation box](https://dev.epicgames.com/community/api/documentation/image/e19a3a8c-39f3-4fd0-8621-ec53103e5669?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e19a3a8c-39f3-4fd0-8621-ec53103e5669?resizing_type=fit)

#### Single Speaker

The **Single Speaker Box Type** displays the speaker's name and text in a box with response buttons to the right of the  speech box. Unlike the default style, you can choose an icon or other material to represent the speaker above the speech box.

In the **Details** panel, locate the **Conversation Materials** option. Add an array element, and click the dropdown to select a material. Then in your conversation graph, you can add a **Set Conversation Material** node to use that material for the speaker.

[![Single Speaker Conversation type provides a way to add an icon to identify the speaker.](https://dev.epicgames.com/community/api/documentation/image/de16b689-b1fd-4f0d-9d4b-ad128041453c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de16b689-b1fd-4f0d-9d4b-ad128041453c?resizing_type=fit)

To learn how to set a custom speaker icon, see the [Custom Conversation UI](https://dev.epicgames.com/documentation/fortnite/custom-conversation-ui-in-unreal-editor-for-fortnite) document.

#### Two Speakers

The **Two Speakers** style displays the current speaker's name and text in a box with response buttons to the right of the speech box. UI Materials can also be used with this box type to identify which character is the current speaker. To learn how to set up two speakers in a conversation graph, see the [Creating Conversations](https://dev.epicgames.com/documentation/fortnite/creating-conversations-in-unreal-editor-for-fortnite#making-a-basic-conversation-graph) document.

![One Speaker](https://dev.epicgames.com/community/api/documentation/image/3d6b6530-8d12-4d96-82a0-582e4515771e?resizing_type=fit&width=1920&height=1080)

![Two Speakers](https://dev.epicgames.com/community/api/documentation/image/d9e9a7e1-aabf-42af-842e-d01d55fa15c9?resizing_type=fit&width=1920&height=1080)

### Custom

You can use the **custom** type to create a completely custom look for all parts of the conversation UI. A customized UI can establish a tone and style for all your in-game conversations.

Custom conversation boxes are created with the [Widget Editor](https://dev.epicgames.com/documentation/fortnite/ui-widget-editor-in-unreal-editor-for-fortnite). See [Custom Conversation UI](https://dev.epicgames.com/documentation/fortnite/custom-conversation-ui-in-unreal-editor-for-fortnite) for details on how to create a custom UI widget.

The custom UI widget needs to be selected in the **Custom Widget** option of a conversation device. The device must be set to use custom UI to successfully initiate conversations.

[![Custom widget assigned](https://dev.epicgames.com/community/api/documentation/image/ab9914de-01be-4c00-af06-85adc8b975bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab9914de-01be-4c00-af06-85adc8b975bf?resizing_type=fit)

The image below shows a simple example for a custom UI, but you can make your custom UI widget as complex and beautiful as you want!

[![Conversation custom](https://dev.epicgames.com/community/api/documentation/image/4ec36ef9-0ece-412d-baf7-125334281585?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ec36ef9-0ece-412d-baf7-125334281585?resizing_type=fit)

## Device Options

Once the Conversation device is placed in the editor, you can start building a conversation, and designing the conversation’s basic user interface (UI) with the tools native to the device. For more detailed information on building conversation bank assets, see [Creating Conversations](https://dev.epicgames.com/documentation/fortnite/creating-conversations-in-unreal-editor-for-fortnite).

You can create a basic conversation using the following options. Default options are in **bold**, values that trigger contextual filtering are in *italic*.

| Options | Values | Description |
| --- | --- | --- |
| **Conversation Type** | **Radial**, *Box*, Custom | Determines the style of the UI displayed when the conversation is active. See the **Conversation Types** section above for more information. |
| **Conversation Type Box** | **Standard**, One Speaker, Two Speakers | This option is only displayed if the **Conversation Type** option is set to **Box**. This determines the type of box is used in the conversation modal UI. |
| **Characters Per Second** | **0.0**, enter a number | Determines the number of characters per second that are displayed onscreen. By default, all the text appears at once. |
| **Skip Text Crawl Message** | **Reveal Tex**t, enter text | If the **Characters Per Second** option's value is greater than **0**, there is a button the player can click to display all the text at once. This option determines what text appears on that button. |
| **Conversation** | Select a conversation bank asset | The device uses this conversation bank asset to run the conversation. |
| **Speaker Name** | Enter a name | Displays the speaker’s name during conversations. If this is left blank, then no name will appear on the screen. |
| **Show Name When Nearby** | On, **Off** | When this option is set to **On**, the speaker's name is displayed when the player is within approximately 5 meters of the speaker. |
| **Show Indicator Bubble** | ***On***, Off | Determines whether a speech bubble indicator displays above a speaker when the player is within the distance set in the **Indicator Bubble Range** option. |
| **Indicator Bubble Range** | **5.0 meter****s**, enter a range | This option is only available if the **Show Indicator Bubble** option is set to **On**. Determines the range, in meters, at which the player is able to see the speech bubble indicator displayed above the speaker. |
| **Title Text Color** | **99DDFFFF**, select a color | This option only displays if the **Conversation Type** option is set to **Box**. Determines the color of the title text. |
| **Title Border Color** | **FFFFFF00**, select a color | This option only displays if the Conversation Type option is set to Box. Determines the color of the title border. |
| **Title Background Color** | **003D94CC**, select a color, select a color | This option only displays if the Conversation Type option is set to Box. Determines the background color for the title text. |
| **Body Text Color** | **FFFFFFCC**, select a color | This option only displays if the Conversation Type option is set to Box. Determines the color of the body text. |
| **Body Border Color** | **003D94CC**, select a color | This option only displays if the Conversation Type option is set to Box. Determines the color of the border around the body text. |
| **Button Text Color** | **FFFFFFFF**, select a color | This option only displays if the Conversation Type option is set to Box. Determines the color of the text on buttons. |
| **Body Background Color** | **00000080**, select a color | This option only displays if the Conversation Type option is set to Box. Determines the color of the background for the body text. |
| **Button Background Color** | **00000080**, select a color | This option only displays if the Conversation Type option is set to Box. Determines the color of the background for button text. |
| ****Button** **Hovered** Color** | **003D94CC**, select a color | This option only displays if the Conversation Type option is set to Box. Determines the color of the button when the mouse is hovered over it. |
| **Show Conversation Text in World Space** | **On**, Off | This option is only available if the **Conversation Type** option is set to **Radial** or **Custom**. Displays the conversation text in world space, as indicated by speech nodes in the conversation graph. |
| **Number of Conversations Allowed** | **1**, enter a number | Determines how many instances of this conversation can happen at one time. |
| **Conversation Maxed Name** | **Can't talk now**, enter text | The text that replaces the speaker's name when the value of **Number of Conversations Allowed** is reached. |
| **Conversation Maxed Color** | **FF0000FF**, select a color | The color of the **Conversation Maxed Nam**e. |
| **Conversation** | **None**, select a conversation bank asset | This points to a conversation bank asset. You can also click the dropdown and select **Conversation Bank** under **Create New Asse****t** to crate a new conversation bank asset. |
| **Conversation Maxed Icon** | **T_UI_NPC_SpeechIconNA**, select an icon | Determines the icon that displays when the **Number of Conversations Allowed** value is reached. |
| **Pressed Sound Override** | **None**, select an audio cue | Choose a custom sound cue for when a button is pressed. |
| **Hovered Sound Override** | **None**, select an audio cue | Choose a custom sound cue for when the mouse is hovered over a button. |
| **Conversation Materials** | **None**, add array elements | If you use the **Set Conversation Material** node in the conversation graph, this is where you indicate which materials will be used. |
| **Custom Widget** | **None**, select a custom UI widget | If you set the **Conversation Type** to **Custom**, this is where you indicate which custom UI widget the device will use. |

## Functions and Events

### Functions

| Function | Description |
| --- | --- |
| **Initiate Conversation** | Forces the associated conversation to start for the player triggering this event. |
| **Exit Conversation** | Forces the current conversation to end for the player triggering this event. |
| **Exit All Conversations** | Leaves all conversations on receiving an event. |
| **Enable** | Enables the device on receiving an event. |
| **Disable** | Disables the device on receiving an event. |
| **Hide Conversation** | Hides the conversation on receiving an event. Responses cannot be selected when a conversation is hidden. |
| **Show Conversation** | Shows the conversation upon receiving an event. |

### Events

| Event | Description |
| --- | --- |
| **On Conversation Started** | Sends an event when a new conversation is started. |
| **On Conversation Ended** | Sends an event for the player when the conversation ends. |
| **On Conversation Cancelled** | Sends an event for a player when forced to exit a conversation early by the **Exit Conversation** or **Exit All Conversations** functions being called. |
| **On Any Conversation Event** | Sends an event when any numbered Event from the associated conversation bank asset is triggered during a conversation. |
| **On Conversation Event [One to Ten]** | Sends an event when the associated conversation bank asset is triggered for a conversation bank's numbered event (**Event One** to **Event Ten**). There is a separate **On Conversation Even**t for each numbered conversation event. |
