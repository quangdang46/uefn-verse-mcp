## https://dev.epicgames.com/documentation/en-us/fortnite/scene-graph-known-issues-in-fortnite

# Scene Graph Known Issues

Learn more about some of the known issues within Scene Graph.

![Scene Graph Known Issues](https://dev.epicgames.com/community/api/documentation/image/671d727d-3dd5-4c7e-8ba0-9f95bcf49c69?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

Following are known issues when you work with with Scene Graph in your project. If you [have any feedback or find issues](https://forums.unrealengine.com/t/scene-graph-feedback-thread/1901696) that are not captured in the list below, report them in the forums.

## Known Issues

- Scene Graph is a Beta feature, and you might encounter unexpected crashes and instability.
- Mesh, sound, and particle effect components are only generated in Verse for assets you import into or create in your project, along with a small selection of built-in mesh shapes. By default, you can’t use Fortnite or FAB assets with Scene Graph.
- In the Prefab Editor, Light components in entities do not display lighting wireframes. The workaround for this is to reselect the entity in the viewport to get the visualizers to show up.
- You cannot clear all overrides from a Prefab instance at once. You must clear each override, one at a time.
- There is no way to save overridden Prefab instances to the Prefab asset.
- Duplicated entities are not named correctly in the Prefab Editor.
- There is currently no way to remove overrides from a Prefab.
- There is unexpected player behavior when colliding with Scene Graph objects.
- Negative scaling can cause abnormal interactions in child entities when rotated.
- Dragging transform values in the Prefab Editor is slower and less performant than changing the values from the widget.
- Prefab assets do not have thumbnails.
- Component logic runs in both Edit and Play modes.
- Components are initialized much earlier than Creative devices, which means that trying to fetch a Creative device from `component.OnBeginSimulation` or `component.OnSimulate` will not work. You should use the round started from the `fort_round_manager`.
- Changes made in the Prefab Editor will not propagate to placed instances of the prefab unless you save your changes.
- Saving the project while Verse code is not compiling can result in corrupted prefab data.
- As you add and change parameters in the Material or Niagara Editors, you will need to build Verse code for those changes to be exposed to the level editor.
- If you move, rename, or delete meshes, sounds, or particle system assets in the editor, it is possible to lose references to the generated component instances in the level editor as the classes that are generated currently cannot utilize redirectors.
- The new [LUF coordinate system](https://dev.epicgames.com/documentation/fortnite/leftupforward-coordinate-system-in-unreal-editor-for-fortnite) affects existing content and Scene Graph content. Any existing Verse code will continue to work. However, if you want to use the same code with Scene Graph, you'll have to convert from the old `/UnrealEngine.com/Temporary/SpatialMath` types to `/Verse.org/SpatialMath` types. There are new conversion functions that can transform between the old and new types:

  - FromVector3
  - FromScalarVector3
  - FromRotation
  - FromTransform

    Verse

    ```
             TeleportLocation := (/Verse.org/SpatialMath:)vector3{Left := 330.0, Up := 20.0, Forward := 50.0}
            TeleportRotation := (/Verse.org/SpatialMath:)MakeRotationFromYawPitchRollDegrees(90.0, 0.0     ,0.0)
            if: 
                FortCharacter := Agent.GetFortCharacter[]
                FortCharacter.TeleportTo[FromVector3(TeleportLocation), FromRotation(TeleportRotation)]
            then:
                Print("Character Teleported")
    ```

     TeleportLocation := (/Verse.org/SpatialMath:)vector3{Left := 330.0, Up := 20.0, Forward := 50.0}
    TeleportRotation := (/Verse.org/SpatialMath:)MakeRotationFromYawPitchRollDegrees(90.0, 0.0 ,0.0)
    if:
    FortCharacter := Agent.GetFortCharacter[]
    FortCharacter.TeleportTo[FromVector3(TeleportLocation), FromRotation(TeleportRotation)]
    then:
    Print(&quot;Character Teleported&quot;)

- Changing the type of default object value in a Verse component class between an entity copy-and-paste will end up importing the reference to the instance of the old type even though the property wasn't overridden.
- Reloading an entity prefab asset with an added entity child triggers an error `OldToNew.Value->HasAnyClassFlags(CLASS_TokenStreamAssembled)`.

## Itemization

- Remapped keys are not respected by some of the inventory inputs.
- Some icons for gamepad input binding are absent when a controller is used.
- There are some UI and presentation issues for inventories and items.

## Update Older Projects to Scene Graph

- With Scene Graph enabled by default, this changes some of the code generation rules for classes generated into `Assets.digest.verse`. This can mean that existing Verse code will no longer compile. You will need to fix up the Verse code before proceeding with your project.

  Key Examples:

  Before Scene Graph:

  Verse

  ```
  # Assets.digest.verse
  MyMesh := class(mesh){}

  MyMaterial := MakeAsset(material, "MyMaterial.uasset")

  # YourVerseFile.verse
  SetMesh(MyMesh)
  SetMaterial(MyMaterial)
  ```

  # Assets.digest.verse
  MyMesh := class(mesh){}
  MyMaterial := MakeAsset(material, &quot;MyMaterial.uasset&quot;)
  # YourVerseFile.verse
  SetMesh(MyMesh)
  SetMaterial(MyMaterial)

  After Scene Graph:

  Verse

  ```
  # Assets.digest.verse
  MyMesh_asset := class(mesh){}
  MyMesh := class(mesh_component){}

  MyMaterial := class(material){}

  # YourVerseFile.verse
  SetMesh(MyMesh_asset)
  SetMaterial(MyMaterial{})
  ```

  # Assets.digest.verse
  MyMesh_asset := class(mesh){}
  MyMesh := class(mesh_component){}
  MyMaterial := class(material){}
  # YourVerseFile.verse
  SetMesh(MyMesh_asset)
  SetMaterial(MyMaterial{})
