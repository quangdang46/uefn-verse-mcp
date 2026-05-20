## https://dev.epicgames.com/documentation/en-us/fortnite/import-from-fab-in-unreal-editor-for-fortnite

# Import from Fab

Learn how to import assets from Fab directly in Unreal Editor for Fortnite.

![Import from Fab](https://dev.epicgames.com/community/api/documentation/image/d87f9e3a-f6a7-4d14-8a4b-519a8842fcaf?resizing_type=fill&width=1920&height=335)

Unreal Editor for Fortnite (UEFN) has a [Fab](https://dev.epicgames.com/documentation/fab/fab-documentation) integration that provides direct access to Fab where you can import third party assets into your UEFN projects to create a truly unique island. Browse the different asset categories to find the perfect custom assets for your island.

Browse assets in Fab from the Epic Games launcher before opening UEFN. For more information, see **[Exporting Assets from Fab in Launcher](https://dev.epicgames.com/documentation/fab/exporting-assets-from-fab-in-launcher)**.

Assets compatible with UEFN and Fortnite Creative are curated and modified to work with Fortnite islands. Look for the **UEFN** tag in [Included formats](https://dev.epicgames.com/documentation/fortnite/fab-user-interface-reference-in-unreal-editor-for-fortnite#product-preview) when browsing Fab. Fab is available from the **Window** menu or by clicking the **Fab** button in the [Content Browser](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#content-browser).

[![You can open Fab from the Window menu.](https://dev.epicgames.com/community/api/documentation/image/f1bd1d8b-e5a8-4167-b17d-2e2b69aecfd6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1bd1d8b-e5a8-4167-b17d-2e2b69aecfd6?resizing_type=fit)

Click to enlarge image.

[![You can open Fab from the Content Browser by clicking the Fab button.](https://dev.epicgames.com/community/api/documentation/image/705c54b4-0999-437c-971e-b33e1c981667?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/705c54b4-0999-437c-971e-b33e1c981667?resizing_type=fit)

Click to enlarge image.

You can dock the Fab window into the UEFN interface.

If you don’t have Fab in the **Window** options list, an [end user license agreement](https://www.fab.com/eula) opens in a popup. You must accept all the terms and conditions to get the Fab entitlements and to continue on to Fab.

## Browsing Custom Assets

Use the [Fab UI](https://dev.epicgames.com/documentation/fortnite/fab-user-interface-reference-in-unreal-editor-for-fortnite) to navigate through the thousands of assets available. To view a larger selection of assets, toggle the [Include 3D compatible formats](https://dev.epicgames.com/documentation/fortnite/fab-user-interface-reference-in-unreal-editor-for-fortnite#navigation-controls) button.

- Assets have a unique look and feel, and are optimized to work in Fortnite while running on different platforms. Assets are free of advertisements and promotional material.
- Adding these customized pieces and packs to your project makes your island stand out because they aren’t Fortnite assets.

When using 3D models from Fab, be aware that some require a lot of memory and may not perform well on some platforms.

## Importing Fab Assets

Follow the instructions below to import an asset into UEFN.

Imported assets appear in the **Content Browser** under the **main project folder** in a new folder entitled, **Referenced Content**.

[![Imported assets appear in the Content Browser under the main project folder in a new folder entitled, Referenced Content.](https://dev.epicgames.com/community/api/documentation/image/d137e7f4-2955-48e9-8b46-0f51fbf5f04e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d137e7f4-2955-48e9-8b46-0f51fbf5f04e?resizing_type=fit)

Click to enlarge image.

Some Fab assets have an option to select [Modifiable Content](https://dev.epicgames.com/documentation/fortnite/import-from-fab-in-unreal-editor-for-fortnite#using-modifiable-content).

For information about selling your creations on Fab, see [Publishing Assets for Sale](https://dev.epicgames.com/documentation/fab/publishing-assets-for-sale-or-free-download-in-fab).

### Referenced Content

**Referenced content** refers to assets that are compatible with UEFN and Fortnite  . These assets can be used in UEFN projects by using a [Verse path](https://dev.epicgames.com/documentation/fortnite/import-from-fab-in-unreal-editor-for-fortnite#verse-path) to reference assets imported from Fab in Verse code.

[![The asset description contains information important to the referenced content.](https://dev.epicgames.com/community/api/documentation/image/b72a2704-2f67-4e8b-94e5-68a8db39adb2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b72a2704-2f67-4e8b-94e5-68a8db39adb2?resizing_type=fit)

Click to enlarge image.

When purchasing an asset through Fab, the **[Included formats](https://dev.epicgames.com/documentation/fortnite/fab-user-interface-reference-in-unreal-editor-for-fortnite#product-preview)** section provides asset update information as well as UEFN compatibility data, such as:

- The collision ready status.
- Optimization for Fortnite vertex, materials, and textures.
- Scale of the asset in [Fortnite units](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#unreal-units).

The benefits of using a referenced asset are:

- Faster moderation times.
- Your asset is always current with the latest version from its asset developer.
- Reduced disk space and cook times.

### Verse Path

A [Verse path](https://dev.epicgames.com/documentation/fortnite/verse-glossary#path) is the global namespace for identifying your Fab assets. These paths are persistent, unique, and discoverable by any Verse programmer.

[![Assets can be referenced through their Verse path.](https://dev.epicgames.com/community/api/documentation/image/571630b5-4c93-47e9-b8e7-32752181994e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/571630b5-4c93-47e9-b8e7-32752181994e?resizing_type=fit)

Click to enlarge image.

Exposing your Fab assets to Verse provides a way to use them from your Verse code to create unique gameplay or events. Adding assets using their Verse path means you will not be able to set [LODs](https://dev.epicgames.com/documentation/fortnite/level-of-detail-lod-best-practices-in-fortnite), [collision](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#collision) or destructibility.

For more information about using a Verse path, see [Exposing Assets with Asset Reflection to Verse](https://dev.epicgames.com/documentation/fortnite/exposing-assets-with-asset-reflection-to-verse-in-unreal-editor-for-fortnite).

### License Types

All available assets in Fab use licensing agreements to legally authorize you to use someone else's intellectual property. You must select a [pricing tier](https://dev.epicgames.com/documentation/fab/licenses-and-pricing-in-fab) before completing a purchase. Free assets are licensed through [Creative Commons Attribution](https://dev.epicgames.com/documentation/fortnite/import-from-fab-in-unreal-editor-for-fortnite#creative-commons-attribution).

Purchasable assets are categorized with one or more of the following standard license types:

- **UEFN - Reference only**: A license that covers an individual developer or a small team with no more than $100k of revenue or funding in the last 12 months. This type of license only includes a referenced version of the asset.
- **Personal**: A license that covers an individual developer or a small team with no more than $100k or revenue or funding in the last 12 months.
- **Professional**: For studios or other entities with over $100k in revenue or funding in the past 12 months.

Pricing tiers vary by asset and standard license type.

#### Creative Commons Attribution

[Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/) requires you to give appropriate credit to the asset’s developer when using their work, along with providing a link to the license and indicating if changes were made to the asset.

This license type has a set of predefined permissions for the use of the asset within specific limits. These permissions typically cover allowance for common uses, such as:

- Copying
- Distributing
- Displaying
- Creating derivative works that credit the original developer

Regardless of license type, you must provide attribution to third party assets used on your island when you publish. To learn more about providing attribution, see [Third Party Assets](https://dev.epicgames.com/documentation/fortnite/attribution-screen-in-fortnite-creative) in the [Using Creator Portal](https://dev.epicgames.com/documentation/fortnite/using-creator-portal-in-fortnite-creative) documentation.

## Using Modifiable Content

Modifiable content refers to assets you can modify in line with the constraints of the license agreement. After importing modifiable content, the asset’s folder appears in the **Content Browser** under the **main project folder**. This folder contains all the import data for your imported asset: [materials](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#material), [meshes](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#mesh), and [textures](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#texture).

In UEFN, modifiable content means:

- The asset is detached from any updates its developer makes and results in slower moderation times.
- You can set the [LODs, collision, and destructibility](https://dev.epicgames.com/documentation/fortnite/configuring-collision-for-a-static-mesh-in-unreal-editor-for-fortnite) to make the asset unique.

## Importing Packs

Packs are multiple assets sold together in a single file and are purchased the same way you would any other asset. Packs are usually modular with all assets inside a pack created using the same style. Packs may include some unique assets that cannot be found elsewhere on their own. The singular assets of a pack are not always available for individual sale on [Fab.com](http://fab.com).

[![Search for packs using the search bar.](https://dev.epicgames.com/community/api/documentation/image/a2142ee9-a6ac-438f-98d2-48ddd78c3067?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2142ee9-a6ac-438f-98d2-48ddd78c3067?resizing_type=fit)

Click to enlarge image.

Packs can be delivered as referenced assets through a single Verse path. The assets in a pack can be individually referenced within UEFN by dragging pack items from the Content Browser into the viewport.

Removing a pack asset from a project does not remove that asset from the pack listed under **[My Purchases](https://dev.epicgames.com/documentation/fab/purchasing-and-downloading-assets-in-fab)**.

## Limitations

- If the total file size of all assets exceeds 256 MB, you will not be able to deploy the level to Fortnite Creative. This limitation is to minimize download times.
- You can check the size of all content by going to File Explorer/Finder and locating the project under Fortnite Projects > ProjectName > Plugins > ProjectName > Content, and right-clicking the Referenced Content folder.
- Referenced assets are not compatible with Scene Graph Beta. Source assets are compatible with Scene Graph Beta, be sure to select the correct content type to use with Scene Graph.
