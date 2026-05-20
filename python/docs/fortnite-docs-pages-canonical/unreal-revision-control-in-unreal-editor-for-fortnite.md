## https://dev.epicgames.com/documentation/en-us/fortnite/unreal-revision-control-in-unreal-editor-for-fortnite

# Unreal Revision Control

Revision control keeps you from overwriting someone else's work or losing your own edits when working as part of a team.

![Unreal Revision Control](https://dev.epicgames.com/community/api/documentation/image/52655185-6143-472a-b71c-60823046007c?resizing_type=fill&width=1920&height=335)

Unreal Editor for Fortnite (UEFN) integrates [revision control](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#revision-control) as an important part of project management, team processes, and quality control. It maintains a single source of truth for the project and developers.

Enabling Unreal Revision Control in team projects facilitates collaboration between team members, keeps work from getting lost, and speeds up an [island’s](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#island) release by shortening production time. Incorporating project [synchronization](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#sync-content) in daily iteration takes a little work, but is well worth the effort in the end.

## How Unreal Revision Control Works

Unreal Revision Control is available out of the box for [all new islands](https://dev.epicgames.com/documentation/fortnite/starting-and-organizing-a-project-in-fortnite) in UEFN. It works by incrementally saving the state of the island and its [assets](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#asset)at various points in time. These incremental save points are called “revisions”.

[![Select Unreal Revision Control to add source control to your projects.](https://dev.epicgames.com/community/api/documentation/image/f10b4d02-810d-41dc-a1da-0800acc7be3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f10b4d02-810d-41dc-a1da-0800acc7be3d?resizing_type=fit)

Click image to enlarge.

Select **Unreal Revision Control** from the **Project Defaults** panel for a new project.

From the **Team Selection** dropdown menu, select **Only Me** if you are working on a project alone, or your team’s name if you are working on a team project. You can disable Unreal Revision Control for your personal projects.

Projects using Unreal Revision Control are hosted on [servers](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#server).

[![Sync changes are marked with a download icon.](https://dev.epicgames.com/community/api/documentation/image/f5cb9d70-cff6-45fa-8a58-dfe00da3d54b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f5cb9d70-cff6-45fa-8a58-dfe00da3d54b?resizing_type=fit)

Sync Latest is marked by a download icon.

You can also use Unreal Revision Control from the **Outliner** panel. An asset's revision control status will display for reference on the right side of an asset's row in the outliner. Additionally, you can right-click an asset from the Outliner panel then select **Revision Control > Check out** from the dropdown menu.

## Use Unreal Revision Control with Your Projects

Enabling source control when you’re creating new projects adds these features to the bottom toolbar:

- **Revision Control**
- **Sync Changes / At Latest**
- **Check-in Changes / No Changes**.

[![Unreal revision control tools on the bottom toolbar.](https://dev.epicgames.com/community/api/documentation/image/e87a6a38-2dfb-49bd-9989-9c6c7df34514?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e87a6a38-2dfb-49bd-9989-9c6c7df34514?resizing_type=fit)

All Unreal Revision Control features appear below the [Details panel](https://dev.epicgames.com/documentation/fortnite/user-interface-reference-for-unreal-editor-for-fortnite) of your project.

### Revision Control

The revision control indicator. A green checkmark indicates that revision control is in use for this project. Click the arrow to open the control menu where you check out modified files and assets and change your revision control settings.

[![Revision control’s control menu.](https://dev.epicgames.com/community/api/documentation/image/caf33f2d-15fe-46a0-940a-9243c4dfeef1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/caf33f2d-15fe-46a0-940a-9243c4dfeef1?resizing_type=fit)

Change your control settings by clicking **Change Revision Control Settings…** from the dropdown menu, this opens the **Revision Control Login**. From here you can toggle on and off automatic settings and review the **Revision Control Log**.

[![Revision control settings.](https://dev.epicgames.com/community/api/documentation/image/377a1d0a-eb5b-4398-9b9a-bb517715294f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/377a1d0a-eb5b-4398-9b9a-bb517715294f?resizing_type=fit)

Click image to enlarge.

### Auto Checkout

**Auto Checkout** is automatically enabled when you create a new project. This feature works by automatically checking out an asset to you when you make changes or move the asset in the viewport.

This feature locks the asset you made changes to and stops another teammate from making changes to the same object while you have it checked out. By looking through the assets listed in the Outliner, you can see which [assets](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#asset) have been checked out by a colleague.

[![Assets checked out by colleagues will have a special icon attached to them in the outliner.](https://dev.epicgames.com/community/api/documentation/image/7a307798-3bfe-4d1c-9d15-4058cbb3457f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7a307798-3bfe-4d1c-9d15-4058cbb3457f?resizing_type=fit)

Using Auto Checkout avoids conflicts and allows you and your teammates to collaborate on projects with as little friction as possible.

If autocheckout is turned off, Unreal Revision Control will ask you to either connect back to the internet or save locally.

### Auto Revert

**Auto Revert** stops you from creating conflicts with team members by automatically undoing your changes to an asset already checked out by another person. You’ll receive a warning about the conflict and reversal of changes.

This feature stops you from putting in hours of work on an asset only to undo all the changes you made in the end. By checking quickly in the Outliner, you’ll know what assets your teammates are currently working on.

### Sync Changes

This feature pulls the latest revision of the project and syncs to disk. You’ll need to sync to the latest project version when you see **Sync Latest**. If there are no changes to sync, the button reads **At Latest**.

[![Clicking Sync Changes updates the project version and the button changes to At Latest.](https://dev.epicgames.com/community/api/documentation/image/8bc89f9e-0abc-4ca4-95d9-49c9fc1c1e05?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8bc89f9e-0abc-4ca4-95d9-49c9fc1c1e05?resizing_type=fit)

Once you click **Sync Latest** you pull the latest project revision down to your local environment where you can continue working on the project.

You can make and save changes without having synced to the latest revision as long as the changes you make do not conflict with the changes in the latest revision and are not changes made to assets currently checked out by another user.

Refer to [Conflicts in Unreal Revision Control](https://dev.epicgames.com/documentation/fortnite/conflicts-in-unreal-revision-control-in-unreal-editor-for-fortnite) for more information on the possible conflicts you may encounter.

### Check-in Changes

Checks in all changes and creates a new project revision with all of the checked-in changes. When you make changes to the project that need to be checked in, the button changes from **No Changes** to **Check-in Changes**.

[![When changes need to be checked in the button reads Check-in Changes. Once changes have been checked in, the button changes to read No Changes.](https://dev.epicgames.com/community/api/documentation/image/b20dcf91-d1a0-4a78-88c9-4562f5debf99?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b20dcf91-d1a0-4a78-88c9-4562f5debf99?resizing_type=fit)

Unreal Revision Control tracks the revision history of source files with formats native to the [UE](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#unreal-engine) ecosystem but does not track the revision history of source files with formats native to other software, (for example Blender, Photoshop, and so on).

Clicking **Check-in Changes** opens the **Check-in Changes** window. In the submit dialog, list the changes made to the assets in the **Changelist Description**, then click **Submit** to create a new revision of the island.

If there's an item on the check-in list that should be reverted to its earlier version, you can do that from the submit window.

Select the asset and right-click, a dropdown menu appears with the **Revert** option. Click **Revert** and any changes to the asset are undone.

[![Revert an asset during the submission process if necessary.](https://dev.epicgames.com/community/api/documentation/image/9a2a4074-5ffe-4532-bd88-9910c634dc41?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a2a4074-5ffe-4532-bd88-9910c634dc41?resizing_type=fit)

[![Revision control requires a change description for all assets checked out and altered. A checkmark means the asset was checked out, a plus sign means it is a new asset added to revision control.](https://dev.epicgames.com/community/api/documentation/image/824158b3-d2f7-4c6c-bc75-97836e04b4fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/824158b3-d2f7-4c6c-bc75-97836e04b4fc?resizing_type=fit)

After your changes are saved then successfully submitted, your teammates will be able to sync to the new project version. The project thumbnail updates for all team members with the download icon on the project thumbnail, informing them the project needs to be synced.

There is a difference between saving your project and checking-in changes. Saving your project saves the project to your disk where checking-in your changes creates a shared revision of the project at a moment in time that you or any collaborator can return to.

These revisions provide a history for your project assets you can later review to understand how and why an asset was changed, and by whom, over time.

[![Check an assets history by right-clicking on the asset and selecting History.](https://dev.epicgames.com/community/api/documentation/image/9eb4eacf-b449-4728-855b-f0e2fae81150?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9eb4eacf-b449-4728-855b-f0e2fae81150?resizing_type=fit)

## Check Out a Project Asset

Checking out an [asset](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#asset) locks that asset from being edited by another teammate. Whoever first checks out the object has control of it as long as it is checked out.

[![The Check-out popup contains the asset names that you have checked-out.](https://dev.epicgames.com/community/api/documentation/image/75dfae5b-f587-47b9-a182-724759156c5f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75dfae5b-f587-47b9-a182-724759156c5f?resizing_type=fit)

To check out an individual asset:

The asset is now checked out to you and the asset thumbnail updates with a red checkmark. Teammates see a different icon on the thumbnail that lets them know the asset is checked out.

[![Checked out assets have a red checkmark on the thumbnail.](https://dev.epicgames.com/community/api/documentation/image/7aae8ea0-e6f4-4783-8321-98c22939124f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7aae8ea0-e6f4-4783-8321-98c22939124f?resizing_type=fit)

After the object is checked in, anyone with access to the project will need to sync to the latest project version to edit the asset.

From the right-click menu you can also do the following:

| Feature | Description |
| --- | --- |
| **Sync And Check Out** | Syncs your project and checks out the asset. |
| **Mark For Add** | Marks an asset for addition to the project. |
| **History** | Opens a window that shows the edit history for the selected asset or project.  [An example of the history window.](https://dev.epicgames.com/community/api/documentation/image/b41cdb0f-c54a-4db8-9a28-68d3def367d9?resizing_type=fit)  Click to enlarge image. |
| **Revert** | Reverts the selected file back to its previous state. |
| **Merge** | Merges two selected asset files together. |
| **Refresh** | Refreshes the selected assets's status. |

## One File Per Entity with Scene Graph

**One File Per Entity (OFPE)** for Scene Graph projects is now in Beta. Until now, edits to Scene Graph entities would lock the entire project file when using Unreal Revision Control (URC), making collaboration very difficult. By saving each entity in its own asset file, OFPE enables multiple collaborators to work in parallel on projects using Scene Graph with fewer conflicts.

### Enable OFPE In Your Project

To enable OFPE in your Scene Graph project, follow these steps.
