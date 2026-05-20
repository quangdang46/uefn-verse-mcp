## https://dev.epicgames.com/documentation/en-us/fortnite/create-your-own-npc-medic-in-unreal-editor-for-fortnite

# Create Your Own NPC Medic

Use Verse Code to create a custom NPC medic.

![Create Your Own NPC Medic](https://dev.epicgames.com/community/api/documentation/image/6c822e28-d978-44f6-b914-b38bc509583a?resizing_type=fill&width=1920&height=335)

Medics are a common character archetype in many games. A medic's job is to heal nearby characters, and they help their teammates recover after sustaining damage. Medics serve different roles depending on the game, for instance, doctors that serve patients in a hospital, combat medics that help their team fight as well as heal, or neutral stations that heal anyone.

The medic character you'll create in this example follows a set of logic rules.

- **Idle:**
- **Begin Healing Agents**
- **Healing Loop**
- **Navigate to Agent**

The medic begins idle, and patrols until an agent enters the healing zone. That agent gets added to the medic's healing queue. The medic needs to track the agent it needs to heal next, and a queue provides a useful data structure for this purpose since queues are a first-in, first-out data structure. This means the character that enters the healing zone first will be the first to get healed.

Once the medic gets the agent it needs to heal next, it first checks if the agent's health is below the healing threshold. If so, it begins healing them at a specific rate until the agent's health reaches the threshold, or the agent exits the healing zone. While healing, the medic will attempt to stay close to the agent by continuously navigating to them. Once the agent's health is back up to the threshold, the medic gets the next agent to heal and starts the process over again. If there are no agents to heal, the medic goes back to being idle.

You can visualize the logic of the medic NPC using the Finite-State Machine below. For more information on finite-state machines, check out [Understanding NPC Behaviors](https://dev.epicgames.com/documentation/fortnite/understanding-npc-behavior-in-unreal-editor-for-fortnite).

[![Medic FSM](https://dev.epicgames.com/community/api/documentation/image/580deac5-c624-4574-b49d-f8e9c600346d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/580deac5-c624-4574-b49d-f8e9c600346d?resizing_type=fit)

By completing this guide, you'll learn how to create a custom medic character using the NPC Behavior Script that heals other nearby characters when their health is under a certain threshold. The complete script is included at the end of this guide for reference.

## Creating a new NPC Behavior Script

To start creating your own NPC Medic Character, create a new NPC Behavior script named **medic_example**. For more information on creating your own NPC Behavior script, see [Create Your Own NPC Behavior](https://dev.epicgames.com/documentation/fortnite/create-custom-npc-behavior-in-unreal-editor-for-fortnite). Open the Verse file in Visual Studio Code.

Follow these steps to create an NPC Behavior Script in UEFN that spawns a medic character that heals nearby players.

## Implementing the Healing Queue

The NPC Behavior Script starts with several values used for character movement and debug visualization. You won't need all of them in this script, so you'll remove the unnecessary code now.

After removing the unneeded code, you can start to build your medic character.

1. At the top of the `medic_example` class definition, add the following values:

   1. editable float `HealingThreshold`. This is the threshold of health characters must be under to receive healing.

      Verse

      ```
       # The HP threshold a character must be at before healing them.
       @editable
       HealingThreshold:float = 50.0
      ```

       # The HP threshold a character must be at before healing them.
      @editable
      HealingThreshold:float = 50.0
   2. Add an editable float `HealingDelay`. This is the amount of time to wait between each instance of healing while healing characters. Change this depending on whether you want your medic to heal slower or faster.

      Verse

      ```
       # The HP threshold a character must be at before healing them.
       @editable
       HealingThreshold:float = 50.0
          
       # How long to wait before healing characters
       @editable
       HealingDelay:float = 1.5
      ```

       # The HP threshold a character must be at before healing them.
      @editable
      HealingThreshold:float = 50.0
      # How long to wait before healing characters
      @editable
      HealingDelay:float = 1.5
   3. An editable float `HealingAmount`. This is the amount of health to heal characters per healing instance. When your medic NPC heals a character, they will heal the character by a `HealingAmount` every `HealingDelay` seconds.

      Verse

      ```
       # How long to wait before healing characters
       @editable
       HealingDelay:float = 1.5
          
       # How much to heal characters per healing instance
       @editable
       HealingAmount:float = 5.0
      ```

       # How long to wait before healing characters
      @editable
      HealingDelay:float = 1.5
      # How much to heal characters per healing instance
      @editable
      HealingAmount:float = 5.0
   4. An editable mutator zone `HealVolume`. This is the volume characters enter to receive healing. You'll use a mutator zone in this example because the mutator zone has an `AgentEntersEvent` which your medic can subscribe to and check for characters that might need healing.

      Verse

      ```
       # How much to heal characters per healing instance
       @editable
       HealingAmount:float = 5.0
          
       # The volume characters enter to receive healing.
       @editable
       HealVolume:mutator_zone_device = mutator_zone_device{}
      ```

       # How much to heal characters per healing instance
      @editable
      HealingAmount:float = 5.0
      # The volume characters enter to receive healing.
      @editable
      HealVolume:mutator_zone_device = mutator_zone_device{}
   5. An editable VFX spawner `VFXSpawner`. Visual feedback is important to know your code is working, so you'll use a VFX spawner to spawn effects when a character is being healed.

      Verse

      ```
       # The volume characters enter to receive healing.
       @editable
       HealVolume:mutator_zone_device = mutator_zone_device{}
          
       # The VFX spawner to play VFX as characters are being healed.
       @editable
       VFXSpawner:vfx_spawner_device = vfx_spawner_device {}
      ```

       # The volume characters enter to receive healing.
      @editable
      HealVolume:mutator_zone_device = mutator_zone_device{}
      # The VFX spawner to play VFX as characters are being healed.
      @editable
      VFXSpawner:vfx_spawner_device = vfx_spawner_device {}
   6. A variable optional `agent` named `AgentToFollow`. This stores a reference to the character the medic should follow while healing them.

      Verse

      ```
       # The VFX spawner to play VFX as characters are being healed.
       @editable
       VFXSpawner:vfx_spawner_device = vfx_spawner_device {}
          
       # The agent to follow while they're being healed
       var AgentToFollow:?agent = false
      ```

       # The VFX spawner to play VFX as characters are being healed.
      @editable
      VFXSpawner:vfx_spawner_device = vfx_spawner_device {}
      # The agent to follow while they&#39;re being healed
      var AgentToFollow:?agent = false
   7. A variable queue of agents named `AgentsToHeal`. If multiple characters need healing, your medic will heal characters based on the order they entered the `HealVolume`. You'll set up the queue code in the next step. For more information on the queue data structure, see [stacks and queues in verse](stacks-and-queues-in-verse).

      Verse

      ```
       # The agent to follow while they're being healed
       var AgentToFollow:?agent = false

       # The queue of agents to heal in the case of multiple agents entering the heal volume.
       var AgentsToHeal<public>:queue(agent) = queue(agent){}
      ```

       # The agent to follow while they&#39;re being healed
      var AgentToFollow:?agent = false
      # The queue of agents to heal in the case of multiple agents entering the heal volume.
      var AgentsToHeal&lt;public&gt;:queue(agent) = queue(agent){}
   8. A variable float `UpdateRateSeconds`. This is the amount of time to wait between updating the position of the `HealVolume` and `VFXSpawner`.

      Verse

      ```
       # The queue of agents to heal in the case of multiple agents entering the heal volume.
       var AgentsToHeal<public>:queue(agent) = queue(agent){}

       # Used to specify how quickly to update the position of the HealVolume and VFXSpawner
       UpdateRateSeconds<private>:float = 0.1
      ```

       # The queue of agents to heal in the case of multiple agents entering the heal volume.
      var AgentsToHeal&lt;public&gt;:queue(agent) = queue(agent){}
      # Used to specify how quickly to update the position of the HealVolume and VFXSpawner
      UpdateRateSeconds&lt;private&gt;:float = 0.1
2. To implement the `AgentsToHeal` queue, you'll use the code provided at the end of this step.

   [![Add New Verse File To Project](https://dev.epicgames.com/community/api/documentation/image/1564e299-9a57-4b33-9139-f9e6de9661e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1564e299-9a57-4b33-9139-f9e6de9661e7?resizing_type=fit)

Your code in `medic_example` should now compile correctly.

## Healing Characters Inside a Volume

When an injured character enters the `HealVolume`, your medic character should begin healing them if their health is less than the `HealingThreshold`. Once the character's health is above the `HealingThreshold`, your medic should stop healing that character, and move to the next character that needs healing. In the case of multiple characters, your medic should heal characters in the order they entered the `HealVolume`. Follow these steps to heal characters when they enter the `HealVolume`.

1. Back in your `medic_example` file, in `OnBegin()` after the `then` statement, start a `loop`. Inside the `loop`, get the result of the `Dequeue()` function from the `AgentsToHeal` queue and save it in a variable `DequeueResult`.

   Verse

   ```
        then:
            loop:
                # Get the next agent in the queue to heal. If there is an agent to heal, heal them by calling AgentToHeal.
                # If there are no agents to heal, wait until an agent enters the HealVolume
                if:
                    DequeueResult := AgentsToHeal.Dequeue[]
   ```

    then:
   loop:
   # Get the next agent in the queue to heal. If there is an agent to heal, heal them by calling AgentToHeal.
   # If there are no agents to heal, wait until an agent enters the HealVolume
   if:
   DequeueResult := AgentsToHeal.Dequeue[]
2. The `DequeueResult` variable is a `tuple` that returns both a copy of the `AgentsToHeal` queue with the first element removed and the agent at the front of the queue. Update `AgentsToHeal` by setting it to the first value in the tuple, and save the second value as the `AgentToHeal`.

   Verse

   ```
        if:
            DequeueResult := AgentsToHeal.Dequeue[]
            set AgentsToHeal = DequeueResult(0)
            AgentToHeal := DequeueResult(1)
   ```

    if:
   DequeueResult := AgentsToHeal.Dequeue[]
   set AgentsToHeal = DequeueResult(0)
   AgentToHeal := DequeueResult(1)
3. Once you have the agent to heal, you need to start healing them while they're in the `HealVolume`. You'll define a new function named `HealCharacter()` to handle this. Add a new function named `HealCharacter()` to the `medic_example` class definition. This function takes the `AgentToHeal` both the `Navigatable` and `Focusable` interfaces of the medic characters as function arguments. Add the `<suspends>` modifier to this function, since it needs to perform several asynchronous tasks when healing a character.

   Verse

   ```
        # Heal the character, then wait a HealingDelayAmount of time.
        # Ends when the character's health reaches the HealingThreshold
        # or the character leaves the HealVolume.
        HealCharacter(AgentToHeal:agent, Navigatable:navigatable, Focusable:focus_interface)<suspends>:void=
   ```

    # Heal the character, then wait a HealingDelayAmount of time.
   # Ends when the character&#39;s health reaches the HealingThreshold
   # or the character leaves the HealVolume.
   HealCharacter(AgentToHeal:agent, Navigatable:navigatable, Focusable:focus_interface)&lt;suspends&gt;:void=
4. In `HealCharacter`, check if the `AgentToHeal` is in the volume by calling `IsInVolume[]`, and passing `AgentToHeal` as an argument. If the agent is in the volume, you can begin healing them. All healable agents implement the `healthful` interface, which is part of the agent's `fort_character`. Get the agent's `fort_character` and save it in a value `CharacterToHeal`.

   Verse

   ```
        HealCharacter(AgentToHeal:agent, Navigatable:navigatable, Focusable:focus_interface)<suspends>:void=
            # Only heal the character if they are inside the HealVolume
            if:
                HealVolume.IsInVolume[AgentToHeal]
                CharacterToHeal := AgentToHeal.GetFortCharacter[]
   ```

    HealCharacter(AgentToHeal:agent, Navigatable:navigatable, Focusable:focus_interface)&lt;suspends&gt;:void=
   # Only heal the character if they are inside the HealVolume
   if:
   HealVolume.IsInVolume[AgentToHeal]
   CharacterToHeal := AgentToHeal.GetFortCharacter[]
5. With the character ready to heal, you need to make sure your medic stays close to the character being healed. Create a `navigation_target` from `AgentToHeal` using `MakeNavigationTarget` and save it in a variable `NavigationTarget`. Then in a `branch` statement, call the `NavigateTo()` function using the NPC's `navigatable` interface to have your medic navigate to the `AgentToHeal`. Also in the `branch` function, call the `MaintainFocus()` function to make sure your medic focuses on the `AgentToHeal`. Using a `branch` statement in this context lets you run both `NavigateTo()` and `MaintainFocus()` asynchronously at the same time, and lets you run any code after your `branch` immediately. For more information on branch expressions, see the branch in Verse page.

   Verse

   ```
        # Only heal the character if they are inside the HealVolume
        if:
            HealVolume.IsInVolume[AgentToHeal]
            CharacterToHeal := AgentToHeal.GetFortCharacter[]
        then:      
            Print("Character is in volume, starting healing")
            NavigationTarget := MakeNavigationTarget(AgentToHeal)
            branch:
                Navigatable.NavigateTo(NavigationTarget)
                Focusable.MaintainFocus(AgentToHeal)
   ```

    # Only heal the character if they are inside the HealVolume
   if:
   HealVolume.IsInVolume[AgentToHeal]
   CharacterToHeal := AgentToHeal.GetFortCharacter[]
   then:
   Print(&quot;Character is in volume, starting healing&quot;)
   NavigationTarget := MakeNavigationTarget(AgentToHeal)
   branch:
   Navigatable.NavigateTo(NavigationTarget)
   Focusable.MaintainFocus(AgentToHeal)
6. Enable the `VFXSpawner` to play VFX as your medic heals a character. Then in a `defer` expression, disable the `VFXSpawner`. Because the code for disabling the `VFXSpawner` is in a `defer` expression, it won't run until the current scope exits. In this situation, it means that the code will only run when the function ends, so it is guaranteed to be the last thing that happens in the function. For more information on defer expressions, see the defer page.

   Verse

   ```
        branch:
            Navigatable.NavigateTo(NavigationTarget)
            Focusable.MaintainFocus(AgentToHeal)
   		    
        VFXSpawner.Enable()
   		    
        defer:
            VFXSpawner.Disable()
   ```

    branch:
   Navigatable.NavigateTo(NavigationTarget)
   Focusable.MaintainFocus(AgentToHeal)
   VFXSpawner.Enable()
   defer:
   VFXSpawner.Disable()
7. When healing the `CharacterToHeal`, healing should stop when one of two conditions happens. Either the character's health is healed past the `HealingThreshold`, or the character exits the `HealVolume`. To accomplish this, you'll use a `race` expression. Set up a `race` expression between a `loop` and an `Await()` on the `HealVolume.AgentExitsEvent.`

   Verse

   ```
        branch:
            Navigatable.NavigateTo(NavigationTarget)
            Focusable.MaintainFocus(AgentToHeal)
        VFXSpawner.Enable()
        defer:
            VFXSpawner.Disable()
        race:
            loop:
            HealVolume.AgentExitsEvent.Await()
   ```

    branch:
   Navigatable.NavigateTo(NavigationTarget)
   Focusable.MaintainFocus(AgentToHeal)
   VFXSpawner.Enable()
   defer:
   VFXSpawner.Disable()
   race:
   loop:
   HealVolume.AgentExitsEvent.Await()
8. Inside the `loop`, get the current health of the character using `GetHealth()` and save it in a value `CurrentHealth`. Then in an `if` statement, check if the `CurrentHealth` plus the `HealingAmount` is greater than the `HealingThreshold`. If so, your medic should stop healing and `break` out of the loop. However, if the character's current health is just a little less than the healing threshold, you want to heal them up to the healing threshold. Add a second `if` statement inside the first one that checks if `CurrentHealth` is less than the `HealingThreshold`. If so, set the character's health to the `HealingThreshold`.

   Verse

   ```
        race:
            loop:
                CurrentHealth := CharacterToHeal.GetHealth()
                if(CurrentHealth + HealingAmount > HealingThreshold):
                    if (CurrentHealth < HealingThreshold):
                        CharacterToHeal.SetHealth(HealingThreshold)
                    PrintNPCB("Character has reached HealingThreshold, stopping healing")
                    break
            HealVolume.AgentExitsEvent.Await()
   ```

    race:
   loop:
   CurrentHealth := CharacterToHeal.GetHealth()
   if(CurrentHealth + HealingAmount &gt; HealingThreshold):
   if (CurrentHealth &lt; HealingThreshold):
   CharacterToHeal.SetHealth(HealingThreshold)
   PrintNPCB(&quot;Character has reached HealingThreshold, stopping healing&quot;)
   break
   HealVolume.AgentExitsEvent.Await()
9. Otherwise if the `CurrentHealth` plus the `HealingAmount` is not greater than the `HealingThreshold`, set the character's health to the `Current Health` plus the `HealingAmount`.

   Verse

   ```
        if(CurrentHealth + HealingAmount > HealingThreshold):
            if (CurrentHealth < HealingThreshold):
                CharacterToHeal.SetHealth(HealingThreshold)
            PrintNPCB("Character has reached HealingThreshold, stopping healing")
            break
        else:
            CharacterToHeal.SetHealth(CurrentHealth + HealingAmount)
   ```

    if(CurrentHealth + HealingAmount &gt; HealingThreshold):
   if (CurrentHealth &lt; HealingThreshold):
   CharacterToHeal.SetHealth(HealingThreshold)
   PrintNPCB(&quot;Character has reached HealingThreshold, stopping healing&quot;)
   break
   else:
   CharacterToHeal.SetHealth(CurrentHealth + HealingAmount)
10. At the end of the `loop`, sleep for a `HealingDelay` amount of time. Without this sleep, characters will be healed every simulation update, so the `HealingDelay` will prevent them from being healed instantly. Your completed `HealCharacter()` code should look like the following.

    Verse

    ```
         # Heal the character, then wait a HealingDelayAmount of time.
         # Ends when the character's health reaches the HealingThreshold
         # or the character leaves the HealVolume.
         HealCharacter(AgentToHeal:agent, Navigatable:navigatable, Focusable:focus_interface)<suspends>:void=
             # Only heal the character if they are inside the HealVolume
             if:
                 HealVolume.IsInVolume[AgentToHeal]
                 CharacterToHeal := AgentToHeal.GetFortCharacter[]
             then:
                 Print("Character is in volume, starting healing")
    ```
11. Back in `OnBegin()`, in the `then` expression inside of your `loop`, call `HealCharacter()` by passing the `AgentToHeal`, the `Navigable` interface, and the `Focusable` interface.

    Verse

    ```
         if:
             DequeueResult := AgentsToHeal.Dequeue[]
             set AgentsToHeal = DequeueResult(0)
             AgentToHeal := DequeueResult(1)
         then:
             Print("Dequeued the next agent to heal")
             HealCharacter(AgentToHeal, Navigatable, Focusable)
    ```

     if:
    DequeueResult := AgentsToHeal.Dequeue[]
    set AgentsToHeal = DequeueResult(0)
    AgentToHeal := DequeueResult(1)
    then:
    Print(&quot;Dequeued the next agent to heal&quot;)
    HealCharacter(AgentToHeal, Navigatable, Focusable)
12. Your medic will not always have a character to heal near them, and the `Dequeue[]` function will fail if there are no agents in the `AgentsToHeal` queue. To handle this, add an `else` statement to the end of the `loop`. Inside this `if` statement, call `Sleep()` for a `HealingDelay` amount of time, then `Await()` the `HealVolume.AgentEntersEvent`. This way your medic character will not endlessly call `Dequeue[]` on the `AgentsToHeal` queue, and will instead wait for a new character to enter the `HealVolume before restarting the loop. Your completed loop should look like the following.

    Verse

    ```
         loop:
             # Get the next agent in the queue to heal. If there is an agent to heal, heal them by calling AgentToHeal.
             # If there are no agents to heal, wait until an agent enters the HealVolume
             if:
                 DequeueResult := AgentsToHeal.Dequeue[]
                 set AgentsToHeal = DequeueResult(0)
                 AgentToHeal := DequeueResult(1)
             then:
                 Print("Dequeued the next agent to heal")
                 HealCharacter(AgentToHeal, Navigatable, Focusable)
    ```

## Tracking when Characters are in the Heal Volume

To know when characters enter or exit the `HealVolume`, you'll subscribe both the `HealVolume`'s `AgentEntersEvent` and `AgentExitsEvent` to new functions.

## Moving the Heal Volume with the Medic

When the medic character moves, the `HealVolume` needs to move with them to match their current position. The same is true for the `VFXSpawner`. To do this you'll use a new function `DeviceFollowCharacter()`.

## Adding your Character to the Level

[![Character Spawner Settings](https://dev.epicgames.com/community/api/documentation/image/19f6a359-afaa-4279-9d9d-5f64421acba5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19f6a359-afaa-4279-9d9d-5f64421acba5?resizing_type=fit)

## Complete Script

The following is a complete script for an NPC Character that heals characters whose HP is under a certain threshold.

### medic_example.verse

Verse

```
using { /Fortnite.com/AI }
using { /Fortnite.com/Characters }
using { /Fortnite.com/Devices }
using { /Verse.org/Colors }
using { /Verse.org/Random }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /UnrealEngine.com/Temporary/SpatialMath }

# A Verse-authored NPC Behavior that can be used within an NPC Definition or a Character Spawner device's Behavior Script Override.
```

### queue.verse

Verse

```
list(t:type) := class:
    Data:t
    Next:?list(t)

queue<public>(t:type) := class<internal>:
    Elements<internal>:?list(t) = false
    Size<public>:int = 0

    Enqueue<public>(NewElement:t):queue(t) =
        queue(t):
```

## On Your Own

By completing this guide, you've learned how to create a medic character that automatically heals characters under a certain threshold. Using what you've learned, try to create your own medic character with their own special behaviors.

- Can you create a medic who swaps between damaging and healing volumes based on whether an enemy is in the volume?
- How about a medic who uses a depletable resource to heal characters? How would the medic restore this resource? Could they restore it over time, or could they restore it by attacking enemies?
