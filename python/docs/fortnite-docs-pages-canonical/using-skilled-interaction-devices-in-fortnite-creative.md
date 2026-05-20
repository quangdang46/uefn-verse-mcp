## https://dev.epicgames.com/documentation/en-us/fortnite/using-skilled-interaction-devices-in-fortnite-creative

# Skilled Interaction Devices

Raise the bar and create interactable user interfaces for minigames like lockpicking and fishing.

![Skilled Interaction Devices](https://dev.epicgames.com/community/api/documentation/image/8de90a52-08a8-48df-9204-7d7dfe9ecaf0?resizing_type=fill&width=1920&height=335)

Use the **Skilled Interaction** device to create skill-based interactions as mini-games for your players. Customize this device's settings to create good, perfect, or bad zones for players to target, which can trigger individual events attached to other devices.

For help on how to find the Skilled Interaction device, see [**Using Devices**](using-devices-in-fortnite-creative).

If you're using multiple copies of a device on an island, it can be helpful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#rename-a-device) them. You can choose names that relate to each device’s purpose, so it’s easier to remember what each one does.

## Interaction Types

You can alter this device's settings to create charge and release, timed, and quick press interactions.

### Charge and Release

The following settings were altered to create a skilled interaction where players can press and hold a command to target good and perfect zones that grant success when hit.

[![Image of customized settings for creating a fishing skill minigame with the Skilled Interaction Device.](https://dev.epicgames.com/community/api/documentation/image/e85d0f40-909d-4b3f-a4f5-7b0b8f12878e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e85d0f40-909d-4b3f-a4f5-7b0b8f12878e?resizing_type=fit)

Customize these settings to create the example displayed above.

### Timed

The following settings were altered to create an interaction where players must hit a set target at the correct time.

[![Image of customized settings for creating a minigame for hitting a target within a time limit.](https://dev.epicgames.com/community/api/documentation/image/23caf28b-e978-4fe7-9266-c056ac928731?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23caf28b-e978-4fe7-9266-c056ac928731?resizing_type=fit)

Customize these settings to create the example displayed above.

### Quick Press

[![](https://dev.epicgames.com/community/api/documentation/image/2664f14b-a2f2-4154-8ff8-7917ec7e96c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2664f14b-a2f2-4154-8ff8-7917ec7e96c0?resizing_type=fit)

The following settings were altered to create an interaction to target moving zones.

[![Image shows customized settings for creating a minigame that requires pressing a control when the target is within a moving zone.](https://dev.epicgames.com/community/api/documentation/image/7c4cbd2b-1996-44b1-8516-2ec5e00f3b5b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c4cbd2b-1996-44b1-8516-2ec5e00f3b5b?resizing_type=fit)

Customize these settings to create the example displayed above.

## Single and Multiplayer

The Skilled Interaction device includes the options for single and multiplayer skill checks.

Activating one of the **Queue Execution Type** options enables multiplayer quick time events. For multiplayer, if there is no room for that round, players are placed in a queue based on the order that they join. You set the queue limit with the **Maximum Queued Players** option. If there are no active players at the time of the call for interaction, then the player skips to the interaction.

[![Multiplayer quick time event diagram](https://dev.epicgames.com/community/api/documentation/image/0ec2d8cf-6791-49c4-8ba1-519c76696253?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ec2d8cf-6791-49c4-8ba1-519c76696253?resizing_type=fit)

Multiplayer quick time event diagram

## Contextual Filtering

Some devices are affected by a feature called **contextual filtering**. This feature hides or displays options depending on the values selected for certain related options. This reduces clutter in the Customize panel and makes options easier to manage and navigate.

However, it may not be easy to recognize which options or values trigger contextual filtering. To help you identify them, in our device docs, we use *italic* for any values that trigger contextual filtering. All options will be listed, including those affected by contextual filtering; if they are hidden or displayed based on a specific option’s value, there will be a note about that in the Description field for that option.

## Device Options

You can configure this device with the following options.

Default values are **bold**. Values that trigger contextual filtering are *italic*.

| Option | Value | Description |
| --- | --- | --- |
| **Header Text** | Enter text | Displays the main text for the interaction. |
| **Description Text** | Enter text | Sets the text for the interaction. |
| **Text Position** | **Top**, Bottom, Left, Right | Displays the text position relative to the meter. |
| **Interaction Type** | **Normal**, Charge and Release | Displays the type of interaction for the device. **Normal** is an automatic animation, which triggers upon button press. **Charge and Release** animates while holding down the button and triggers upon release. |
| **UI Type** | **Circular**, Pulsing, *Bar* | Sets the type of user interface to display. If you select **Bar**, an additional option displays. |
| **Meter Thickness** | **40** (for Circular), **70** (for Pulsing), Pick or enter a value | This option displays if the **UI Typ**e option is set to **Circular** or **Pulsing**. Determines the thickness in pixels for the circular type. |
| **Scrubber Thickness** | **4**, Pick or enter an amount | This option only displays if the **UI Type** option is set to **Pulsing**. Determines the thickness of the scrubber, in pixels. |
| **Set Custom Size** | On, **Off** | This option only displays if the UI Type option is set to Pulsing. If this is set to **On**, the meter will use a custom height and width. The custom height and width can only be set using UEFN. |
| **Movement Type** | **Linear**, PingPong, Wiggle | This option only displays if the UI Type option is set to Pulsing. Determines the movement pattern for the pulsing meter. If this is set to **Wiggle**, two additional options display below this one. |
| **Wiggle Time Min** | **0.5 seconds**, Pick or enter an amount | Determines the minimum amount of time the meter wiggles before movement. |
| **Wiggle Time Max** | **1.0 seconds**, Pick or enter an amount | Determines the maximum amount of time the meter wiggles before movement. |
| **Widget Orientation** | Vertical, **Horizontal** | This option only displays if the **UI Type** option is set to **Bar**. Determines whether the meter displays horizontally or vertically. |
| **Movement Speed** | **50%**, Pick or enter a value | Determines how fast the meter moves across the interaction in percent per second. |
| **Good Zone Size** | **50%**, Pick or enter a value | Sets the good zone's size as a percent of the total meter. |
| **Good Zone Position** | **50%**, Pick or enter a value | Sets the position of the good zone. |
| **Position Zone Randomly** | *On*, **Off** | Determines whether the good zone positions itself randomly. |
| **Perfect Zone Size** | **25%**, Pick or enter a value | Determines the perfect zone's size as a percent of the good zone. |
| **Perfect Zone Position** | **50%**, Pick or enter a value | Determines the position of the perfect zone. |
| **Allowed Team** | **Any**, Pick or enter a team number | Determines which team can activate the device. |
| **Allowed Class** | **Any**, Pick or enter a class number | Determines which class can activate the device. |
| **Invert Team Selection** | On, **Off** | If set to **Off**, only the selected team can activate the device. If set to **On**, all teams except the selected team can activate the device. |
| **Invert Class Selection** | On, **Off** | If set to **Off**, only the selected class can activate the device. If **True**, all classes except the selected class can activate the device. |
| **Interaction Label** | Enter text | Determines the text label shown on the input panel. |

### Additional UEFN-Only Option

| Option | Values | Description |
| --- | --- | --- |
| General |  |  |
| **Starts Enabled** | **True**, False | Determines whether or not the device is enabled automatically. |
| UI |  |  |
| --- | --- | --- |
| **Custom Widget** | **Don't Override**, Pick a widget | Select a custom widget to use for the interaction. |
| **Screen Anchor** | **Center**, Pick a position | Determines where on the screen the UI will align and anchor to. |
| **Placement Horizontal** | **0.0**, Pick or enter a position | Determines how far away from the anchor the widget will be. Negative numbers will move to the left. |
| **Placement Vertical** | **0.0**, Pick or enter a position | Determines how far away from the anchor the widget will be. Negative numbers will move upwards. |
| **Background Color** | **000000FF**, Pick a color | Sets the background color of the meter UI. |
| **Background Opacity** | **80%**, Pick or enter an amount | Sets the background opacity as a percentage. If set to **0%**, there will be no background shown. |
| **Background Corners Type** | Square, **Round** | Sets the type of background color to apply. |
| **Hide HUD** | **True**, False | If set to On, the game HUD will be hidden when the interaction is active. |
| **Active Player Color** | **FFFFFFFF**, Pick a color | Determines the color of the player actively interacting with the device. |
| **Waiting Player Color** | **FFFFFF99**, Pick a color | Determines the color of the player waiting to interact with the device. |
| **Fail Player Color** | **E33243FF**, Pick a color | Determines the color of a player who fails the interaction. |
| **Success Player Color** | **21FE99FF**, Pick a color | Determines the color of a player who succeeds the interaction. |
| **Show Player List** | True, False | Displays the list of players interacting with the device. |
| **Persist UI Duration** | **0.0 seconds**, Pick or enter an amount | Determines how long the interaction UI remains onscreen after a success or failure. |
| **Hide UI When** | **Player Interaction Complete**, All Interactions Complete. | Determines what condition must be met for the interaction UI to be hidden.   - **Player Interaction Complete**: UI is hidden when the active player's interaction is succeeded or failed. - **All Interactions Complete**: UI is hidden when all players in the queue succeed or fail the interaction. |
| Device |  |  |
| --- | --- | --- |
| **Perfect Input Behavior** | **Instant Success**,Counts For Two, No Special Behavior | Determines what should happen when a perfect input occurs. |
| **Speed Up on Subsequent Interacts** | **Off**, Pick or enter a value | Determines how much to speed up on subsequent successful interactions. Resets when the device is retriggered. |
| **Shrink Zones on Subsequent Interacts** | **Off**, Pick or enter a value | Determines how much to shrink the zone on subsequent interactions. Resets when the device is retriggered. |
| **Success Target** | **None**, 1, 2, 3, 4, 5 | Sets how many successful inputs are required for the minigame to complete. |
| **Show Successes** | True, **False** | Determines whether to display the success counter on screen. |
| **Success Counter Icon** | Small Checkmark, Large Checkmark, Select another icon | Determines the icon to use for the Success Target indicator. |
| **Success Counter Color** | **FFFFFFFF**, Pick a color | Determines the color of the Success Target indicator. |
| **Failure Limit** | *None*, **1**, 2, 3, 4, 5 | Determines how many times a bad input can be provided before failing the minigame. If this is set to 0 (None), an additional option is available. |
| **Show Failures** | True, **False** | This option is only available if the **Failure Limit** option is set to **0 (None)**. Determines whether to display the fail counter on screen. |
| **Fail Counter Icon** | **X**, Pick an icon | Determines the icon to use for the Fail Limit indicator. |
| **Clear Successes on Fail** | True, **False** | If this is set to True, the Interaction Success Count resets on a bad input. |
| **Lock Out on Fail Time** | 0.0 seconds, **1.0 seconds**, Enter an amount | If a bad input is provided, the interact will lock for the amount of time set. Set to 0 to disable this function. |
| **Waiting Icon** | Small None Icon, Large None Icon, Select another icon | Determines the icon to use for the waiting player indicator. |
| **Waiting Icon Color** | **FFFFFFFF**, Pick a color | Determines the color of the waiting player indicator icon. |
| **Active Icon** | Small Hourglass icon, Large Hourglass icon, Select another icon | Determines the icon to use for the active player indicator. |
| **Active Icon Color** | **FFFFFFFF**, Pick a color | Determines the color of the active player indicator icon. |
| Meter |  |  |
| --- | --- | --- |
| Meter Custom Width | **72**, Pick or enter a value | This only displays if you have set the Set Custom Size option to On. Determines the width of the meter. |
| **Meter Custom Height** | **72**, Pick or enter a value | This only displays if you have set the **Set Custom Size** option to **On**. Determines the height of the meter. |
| Meter Color | **0044CBFF**, Pick a color | Determines the meter's color. |
| Scrubber Color | **FFFFFFFF**, Pick a color | Determines the color of the meter scrubber. |
| Zones |  |  |
| --- | --- | --- |
| Good Zone Color | **5CAAFFFF**, Pick a color | Determines the good zone's color. |
| Perfect Zone Color | **32EDFEFF**, Pick a color | Determines the color of the perfect zone. |
| Timer |  |  |
| --- | --- | --- |
| **Interact Time Limit** | **0.0 seconds**, Pick or enter a value | Sets how long the player has to complete the interaction. Taking too long will result in failure. |
| **Show Timer** | **True**, False | If this is set to **True**, the timer will display on the screen. |
| **Timer Position** | **Top**, Bottom | Sets the timer's position. |
| **Timer Color** | **FFFFFFFF**, Pick a color | Determines the timer's color. |
| **Timer Size** | **Normal**, Large | Determines the timer's size. |
| **Timer Background Type** | None, **Transparent**, Opaque | Sets the transparency level of the timer's background. |
| Sound |  |  |
| --- | --- | --- |
| Interact Complete Sound | Pick a sound | Sets the sound that plays when the minigame is completed successfully. |
| Interact Failure Sound | Pick a sound | Sets the sound that plays when the minigame is completed unsuccessfully. |
| **Interact Interrupted Sound** | Pick a sound | Sets the sound that plays when the minigame is interrupted. |
| **Good Input Sound** | Pick a sound | Sets the sound that plays when a player hits within the success zone. |
| **Perfect Input Sound** | Pick a sound | Sets the sound that plays when a player hits within the perfect zone. |
| **Bad Input Sound** | Pick a sound | Sets the sound that plays when a player hits outside the success zone. |
| **Minigame Start Sound** | Pick a sound | Sets the sound that plays when the minigame starts. |
| **Minigame Looping Sound** | Pick a sound | Sets a looping sound that plays during the interaction. |
| **Looping Audio Pitch Multiplier** | **1.0**, Pick or enter a multiplier | Sets a pitch multiplier for the looping sound. This will increase by the selected amount each time a player gets a successful or perfect interaction. It will reset when the minigame is restarted. |
| Queue |  |  |
| --- | --- | --- |
| **Allow Duplicate Player Entries** | **True**, False | Determines if a player can make duplicate entries in the queue. Useful for re-initiating skill checks without restarting the quick time event. |
| **Next in Queue Delay** | **3.0 seconds**, Pick an amount | Sets the time between a player finishing an interaction and starting a new interaction with the next player in the queue. |
| **Queue Execution Type** | **None**, Synchronous, Random, Sequential | Sets the order for completing the quick time event.   - Synchronous: Plays the skill check at the same time. - Random: Plays the skill check for one player. - Sequential: Plays the skill check in the order players joined. |
| **Synchronous Player Limit** | **5**, Enter a number | Sets the max number of players completing the skill check at the same time. This skips any duplicate entries. |
| **Maximum Queued Players** | **20**, Enter a number | Sets the total number of players that can join the queue for the event. |

## Direct Event Binding

Following are the [direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) listens for an event on a device and then performs an action.

| Option | Description |
| --- | --- |
| **Begin Interaction for Instigator** | Activates the interaction for the instigating player. |
| **End Interaction for Instigator** | Deactivates the interaction for the instigating player. |
| **Enable** | Enables the device on triggered. |
| **Disable** | Disables the device on triggered. |

### Events

An [event](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| **On Interact Success Transmit Event** | Sets the event when the interaction is successful. |
| **On Interact Fail Transmit Event** | Sets the event when the interaction is failed, either because of bad inputs or timeout. |
| **On Interact Bad Input Transmit Event** | Sets the event when the player provides abad input. |
| **On Interact Good Input Transmit Event** | Sets the event when the player provides a good input. |
| **On Interact Perfect Input Transmit Event** | An event occurs when the player provides a perfect input. |
| **On Interact Interrupted Transmit Event** | An event occurs when the interaction is interrupted, either due to player elimination, manual deactivation, or disabled. |
| **On Interact Started**Transmit Event | When an interaction is started, an event occurs. |
| **On Removed Agent From Queue****Transmit** **Event** | An event occurs when an agent is removed from the queue for the interaction. |
| **On Queue Agent Transmit Event** | An event occurs when an agent enters the queue. |
| **On Advance Agent From Queue Transmit Event** | An event occurs when an agent moves up in the queue. |
| **On Group Interact Success Transmit Event** | An event occurs when all members of a group succeed on an interaction. |
| **On Group Interact Failed Transmit Event** | An event occurs when all members of a group fail an interaction. |
| **On All Interactions Complete Transmit Event** | An event occurs when all players in the queue have completed the interaction. |
