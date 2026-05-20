## https://dev.epicgames.com/documentation/en-us/fortnite/unreal-revision-control-extensions-in-unreal-editor-for-fortnite

# Unreal Revision Control Extensions

Add Unreal Revision Control extensions to Visual Studio Code and take advantage of revision control features in your Verse files.

![Unreal Revision Control Extensions](https://dev.epicgames.com/community/api/documentation/image/475c0249-b627-40ac-98bc-3dbee9c2c1ce?resizing_type=fill&width=1920&height=335)

The **Unreal Revision Control** (URC) extension for Visual Studio Code (VSC) provides instant revision control feedback in your Verse script and [Branch History](https://dev.epicgames.com/documentation/fortnite/revision-history-and-conflict-resolution-in-unreal-editor-for-fortnite). The URC extension adds features and functionality that complement pre-existing VSC tools and makes tracking changes in Verse code easier for you and your team.

The extension allows you to view the revision history inside VSC and highlights all Verse code changes in the file editor and Explorer.

## Unreal Revision Control Extension

The URC extension is installed by default on VSC. To read information about the URC extensions, select **Extensions** from the left column menu. Different extensions appear in the left column of the VSC window. Selecting the **Unreal Revision Control extension** opens the extension window where you can read the list of extension features.

[![](https://dev.epicgames.com/community/api/documentation/image/c8c53899-3417-4850-bdf9-b9be6a4eee6f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c8c53899-3417-4850-bdf9-b9be6a4eee6f?resizing_type=fit)

## Source Control View

The URC extension captures all changes in the Verse code of your UEFN projects and enables you to view the revision history for all the changes in the Verse script.

The extension adds **Source Control** and Branch History panels to VSC. The **Source Control** panel records all uncommitted changes made to the Verse code since the project's last revision. All committed changes are recorded in the Branch History panel.

[![The Source Control panel.](https://dev.epicgames.com/community/api/documentation/image/94d7fe20-188b-45d0-9388-187980ce898a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94d7fe20-188b-45d0-9388-187980ce898a?resizing_type=fit)

Clicking on your Verse file from the **Source Control** panel opens your file in two side-by-side windows so you can review and compare the changes in your code. The window on the left is the current version of your code. The window on the left is the version you're synced to, the version on the right has your local changes.

[![Clicking on the changes you made opens a comparison window where you can see the changes you made vbersus the live content.](https://dev.epicgames.com/community/api/documentation/image/340a8063-761d-4e8e-a723-fb551282cc86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/340a8063-761d-4e8e-a723-fb551282cc86?resizing_type=fit)

Click image to enlarge.

You can submit your changes to UEFN from the **Source Control** panel. Clicking on the **Create Revision**icon opens the editor’s **Submit File** window. Enter all the revision details into the **Changelist Description** field and click **Submit** to save a new revision.

[![Create a new snapshot from VSC.](https://dev.epicgames.com/community/api/documentation/image/7189fa8a-1206-4f45-85c9-242ba5578c14?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7189fa8a-1206-4f45-85c9-242ba5578c14?resizing_type=fit)

You cannot sync to the latest revision from VSC, you must sync all changes in UEFN.

## Editor Windows

As you’re working on your Verse code, items that have been added, deleted, and modified appear in the **Source Control** panel. The place in the Verse script where the changes occurred becomes highlighted. This allows you to see the difference between your changes and the current file.

All changes are marked with a letter in the **Source Control** panel:

- **M** - Modified
- **A** - Added
- **D** - Deleted

[![Changes highlight in the code and are marked with a letter in the Source Control panel.](https://dev.epicgames.com/community/api/documentation/image/ea8e3e17-c6ec-4bf1-b26a-8781d234e8f1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ea8e3e17-c6ec-4bf1-b26a-8781d234e8f1?resizing_type=fit)

Click image to enlarge.

## File Level Changes

**File Level Changes** can change the way you edit and update code versions. Instead of working solely on the current version of code, browse older versions in your **File History**, and select to review an older file while editing a new file.

[![Instead of working solely on the current version of code, browse older versions in your **File History**, and select to review an older file while editing a new file.](https://dev.epicgames.com/community/api/documentation/image/46ff32f1-6379-45cd-8b86-162a6f8fe5fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46ff32f1-6379-45cd-8b86-162a6f8fe5fc?resizing_type=fit)

Use your project’s File History to open an existing file in a read-only mode to review older code files next to the new file versions. This provides you with the ability to compare your code changes live with an older version.

Read-only view opens new tabs beside the currently edited file to avoid overwriting the new file you’re working on.
