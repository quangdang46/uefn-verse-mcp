## https://dev.epicgames.com/documentation/en-us/fortnite/grind-vine-device-design-example-in-fortnite-creative

# Grind Vine Device Design Example

Build a mini-game where players shoot targets as they grind through bumpy terrain.

![Grind Vine Device Design Example](https://dev.epicgames.com/community/api/documentation/image/c05598ba-fe2b-498b-bdbf-74bc87466216?resizing_type=fill&width=1920&height=335)

The **Grind Vine** device uses an outdoor jungle theme to provide a fun way for players to quickly traverse from one location to another.

## Grind Vine Shooter Mini-Game

In this design example, you'll learn how to create a mini-game where a player grinds through a swampy path while shooting targets along the way.

The game awards points based on how quickly a player completes the course, and bonus points for shooting dangerous plants along the way.

If this is your first time using the Grind Vine device, it's a good idea to follow the [**Grind Rail design example**](grind-rail-device-design-example-in-fortnite-creative) first to familiarize with the basics of working with the grind device features. This project uses more advanced techniques introduced in that example.

### Devices Used

- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [**Water**](using-water-devices-in-fortnite-creative) device
- 1 x **[Grind Vine](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-grind-rail-devices-in-fortnite-creative)** device
- Several [**Bomb Flower**](using-bomb-flower-devices-in-fortnite-creative) devices
- Several [Stink Flower](https://dev.epicgames.com/documentation/fortnite/using-stink-flower-devices-in-fortnite-creative) devices
- 1 x [**Timer**](using-timer-devices-in-fortnite-creative) device
- 1 x [Score Manager](https://dev.epicgames.com/documentation/fortnite/using-score-manager-devices-in-fortnite-creative) device
- 1 x [**Item Spawner**](using-item-spawner-devices-in-fortnite-creative) device
- 1 x [**Capture Area**](using-capture-area-devices-in-fortnite-creative) device
- 1 x [**End Game**](using-end-game-devices-in-fortnite-creative) device

You will also use a number of terrain assets and a weapon.

### Build Your Own

You will:

- Lay out the obstacles for the course
- Create the vine and wind it among the obstacles
- Add targets for shooting and a weapon for players to shoot with
- Create the scoring system
- [Bind](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) devices as needed
- Configure the Island Settings

### Add the Course Obstacles

The base of the course in this example is a water volume created with a Water device. You can add rocks and trees to create the environment and to support the twists and turns of your grind vine.

1. Add a **Water** device. This will frame the course.

   [![](https://dev.epicgames.com/community/api/documentation/image/9f7dee51-cff8-45ad-a538-226bfad61364?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f7dee51-cff8-45ad-a538-226bfad61364?resizing_type=fit)
2. Modify the water as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/48df2129-69c2-494e-8f20-867902045588?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48df2129-69c2-494e-8f20-867902045588?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Zone Width** | 40.0 | You're setting the basic dimensions based on grid counts. This and the depth provides enough of an area to build a fun course. |
   | **Zone Depth** | 8.0 | See Zone Width. |
   | **Zone Height** | 0.5 | This is how deep the water volume is. You don't really need more depth than this. |
3. Add the major **terrain features**. In this example, there are rocks and trees that support the vine. Use whatever assets you want, but the ones used here are from the following galleries and prefabs:

   - Nature 4 Cliff Gallery
   - Variant Rock Gallery
   - Kapok Tree Gallery
   - Nature Tree Gallery
   - Wood Shanty prefab (for a lookout tower at the end of play area)

You can place rocks in the water that are large enough to rise above the water, then populate them with foliage.

You'll want to start the course with a rock or cliff large enough to place a Player Spawner device, and end it with a surface large enough to place a tower.

### Add the Grind Vine

Once you've positioned your terrain assets, you can add the Grind Vine device.

### Vine Grind Shaping Tips

Fine-tune the bend that a control point creates by adjusting the point's **tangent intensity**.

Below is a bent grind vine with a control point that uses the default tangent intensity setting of **300.0**.

[![](https://dev.epicgames.com/community/api/documentation/image/435dcb30-89ff-40c3-99e0-01e1be2a5f4b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/435dcb30-89ff-40c3-99e0-01e1be2a5f4b?resizing_type=fit)

Think of this as how much the bend angle of the control point stretches along the length of the vine.

If you adjust this value higher, say to **800.0**, you will see that the bend angle stretches out further along the length of the vine, making a smoother curve.

[![](https://dev.epicgames.com/community/api/documentation/image/bbda7aed-bcea-48fe-8bf0-e72221873600?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bbda7aed-bcea-48fe-8bf0-e72221873600?resizing_type=fit)

Be careful when copying, pasting, or deleting control points! Double-check to make sure that you have a control point selected, and not the entire vine!

By copy-pasting the end point of your vine, then rotating the point to create a more natural flow, you can more easily extend the vine around or through obstacles.

### Add Targets

Add targets for your players to shoot at as they ride the grind vine.

This example uses Bomb Flower and Stink Flower devices, with a total of six plants as targets, but you can place as many as you want!

### Add a Weapon

Equipping a player with a weapon requires an Item Spawner device, and a weapon dropped on the spawner.

### Add Devices to Control the Game State

Use the following devices to set up and control the game state:

- Timer device
- Score Manager device
- Capture Area device
- End Game device

  Since Timer and Score Manager devices require no direct player interaction, it's fine to place them outside of the gameplay area.

### Bind Devices

[Direct event binding](getting-started-with-direct-event-binding-in-fortnite-creative) is how devices communicate with each other. There are several bindings you'll need to set up for the game mechanics to work correctly.

### Configure the Island Settings

The only crucial Island Setting for this mini-game ensures that players won’t accidentally destroy the obstacle course as they ride the grind vine and shoot at the targets.

## Design Tip

And there you have it — an impressive mini-game style and challenges player skill!

Try adding multiple rails through your obstacle course, changing the weapons you award, or even the score to create a mini-game your players will love.
