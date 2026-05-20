## https://dev.epicgames.com/documentation/en-us/fortnite/time-trial-pizza-pursuit-in-verse

# Time Trial: Pizza Pursuit

Create a game with Verse where players must pick up and deliver pizzas before the time runs out!

![Time Trial: Pizza Pursuit](https://dev.epicgames.com/community/api/documentation/image/821c0434-8019-457a-834d-e0e464f8f907?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [Making a Custom Countdown Timer](https://dev.epicgames.com/documentation/fortnite/making-a-custom-countdown-timer-using-verse)
- [Moving Objective Marker](https://dev.epicgames.com/documentation/fortnite/objective-marker-gameplay-tutorial-in-unreal-editor-for-fortnite)

**Time Trial: Pizza Pursuit** is a single-player game, where the goal is to pick up pizzas and deliver them to the designated delivery zone before the time runs out. Each successful delivery adds time to the countdown.

After each pizza pickup, a **difficulty meter**, called the **pickup level** in this example, increases. Pickup zones are tagged with their pickup level, and each new pickup zone is selected from the available pickup zones for the current pickup level.

Higher-level pickups should be harder to reach, but give more points to the player.

After a delivery, the pickup level resets.

This tutorial is a step-by-step guide on how to create this game using Verse.

## Verse Language Features Used

- loop: This example uses the `loop` expression to repeat the selection of pickup and delivery zones, and loop the core gameplay.
- race: The `race` expression runs the pickup / delivery loop and stops the loop when the time runs out. A `race` expression executes multiple expressions at the same time and cancels any expression that doesn’t finish first.
- spawn: A `spawn` expression starts an asynchronous expression in any context.
- option: The `option` type can contain one value or can be empty.
- defer: The `defer` expression delays the execution of code until the current scope exits.
- block: This example uses the `block` expression to execute code sequentially in an asynchronous context, the `race` expression.
- if: The `if` expression tests conditions and accesses values that might fail.
- class: This example creates a Verse class for managing and displaying the player’s score.
- constructor: A constructor is a special function that creates an instance of the class that it’s associated with.
- Access specifiers: You can use access specifiers to set the access level of your code.

## Verse APIs Used

- [Gameplay Tags](https://dev.epicgames.com/documentation/fortnite/verse-tags-in-fortnite): With gameplay tags, you can find actors marked with a specific tag while the game is running.
- [Events](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event): You can create your own events in Verse and add custom functionality when they occur.
- [Verse UI](https://dev.epicgames.com/documentation/fortnite/ingame-user-interfaces-in-unreal-editor-for-fortnite): Create custom in-game UI to display information about the player and game.

## Overview

Here's an overview of the steps you'll take to recreate this island in their ideal sequence.

This project builds on top of the following tutorials, so complete these before continuing:

After building the objective marker and countdown timer, complete these steps to make the full game:

- [![1. Setting up the Pizza Pursuit Level](https://dev.epicgames.com/community/api/documentation/image/44fcd048-0427-4894-9fd9-1788a62980e7?resizing_type=fit&width=640&height=640)

  1. Setting up the Pizza Pursuit Level

  Create a game with Verse where players must pick up and deliver pizzas before the time runs out!](https://dev.epicgames.com/documentation/fortnite/pizza-pursuit-1-setting-up-the-level-for-time-trial-in-verse)
- [![2. Defining the Pickup and Delivery Zones](https://dev.epicgames.com/community/api/documentation/image/350c587d-38e5-480b-9643-b91eed7fbba7?resizing_type=fit&width=640&height=640)

  2. Defining the Pickup and Delivery Zones

  Create a game with Verse where players must pick up and deliver pizzas before the time runs out!](https://dev.epicgames.com/documentation/fortnite/pizza-pursuit-2-defining-the-pickup-and-delivery-zones-for-time-trial-in-verse)
- [![3. Creating the Game Loop](https://dev.epicgames.com/community/api/documentation/image/806c8e89-6c49-46fb-91aa-c9ba4d92a621?resizing_type=fit&width=640&height=640)

  3. Creating the Game Loop

  Create a game with Verse where players must pick up and deliver pizzas before the time runs out!](https://dev.epicgames.com/documentation/fortnite/pizza-pursuit-3-creating-the-game-loop-for-time-trial-in-verse)
- [![4. Managing and Displaying the Score](https://dev.epicgames.com/community/api/documentation/image/e9125c7b-d02e-41aa-a82e-9e42a1013818?resizing_type=fit&width=640&height=640)

  4. Managing and Displaying the Score

  Create a game with Verse where players must pick up and deliver pizzas before the time runs out!](https://dev.epicgames.com/documentation/fortnite/pizza-pursuit-4-managing-and-displaying-the-score-for-time-trial-in-verse)
- [![5. Improving Feedback and Player Experience](https://dev.epicgames.com/community/api/documentation/image/ef2f6a04-7153-4a76-9a3f-ad26e0b7ffca?resizing_type=fit&width=640&height=640)

  5. Improving Feedback and Player Experience

  Create a game with Verse where players must pick up and deliver pizzas before the time runs out!](https://dev.epicgames.com/documentation/fortnite/pizza-pursuit-5-improving-feedback-and-player-experience-for-time-trial-in-verse)
- [![6. Pizza Pursuit Final Result](https://dev.epicgames.com/community/api/documentation/image/4987faba-6a74-4495-beaf-806d9aaa52fe?resizing_type=fit&width=640&height=640)

  6. Pizza Pursuit Final Result

  Create a game with Verse where players must pick up and deliver pizzas before the time runs out!](https://dev.epicgames.com/documentation/fortnite/pizza-pursuit-6-final-result-for-time-trial-in-verse)
