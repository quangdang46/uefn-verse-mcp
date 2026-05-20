## https://dev.epicgames.com/documentation/en-us/fortnite/big-rig-device-design-example-in-fortnite-creative

# Big Rig Device Design Example

Slap on some off-road tires and your players can take this Big Rig anywhere!

![Big Rig Device Design Example](https://dev.epicgames.com/community/api/documentation/image/67ddb1f2-df91-41cb-a7bc-1f45b5120a58?resizing_type=fill&width=1920&height=335)

Like many of the vehicles in Fortnite, the **Big Rig** can be equipped with off-road tires that players can use to drive up steep hills or over difficult obstacles.

In this design example, you will learn how to create a fun mini-game that challenges players to climb a tricky path using the off-road tires on the Big Rig.

The objective is to reach the end of the path and press the button before the game timer expires. Players earn score based on how much time remains when the button is pressed.

## Devices Used

- 2 x [**Air Vent**](using-air-vent-devices-in-fortnite-creative) devices (optional)
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [**Big Rig Spawner**](using-big-rig-spawner-devices-in-fortnite-creative) device
- 1 x [**Button**](using-button-devices-in-fortnite-creative) device
- 1 x [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) device
- 1 x [**End Game**](using-end-game-devices-in-fortnite-creative) device

## Overview

You will assemble a challenging path for the Big Rig to climb, then place and customize the devices needed to create the gameplay. Finally, you will configure the Island Settings to support the game mode.

## Construct the Play Arena

Using props from the **Content** browser **Gallery** category, construct a steep path for your Big Rig vehicle to climb. There are lots of cool shapes you can use, so have some fun with this — and don't be afraid to defy gravity!

[![](https://dev.epicgames.com/community/api/documentation/image/03f52f5f-fbdd-422e-b1ac-ee9026599e70?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/03f52f5f-fbdd-422e-b1ac-ee9026599e70?resizing_type=fit)

For tips on navigating and selecting gallery items, see [Using Prefabs and Galleries](https://dev.epicgames.com/documentation/fortnite/using-prefabs-and-galleries-in-fortnite-creative)!

As you create your path, experiment with placing different obstacles in the way to make it more tricky to drive over. In the example island, **Air Vent** devices were also added to make the obstacles more fun!

[![](https://dev.epicgames.com/community/api/documentation/image/16d80bde-61d1-429c-837a-0b6ea8c61285?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16d80bde-61d1-429c-837a-0b6ea8c61285?resizing_type=fit)

Add a goal area at the end of your path where the target button will be located.

[![](https://dev.epicgames.com/community/api/documentation/image/0de5dd2a-0704-4932-9e00-f69c186ecc05?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0de5dd2a-0704-4932-9e00-f69c186ecc05?resizing_type=fit)

## Place and Customize the Gameplay Devices

## Bind the Devices

[**Direct event binding**](getting-started-with-direct-event-binding-in-fortnite-creative) is how you set devices to communicate directly with other devices. This involves setting **functions** or **events** for the devices involved.

[![](https://dev.epicgames.com/community/api/documentation/image/d0800e70-6f29-47f1-bb8e-5860da89273d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0800e70-6f29-47f1-bb8e-5860da89273d?resizing_type=fit)

| Event | Select Device | Select Function |
| --- | --- | --- |
| **On Success Send Event To** | End Game Device | Activate |

This activates the End Game device to when the timer runs out.

## Configure the Island Settings

The final step is to customize the Island Settings.

For more on these settings, see [**Understanding Island Settings**](understanding-island-settings-in-fortnite-creative).

1. Go to **Island Settings** and select the **Mode** category, then **Structure**.
   Under **Structure**, select **Teams** and set to **Free for All**.

   (w:600)
2. Still under Structure, select **Team Size** and set to **Dynamic**.
3. Go to **Scoring**, select **Show Individual Scores**, and set to **Yes**.
4. Go to **Victory Condition**, select **Game Win Condition**, and set to **Most Score Wins**.
5. Go to **Post Game**, select **Game End Callout**, and set to **Placement**.
6. Under **Spawning**, scroll down to **Join in Progress** and set to **Spectate**.
7. Finally, go to **Scoring**, then select **Show Individual Scores** and set to **No**.

You have created your own Big Rig mini-game! Compete with your friends to see who can get the best score by reaching the top the fastest!

## Design Tip

For variety, replace the Big Rig Spawner with other vehicle spawners, or set the vehicle trick modifier score higher to encourage players to try some risky stunts while driving.
