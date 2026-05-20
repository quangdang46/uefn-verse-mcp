## https://dev.epicgames.com/documentation/en-us/fortnite/importing-fortnite-islands-into-unreal-editor-for-fortnite

# Importing Fortnite Islands

Bring your Fortnite islands into Unreal Editor for Fortnite to make them even better.

![Importing Fortnite Islands](https://dev.epicgames.com/community/api/documentation/image/6bab5820-f695-4a88-988f-b983c7e72c0c?resizing_type=fill&width=1920&height=335)

You can import an existing Fortnite island into **Unreal Editor for Fortnite (UEFN)** to upgrade the look and feel of your experience with the tools and editing power of UEFN.

You can also push the boundaries of your island design by adding [Verse devices and functionalities](https://dev.epicgames.com/documentation/fortnite/uefnonly-devices-in-fortnite) not available in **Creative**.

[![How the FNC island looks before being imported into UEFN](https://dev.epicgames.com/community/api/documentation/image/7e2b13f0-a623-4fd1-903a-e128a21fc8e4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e2b13f0-a623-4fd1-903a-e128a21fc8e4?resizing_type=fit)

## Import a Fortnite Island

Player data will not transfer from your Creative island to a UEFN project. If you revert your island back to its Creative state, your player data is retained.

Importing a Fortnite island into UEFN creates a **fork** in the editing access for a project. Once converted to UEFN, a Fortnite island project can only be edited within UEFN, using UEFN tools and features.

Whether you create islands in Fortnite or in UEFN, all of the islands you create show in both the UEFN project menu and the Fortnite island menu. Projects created in UEFN have the Unreal Engine icon next to the project in the menu in Fortnite.

Alternatively, Fortnite islands have a **download cloud icon** on the project thumbnail in UEFN.

[![](https://dev.epicgames.com/community/api/documentation/image/7e118777-1730-4c44-8a23-2820b976bea6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e118777-1730-4c44-8a23-2820b976bea6?resizing_type=fit)

The project menu for UEFN is on the left, and the project menu for Fortnite is in the right. (Click image to enlarge)

When converting a Fortnite Creative Island into a UEFN Project, islands are now found under the “No Team (Just Me)” view instead of the default “My Local Projects” view.

[![](https://dev.epicgames.com/community/api/documentation/image/3451f1ed-0764-4842-83b8-b60e3ed6a6a1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3451f1ed-0764-4842-83b8-b60e3ed6a6a1?resizing_type=fit)

[![The Fortnite island is imported into UEFN.](https://dev.epicgames.com/community/api/documentation/image/aa084d1c-0a6a-4764-986d-6336f7d702c1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa084d1c-0a6a-4764-986d-6336f7d702c1?resizing_type=fit)

When the import process finishes, the project will be accessible through UEFN, and the project thumbnail will change to a UEFN thumbnail.

You’ll be able to playtest your island in a Fortnite client and play the island from your golden rift in Creative, but to make any changes to the island from Fortnite Creative, you must first open the project in UEFN.

The point when the UEFN version of the project becomes playable in Creative is after the first time it has been run ("Launch Session") from UEFN.

## Roll Back to Fortnite

You can revert your project back to a Fortnite island at any point through the [Creator Portal](https://dev.epicgames.com/documentation/fortnite/creator-portal). For example, you might want to revert if you’re not satisfied with the changes you made in UEFN and want to test game mechanics and device programming in another UEFN project before making final changes to your Fortnite island in UEFN.

[![revert using Creator Portal](https://dev.epicgames.com/community/api/documentation/image/1a200f9d-651c-4b19-a477-f13a24ca2755?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a200f9d-651c-4b19-a477-f13a24ca2755?resizing_type=fit)

To use the Creator Portal, you must have a [Developer Profile](https://dev.epicgames.com/documentation/fortnite/creator-portal).

You cannot convert a brand new UEFN project to a Fortnite Creative island, you can only revert a UEFN project that was previously converted from a Fortnite Creative island.

The page automatically refreshes and the project is now listed as **Project Type: FNC**. Any previous releases under UEFN will be visible on the list but greyed out.

The island is now accessible through the golden rift in the Creative hub.

If the project is reverted while being edited in UEFN, the person using UEFN cannot playtest the project. Instead, they are prompted to import the island again to continue editing in UEFN.

At this point, either the project must be imported, or UEFN must be closed.
