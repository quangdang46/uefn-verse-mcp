## https://dev.epicgames.com/documentation/en-us/fortnite/migrating-assets-from-unreal-engine-to-unreal-editor-for-fortnite

# Migrating Assets in UEFN and Unreal Engine

Workflows for moving content between UEFN and Unreal Engine.

![Migrating Assets in UEFN and Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/b2d42d47-876d-44d2-bbe3-b07c3e03da67?resizing_type=fill&width=1920&height=335)

The content your project holds, whether it’s something you’ve imported from a third-party application, or it is something you created in the editor, can be migrated between different projects and engines. This allows you to reuse content between different projects with little to no set up whether they are using Unreal Editor for Fortnite (UEFN) or Unreal Engine.

## Content Migration Workflow

When you have content in your project you want to use in other projects in Unreal Engine or UEFN, you can use the **Migration Tool** to select the assets you want to migrate from the Content Browser using the right-click context menu.

[![](https://dev.epicgames.com/community/api/documentation/image/64f22053-d7de-46d5-a4a4-0ee388e99918?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64f22053-d7de-46d5-a4a4-0ee388e99918?resizing_type=fit)

The Asset Report Window seen when choosing to Migrate Content to another Project/Editor.

This tool enables you to migrate various types of assets between your projects. Some types of assets can only be migrated one way or not at all depending on the type of content it is. For example, content located in brand intellectual property (IP) folders cannot be migrated at all.

When you think about all the ways you can migrate content between Unreal Engine and Unreal Editors, you’ll want to think about the ways in which you can migrate your content between them. You can migrate from:

- Unreal Engine to Unreal Engine (Same version or newer)
- Unreal Engine to UEFN
- UEFN to UEFN (Same version or newer)

Additionally, with any of these content migrations, you must consider the release version you are migrating from, which can be:

- Releases that are on the same version
- Older release version to a newer release version

You cannot migrate from a current (or latest) version release to an older version release. Assets are not version agnostic in this way.

## What To Know About Migrating Content?

Here are some things to keep in mind when migrating content between projects and editors. This is **not** an exhaustive list.

- **The Migration Tool is a means to move content but does not verify its compatibility with the engine you're migrating to.**

  - It’s important to understand where you’re migrating content from and to whereas there aren’t many restrictions with the types of assets you can move between projects and engine versions. Compatibility doesn’t just mean the content is supported, but also that it’s migrated to a release that is the same or newer than the one you are currently using.
- **Assets must be moved to a Content folder.**

  - The tool will only migrate content to appropriate locations within a project. This ensures that content won’t lose references to the assets that it needs and the content will work as intended. For example, choosing a different folder than the Content folder or a path outside of a project will result in messages like the ones below.

    |  |  |
    | --- | --- |
    |  |  |
    | Migrating to a folder that doesn’t have an Unreal project associated with it. | Migrating to a folder different than a Content folder inside of an Unreal project. |
- **Migrating to supported engine versions.**

  - You can maintain working content by migrating assets to Unreal Engine and UEFN versions with the same release version or from older version releases to newer version releases. Content migrated from a newer version release to an older one will not work, the assets may show up in the content browser, but you cannot open and edit them.
- **Supported Content and Assets.**

  - UEFN does not support all of Unreal Engine’s asset types for migration. Further, some supported asset types have additional limitations to enable them to comply with Fortnite performance requirements. For example, Static Mesh assets should not exceed 20k vertices.
- **Single Assets can be made up of many other assets.**

  - Individual assets can be made up of additional assets, such as materials that have multiple texture assets associated with them. When you migrate any of these assets, the references they have to other content in the project gets picked up for migration as well. To better understand what references to other assets your content may have, you can use the [Reference Viewer](https://dev.epicgames.com/documentation/unreal-engine/reference-viewer-in-unreal-engine?application_version=5.5) to see these connections.

## Migration Tool Requirements

The Migration Tool has the following requirements:

- **Asset Source:** This should be content from a UEFN or Unreal Engine project running on Unreal Engine 5.1 or a later version release.
- **Destination:** This should be a UEFN project running on latest version of Fortnite, or Unreal Engine running on Unreal Engine 5.1 or a later version release.

### Using the Migration Tool

To migrate content between projects and engine versions with the Migration Tool, use the following steps:

You can now check the project you migrated the content to see that it migrated successfully. Even if the project is currently open when you initiate and complete the migration process, you should still see this become available in the project’s content browser to check it.

## Limitations

When migrating content, the tool itself does not perform content validation and is not aware of any limitations the content might have when migrating to a specific editor or engine. In other words, the Migration Tool will copy your assets whether or not they are actually compatible with their destination project.

As mentioned in the section above, UEFN has limited support for some features based on its integration with Fortnite and maintaining performance and operability. This means that some assets cannot exceed certain sizes, and some Unreal Engine asset types have restrictions or simply aren’t supported at all.

## Troubleshooting

When you migrate an asset type from Unreal Engine that is not recognized by UEFN, the content will still appear in the Content Browser but will be listed as an unsupported asset type.

[![Unsupported Assets](https://dev.epicgames.com/community/api/documentation/image/3ff6c5ca-3573-468a-99db-d13b1cf54e8d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ff6c5ca-3573-468a-99db-d13b1cf54e8d?resizing_type=fit)

Example of unsupported assets migrated to a project.

Having these types of assets in your project can prevent you from testing your UEFN experience, so it is recommended that you delete these assets to avoid potential errors in the project.
