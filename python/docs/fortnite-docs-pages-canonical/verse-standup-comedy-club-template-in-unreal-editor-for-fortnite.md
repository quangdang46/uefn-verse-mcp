## https://dev.epicgames.com/documentation/en-us/fortnite/verse-standup-comedy-club-template-in-unreal-editor-for-fortnite

# Stand-Up Comedy Club Template

Learn how to create a stand-up comedy show and other linear content using this UEFN template.

![Stand-Up Comedy Club Template](https://dev.epicgames.com/community/api/documentation/image/9c765df7-26d7-4c66-bce8-60f2efed972e?resizing_type=fill&width=1920&height=335)

This tutorial is a companion document to the **Verse Stand-Up template**, which showcases how to use devices that support a social and cinematic experience inside of a comedy club:

- Using detailed, MetaHumans Animator assets with the [**Character devices**](https://www.fortnite.com/fortnite/en-US/creative/docs/using-character-devices-in-fortnite-creative)
- Triggering gameplay events on player input bindings with [**Input Trigger devices**](https://www.fortnite.com/fortnite/en-US/creative/docs/using-input-trigger-devices-in-fortnite-creative)
- Locking a player in place to view the experience with the [**Chair device**](https://www.fortnite.com/fortnite/en-US/creative/docs/using-chair-devices-in-fortnite-creative)

A **Verse** device runs the show, with the key concepts of the Verse code explained [below](https://dev.epicgames.com/documentation/fortnite/verse-standup-comedy-club-template-in-unreal-editor-for-fortnite).

The Verse Stand-Up template can be found in the **Feature Examples** section of UEFN (Unreal Editor for Fortnite).

[![Stand Up Template UEFN](https://dev.epicgames.com/community/api/documentation/image/1adc0fc9-ff6e-4683-bb22-9d1b5744d59c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1adc0fc9-ff6e-4683-bb22-9d1b5744d59c?resizing_type=fit)

**Devices used:**

- 1 x [Chair](https://www.fortnite.com/fortnite/en-US/creative/docs/using-chair-devices-in-fortnite-creative)
- 4 x [Input Trigger](https://www.fortnite.com/fortnite/en-US/creative/docs/using-input-trigger-devices-in-fortnite-creative)
- 4 x [Character](https://www.fortnite.com/fortnite/en-US/creative/docs/using-character-devices-in-fortnite-creative)
- 6 x [Cinematic Sequence](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite)

The **Verse** concepts used in this tutorial are:

- Subscriptions
- If Statements
- Arrays
- Cinematic Sequences
- Chair device API
- Input Trigger device API

Be aware that most of the modified settings for device interactions are done using Verse code, therefore the modified user options for most devices will appear slimmed down.

## Island Settings

Here are the modified Island Settings for the Verse Stand-Up template:

| Option | Value | Explanation |
| --- | --- | --- |
| **Max Players** | 1 | This is a single-player experience. |
| **Team Size** | 1 | Only one team is necessary. |
| **Join In Progress** | Spectate | Players will spectate if they join a game that has already begun. |
| **After Last Spawn Go To** | Team Index: 1 | Players will respawn on their team. |
| **Voice Chat** | All | Voice chat is allowed between players. |
| **Start With Pickaxe** | False | Players will not start the game with a pickaxe. |
| **Allow Spectating Other Teams** | Disallowed | Players cannot spectate another team. |
| **Time Limit** | 120 | The time limit is set to two hours. |
| **Hide Back Bling** | True | Back bling will not appear on this island. |
| **Allow Mantling/Hurdling** | False | Players will not be able to hurdle or mantle. |
| **Sprinting Energy Cost Per Second** | 2.0 | The energy cost consumed by sprinting. |
| **Invincibility** | True | Players are invincible. |
| **Allow Building** | None | Players cannot build. |
| **Building Can Destroy Environment** | False | Building cannot destroy the environment. |
| **Environment Damage** | Off | Players cannot damage the environment. |
| **Infinite Building Materials** | False | Building is disabled in this experience. |
| **Time of Day** | 12:00 AM | Night time setting. |
| **Light Brightness** | 0 | All light sources in this experience are emanating from lamps. |
| **Fog Thickness** | 30% | Environment is slightly foggy. |
| **Fog Color** | Blue | Determines fog color. |
| **Custom Victory Callout** | Thank you for coming to The Cheese Cannery | What players see after finishing the game. |
| **Show Elimination Feed** | False | Eliminations are not displayed. |
| **Show Wood/Stone/Metal Resource Count** | False | Resources are not displayed. |
| **Show Party Eliminations** | False | Party eliminations are not displayed. |
| **Debug** | True | Debug features are enabled. |
| **Fast Iteration Mode** | True | Fast Iteration between Edit and Play mode is enabled. |

## Chair Device

As the player walks into the comedy club, they see a chair in front of a lit-up stage. They are prompted to sit in this chair. Sitting in the chair keeps the player in a fixed location and sets in motion the chain of events that will take them through the rest of the experience.

[![Chair device](https://dev.epicgames.com/community/api/documentation/image/cf16e387-c82d-4a83-afd1-8748c5975c53?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf16e387-c82d-4a83-afd1-8748c5975c53?resizing_type=fit)

Here are the modified **User Options** for the Chair device:

| Option | Value | Explanation |
| --- | --- | --- |
| **Chair Model** | Custom | For this experience, the chair is actually made invisible, then replaced with a Fortnite chair prop in order to better fit the club environment. |
| **Interaction Angle** | 180 degrees | Determines the angle in either direction from the front of the chair needed to interact with it. |
| **Interaction Radius** | 1.2m | Determines the distance the player can enter the chair from. |

## Input Trigger Devices

An [Input Trigger device](https://dev.epicgames.com/documentation/fortnite/verse-standup-comedy-club-template-in-unreal-editor-for-fortnite) goes hand-in-hand with the Chair device. It binds player inputs to a variety of actions, which are triggered each time the player presses the reassigned button. The input triggers are configured to allow the player to change the cameras as the performance is taking place.

[![Input Trigger device](https://dev.epicgames.com/community/api/documentation/image/91eab5a9-5354-4cf9-8168-b90a8a9aae5d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/91eab5a9-5354-4cf9-8168-b90a8a9aae5d?resizing_type=fit)

The device contains twelve available inputs to choose from. Once you choose an input, you can add a HUD description to clarify what the new input does.

[![Creative Inputs](https://dev.epicgames.com/community/api/documentation/image/850b082f-26e0-4f3a-a4d0-ee46927511d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/850b082f-26e0-4f3a-a4d0-ee46927511d2?resizing_type=fit)

Here are the modified **User Options** for this device. Each of the devices will have a different binding and HUD Description as they are bound to distinct Cinematic Sequence devices.

| Option | Value | Explanation |
| --- | --- | --- |
| **Creative Input** | Custom 5 (Sprint) | Defines the input this device is listening for. |
| **HUD Description** | "Previous Camera" | An opportunity to explain the new input to the player. |
| **Registered Player Behavior** | Require Registration | - REQUIRE REGISTRATION: Players must be registered and counted by the device in order to be eligible. - ADD REGISTERED: Players can be either registered or counted by the device. - IGNORE REGISTERED: Players must be counted by the device but NOT registered. |

## Character Devices

The Character devices are ways for you to interact directly with the player or with other characters in a scene. This template uses four characters that cycle during the on-stage routine.

[![character spawner device](https://dev.epicgames.com/community/api/documentation/image/456a52af-5e85-499f-a607-f9a4202d3302?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/456a52af-5e85-499f-a607-f9a4202d3302?resizing_type=fit)

Here are the modified **User Options** for the Character device:

| Option | Value | Explanation |
| --- | --- | --- |
| **Character** | Pick a character | Determines which character is displayed. |
| **Custom Idle** | Sitting | Chooses a custom idle position for the character. |
| **Random Idle Start** | True | Determines whether the idle should start at a random position. |

The main character is sitting on a staircase backstage, and the rest of the characters are waiting in a small room in the back.

[![other characters](https://dev.epicgames.com/community/api/documentation/image/7eb1d31f-0f88-4f5b-8e1d-03962b983418?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7eb1d31f-0f88-4f5b-8e1d-03962b983418?resizing_type=fit)

Experiment with different character skins from the **Character** dropdown menu and see how they look on stage!

This template uses imported [MetaHuman](https://www.unrealengine.com/metahuman) animations. To learn more about how these animations were captured and imported, see the [Importing MetaHuman Animations](importing-metahuman-animations-in-unreal-editor-for-fortnite) page.

## Cinematic Sequence Devices

The six Cinematic Sequence devices allow the player to view the show from various angles while sitting in the chair device.

This page does not go into detail about creating cinematic sequences. For more information, see the [Sequencer and Control Rig](https://dev.epicgames.com/documentation/fortnite/sequencer-and-control-rig-in-unreal-editor-for-fortnite) page, and for a deeper dive, check out the [How To Make Movies in Unreal Engine](https://docs.unrealengine.com/how-to-make-movies-in-unreal-engine/).

[![Cinematic sequence devices](https://dev.epicgames.com/community/api/documentation/image/bac9820d-5f77-4b42-9bc0-2a9d0f33a5f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bac9820d-5f77-4b42-9bc0-2a9d0f33a5f8?resizing_type=fit)

The only modification for this device is the loaded cinematic sequence.

[![Cinematic sequence options](https://dev.epicgames.com/community/api/documentation/image/f5a6d12c-993e-431e-b139-33b8f62a6731?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f5a6d12c-993e-431e-b139-33b8f62a6731?resizing_type=fit)

## How Verse Runs the Show

This template uses Verse to start the show when a player sits in the chair device, as well as change their camera to a cinematic view called **TV mode**. It also allows the player to switch between multiple cameras, as well as return to **TV mode** or **Free Look** for different viewing experiences.

[Create a new Verse Device](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite) in your project called `show_template_device.verse` using [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite) and drag the device into the template. Double-click your Verse file to open it in Visual Studio Code.

You’ve set up devices in your template that help run the standup show, and now you’ll reference those devices in your [code](https://dev.epicgames.com/documentation/fortnite/verse-glossary#code).

Add the following fields to the `show_template_device` file:

1. First, above the `show_template_device` [class](https://dev.epicgames.com/documentation/fortnite/verse-glossary) definition, add a `log_channel` named `log_show_template_device`.

   Verse

   ```
        # Create a custom log channel for the show_template_device. This helps with log filtering in complex games with lots of log sources.
        log_show_template_device := class(log_channel){}
   		
        # A Verse-authored creative device that can be placed in a level
        show_template_device := class(creative_device):
   ```

    # Create a custom log channel for the show_template_device. This helps with log filtering in complex games with lots of log sources.
   log_show_template_device := class(log_channel){}
   # A Verse-authored creative device that can be placed in a level
   show_template_device := class(creative_device):
2. Now at the top of the `show_template_device` class definition, add a logger that uses the `log_show_template_device` channel, so you can tell which `Print()` statements are coming from this device.

   Verse

   ```
        # A Verse-authored creative device that can be placed in a level
        show_template_device := class(creative_device):
   		
            # Logger that uses custom log channel.
            Logger:log = log{Channel := log_show_template_device}
   ```

    # A Verse-authored creative device that can be placed in a level
   show_template_device := class(creative_device):
   # Logger that uses custom log channel.
   Logger:log = log{Channel := log_show_template_device}
3. An [editable](https://dev.epicgames.com/documentation/fortnite/verse-glossary#editable) chair device named `TheChair`. This is the chair players will sit in to start the standup show.

   Verse

   ```
        # The chair device the player should sit in.
        @editable
        TheChair:chair_device = chair_device{}
   ```

    # The chair device the player should sit in.
   @editable
   TheChair:chair_device = chair_device{}
4. Two editable [cinematic sequence devices](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) named `MainSequence` and `TVModeSequence`. The `MainSequence` is the cinematic sequence that runs the standup show, driving animation and audio on the character device in the level. The `TVModeSequence` switches the player’s camera to a viewing mode that follows along with the `MainSquence`, switching between multiple angles.

   Verse

   ```
        # The sequence that drives animation and audio on the character device in the level.
        @editable
        MainSequence:cinematic_sequence_device = cinematic_sequence_device{}
        # The sequence that drives the TV mode sequence for viewing in the level.
        @editable
        TVModeSequence:cinematic_sequence_device = cinematic_sequence_device{}
   ```

    # The sequence that drives animation and audio on the character device in the level.
   @editable
   MainSequence:cinematic_sequence_device = cinematic_sequence_device{}
   # The sequence that drives the TV mode sequence for viewing in the level.
   @editable
   TVModeSequence:cinematic_sequence_device = cinematic_sequence_device{}
5. An editable [array](https://dev.epicgames.com/documentation/fortnite/verse-glossary) of `cinematic_sequence_device` named `CameraSwitches`. This array holds references to each of the cameras players can switch between during the show.

   Verse

   ```
        # A list of alternative camera sequences that are provided to view from during the main sequence.
        @editable
        CameraSwitches:[]cinematic_sequence_device = array{}
   ```

    # A list of alternative camera sequences that are provided to view from during the main sequence.
   @editable
   CameraSwitches:[]cinematic_sequence_device = array{}
6. Four editable `input_trigger_device`s. Each of these devices takes player input to swap between different camera modes. The `ReturnToFreeLook` trigger returns the player to the default camera, while `ReturnToTVMode` returns the player to the `TVModeSequence`. The `NextCamera` and `PreviousMode` camera switches the player between the different cinematic sequences in the `CameraSwitches` array.

   Verse

   ```
        # An input trigger that will return us to free look while in the chair.
        @editable
        ReturnToFreeLook:input_trigger_device = input_trigger_device{}
   		
        # An input trigger that will return us to TV mode when appropriate in the chair.
        @editable
        ReturnToTVMode:input_trigger_device = input_trigger_device{}
   		
        # An input trigger that will choose the next camera while in the chair.
        @editable
   ```
7. An optional cinematic sequence device [variable](https://dev.epicgames.com/documentation/fortnite/verse-glossary) named `CurrentSequence`. If a cinematic sequence such as `TVModeSequence` is playing, this option stores a reference to it. You don’t want to play multiple cinematic sequences for the character at once, so you can use this option to turn the current sequence off when switching to a new one.

   Verse

   ```
        # The alternative camera sequence that is playing if valid.
        var CurrentSequence:?cinematic_sequence_device = false
   ```

    # The alternative camera sequence that is playing if valid.
   var CurrentSequence:?cinematic_sequence_device = false
8. Two logic variables named `MainSequencePlaying` and `InTvMode`. These let you track when the `MainSequence` or `TVModeSequence` are playing respectively.

   Verse

   ```
        # Helps us track when the main sequence on the character device is playing.
        var MainSequencePlaying:logic = false
   		
        # When we are in TV mode.
        var InTVMode:logic = false
   ```

    # Helps us track when the main sequence on the character device is playing.
   var MainSequencePlaying:logic = false
   # When we are in TV mode.
   var InTVMode:logic = false
9. A variable int named `CurrentCameraIndex`. This tracks the index of the cinematic sequence in the `CameraSwitches` array that is currently playing.

   Verse

   ```
        # Keeps track of what camera we are viewing when using other cameras besides TV Mode.
        var CurrentCameraIndex:int = -1
   ```

    # Keeps track of what camera we are viewing when using other cameras besides TV Mode.
   var CurrentCameraIndex:int = -1
10. Five optional `cancelable` variables that track subscriptions for all the [events](https://dev.epicgames.com/documentation/fortnite/verse-glossary) referenced in this template. Different [functions](https://dev.epicgames.com/documentation/fortnite/verse-glossary) need to run when the player switches between cameras, returns to free look or TV mode, or exits the chair device. Later in this tutorial, you will [subscribe](https://dev.epicgames.com/documentation/fortnite/verse-glossary#subscribe) the functions to the events that trigger them, and store a reference to each subscription so you can cancel them when they’re no longer needed.

    Verse

    ```
         # Subscriptions to all the events we listen for while running.
         var ReturnToFreeLookSubscription:?cancelable = false
         var NextCameraSubscription:?cancelable = false
         var PrevCameraSubscription:?cancelable = false
         var ReturnToTVModeSubscription:?cancelable = false
         var ChairExitSubscription:?cancelable = false
    ```

     # Subscriptions to all the events we listen for while running.
    var ReturnToFreeLookSubscription:?cancelable = false
    var NextCameraSubscription:?cancelable = false
    var PrevCameraSubscription:?cancelable = false
    var ReturnToTVModeSubscription:?cancelable = false
    var ChairExitSubscription:?cancelable = false
11. Save the script in Visual Studio Code and [compile](https://dev.epicgames.com/documentation/fortnite/verse-glossary#compile) it to update your Verse-authored device in the level.
12. Select the `show_template_device` in your template. In the **Details** panel, assign each device reference in your script to the associated device in the level, including each of your input triggers and cinematic sequences.

    [![Show Template Device Setup](https://dev.epicgames.com/community/api/documentation/image/e81bb7a3-6ddc-4621-a56b-eb80f372904b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e81bb7a3-6ddc-4621-a56b-eb80f372904b?resizing_type=fit)

### Triggering the Sequence

The show starts when a player sits in the chair device, you’ll want the cinematic sequence to start once the player is seated. Follow the steps below to trigger the main sequence when a player sits in the chair, as well as start the TV mode so the player can watch along.

1. Add a new function `RunSequence()` to the `show_template_device` class. This function takes the [agent](https://dev.epicgames.com/documentation/fortnite/verse-glossary#agent) who started the show and starts both the MainSequence and `TVModeSequence`. Add the  modifier to `RunSequence()` to let it run asynchronously. This function needs to be asynchronous so that you can run other code [concurrently](https://dev.epicgames.com/documentation/fortnite/verse-glossary#concurrent) with it, and allow the player to swap between camera views without interrupting the `RunSequence()` code.

   Verse

   ```
        # Handles running the main sequence which runs the character and TV mode sequences for viewing and then calls a function to await finishing.
        RunSequence(Agent:agent)<suspends>:void =
   ```

    # Handles running the main sequence which runs the character and TV mode sequences for viewing and then calls a function to await finishing.
   RunSequence(Agent:agent)&lt;suspends&gt;:void =
2. In `RunSequence()`, [call](https://dev.epicgames.com/documentation/fortnite/verse-glossary#call) `Sleep()` for a second to let the animation of the player sitting in the chair finish before starting the show. Then call `Play()` on the `MainSequence`, and set `MainSequencePlaying` to true.

   Verse

   ```
        # Sleep for a second because we just entered the chair and the animation to sit takes a moment.
        Sleep(1.0)
   		
        # Run the Main sequence on the character device and the TV mode viewing sequence.
        Logger.Print("Main Sequence Playing")
        set MainSequencePlaying = true
        MainSequence.Play()
   ```

    # Sleep for a second because we just entered the chair and the animation to sit takes a moment.
   Sleep(1.0)
   # Run the Main sequence on the character device and the TV mode viewing sequence.
   Logger.Print(&quot;Main Sequence Playing&quot;)
   set MainSequencePlaying = true
   MainSequence.Play()
3. Call `Play()` on the `TVModeSequence`, passing the agent who started the show to change their camera to the cinematic view. Set `InTVMode` to true, and call a new function that awaits the ending of the `MainSequence` called `AwaitMainSequenceEnding()`, passing the agent. You’ll set up this function in the next step. Your completed `RunSequence()` code should look like the following:

   Verse

   ```
        # Handles running the main sequence which runs the character and TV mode sequences for viewing and then calls a function to await finishing.
        RunSequence(Agent:agent)<suspends>:void =

            # Sleep for a second because we just entered the chair and the animation to sit takes a moment.
            Sleep(1.0)

            # Run the Main sequence on the character device and the TV mode viewing sequence.
            Logger.Print("Main Sequence Playing")
            set MainSequencePlaying = true
            MainSequence.Play()
   ```
4. Add a new function `AwaitMainSequecingEnding()` to the `show_template_device` class that takes the `agent` from `RunSequence()`. This function also needs the `<suspends>` modifier since you want it to run in the background and trigger when the `MainSequence` ends.

   Verse

   ```
        # When the main sequence finishes, we clear the flag so that if the player sits back down, it will play again.
        AwaitMainSequencingEnding(Agent:agent)<suspends>:void =
   ```

    # When the main sequence finishes, we clear the flag so that if the player sits back down, it will play again.
   AwaitMainSequencingEnding(Agent:agent)&lt;suspends&gt;:void =
5. In `AwaitMainSequencingEnding()`, call `Await()` on the `MainSequence.StoppedEvent()`. When the `MainSequence` ends, set `MainSequencePlaying` to `false`, and kick the player out of the chair using the chair’s `Eject()` function. Your completed `AwaitMainSequencingEnding()` function should look like the following:

   Verse

   ```
        # When the main sequence finishes, we clear the flag so that if the player sits back down, it will play again.
        AwaitMainSequencingEnding(Agent:agent)<suspends>:void =
            MainSequence.StoppedEvent.Await()
            Logger.Print("Main Sequence Ended")
            set MainSequencePlaying = false

            # Kick the player out of the chair after the performance
            TheChair.Eject(Agent)
   ```

    # When the main sequence finishes, we clear the flag so that if the player sits back down, it will play again.
   AwaitMainSequencingEnding(Agent:agent)&lt;suspends&gt;:void =
   MainSequence.StoppedEvent.Await()
   Logger.Print(&quot;Main Sequence Ended&quot;)
   set MainSequencePlaying = false
   # Kick the player out of the chair after the performance
   TheChair.Eject(Agent)
6. Add two new functions `DoReturnToTVMode()` and `DoReturnToFreeLook()` to the `show_template_device` class. These functions handle the [logic](https://dev.epicgames.com/documentation/fortnite/verse-glossary) when a player returns to the TV mode or free look respectively, but you’ll leave them empty for now and fill them out in a later step.

   Verse

   ```
        # Returns us to our TV viewing mode sequence by checking where the main sequence is and aligning our playback to that point.
        DoReturnToTVMode(Agent:agent):void =
            Logger.Print("Return to TV Mode")
   		
        # Determine if we are in TV mode or another camera sequence and return control to the main player camera.
        DoReturnToFreeLook(Agent: agent):void =
            Logger.Print("Return to Free Look")
   ```

    # Returns us to our TV viewing mode sequence by checking where the main sequence is and aligning our playback to that point.
   DoReturnToTVMode(Agent:agent):void =
   Logger.Print(&quot;Return to TV Mode&quot;)
   # Determine if we are in TV mode or another camera sequence and return control to the main player camera.
   DoReturnToFreeLook(Agent: agent):void =
   Logger.Print(&quot;Return to Free Look&quot;)
7. Add a new function `OnSeated()` to the `show_template_device` class that takes the agent who sat in `TheChair`.

   Verse

   ```
        # This function handles the player sitting down and starting up the performance if it isn't already running and setting up the input triggers.
        OnSeated(Agent:agent):void =
            Logger.Print("Player sat down")
   ```

    # This function handles the player sitting down and starting up the performance if it isn&#39;t already running and setting up the input triggers.
   OnSeated(Agent:agent):void =
   Logger.Print(&quot;Player sat down&quot;)
8. In `OnSeated()`, if the `MainSequence` is not already playing, spawn a `RunSequence()` function, passing the agent who sat in the chair device. Otherwise, call `DoReturnToTVMode()` with the same agent.

   Verse

   ```
        # This function handles the player sitting down and starting up the performance if it isn't already running and setting up the input triggers.
        OnSeated(Agent:agent):void =
            Logger.Print("Player sat down")
   		
            # If the main sequence is not playing on the character device in the level, run it, otherwise if it is running then just return to the TV mode viewing experience.
            if (MainSequencePlaying = false):
                spawn{RunSequence(Agent)}
            else:
                DoReturnToTVMode(Agent)
   ```

    # This function handles the player sitting down and starting up the performance if it isn&#39;t already running and setting up the input triggers.
   OnSeated(Agent:agent):void =
   Logger.Print(&quot;Player sat down&quot;)
   # If the main sequence is not playing on the character device in the level, run it, otherwise if it is running then just return to the TV mode viewing experience.
   if (MainSequencePlaying = false):
   spawn{RunSequence(Agent)}
   else:
   DoReturnToTVMode(Agent)
9. Add a new function `OnChairExited()` to the `show_template_device` class that takes the player who exited the chair. You’ll fill out the logic for this function in a later step.

   Verse

   ```
        # Handles the player leaving the chair and removing access to the input triggers that are available while in the chair.
        OnChairExited(Agent:agent):void =
            Logger.Print("Player got up")
   ```

    # Handles the player leaving the chair and removing access to the input triggers that are available while in the chair.
   OnChairExited(Agent:agent):void =
   Logger.Print(&quot;Player got up&quot;)
10. In `OnBegin()`, subscribe `TheChair.SeatedEvent` to the `OnSeated()` function. Now whenever a player sits in `TheChair`, the show will run.

    Verse

    ```
         # Runs when the device is started in a running game.
         OnBegin<override>()<suspends>:void =
             Logger.Print("Standup Template device started")
             TheChair.SeatedEvent.Subscribe(OnSeated)
    ```

     # Runs when the device is started in a running game.
    OnBegin&lt;override&gt;()&lt;suspends&gt;:void =
    Logger.Print(&quot;Standup Template device started&quot;)
    TheChair.SeatedEvent.Subscribe(OnSeated)

Save the script in Visual Studio Code, compile it, and click **Launch Session** in the UEFN toolbar to playtest the template. When you run your game, sitting in the chair device should start your show, and set the player’s camera to cinematic mode. When the show ends, the player should be kicked out of the chair.

### Switching Cameras

During the show, the player sitting in the `TheChair` can switch between multiple different camera views, handled by different cinematic sequences. Follow the steps below to set up the logic for switching between these different sequences.

1. Add a new function `DoCameraSwitch()` to the `show_template_device` class. This function takes the agent whose camera you’re switching, as well as an `int` corresponding to the cinematic sequence index in `CameraSwitches`.

   Verse

   ```
        # Switches us between camera sequences that have been specified by stopping any current ones and moving to the next appropriate one on the list.
        DoCameraSwitch(Agent:agent, Value:int):void =
   ```

    # Switches us between camera sequences that have been specified by stopping any current ones and moving to the next appropriate one on the list.
   DoCameraSwitch(Agent:agent, Value:int):void =
2. In `DoCameraSwitch()`, in an `if` statement, get the cinematic sequence at the Value index in the `CameraSwitches` array. Then stop any currently playing sequences by checking if `CurrentSequence` contains a cinematic sequence and calling `Stop()` on it.

   Verse

   ```
        # Switches us between camera sequences that have been specified by stopping any current ones and moving to the next appropriate one on the list.
        DoCameraSwitch(Agent:agent, Value:int):void =
            if (CameraSwitch := CameraSwitches[Value]):
                Logger.Print("Switching Cameras to {Value}")
   		
                # Stop any currently playing other camera sequence.
                if (PlayingSequence := CurrentSequence?):
                    PlayingSequence.Stop(Agent)
   ```

    # Switches us between camera sequences that have been specified by stopping any current ones and moving to the next appropriate one on the list.
   DoCameraSwitch(Agent:agent, Value:int):void =
   if (CameraSwitch := CameraSwitches[Value]):
   Logger.Print(&quot;Switching Cameras to {Value}&quot;)
   # Stop any currently playing other camera sequence.
   if (PlayingSequence := CurrentSequence?):
   PlayingSequence.Stop(Agent)
3. Start playing the new cinematic sequence by calling `Play()` on `CameraSwitch`. Then set `CurrentSequence` to say which sequence is currently playing. Finally, `Register()` the `agent` whose camera you’re switching with the `ReturnToTVMode` and `ReturnToFreeLook` input triggers to allow them to return to those modes when viewing other cameras. Your completed `DoCameraSwitch()` function should look like the following:

   Verse

   ```
        # Switches us between camera sequences that have been specified by stopping any current ones and moving to the next appropriate one on the list.
        DoCameraSwitch(Agent:agent, Value:int):void =
            if (CameraSwitch := CameraSwitches[Value]):
                Logger.Print("Switching Cameras to {Value}")
   		
                # Stop any currently playing other camera sequence.
                if (PlayingSequence := CurrentSequence?):
                    PlayingSequence.Stop(Agent)
   		
                # Start up the new camera viewing sequence.
   ```
4. To switch between the next and previous cameras, you’ll set up two very similar functions, `DoNextCamera()` and `DoPreviousCamera()`. You’ll fill out the logic for the next camera first, so add a new function `DoNextCamera()` to the `show_template_device` class. This function takes the `agent` whose camera you’re switching.

   Verse

   ```
        # Switches to the next camera on our list, or the first if we are in TV mode.
        DoNextCamera(Agent:agent):void =
            Logger.Print("Next Camera")
   ```

    # Switches to the next camera on our list, or the first if we are in TV mode.
   DoNextCamera(Agent:agent):void =
   Logger.Print(&quot;Next Camera&quot;)
5. In `DoNextCamera()`, check if the player is currently in TV mode. If so, `Stop()` the `TVModeSequence`, set `InTVMode` to false and set `CurrentCameraIndex` to `-1`. You use `-1` here because you want to index into the next cinematic sequence the `CameraSwitches` array, which would be index `0`.

   Verse

   ```
        # If we are currently viewing from TV Mode, end that sequence and clear associated values.
        if (InTVMode?):
            TVModeSequence.Stop(Agent)
            set InTVMode = false
            set CurrentCameraIndex = -1
   ```

    # If we are currently viewing from TV Mode, end that sequence and clear associated values.
   if (InTVMode?):
   TVModeSequence.Stop(Agent)
   set InTVMode = false
   set CurrentCameraIndex = -1
6. You then need to figure out the next camera to switch to based on the index of the current camera. To do this, set a new variable `NextCameraValue` to the `Mod` of the `CurrentCameraIndex + 1` and `CameraSwitches.Length`. This lets you clamp `NextCameraValue` to a [value](https://dev.epicgames.com/documentation/fortnite/verse-glossary#value) that’s between `0` and the length of `CameraSwitches` and prevents you from getting a `NextCameraValue` that’s outside the `CameraSwitches` array. Once you have `NextCameraValue`, set `CurrentCameraValue` to `NextCameraValue`, and call `DoCameraSwitch()` passing the `agent` and the `CurrentCameraIndex`. Your completed `DoNextCamera()` function should look like the following:

   Verse

   ```
        # Switches to the next camera on our list, or the first if we are in TV mode.
        DoNextCamera(Agent:agent):void =
            Logger.Print("Next Camera")
   		
            # If we are currently viewing from TV Mode, end that sequence and clear associated values.
            if (InTVMode?):
                TVModeSequence.Stop(Agent)
                set InTVMode = false
                set CurrentCameraIndex = -1
   		
   ```
7. To switch to the previous camera, add a new function named `DoPreviousCamera()` to the `show_template_device` class. Copy the code from `DoNextCamera()` into this function. When checking if the player is in TV mode, set `CurrentCameraIndex` to `0` instead of `-1`. Also, change `NextCameraValue` to be the `Mod` of `CurrentCameraIndex - 1` and `CameraSwitches.Length.` Your completed `DoPreviousCamera()` function should look like the following:

   Verse

   ```
        # Switches us to the previous camera on the list or last camera if we are leaving TV mode.
        DoPreviousCamera(Agent:agent):void =
            Logger.Print("Prev Camera")
   		
            # If we are currently viewing from TV Mode, end that sequence and clear associated values.
            if (InTVMode?):
                TVModeSequence.Stop(Agent)
                set InTVMode = false
                set CurrentCameraIndex = 0
   		
   ```

When a player is sitting in `TheChair` and viewing from a different camera in `CameraSwitches`, they can return to either TV mode or Free Look. You set up the `DoReturnToFreeLook()` and `DoReturnToTVMode()` functions earlier, and you’ll fill them out now.

### Linking Everything Together

You’ve set up a lot of functions in the previous part of this tutorial, and now it’s time to link them all together to the various input triggers that call them.

Save the script in Visual Studio Code, compile it, and click **Launch Session** in the UEFN toolbar to playtest the template. When you playtest, sitting in the chair device should start the show. During the show, you should be able to switch between TV mode, free look, and multiple other camera angles. Returning to TV mode should align the TV mode sequence with the main sequence. When the show ends, you should be returned to free look and exit the chair.
