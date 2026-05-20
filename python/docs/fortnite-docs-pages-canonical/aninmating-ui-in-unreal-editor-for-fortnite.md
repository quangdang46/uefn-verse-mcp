## https://dev.epicgames.com/documentation/en-us/fortnite/aninmating-ui-in-unreal-editor-for-fortnite

# Animating UI

Use sequencer to animate UI widgets.

![Animating UI](https://dev.epicgames.com/community/api/documentation/image/a23a8241-f7b1-4bf7-8d1a-677e53805dc8?resizing_type=fill&width=1920&height=335)

Currently, there is a bug where you will not see a UI Animation Condition field in View Bindings when there are no regular view bindings created. You must first create a regular view binding to be able to see the Condition binding fields. This bug is fixed in 33.00.

Use [Sequencer](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#sequencer) in UMG to animate widgets. Widgets animate based on values entered into a [material parameter](https://dev.epicgames.com/documentation/fortnite/conversion-function-setting-material-parameters-in-umg-in-unreal-editor-for-fortnite).

Currently, animating UI only works with [float](https://dev.epicgames.com/documentation/fortnite/verse-glossary) and [int](https://dev.epicgames.com/documentation/fortnite/verse-glossary) type [variables](https://dev.epicgames.com/documentation/fortnite/verse-glossary). More functionality will be added to animating UI in the future.

## Setting Up the Widget

The widget is using the **Tracker widget** from the example in [Setting Material Parameters in UMG](https://dev.epicgames.com/documentation/fortnite/conversion-function-setting-material-parameters-in-umg-in-unreal-editor-for-fortnite).

Create a Tracker widget if you don’t have one ready to use. Then do the following:

## Setting Up the Animation

To add animation to your UI, you’ll open **Sequencer** under the **Event Graph** to animate the icon and "+1". Then you’ll set up the animation in Sequencer.

For this example, the icon pops and the "+1" text appears when the player’s Tracker progresses like in the gif below.

[![For this example, the icon pops and the "+1" text appears when the player’s Tracker progresses.](https://dev.epicgames.com/community/api/documentation/image/426338bd-aada-44da-ab2f-e16c9465674f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/426338bd-aada-44da-ab2f-e16c9465674f?resizing_type=fit)

For information on how to use the Sequencer refer to the [**Sequencer and Control Rig**](sequencer-and-control-rig-in-unreal-editor-for-fortnite) document.

## Animating a Widget’s Visibility

To animate the UI, you’ll identify the widget to animate, then animate the material or texture associated with that widget in Sequencer in the Animation Window. Start the animation by selecting the **IncrementText (+1)**.

1. Select **OnIncrement**, then select the **+1 Text**, then select **+Add** > **Increment Text**.

   [![Select OnIncrement, then select the +1 Text, then select +Add > Increment Text.](https://dev.epicgames.com/community/api/documentation/image/af77fb7f-aea2-43a3-bf22-28cf9dcdcafa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af77fb7f-aea2-43a3-bf22-28cf9dcdcafa?resizing_type=fit)
2. Select the **+plus icon** in the **IncrementText track** and select **Render Opacity**. This allows you to track the Opacity on the animation timeline.

   [![Select the +plus icon in the IncrementText track and select Render Opacity.](https://dev.epicgames.com/community/api/documentation/image/7edce8d1-d5f0-4559-8c85-b74024cbed29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7edce8d1-d5f0-4559-8c85-b74024cbed29?resizing_type=fit)
3. Set a **key** for the beginning of the animation. This determines where the Text begins to fade in and out.

   [![Set a key for the beginning of the animation.](https://dev.epicgames.com/community/api/documentation/image/2a08097e-1a7e-436b-aa6e-f1e0a5d44b6a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2a08097e-1a7e-436b-aa6e-f1e0a5d44b6a?resizing_type=fit)
4. Set the **Render Opacity** to:

   [![Set the Render Opacity levels into seconds the animation should last.](https://dev.epicgames.com/community/api/documentation/image/55efb8ed-f8ad-4193-951a-413003c84e00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55efb8ed-f8ad-4193-951a-413003c84e00?resizing_type=fit)
5. Now you have an animation that fades the text in and out everytime the player gets an elimination.

   [![Now you have an animation that fades the text in and out everytime the player gets an elimination.](https://dev.epicgames.com/community/api/documentation/image/f9b22f4a-f37a-4d15-a700-fbf32e90cd1d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9b22f4a-f37a-4d15-a700-fbf32e90cd1d?resizing_type=fit)

## Animating a Widget’s Position

Add an animation to the text widget’s position so that the text moves up when it’s visible before it fades away.

Now the text moves upwards when it appears.

[![Now the text moves upwards when it appears.](https://dev.epicgames.com/community/api/documentation/image/d195dfb6-2500-4601-aee0-f45b6b8fa29a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d195dfb6-2500-4601-aee0-f45b6b8fa29a?resizing_type=fit)

## Animating a Widget’s Scale

Increase the size of the animated +1 text as it moves to draw attention to the eliminations by animating the widget’s scale settings. This animation gives the illusion of the text "popping" on the screen.

Now the +1 text pops in a dramatic effect when the animation plays.

[![Set the Scale X and Y as keyframes on your OnIncrement timeline.](https://dev.epicgames.com/community/api/documentation/image/0fc4782c-9868-4467-a21e-268bf84e1d3a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0fc4782c-9868-4467-a21e-268bf84e1d3a?resizing_type=fit)

## Animating an Image Brush’s Material Parameter

To make the Icon in the material expand with the Tracker progress, access the Material through Sequencer.

1. Select the **TrackerMaterial** in the **Hierarchy** panel, then click **+Add** > **TrackerMaterial** in the **OnIncrement** animation.

   [![Select the TrackerMaterial Image, then click +Add > TrackerMaterial in the OnIncrement animation.](https://dev.epicgames.com/community/api/documentation/image/9a8c40e0-701c-4455-8f8b-7182cacb58d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a8c40e0-701c-4455-8f8b-7182cacb58d6?resizing_type=fit)
2. Click the **+plus icon** in your **TrackerMaterial** track and select **Transform**. This adds a material track to the TrackerMaterial.

   [![Click the +plus icon in your TrackerMaterial track and select Transform.](https://dev.epicgames.com/community/api/documentation/image/4416b04b-9161-4ce7-8e64-2ed9690e4e98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4416b04b-9161-4ce7-8e64-2ed9690e4e98?resizing_type=fit)
3. Expand the **Transform** and **Scale**tracks. Scale provides a way to increase and decrease the material's **X** and **Y** axes.

   [![Expand the Transform and Scale options.](https://dev.epicgames.com/community/api/documentation/image/32efa5d6-1214-484c-b4f1-20d538855530?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32efa5d6-1214-484c-b4f1-20d538855530?resizing_type=fit)

   You can easily manipulate these parameters in Sequencer when the OnIncrement animation plays. By using Transform you can animate the material scaling the X and Y axes up and back down.
4. Set both X and Y to:

   [![Set the scale parameter's increments and set keys to each incremental increase and decrease.](https://dev.epicgames.com/community/api/documentation/image/e2d42b83-d2ed-4786-b4f9-d6e9550a3959?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e2d42b83-d2ed-4786-b4f9-d6e9550a3959?resizing_type=fit)

Now the animation uses the material parameters from TrackerMaterial to animate the icon like in the gif below.

[![Now the animation uses the material parameters from TrackerMaterial.](https://dev.epicgames.com/community/api/documentation/image/7ec1a606-590c-4255-8321-5ac7dacbb8bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ec1a606-590c-4255-8321-5ac7dacbb8bf?resizing_type=fit)

## Adding an Animation Condition

Now that your animation is ready to go, tie it to a gameplay value so that it plays an animation when a gameplay value changes.

1. Open the **View Bindings** window by selecting **Window** > **View Bindings**.

   [![Open the View Bindings window by selecting Window > View Bindings.](https://dev.epicgames.com/community/api/documentation/image/dd14fec1-f07e-4a11-8759-56d1dadac1cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd14fec1-f07e-4a11-8759-56d1dadac1cd?resizing_type=fit)
2. In the **View Bindings** window, select **+Add Condition**.

   [![In the View Bindings window, select +Add Condition.](https://dev.epicgames.com/community/api/documentation/image/82792f55-0dd5-4532-8ffa-7fd9b3ed35d9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82792f55-0dd5-4532-8ffa-7fd9b3ed35d9?resizing_type=fit)

   The left box is for the gameplay value that you want tracked for changes so that it will play the animation on the right. Right now, +Add Condition only accepts [Float](https://dev.epicgames.com/documentation/fortnite/verse-glossary) or [Int](https://dev.epicgames.com/documentation/fortnite/verse-glossary) values.

   [![Right now, +Add Condition only accepts Float or Int values.](https://dev.epicgames.com/community/api/documentation/image/98b4eb54-b09a-43cd-b89e-13386a74113f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98b4eb54-b09a-43cd-b89e-13386a74113f?resizing_type=fit)
3. Select the left box, then select **MVVM_UEFN_Tracker** > **Value**. This tracks the **Tracker progress** by playing an animation whenever the Tracker value increments.

   [![Select the left box, then select MVVM_UEFN_Tracker > Value.](https://dev.epicgames.com/community/api/documentation/image/664f1cff-e551-4c0f-9bdd-4b950ad6f00f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/664f1cff-e551-4c0f-9bdd-4b950ad6f00f?resizing_type=fit)
4. Click the **middle dropdown** and select **More Than (>)**.

   The 2 boxes in the middle are the conditions that you want fulfilled to play the animation. Whenever the value changes, it checks if it’s within that condition and if it is, it will play the animation.

   By setting it to More Than **(>) 0.0**, the UI will play the animation whenever this value changes.

   [![Click the middle dropdown and select More Than (>).](https://dev.epicgames.com/community/api/documentation/image/5fbd0eae-c2c3-4fe1-bac6-4294aab94adf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5fbd0eae-c2c3-4fe1-bac6-4294aab94adf?resizing_type=fit)
5. Select the right box, then select **WBP_{YourWidgetName}** > **Queue Play Animation**. The right box is the action to take when this value fulfills the condition. In this case, to play the **OnIncrement animation** created above.

   [![Select the right box, then select WBP_{YourWidgetName} > Queue Play Animation.](https://dev.epicgames.com/community/api/documentation/image/881c74d6-2d76-437b-a091-ae061bbf30ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/881c74d6-2d76-437b-a091-ae061bbf30ab?resizing_type=fit)

   A list of options pertaining to the animation you want to play appear in View Bindings.

   - **In Animation** = Play
   - **Start at Time** = Select a time
   - **Num Loops to Play** = Number of times the animation loops
   - **Play Mode** = **Forward**, Reverse, or Ping Pong
   - **Playback Speed** = Speed up or slow the animation down
   - **Restore State** = Restores the animation to its default state

   [![A list of options pertaining to the animation you want to play appear in View Bindings.](https://dev.epicgames.com/community/api/documentation/image/3736b040-5b05-4f5c-85b1-db166aab1caa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3736b040-5b05-4f5c-85b1-db166aab1caa?resizing_type=fit)
6. Click the **link icon** next to **InAnimation**, then select **WBP_{YourWidgetName}** > **OnIncrement** > **Select**.

   [![Click the link icon next to InAnimation, then select WBP_{YourWidgetName} > OnIncrement > Select.](https://dev.epicgames.com/community/api/documentation/image/22c97e50-af64-4fa2-a7ef-c4238bea5406?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22c97e50-af64-4fa2-a7ef-c4238bea5406?resizing_type=fit)

Now your animation is set up to play whenever the Tracker progresses.

[![Now your animation is set up to play whenever the Tracker progresses.](https://dev.epicgames.com/community/api/documentation/image/c000cb7d-cc50-4d09-841b-c379036c368c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c000cb7d-cc50-4d09-841b-c379036c368c?resizing_type=fit)

## Final Result

As the players eliminate enemies or NPCs, the UI shows the elimination progress with the icon popping and the +1 appearing, popping, and disappearing.

[![As the players eliminate enemies or NPCs, the UI shows the elimination progress with the icon popping and the +1 appearing, popping, and disappearing.](https://dev.epicgames.com/community/api/documentation/image/4932d335-7e50-4b98-b902-abbfd844d787?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4932d335-7e50-4b98-b902-abbfd844d787?resizing_type=fit)
