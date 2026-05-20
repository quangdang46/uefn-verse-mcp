## https://dev.epicgames.com/documentation/en-us/fortnite/creating-conversations-in-unreal-editor-for-fortnite

# Creating Conversations

Learn about creating conversations for different situations.

![Creating Conversations](https://dev.epicgames.com/community/api/documentation/image/b3d6e470-6895-4528-b4ea-f80a47967ed0?resizing_type=fill&width=1920&height=335)

The narrative choices you make for your project don’t have to be sophisticated to be immersive and leave an impression on players. Even simple interactions can have a meaningful impact on gameplay.

This page will give you a crash course on writing for conversations, then dive into how you can structure different types of conversations. You will also get some tips on using the Conversation graph as featured in the **Conversation Template** in UEFN.

For an in-depth dive on the device itself, see the [Conversation device](https://dev.epicgames.com/documentation/fortnite/using-the-conversation-device-in-unreal-editor-for-fortnite) page.

## Writing for Conversations

Before you connect your narrative to gameplay with the Conversation device, make sure that your conversation flows, makes sense, and fits the kind of experience you’re building. If you’ve never done any creative writing before you should:

- **Play games that use narration and conversation**. Having an example of what good (or possibly bad) conversational writing looks like can help your creative process.
- **Think about the NPCs with speaking roles**. Having an idea about where the characters are from, what kind of life they lead, and who they are will help you write better dialog for them and stop them from all sounding the same.
- **Think about how the people in your life talk**. This can help you find vocal cadences or ways of speaking for different characters.
- **Think about what is happening during the conversation.** Life doesn’t stand still when you’re talking with someone. Think about where the conversation is taking place and if anything should be happening in the background.

### Game Dialogue

Video game dialogue is a lot like a movie, except that players can alter a storyline just by interacting with the NPCs. Games use dialogue to perform a number of functions:

- Provide background information.
- Explain gameplay or give clues.
- Exchange goods and services in the game.
- Set the player on a certain path or alter the player’s path based on choices the player makes.

Introductions are important, and meeting NPCs is an integral part of gameplay that helps immerse players in the overall experience. Players need an introduction to NPCs in your game to:

- Understand who an NPC is and their role in the game.
- Receive basic information they can act on.
- Orient themselves in the game.

Dialogue should resemble normal conversation as much as possible, and yes, that includes using slang and shorthand to make the dialogue feel more natural.

### Quests

You can use a certain character to impart information that only they would know, or clarify something technical to the player. An NPC might also hold a clue or know a secret they can share with the player.

Below is a table that outlines what a simple exchange with an NPC could look like. The NPC is giving the player a choice of whether to participate in their quest.

Each response has an event that triggers when the player chooses whether to accept or reject the quest. If the player accepts the quest, they get paid and can use that NPC in a future quest. If they refuse the quest, a new storyline is created and the NPC won’t help the player on a future quest, thereby altering the gameplay and outcome of the narrative.

| Player | Speech | Response | Outcome | NPC |
| --- | --- | --- | --- | --- |
| [Character 1](https://dev.epicgames.com/community/api/documentation/image/15f3d402-7b96-4196-81b8-3138abb5eb57?resizing_type=fit) | **NPC:** "Hey! I have to hand in this essay, but I’d rather go out and play hackysack. Would you hand in my essay for me?" | -- | -- | [Character 2](https://dev.epicgames.com/community/api/documentation/image/b83a037b-14b9-48b8-ae6c-f4a3de636e17?resizing_type=fit) |
| -- | -- | **YOU**: “Yes - for 5 gold.” | **Yes:** NPC pays you 5 gold and walks off in the direction of the quad. | -- |
| -- | -- | **YOU:**“No - Why would I?” | **No:** NPC will remember this and not help you in another quest. | -- |
| -- | **NPC:** “Jeez, good help is hard to find!” | -- | -- | -- |

## Making a Basic Conversation Graph

Depending on what you’re trying to achieve through dialogue, the conversation tree could be large or small. Create a Conversation Bank and open the Conversation Editor to begin creating a graph:

You can also right-click in the graph and create the desired node before linking two nodes using an arrow. To connect the nodes, hover over the bottom of the node until it turns yellow, then drag. Stop dragging when the top bar of the receiving node turns yellow.

Create as many Speech nodes as you need. Players can walk away from the NPC to end an interaction mid-conversation.

Nodes of the same type cannot be connected by an arrow. The operation won't complete if you attempt this.

Here is a list of allowed node connections. The cells preceded by a **NO** indicate invalid connections:

| -- | Default Entry Point | Conversation Event | Repeat | Response | Restart Conversation | Speech | Random |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Default Entry Point |  | Entry Point > Event | **NO** Entry Point > Repeat | **NO** Entry Point > Response | **NO** Entry Point > Restart | Entry Point > Speech | Entry Point > Random |
| Conversation Event | N/A |  | Event > Repeat | Event > Response | Event > Restart | Event > Speech | Event > Random |
| Repeat | N/A | Repeat > Event |  | Repeat > Response | Repeat > Restart | Repeat > Speech | Repeat > Random |
| Response | N/A | Response > Event | Response > Repeat |  | Response > Restart | Response > Speech | Response > Random |
| Restart Conversation | N/A | **NO** Restart > Event | **NO** Restart > Repeat | **NO** Restart > Response |  | **NO** Restart > Speech | **NO** Restart > Random |
| Speech | N/A | Speech > Event | Speech > Repeat | Speech > Response | Speech > Restart |  | Speech > Random |
| Random | N/A | Random > Event | Random > Repeat | NO Random > Response | NO Random > Restart | Random > Speech |  |

### Create a Conversation with Two Speakers

Creating a conversation with two speakers in one Conversation Graph is possible with the [Set Conversation Material node](https://dev.epicgames.com/documentation/fortnite/using-the-conversation-device-in-unreal-editor-for-fortnite). Under the **Default Entry Point** add your first **Set Conversation Material** node then customize the node to the first speaker in the Details panel.

[![Set the first Set Conversation Material to the first character speaker.](https://dev.epicgames.com/community/api/documentation/image/d5de09ae-633b-439c-bd58-17ad1ee6c154?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5de09ae-633b-439c-bd58-17ad1ee6c154?resizing_type=fit)

Click image to enlarge.

Continue to build your conversation to the point that a second speaker is introduced. At this point set a second **Set Conversation Material** node and customize the node in the **Details** panel to the second speaker.

[![Add a second Set Conversation Material node and set this node to the second character speaker.](https://dev.epicgames.com/community/api/documentation/image/b76a3940-e27f-4eaf-b952-d26d329d0640?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b76a3940-e27f-4eaf-b952-d26d329d0640?resizing_type=fit)

Click image to enlarge.

Creating your own conversation UI provides greater control over the material size.

### Add Events

Event Nodes can trigger events or offer a selection of choices to the player. An event could be basic, like the NPC reacting to the choice the player makes using a [Cinematic Sequence device](cinematic-sequence-device-in-unreal-editor-for-fortnite) or cause a boss fight to break out.

[![Conversation event example](https://dev.epicgames.com/community/api/documentation/image/0853d69e-366c-4e7e-b28a-8b132c57008a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0853d69e-366c-4e7e-b28a-8b132c57008a?resizing_type=fit)

Click image to enlarge.

Create an event node by left-clicking and dragging from the bottom of an existing node, then selecting **Conversation Event** from the dropdown menu. You can connect a single conversation to up to **10 events**. For more information, see the [Conversation device](conversation-devices-in-unreal-editor-for-fortnite) page.

### Add UI Materials

Create a UI material and add it to your Conversation device under the **Conversation Material** option. Click the **Array icon** (+) to add your material to the **Index** list.

[![Add your custom UI material to the Conversation Material option in the Conversation device.](https://dev.epicgames.com/community/api/documentation/image/7efbbe6f-bb48-4437-bf03-72f3d3981d28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7efbbe6f-bb48-4437-bf03-72f3d3981d28?resizing_type=fit)

Click image to enlarge.

Add the **Set Conversation Material** node under the **Default Entry Point** node. This tells the Conversation device to set the conversation UI material with the Conversation Material option and this Conversation Bank.

[![The Set Conversation Material uses your custom UI material in the conversation box.](https://dev.epicgames.com/community/api/documentation/image/0e188d63-d793-446c-96d8-6d7957db3228?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e188d63-d793-446c-96d8-6d7957db3228?resizing_type=fit)

Click image to enlarge.

## Hiding and Showing Conversations

Temporarily hide and reveal conversations for cinematic effect. This is done with the **[Hide Conversation](https://dev.epicgames.com/documentation/fortnite/using-the-conversation-device-in-unreal-editor-for-fortnite)** node alongside the **Hide Conversation** and **Show Conversation** functions in the Conversation device.

The **Hide Conversation** function hides the character's conversation UI from the player and prevents them from selecting an option until the UI is shown again. When using the Hide Conversation node and function, the player's conversation Ui becomes invisible, this means:

- Players are not able to select, view, or navigate any responses while the conversation is hidden.
- Either Verse code or a device must trigger the Show Conversation function to reveal the conversation to the player again and continue the conversation.

The **Show Conversation** function reveals the conversation UI to the player. Once the conversation is revealed again, the player can continue through the conversation and select options again.

## Staying Organized

This section will cover best practices for creating more complex conversations. All of these tips can be found in the **Conversation Template** in UEFN under **Feature Examples**.

[![Conversation Template](https://dev.epicgames.com/community/api/documentation/image/16c97595-87d6-4ac1-8076-87e528f9bfff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16c97595-87d6-4ac1-8076-87e528f9bfff?resizing_type=fit)

### Comments

**Comments** are a way to easily keep track of complex conversation graphs. A comment can be as short as one letter to help you distinguish various branching paths, or it can be a more detailed account of what happens in a particular section of the conversation.

[![Example Comment](https://dev.epicgames.com/community/api/documentation/image/a8c2b391-ee0c-427d-a5db-21b41148d981?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8c2b391-ee0c-427d-a5db-21b41148d981?resizing_type=fit)

To create a new comment, select any node(s) on the graph and press **C**. This will generate a text box with a title.

In the Details panel for the comment, you can select the color of the region, whether to show a bubble when zoomed out, what color that bubble appears, and whether the comment will move with or without the nodes contained within.

[![Comment details](https://dev.epicgames.com/community/api/documentation/image/b2dbf6b7-409b-4a3f-aae3-e9358a766c2a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2dbf6b7-409b-4a3f-aae3-e9358a766c2a?resizing_type=fit)

### Reroute Nodes

**Reroute nodes** do exactly what their title suggests — reroute. When a conversation branches off in multiple directions, it’s possible to use reroute nodes to keep your logical flow organized. Without them, arrows between nodes may end up criss-crossing the screen and creating a lot of visual pollution in your graph.

Using reroute nodes to stay organized will allow you to be intentional about the flow of your conversations, and will let you stay flexible about making changes to existing paths.

Take the complex conversation below. It uses reroute nodes to declutter the various paths a player could take based on their choices. Now move the slider to the left and see the same conversation without reroute nodes. It comes down to personal preference, but the more complex a conversation, the more likely you are to confuse yourself!

![using reroute nodes](https://dev.epicgames.com/community/api/documentation/image/d9b10770-f000-4fd1-a708-29c0923f5af4?resizing_type=fit&width=1920&height=1080)

![not using reroute nodes](https://dev.epicgames.com/community/api/documentation/image/a133c58e-7703-45bc-87a6-aa5e99243c87?resizing_type=fit&width=1920&height=1080)

## Conversation Editor

All dialogue is built inside the **Conversation Editor** using nodes to fill out the conversation hierarchy.

The Conversation editor is the only way you can create a Conversation Graph. A Conversation Graph can be simple or complex. While there is no upper limit on responses in the conversation graph, there is a limit on the number of responses certain modals can handle at once.

Opening the Conversation Editor

Conversation graphs are built inside the Conversation editor. Double-clicking the Conversation Bank opens the Conversation editor. To use the editor you right-click in the graph area and select the nodes from the right-click **Node Selection** menu.

There are four important parts to the Conversation Editor:

[![1. Node Graph 2. Right-click Node Selection menu 3. Details Panel 4. Conversation Tree](https://dev.epicgames.com/community/api/documentation/image/b868d144-c4f9-4e53-ae79-1da2ce1cfbfc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b868d144-c4f9-4e53-ae79-1da2ce1cfbfc?resizing_type=fit)

The Conversation Editor and its parts

## Conversation Graph

Conversation graphs are created by linking a series of conversation nodes together. The nodes use the graph hierarchy to determine where in the conversation the player is and when a graph is completed. It resembles a flowchart.

A typical design for a conversation looks something like this:

[![](https://dev.epicgames.com/community/api/documentation/image/0de362b4-6b31-47c6-a56e-a6980fe3abe7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0de362b4-6b31-47c6-a56e-a6980fe3abe7?resizing_type=fit)

A diagram example of a typical conversation tree

Node hierarchy tracks how deep into the conversation the player can go based on the player’s choices in the conversation tree. Hierarchy is created by adding events, responses, and more conversation nodes to the graph.

## Conversation Nodes

Conversation nodes are the base of an action in the conversation. For example, kick off a conversation or offer a selection of choices represented by buttons the player selects from.

Nodes have an editable field in the Details panel. This is where you enter text. The table below describes the different Conversation nodes.

|  |  |
| --- | --- |
| **Node Name** | **Description** |
| **Default Entry Point** | The Default Entry Point node begins the Conversation graph. |
| **Speech** | This is the main node type that most conversations will use. This node creates a text selection that appears on the primary UI during playback by the NPC or Conversation target. This field uses the Message area to enter text. |
| **Response** | The node used to create choices in a conversation. Having multiple Response nodes branching off a single Speech node will stop the Conversation and allow users to select between multiple options. In the node, creators can enter the text that will appear as the Choices when the Conversation is played during the game. **Note:** Radial only allows up to **5** choices to be shown at a time, Custom allows up to **6** to be shown, and Box has no limit. |
| **Repeat** | This node returns to the previous connected node in the graph. If there is no Speech node, players will have to manually back out of the conversation. You can set Number Of Times To Repeat, and whether it should only repeat the value set in Number Of Times To Repeat. If Number Of Times To Repeat is set to 0, it will repeat an infinite number of times. |
| **Event** | The Event node triggers a device event associated with the Conversation device through the Conversation Graph. |
| **Restart Conversation** | Restart Conversation takes the player back to the start of the conversation tree. |
| **Reroute** | The Reroute node makes Conversation Graphs easier to read visually. Only one outgoing execution line can come off a reroute node, but it can receive from numerous sources in the graph. |

## Node Activation Order

Nodes are activated in the order that they are connected. Take a look at the example below:

[![](https://dev.epicgames.com/community/api/documentation/image/b8aed918-c0b5-4c3d-ae1f-134b9d18251d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8aed918-c0b5-4c3d-ae1f-134b9d18251d?resizing_type=fit)

In this example:

To follow the flow of the conversation, look at the way the arrows are pointing in the image above.
