## https://dev.epicgames.com/documentation/en-us/fortnite/levels-in-fortnite

# Levels

Learn how to work with levels in UEFN to prototype your game development ideas and more.

![Levels](https://dev.epicgames.com/community/api/documentation/image/b864fad3-df71-4ef5-9d01-81e0b4570437?resizing_type=fill&width=1920&height=335)

A great feature of Unreal Editor for Fortnite (UEFN) is the option to create multiple [levels](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#level) within a single [project](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#project). Adding multiple levels to a project provides a way to prototype your game design and development ideas by creating a secondary (or more) blank environment where you can create Verse devices, [graybox](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#grayboxing) designs, and more.

Additional levels in UEFN are assets and should not be confused with how Unreal Engine uses levels. You cannot link levels within the project to create a multi-level island, and you cannot link them to projects created in Unreal Engine. Only one level can be the **Default Map** in a UEFN project.

Creating a level in UEFN means:

- A new blank level is available from the Content Browser.
- The level can only be accessed by opening the project.
- Levels can be promoted within the project to become the Default Map.

There several things to consider when adding a level to your project:

- Levels can be duplicated, this provides a way for you to prototype a game mechanic or Verse device in the new level without breaking your main level.
- Additional levels contribute to the overall size of your project, so be sure to delete the extra levels before you publish your island.
- Creating a new level inside a project that uses an island template results in a completely blank level. You’ll need to create your own landscape in the new level.

## Create a New Level

Although you can’t link levels to create a multi-island experience, you can use additional levels to prove your game concepts without adding Verse devices, imported assets, and more to the Default Map. Here are a few ways to add a level to your project.

### From the File Menu

### From the Content Browser

If you’re testing out a concept it’s helpful to name the additional level after the concept. For example, **Graybox_Ideas**.

### Duplicate a Level

Another way to create a new level is to duplicate an existing one. Duplicating a level provides a way to explore ideas in gameplay, level design, and more without breaking the original. This workflow only works if the level being duplicated is not currently open in the viewport.

If you only have one level and want to duplicate it, you need to create a temporary second level you can switch to. You can then keep it or delete it once duplication is complete.

To duplicate a level, follow these steps.

The duplicated level contains all the same content as the original.

## Open a Level

There are a few ways you can open a level in your project.

### From the File Menu

Inside an open project, you can use the **File menu** to open a new level. To open a level follow these steps.

- Select **File** > **Open Level**. A window appears with all the levels you've created within this project. Select a level and it will open in the [viewport](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#viewport). This will also cause the currently open level to save and close.

  [![](https://dev.epicgames.com/community/api/documentation/image/50de8101-7df3-4ee2-9c7d-01deeb151a43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50de8101-7df3-4ee2-9c7d-01deeb151a43?resizing_type=fit)

- Select **File** > **Recent Levels**. Select the arrow to select from the list of recent levels you were working on.

### From the Content Browser

To open a level inside the Asset View, follow these steps.

## Promote a Level

If one of the project levels becomes the one you want to publish, you can promote that level to **Default Map** status in **GameFeatureData**. Promoting a level means:

- The level becomes publishable.
- The level opens when you open the project.

To promote a level, follow these steps.

## Map Data

Map Data refers to the multiple levels within the project. All levels you create within a project can be added to the **MapData array**. Multiple test levels drastically increase the package size of your project, which makes your project less performant and can create memory issues when you’re ready to publish.

[![](https://dev.epicgames.com/community/api/documentation/image/c128c434-2e3d-4423-b8b6-4afba0340350?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c128c434-2e3d-4423-b8b6-4afba0340350?resizing_type=fit)

This option provides a way for you to ensure all project data is cooked and distributed to the server at runtime and removes references to additional levels that have been deleted from the project.

### Remove Level References and Delete Levels

To remove references to additional levels, do the following:

This task takes some time to complete.

The level data is removed from the project and no longer contributes to the overall size of the project.

## Additional Level Information

The following is important information about working in a project with multiple levels.

- A new level doesn’t open automatically when the project is selected from the Project Browser.
- There is no limit to the number of levels you can add to a project.
- Team members can work in different levels within the project without blocking one another.
- On rare occasions a whole level may be blocked from editing when a team member is working in the level.
- Editing Scene Graph entities in a level will lock that level from teammembers because Scene Graph doesn’t support one file per actor.
- Editing props, devices, Island settings, and more should be fine as they support one file per actor.
