## https://dev.epicgames.com/documentation/en-us/fortnite/using-accolades-devices-in-unreal-editor-for-fortnite

# Using Accolades

Learn to grant players different types of Accolades in UEFN!

![Using Accolades](https://dev.epicgames.com/community/api/documentation/image/b31ad7f2-dfe2-4688-81f4-41af9a3ae18b?resizing_type=fill&width=1920&height=335)

Want to grant players Battle Pass XP while they play your UEFN experience? This tutorial shows you how to use the Accolade device to grant XP to players through UEFN and Verse.

For more information on how this device grants players XP, see [Accolade Devices](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-accolades-devices-in-fortnite-creative) for Fortnite Creative.

## Awarding XP for Zombie Eliminations

1. Launch UEFN from the Epic Game Store.

   [![UEFN](https://dev.epicgames.com/community/api/documentation/image/f973e560-7a26-45ca-b0d0-b39db2ccaa9e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f973e560-7a26-45ca-b0d0-b39db2ccaa9e?resizing_type=fit)
2. Create a new island or load an existing island.
3. In the Content Browser, navigate to **All** > **Fortnite** > **Devices** and search for "accolade".

   [![accolades search](https://dev.epicgames.com/community/api/documentation/image/a678f68a-1874-4ce0-b82d-b3abe155a25a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a678f68a-1874-4ce0-b82d-b3abe155a25a?resizing_type=fit)
4. Drag the Accolade device into your level.

   [![Drag accolade](https://dev.epicgames.com/community/api/documentation/image/acc6f198-f96b-4db5-b58b-5f4b027abdcd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/acc6f198-f96b-4db5-b58b-5f4b027abdcd?resizing_type=fit)
5. Make sure the Accolade device is selected.
6. In the Details panel, modify the following User Options:

   [![Details panel](https://dev.epicgames.com/community/api/documentation/image/231a35e4-2138-472f-96a0-cc99b2446590?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/231a35e4-2138-472f-96a0-cc99b2446590?resizing_type=fit)

   | Option | Value | Explanation |
   | --- | --- | --- |
   | **Name** | "Zombie Elimination" | A brief message to explain the type of award. |
   | **XP Award** | Very Small | Since this is an easy to achieve goal, the award should be small. |
   | **Splash Size** | Small | The message on the player’s screen will take up a small amount of space. |
7. In the Content Browser, navigate to **All** > **Fortnite** > **Devices** and search for "creature spawn".

   [![creature spawner](https://dev.epicgames.com/community/api/documentation/image/5c4d127f-49ab-4dc1-9102-baf467fe0924?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5c4d127f-49ab-4dc1-9102-baf467fe0924?resizing_type=fit)
8. Drag a **Creature Spawner** into your level.
9. Find and drag a **Mounted Turret** device into your level, within range of the creature spawner. This will allow players to eliminate the zombies.

   [![turret-range](https://dev.epicgames.com/community/api/documentation/image/041290bf-77fa-4efc-9a03-810c996f87ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/041290bf-77fa-4efc-9a03-810c996f87ee?resizing_type=fit)

### Direct Event Binding

You can use direct event binding to trigger the Accolade device whenever a zombie is eliminated. This workflow is performed in the editor only. To see how this is done in Verse, go to [Awarding XP Using Verse](https://dev.epicgames.com/documentation/fortnite/using-accolades-devices-in-unreal-editor-for-fortnite).

## Awarding XP for Time Spent In-Game

### Direct Event Binding

Use direct event binding to trigger the Accolade device whenever the timer completes.

[![timer success](https://dev.epicgames.com/community/api/documentation/image/c44dc5bb-d52c-4c3a-8d89-36adc6eb2bfa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c44dc5bb-d52c-4c3a-8d89-36adc6eb2bfa?resizing_type=fit)

## Awarding XP Using Verse

This example builds on the [zombie elimination](https://dev.epicgames.com/documentation/fortnite/using-accolades-devices-in-unreal-editor-for-fortnite) example above. Zombies drop bones that can be picked up. The following section shows how to award a large amount of XP whenever a player submits 5 bones.

1. From the Content Browser, navigate to **All** > **Fortnite** > **Devices** and search for "elimination".
2. Drag an **Elimination Manager** device into your scene.
3. From the **Details** panel, under **User Options:**
4. Drag another Accolade device into your scene.
5. From the **Details** panel of the new Accolade device:
6. Search for "conditional" in the Content Browser.
7. Drag a **Conditional Button** device into your scene.
8. From the Details panel of the new Conditional Button device:

### Creating the Verse Script

1. Create a new Verse device named **accolade_example** using [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite), and drag the device into the level. To learn how to create a new device in Verse, see [Create Your Own Device Using Verse](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite).
2. Open [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite) and double-click **accolade_example.verse** to open the script in Visual Studio Code.
3. In the `accolade_example` class definition, add the following fields.
4. In `OnBegin()`, subscribe the `ConditionalButton` `ActivatedEvent` to a new function named `BountyComplete`.

   Verse

   ```
        OnBegin<override>()<suspends>:void=
            ConditionalButton.ActivatedEvent.Subscribe(BountyComplete)
   ```

    OnBegin&lt;override&gt;()&lt;suspends&gt;:void=
   ConditionalButton.ActivatedEvent.Subscribe(BountyComplete)
5. Add the new method `BountyComplete()` to the `accolade` class. This method awards the player who activated the `ConditionalButton` with the `Accolades` score.

   Verse

   ```
        # Awards score to the player who activated
        # the ConditionalButton
        BountyComplete(Agent:agent):void=
            Accolades.Award(Agent)
   ```

    # Awards score to the player who activated
   # the ConditionalButton
   BountyComplete(Agent:agent):void=
   Accolades.Award(Agent)
6. Your `accolade_example` code should now look like:

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/Diagnostics }

        accolade_example := class(creative_device):

            @editable
            Accolades:accolades_device = accolades_device{}

            @editable
   ```
7. Save the script in Visual Studio Code, and in the Main Menu, under Verse, click **Build Verse Code** to compile your code. If errors are discovered, you can find them in the Message Log panel under the **Verse Build** section.

   [![build verse code](https://dev.epicgames.com/community/api/documentation/image/6e850b7f-52bf-411f-99f5-d09309ef5810?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e850b7f-52bf-411f-99f5-d09309ef5810?resizing_type=fit)
8. Navigate to **<ProjectName> Content** > **Creative Devices**, find your Verse device, and drag it into your scene.
9. With the Verse device selected, in the **Details** panel, assign the object reference for the Accolade device and the Conditional Button device. You can use the eyedropper to pick the object in the viewport, or use the dropdown and search for the device.

   [![Verse Devices Details](https://dev.epicgames.com/community/api/documentation/image/acc8bed5-12c0-4886-88a6-8fc21f8f5efe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/acc8bed5-12c0-4886-88a6-8fc21f8f5efe?resizing_type=fit)

## Playtesting Your Island

Once everything is set up and ready to go, [playtest your island](https://dev.epicgames.com/documentation/en-us/uefn/playtesting-your-island-unreal-editor-for-fortnite) to make sure that it runs as expected in Fortnite.

When playing your level, you should see boilerplate debug text on the screen that tells you when the accolade device is activated and awarding XP.

This is what happens when you eliminate zombies.

This is what happens when you cash in 5 bone parts.

## Publishing Your Island

To **Publish** your island, see [Publishing Projects](https://dev.epicgames.com/documentation/en-us/uefn/publishing-projects-in-unreal-editor-for-fortnite).

After your island’s [calibration](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#calibration) period completes, you should be able to play your game and see XP awards.
