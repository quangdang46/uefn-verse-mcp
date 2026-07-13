## https://dev.epicgames.com/documentation/en-us/fortnite/using-notes-in-unreal-editor-for-fortnite

# Using Notes

Leave feedback for your team members using Notes.

![Using Notes](https://dev.epicgames.com/community/api/documentation/image/2d4b1c73-132a-4bae-9d8f-1e9093eda87f?resizing_type=fill&width=1920&height=335)

Providing feedback to collaborators and reminders for yourself are key parts of the iterative project workflow. Notes is a feature within UEFN that brings this real-time feedback loop directly into the editor.

In this article, we’ll give an overview of the feature including *creating*, _reviewing, _and _resolving _notes.

## Creating Notes

Let’s start creating some notes! The easiest way to get started is by pressing the shortcut **C**. This will replace your cursor with a blue gizmo that aligns with the mesh you are pointing to. Click on the desired location within your level to create an **Anchored** note—a note attached to a specific object in your level.

[![The letter icon in the image represents a note left on an asset.](https://dev.epicgames.com/community/api/documentation/image/8108d1ff-2430-4b86-baf7-4474cf7e8df2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8108d1ff-2430-4b86-baf7-4474cf7e8df2?resizing_type=fit)

This will open the editing widget where you can type a description to give context to your note.

Notes do not get counted as part of your project memory calcualtion. Notes are a cloud feature that loads note data into transient actors that do not get saved as a file.

A simple description may be all you need since Notes are captured with a screenshot of the viewport at the time of creation as well as other contextual data to help you or your collaborators navigate back to the original perspective from which they were created. Simply click Create, and the note is immediately accessible to you and any collaborators working on the project.

[![Creating a note for the Taco sign.](https://dev.epicgames.com/community/api/documentation/image/0b5ce0a6-19e4-4e90-b184-eb144ac8988a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b5ce0a6-19e4-4e90-b184-eb144ac8988a?resizing_type=fit)

If you’d like to add additional context, whether before you create or through subsequent edits, you can optionally choose to attach additional actors, capture additional screenshots, or attach external images for reference.

[![Seelct the Attached Actors icon to take a screen shot of the asset for the note.](https://dev.epicgames.com/community/api/documentation/image/8c2facfa-76e5-417f-9b7a-41a02956a014?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c2facfa-76e5-417f-9b7a-41a02956a014?resizing_type=fit)

When capturing more screenshots, you can choose to take a full viewport screenshot or a cropped one.

[![Taking a screen shot of the asset in Notes.](https://dev.epicgames.com/community/api/documentation/image/d407868d-1f2f-4ebc-9fce-c7f5c3bd20ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d407868d-1f2f-4ebc-9fce-c7f5c3bd20ec?resizing_type=fit)

*Click image to enlarge.*

There is also a second creation mode for notes other than Anchored notes called **Camera** notes—notes that are placed at the position of the viewport camera. They are especially helpful when reviewing cinematics or capturing feedback on an area of the map from the player's perspective. You can trigger the creation of a Camera note with the shortcut **Shift + C**.

Have trouble keeping track of shortcuts? No problem. You can also create both types of notes by using the right-click context menu in the viewport. Selecting either option immediately opens the note widget for editing.

[![Select Add Anchor Note to anchor a note to an asset.](https://dev.epicgames.com/community/api/documentation/image/c7ec9a8c-46be-42c9-a3b7-9f57593a9b3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7ec9a8c-46be-42c9-a3b7-9f57593a9b3d?resizing_type=fit)

## Interacting with Notes in the viewport

Once you or your collaborators have created some notes, you’ll see note markers placed throughout the level. You can hover your cursor above the icon to see a small preview of the note.

[![An example of a note.](https://dev.epicgames.com/community/api/documentation/image/21d1477d-1d04-4203-b995-1983c1ee0ae6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21d1477d-1d04-4203-b995-1983c1ee0ae6?resizing_type=fit)

Clicking the marker will open up the note widget within the viewport and select the actors associated with the note. If you would like to view the note from the exact point of view from which it was created, click the **Reframe to Note** option in the widget’s context menu.

To review notes quickly, you can also page through a level’s notes sequentially by clicking the arrows toward the bottom right of a note widget. Each time you click, your viewport refocuses to the exact coordinates and orientation the selected note was created.

[![An example of an open note left by a colleague.](https://dev.epicgames.com/community/api/documentation/image/84198f83-78e4-4d76-929c-98b93e2e6224?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/84198f83-78e4-4d76-929c-98b93e2e6224?resizing_type=fit)

[![The available Notes options.](https://dev.epicgames.com/community/api/documentation/image/41d08aeb-2cf7-4b71-b148-c7bcfd4bbc0d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41d08aeb-2cf7-4b71-b148-c7bcfd4bbc0d?resizing_type=fit)

An additional way to review notes is with the Notes panel, where you’ll see a list of all the notes within the level.

To open it you can either:

Selecting a note in the side panel will open it in the viewport and align it to the viewpoint from which it was created.

[![An example of the Notes tab.](https://dev.epicgames.com/community/api/documentation/image/bff07001-8060-4420-92b4-381476543c0c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bff07001-8060-4420-92b4-381476543c0c?resizing_type=fit)

By default, the side panel list will display all unresolved notes for the project. If you’d like to additionally review resolved notes or drill down into notes created by a particular subset of your team, you can change the list’s filters via the filter dropdown. Changing the filter applies to both the notes that appear in the list and the markers you see in the viewport.

[![An example of the available filters on Notes.](https://dev.epicgames.com/community/api/documentation/image/0d22a3f3-7fb8-4627-8004-ef5922c267d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d22a3f3-7fb8-4627-8004-ef5922c267d5?resizing_type=fit)

If you’re using Lore Version Control in your project, your notes list also filters by default to only show Notes that were created in or before your currently-synced snapshot, since notes created in future snapshots are likely not relevant. You can override this filter if you wish by turning on the **Show Future Snapshot Notes** option.

[![Setting the Show Future Snapshot Notes feature.](https://dev.epicgames.com/community/api/documentation/image/d33ebc5b-e5b9-4623-8cd2-a50dfa3d0cc4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d33ebc5b-e5b9-4623-8cd2-a50dfa3d0cc4?resizing_type=fit)

## Resolving Notes

A note’s life cycle ends when it is **Resolved**. Once the feedback in a note has been actioned and any tasks related to it have been completed, you can resolve it simply by clicking the **Resolve** icon with the Note outline with a check mark inside, found either on the viewport widget for a note or in the side panel. On unresolved notes, this icon will be gray and on resolved notes, it will be green.

With default filters applied, resolving a note makes it disappear from the Notes panel and the viewport. If you ever need to review resolved notes, showing them again is as simple as changing your Notes panel filter to include resolved notes. You can reopen a Note simply by clicking the **Resolve** icon again.

[![Examples of the Resolve icon status.](https://dev.epicgames.com/community/api/documentation/image/a8b45cc9-0d79-45d5-8223-c13ddbe247b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8b45cc9-0d79-45d5-8223-c13ddbe247b2?resizing_type=fit)

*Click image to enalrge.*
