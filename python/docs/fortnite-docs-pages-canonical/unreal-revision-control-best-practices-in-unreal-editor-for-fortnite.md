## https://dev.epicgames.com/documentation/en-us/fortnite/unreal-revision-control-best-practices-in-unreal-editor-for-fortnite

# Unreal Revision Control Best Practices

Revision control keeps multiple team members from losing their work or overwriting the work of others.

![Unreal Revision Control Best Practices](https://dev.epicgames.com/community/api/documentation/image/26f4ab97-9569-48e8-b065-edb6bcacd8f4?resizing_type=fill&width=1920&height=335)

**Unreal Revision Control** is a custom embedded [revision](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#revision) control feature in Unreal Editor for Fortnite (UEFN).

[Revision control](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#revision-control) is a way for individuals and teammates or collaborators to store different versions of project files, track changes, keep a primary source file for projects, and even roll back to an earlier project version if necessary.

## Revision Control Overview

Revision control is similar to, but not entirely the same as, source control. Source control is concerned with text-based files, revision control is concerned with project and file versions.

Unreal Revision Control is a stable way to track changes made to your project and individual project files. Revision control keeps a history of changes to track who made changes to what file, when the changes were made, and why.

Revision control keeps a record of the checked-in files. By checking in changes made to the project and project assets, you record a history. As long as you and your team consistently and periodically check-in your changes, you’ll have a record that goes all the way back to the first file you created.

This means UEFN projects all have a base file with information about the project from the day the project file was created and assets were checked in. As a project progresses, files are added and removed from revision control as well.

Unreal Revision Control works by tracking the changes made when files are checked out, merging changed files to the primary source file, and capturing a new revision of the project, which becomes the new primary source file. This is the project’s “source of truth”.

Unreal Revision Control keeps a repository for all your projects that contains all the changes ever made, as well as the current state of the projects. You can view the history and revert changes in UEFN when Unreal Revision Control is enabled.

## Best Practices

Following are some best practices for getting the most out of Unreal Revision Control.

- Always add revision control to new projects you are creating.
- Check-in your changes regularly every time you use Unreal Revision Control.
- Do not enable multiple revision control methods outside of Unreal Revision Control, enabling multiple revision control or backup systems on the same project/location in your filesystem can end up causing unexpected behavior since there won't be a clear source of truth for either to reference.
- When opening a project, always **[Sync](unreal-editor-for-fortnite-glossary#sync-content) Latest** before making changes.
- When working collaboratively, let your teammates know which files you have checked out.
- Collectively agree which team member has priority to check out assets when working on teams.
- Remember to watch for revision control’s visual cues on projects and objects within projects to identify when another developer has checked out a project or object to avoid conflicts and errors.
- Recognize alerts that indicate another user has checked out an asset and is actively editing the project / object.
- Communicate changes to fellow developers when handing a project over to a teammate for editing.
- If your changes could be in conflict with another developer’s work, make a record of the changes you’ve made before you attempt to sync the project.
- If necessary, create an editing schedule for assets to reduce conflicts and errors.
- Do not check out all assets on a project as this can block another dev from their work.
- If you are planning to change a feature or area in your project, try to check out the corresponding files in advance. This avoids conflicts with another team member's changes.
- Add descriptions to your currently checked-out revision to remind yourself (and others) what you did with the checked-out files before submitting them.
