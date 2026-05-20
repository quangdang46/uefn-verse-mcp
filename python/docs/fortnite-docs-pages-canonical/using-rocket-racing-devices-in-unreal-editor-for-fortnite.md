## https://dev.epicgames.com/documentation/en-us/fortnite/using-rocket-racing-devices-in-unreal-editor-for-fortnite

# Rocket Racing Devices

Everything you need to know about Rocket Racing devices!

![Rocket Racing Devices](https://dev.epicgames.com/community/api/documentation/image/259a90a7-bd7b-44d1-91b5-0d8f758e538d?resizing_type=fill&width=1920&height=335)

**Rocket Racing (RR)** has a specialized set of devices that are only found on the Rocket Racing islands. You can use these devices to create your own Rocket Racing tracks and experiences.

At this time, Rocket Racing devices do not have [Verse](https://dev.epicgames.com/documentation/fortnite/programming-with-verse-in-unreal-editor-for-fortnite) [APIs](https://dev.epicgames.com/documentation/fortnite/verse-glossary#api).

## Device Setup Requirements

When you launch a session in UEFN, your Rocket Racking island will go through validation to make sure your island is set up for a Rocket Racing experience. Any check that fails will report an error message in the Output Log.

All Rocket Racing-specific devices have specific checks and error messages, so refer to the documentation for each device for details on how to avoid these errors.

## Finding Rocket Racing Devices

You can find the Rocket Racing devices in a couple of ways.

You can search in the **Content Browser** directly using **Rocket Racing**, or find all the Rocket Racing devices listed in the **Devices** folder.

[![Rocket Racing Devices in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/4dcc714c-7775-439c-b6f0-e75c2ee31f05?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4dcc714c-7775-439c-b6f0-e75c2ee31f05?resizing_type=fit)

You can also find them with the **Devices** category in the **Creative inventory** by searching for Rocket Racing or browsing the **Rocket Racing** subcategory.

The Rocket Racing devices only show up in Creative inventory if you access it from UEFN. Since these devices can't be used in Fortnite Creative, they won't show from there.

[![Rocket Racing Devices in the Creative Inventory](https://dev.epicgames.com/community/api/documentation/image/b564daad-f4ee-42c1-81d9-4be12b6b8b08?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b564daad-f4ee-42c1-81d9-4be12b6b8b08?resizing_type=fit)

## Rocket Racing Tools

These devices are marked as Beta. Use caution when shipping with them.

New Rocket Racing devices are now available outside of the Rocket Racing island template, you can build racing experiences directly within standard Fortnite Creative and UEFN workflows. These devices include:

- [Rocket Racing Vehicle Spawner Device](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-vehicle-spawner-devices-in-fortnite-creative)
- [Rocket Racing Boost Pad Devices](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-boost-pad-devices-in-unreal-editor-for-fortnite)
- [Rocket Racing EMP Volume Hazard Devices](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-emp-volume-devices-in-unreal-editor-for-fortnite)
- [Rocket Racing Track Devices](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-track-devices-in-unreal-editor-for-fortnite)

The Rocket Racing Boost Pad and EMP Volume Hazard are designed specifically for Rocket Racing vehicles and will not affect other vehicle types.

- [![RR Active Track Volume Devices](https://dev.epicgames.com/community/api/documentation/image/bda3093f-7840-46d7-9bfa-a412c90c0e19?resizing_type=fit&width=640&height=640)

  RR Active Track Volume Devices

  Change which track a player is racing on, or force a player onto a specific track.](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-active-track-volume-devices-in-unreal-editor-for-fortnite)
- [![RR Checkpoint Devices](https://dev.epicgames.com/community/api/documentation/image/9f213faa-3f49-4a22-bc1e-3ac6281e5335?resizing_type=fit&width=640&height=640)

  RR Checkpoint Devices

  Set checkpoints to track player progress in a race.](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-checkpoint-devices-in-unreal-editor-for-fortnite)
- [![RR Competitive Race Manager Devices](https://dev.epicgames.com/community/api/documentation/image/c2013db8-7ee1-408f-af34-3bcafac512c6?resizing_type=fit&width=640&height=640)

  RR Competitive Race Manager Devices

  Create multiplayer races with players charging the finish line!](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-competitive-race-manager-devices-in-unreal-editor-for-fortnite)
- [![RR Elimination Volume Devices](https://dev.epicgames.com/community/api/documentation/image/4141d4d8-2952-4c72-ae5a-c612966ccc17?resizing_type=fit&width=640&height=640)

  RR Elimination Volume Devices

  Create hazardous zones on your track with an elimination volume!](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-elimination-volume-devices-in-unreal-editor-for-fortnite)
- [![RR Player Start Position Devices](https://dev.epicgames.com/community/api/documentation/image/9a609808-6c05-47c4-af13-ac83489f64d0?resizing_type=fit&width=640&height=640)

  RR Player Start Position Devices

  Place spawn positions for the start of the race.](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-player-start-position-devices-in-unreal-editor-for-fortnite)
- [![RR Speed Run Manager Devices](https://dev.epicgames.com/community/api/documentation/image/87a6b044-9928-40ee-a2aa-2dbcc7330e15?resizing_type=fit&width=640&height=640)

  RR Speed Run Manager Devices

  Create time trial races for players to race for best time!](https://dev.epicgames.com/documentation/fortnite/using-rocket-racing-speed-run-manager-devices-in-unreal-editor-for-fortnite)
