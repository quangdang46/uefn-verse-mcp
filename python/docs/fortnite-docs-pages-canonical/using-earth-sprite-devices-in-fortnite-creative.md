## https://dev.epicgames.com/documentation/en-us/fortnite/using-earth-sprite-devices-in-fortnite-creative

# Modeling Mode
Learn how to create and edit meshes with the Unreal Editor for Fortnite Model Mode.
![Modeling Mode](https://dev.epicgames.com/community/api/documentation/image/f0d4b530-07df-4ca2-ab31-f263df32c21e?resizing_type=fill&width=1920&height=335)
UEFN includes an editing mode for [meshes](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#mesh) called **Modeling Mode**. With it, you can create and sculpt a custom mesh then use the modeling edit tools to create custom props for your projects that you can also share with other developers.
Whether you're creating a new [mesh](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#mesh) or want to edit a mesh you downloaded, use Modeling Mode to edit your mesh's shape, attributes, [volume](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#volume), [voxels](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#voxel), [LODs](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#lod), and [UVs](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#uv-mapping). When you're done editing your mesh, decide how to [bake](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#bake) the final product, then use your mesh with your project.
To learn more about Modeling Mode refer to the [UE5 Modeling Mode Overview document](https://docs.unrealengine.com/modeling-mode-overview/).
##  How It Works
When you open Modeling Mode, a panel opens in the Viewport with options for creating or editing a mesh.
[![The Modeling Mode panel.](https://dev.epicgames.com/community/api/documentation/image/ed0eaa4d-c184-4055-9938-09bdd99b2077?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed0eaa4d-c184-4055-9938-09bdd99b2077?resizing_type=fit)
To create your own mesh, select from:
Option Icon  |  Modeling Option  |  Description
---|---|---
[![The Favorite icon.](https://dev.epicgames.com/community/api/documentation/image/567b70b4-537e-4b0a-a260-343ca9bf0415?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/567b70b4-537e-4b0a-a260-343ca9bf0415?resizing_type=fit) |  **Favorites** |  All tools that you have favorited appear under Favorites.
[![The Shape icon.](https://dev.epicgames.com/community/api/documentation/image/2f464f61-6d74-4f70-82e4-43887a82ef9f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f464f61-6d74-4f70-82e4-43887a82ef9f?resizing_type=fit) |  [Shapes](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#shape) |  Offers different shapes you can add to the viewport where you can edit them further. All shape meshes will appear in the **Outliner** panel, and are editable in the **Details** panel.
[![The Create icon.](https://dev.epicgames.com/community/api/documentation/image/fc0b1f59-b16a-46a2-81a0-79d35bc8c4c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc0b1f59-b16a-46a2-81a0-79d35bc8c4c4?resizing_type=fit) |  [Create](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#create) |  A selection of tools to create a mesh. Draw [polygons](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#polygon) with lines to create a path or an object. Use these tools to copy, merge, or revolve the mesh you created.
To edit an existing mesh, select from one of the following options:
Option Icon  |  Modeling Option  |  Description
---|---|---
[![The Poly Edit icon.](https://dev.epicgames.com/community/api/documentation/image/0d3363de-1684-4f75-821f-e5648c0dd3ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d3363de-1684-4f75-821f-e5648c0dd3ac?resizing_type=fit) |  [PolyEdit](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite) |  Edit meshes and PolyGroups.
[![The Tri Tools icon.](https://dev.epicgames.com/community/api/documentation/image/bed720ea-106f-40d0-97ac-a3cf77e2c606?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bed720ea-106f-40d0-97ac-a3cf77e2c606?resizing_type=fit) |  [TriTools](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite) |  Edits meshes through their triangles.
[![The Deform icon.](https://dev.epicgames.com/community/api/documentation/image/d0db9d66-5c98-4a9f-bdd6-c1d84c31fbb0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0db9d66-5c98-4a9f-bdd6-c1d84c31fbb0?resizing_type=fit) |  [Deform](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#deform) |  Deforms the selected mesh.
[![The Transform icon.](https://dev.epicgames.com/community/api/documentation/image/3d475f5c-2da6-4d12-87a0-60f3302f3cde?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d475f5c-2da6-4d12-87a0-60f3302f3cde?resizing_type=fit) |  [Transform](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#transform) |  Change and transform meshes.
[![The MeshOps icon.](https://dev.epicgames.com/community/api/documentation/image/20dbaab0-6860-4275-adf4-6a72ca86cd6c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20dbaab0-6860-4275-adf4-6a72ca86cd6c?resizing_type=fit) |  [MeshOps](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#mesh-ops) |  Perform complex mesh operations.
[![The VoxOps icon.](https://dev.epicgames.com/community/api/documentation/image/202e8e5f-e447-42ec-bc5a-1fa12b447953?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/202e8e5f-e447-42ec-bc5a-1fa12b447953?resizing_type=fit) |  [VoxOps](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#vox-ops) |  Edit the 3D cubes of your mesh.
[![The Attribute icon.](https://dev.epicgames.com/community/api/documentation/image/0e7a1c7f-2c56-4c2c-9235-63e3339d9c6f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e7a1c7f-2c56-4c2c-9235-63e3339d9c6f?resizing_type=fit) |  [Attribute](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#attributes) |  Edit the attributes of your mesh or its triangles.
[![The UVs icon.](https://dev.epicgames.com/community/api/documentation/image/25f97853-e080-42e1-8737-3068e12d372b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25f97853-e080-42e1-8737-3068e12d372b?resizing_type=fit) |  [UVs](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#u-vs) |  Tools to edit and tune the UVs of your mesh.
[![The Baking icon.](https://dev.epicgames.com/community/api/documentation/image/01cbe5a9-bcf4-49c3-9157-8587db5936cb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01cbe5a9-bcf4-49c3-9157-8587db5936cb?resizing_type=fit) |  [Baking](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#baking) |  Three different baking options for your mesh.
[![The Volumes icon.](https://dev.epicgames.com/community/api/documentation/image/678b3ef3-80ed-4fb9-89e3-7ed4693557f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/678b3ef3-80ed-4fb9-89e3-7ed4693557f2?resizing_type=fit) |  [Volumes](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#volumes) |  Edit the volume on your mesh to define collision and your mesh's physical space.
[![The LODs icon.](https://dev.epicgames.com/community/api/documentation/image/c5db0a62-6799-45fb-ac17-e8fc5b3bdb83?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5db0a62-6799-45fb-ac17-e8fc5b3bdb83?resizing_type=fit) |  [LODs](https://dev.epicgames.com/documentation/fortnite/modeling-mode-in-unreal-editor-for-fortnite#lo-ds) |  Defines and edits the level of detail(LOD) for your mesh.
You can save your mesh data in a file in the Content Browser, then share the file with other developers, or use it in other projects.
It is possible to lose mesh data (weightmaps, PolyGroups, and vertex colors) during transfer when you are importing and exporting a mesh.
##  Shape
[![Shape option tools.](https://dev.epicgames.com/community/api/documentation/image/cc2ab50f-fdb0-47cf-8018-cee7937f1109?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc2ab50f-fdb0-47cf-8018-cee7937f1109?resizing_type=fit)
Begin creating a mesh by adding shapes to the [viewport](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#viewport) that you edit and define with material instances, LODs, collision and more. You can even use the shapes along with other modeling tools to greybox your level design. To learn more about [greyboxing](https://dev.epicgames.com/documentation/fortnite/greyboxing-in-unreal-editor-for-fortnite), scroll to the end of the document.
Click on the shape from the popup window then click in the viewport to add the shape to your project, Before clicking **Accept** , you can edit the parameters of the mesh with the **Shape** toolset. Once you click **Accept** , you can edit the mesh in the Details panel.
Learn how to use basic shapes and the model editing tools to create a column in the [Basic Tutorial: Creating a Column](https://dev.epicgames.com/documentation/fortnite/creating-a-column-with-modeling-mode-in-unreal-editor-for-fortnite).
[![The Shape editing options.](https://dev.epicgames.com/community/api/documentation/image/851c306f-f87d-4000-8898-9666b20551e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/851c306f-f87d-4000-8898-9666b20551e7?resizing_type=fit)
_These tools are available for every shape._
Shape  |  Image
---|---
Box |  [![Box shape](https://dev.epicgames.com/community/api/documentation/image/8a0bd6da-8c30-4842-93a0-75e2ad81f312?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a0bd6da-8c30-4842-93a0-75e2ad81f312?resizing_type=fit)
Sphere |  [![Sphere shape](https://dev.epicgames.com/community/api/documentation/image/f7c28458-7fb8-4fe4-99db-2bc1256e2224?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7c28458-7fb8-4fe4-99db-2bc1256e2224?resizing_type=fit)
Cylinder |  [![Cylinder shape](https://dev.epicgames.com/community/api/documentation/image/56ef3585-d7c1-4b25-acb0-e40e86840d2f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56ef3585-d7c1-4b25-acb0-e40e86840d2f?resizing_type=fit)
Cone |  [![Cone shape](https://dev.epicgames.com/community/api/documentation/image/aeb6fab2-ef96-409a-9f70-225b418e3b97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aeb6fab2-ef96-409a-9f70-225b418e3b97?resizing_type=fit)
Torus |  [![Torus shape](https://dev.epicgames.com/community/api/documentation/image/8f766b33-a46d-4312-8e30-766eadb10744?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f766b33-a46d-4312-8e30-766eadb10744?resizing_type=fit)
Arrow |  [![Arrow shape](https://dev.epicgames.com/community/api/documentation/image/aedc5dc2-25f6-46ff-856b-a3ed8a818ee2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aedc5dc2-25f6-46ff-856b-a3ed8a818ee2?resizing_type=fit)
Rectangle |  [![Flat rectangle shape](https://dev.epicgames.com/community/api/documentation/image/6794cc6e-24ac-4c6e-a98a-4ca7dedba0fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6794cc6e-24ac-4c6e-a98a-4ca7dedba0fa?resizing_type=fit)
Disc |  [![Flat disc shape](https://dev.epicgames.com/community/api/documentation/image/e1a133ca-b443-4b37-9da9-edfe8d6ace48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1a133ca-b443-4b37-9da9-edfe8d6ace48?resizing_type=fit)
Stairs |  [![Stairs](https://dev.epicgames.com/community/api/documentation/image/4319314f-9c63-4e4f-9bc7-11bc349ba52e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4319314f-9c63-4e4f-9bc7-11bc349ba52e?resizing_type=fit)
##  Create
Create your own custom mesh with tools that extrude the shapes and paths you create. The mesh must be selected in the viewport for the editing to take any effect. Each tool opens up specific operational tools in the Model Mode panel.
[![Create tools in Modeling Mode.](https://dev.epicgames.com/community/api/documentation/image/54d16809-c165-4d15-8388-bd5823a6001b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54d16809-c165-4d15-8388-bd5823a6001b?resizing_type=fit)
Tool  |  Operation  |  Demo
---|---|---
Extrude Polygon |  Draw and extrude polygons to create new objects. Opens a toolset that edits the polygon attributes. |
Extrude Path |  Draw and extrude polypaths to create new objects. Opens a toolset that edits the path’s attributes. |
Revolve Path |  Draw and revolve pathways to create new objects. Opens a toolset that edits the pathway and the revolution of the mesh. |
Boundary Revolve |  Revolves the mesh boundary loops to create new objects. Opens a toolset that determines the mesh boundary and revolution. |
Merge |  Merge multiple meshes to create new objects. Opens a toolset that determines the attributes of the merge. |
Duplicate |  Duplicate a single meshes to create new objects. Opens a toolset that determines the attributes of the duplicate mesh. |
Pattern |  Creates a pattern using the selected mesh. The pattern takes on a shape as well:
  * Line
  * Grid
  * Circle

|
##  Transform
Transform and change the pivot points on your mesh or its child components with the following tools. Each tool opens specific operational tools in the Modeling Mode panel.
Perform multiple actions to either control the movement of the mesh, or capture mesh data after editing and moving mesh parts or whole meshes.
[![Transform editing options.](https://dev.epicgames.com/community/api/documentation/image/188c6055-edcd-4563-94b6-7991ca52bb6c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/188c6055-edcd-4563-94b6-7991ca52bb6c?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
Transform |  Opens a toolset to transform different aspects of the selected mesh. |
Align |  Opens a toolset that aligns the selected meshes in relation to one another. |
Edit Pivot |  Opens tools to edit the pivot point placement on the selected mesh. |
Pivot Actor |  Adds an Actor object to the selected mesh to act as a pivot for child components, and opens tools to edit the pivot points and Actor object. |
Bake Transform |  Bakes the scale and rotation values of an instanced mesh into the parent Static Mesh Asset. |
Transfer |  Transfers the data of one mesh to a target mesh or to a specific LOD used by the target mesh. |
Convert |  The mesh body is converted to a solid or surface body and displayed in the canvas and the Browser. A toolset opens to edit the surface of the mesh body. |
Split |  Takes a mesh with disconnected geometry and splits them into separate mesh assets. |
##  Deform
Deforms a mesh in different ways by selecting sections of the mesh and applying an effect to the mesh or editing the mesh directly by sculpting selected areas.
[![Deform editing options.](https://dev.epicgames.com/community/api/documentation/image/6a14b0a6-e638-4c48-bbe4-d644082a4978?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6a14b0a6-e638-4c48-bbe4-d644082a4978?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
Vertex Sculpt |  Enables sculpting on the target mesh through the use of several different sculpting brushes. |
Dynamic Sculpt |  Enables sculpting on the target mesh through the use of several different sculpting brushes and dynamically adds new geometry to the mesh through remeshing. |
Smooth |  Flattens the surface of the mesh and opens a toolset to determine the degree of smoothness to apply to the mesh. |
Offset |  Offsets the surface of the selected mesh. |
Warp |  Warps applies some kind of bend or flare to the overall profile of the target mesh and opens a toolset that determines the amount of wrapping and how to warp the mesh. |
Lattice |  Adds a lattice effect to the surface of the selected mesh and opens tools that determine where and how the lattice effect will apply to the mesh. |
Displace |  Adds a wave effect to the surface of the selected mesh and opens tools that determine how to add the effect, and to what degree to add the deformity to the mesh surface. |
##  PolyEdit
Edit the polygons of your mesh to create a new asset for your project, or transform an object you downloaded. Polymodel tools work by selecting groups of polygons. The edits made directly affect all the selected polygons in the group according to the PolyModel tool you use and the edits you make.
[![The Poly Edit tool options](https://dev.epicgames.com/community/api/documentation/image/dab3b189-dc57-469a-82af-38adccc9026d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dab3b189-dc57-469a-82af-38adccc9026d?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
PolyGroup Edit |  Opens tools to edit meshes via PolyGroups. |
Deform PolyGroups |  Opens tools to deform meshes via their PolyGroups. |
CubeGrid |  Opens tools to create blockout meshes using a repositionable grid. |
Boolean |  Opens tools to apply boolean operations to mesh pairs. |
Mesh Cut |  Split one mesh into parts using a second mesh. A toolset opens to determine how to split the mesh. |  [![Splitting a mesh with another mesh](https://dev.epicgames.com/community/api/documentation/image/21ef240e-2ac2-4b0b-9dd7-aff62f143d34?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21ef240e-2ac2-4b0b-9dd7-aff62f143d34?resizing_type=fit)
Subdivide |  Subdivide mesh by PolyGroups or triangles. A toolset opens to determine how to subdivide the mesh. |  [![Subdivide mesh gif](https://dev.epicgames.com/community/api/documentation/image/be33b6f1-9e56-48f5-b31b-1ca38b519ddf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be33b6f1-9e56-48f5-b31b-1ca38b519ddf?resizing_type=fit)
##  TriTools
Edit the triangles of your mesh to create a new object for your project. TriModel tools work by selecting and editing groups of triangles or creating triangle groups on the selected mesh.
[![TriTools editing options.](https://dev.epicgames.com/community/api/documentation/image/e4088e2a-e4fe-4c54-a76b-6e5b3261df3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4088e2a-e4fe-4c54-a76b-6e5b3261df3d?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
Tri Select |  Select and edit mesh triangles with the tools that determine brush size and radius as well as triangle tolerances and polygroup layers. |
Triangle Edit |  Opens tools to edit the mesh via triangles. |
Fill Holes |  Fills any holes in your mesh. |
Plane Cut |  Cut Selected mesh on a plane. Opens tools to determine the scope of cut to be made. |  [![Cut a mesh on a plane](https://dev.epicgames.com/community/api/documentation/image/c35dd530-2f4f-4e3b-8022-980f0a4887d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c35dd530-2f4f-4e3b-8022-980f0a4887d6?resizing_type=fit)
Mirror |  Creates a mirror with the extrude polygon and opens a toolset to define the new mesh. |
PolyCut |  Cut the selected mesh with extrude polygon and open tools to define the new mesh. |
Trim |  Trim or cut selected meshes with a second mesh. Use the tools to determine how to trim the second mesh. |
##  MeshOps
Edit the mesh’s polygons and triangles with the tools available in MeshOps. Each tool opens specific operational tools in the Modeling Mode panel. The tools target triangle groups to add or reduce triangles that alter a mesh’s structural integrity.
[![MeshOps editing options.](https://dev.epicgames.com/community/api/documentation/image/3b85ebed-4457-465e-9204-603506860b2f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3b85ebed-4457-465e-9204-603506860b2f?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
Simplify |  Attempts to reduce the triangle density of the selected mesh and opens a toolset that edits different aspects of the mesh’s polygons and triangles. |
Remesh |  Opens a set of tools to retriangulate and increase triangle density on the selected mesh. |
Weld |  Automatically welds disconnected edges of the selected meshes within a given tolerance, and opens a toolset to edit the weld settings. |
Jacket |  Opens a toolset that removes hidden triangles from the selected meshes. |
Union |  Resolves self-intersections (including Self-Union) using Boolean Union on selected meshes. |
Project |  Opens a toolset to map or remesh one mesh onto the targeted mesh (the second selected mesh). |
##  VoxOps
Adds and edits the [voxels](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#voxel) associated with your mesh. Each tool opens up specific operational tools in the Model Mode panel that add, reduce, or edit the mesh’s three dimensional data according to the settings chosen.
[![The VoxOps editing options](https://dev.epicgames.com/community/api/documentation/image/c7e7116d-60ed-4b02-b1a3-d82aecbb0b2d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7e7116d-60ed-4b02-b1a3-d82aecbb0b2d?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
Vox Wrap |  Opens a toolset to wrap selected meshes using voxels. (Voxel-based) |
Vox Blend |  Opens a toolset to blend selected meshes using voxels. (Voxel-based) |
Vox Offset |  Opens a toolset that can offset or inset selected meshes using voxels. (Voxel-based) |
Vox Boolean |  Opens a toolset to perform boolean operations on selected meshes and then wrap the result with voxels. (Voxel-based) |
Vox Merge |  Opens a toolset that merges selected meshes then voxelates the result. (Voxel-based) |
##  Baking
Use the baking tools to bake a custom mesh to the specs you set. Baking is the process of saving and editing texture information of the selected mesh.
[![Baking edit options.](https://dev.epicgames.com/community/api/documentation/image/aadd372c-b1e2-4850-aac1-35d86c3bd237?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aadd372c-b1e2-4850-aac1-35d86c3bd237?resizing_type=fit)
Tools  |  Operation  |  GIF
---|---|---
Bake Textures |  Opens a toolset to bake textures for a single mesh. |
Bake All |  Opens a toolset to bake textures for single meshes from the multiple source meshes. |
Bake Vertex Colors |  Opens a toolset that bakes vertex colors for single meshes. |
##  UVs
Edit the [UV](https://docs.unrealengine.com/uvs-category-in-unreal-engine/) coordinates of a mesh, changing how textures are mapped to the surface. The UV tools determine whether the mesh’s material displays evenly across the mesh.
[![UV editing options.](https://dev.epicgames.com/community/api/documentation/image/1c9ae0fd-8fa8-4a04-97e1-76b586ffd6c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c9ae0fd-8fa8-4a04-97e1-76b586ffd6c5?resizing_type=fit)
Tools  |  Operation  |  GIF
---|---|---
AutoUV |  Automatically unwrap and pack UVs for the selected mesh. |
UV Unwrap |  Recompute UVs for existing UV islands or PolyGroups, helping minimize stretched and squashed areas. |
Project UVs |  Creates UVs from casting a predefined shape or point onto your target mesh. |
Edit UV Seams |  Interactively separate edges in the Viewport to create seams. |
Transform UVs |  Interactively scale, rotate, and translate UV islands in the Viewport. |
Layout UVs |  Transform, stack, or repack existing UVs. |
UVEditor |  Launch a dedicated [Editor](https://docs.unrealengine.com/uv-editor-in-unreal-engine/) for creating and editing UVs. |
For more information on how to add shading on your static mesh, refer to [Shading Models in Unreal Engine](https://docs.unrealengine.com/shading-models-in-unreal-engine/).
##  Attributes
Update, edit, and add attributes to meshes in your project. Each tool opens up specific operational tools which edit the mesh’s topographical data necessary for creating and assigning data to UVs.
[![The Attribute editing options.](https://dev.epicgames.com/community/api/documentation/image/ce56ed25-c28a-47e3-8c7e-5cc1b52d8537?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce56ed25-c28a-47e3-8c7e-5cc1b52d8537?resizing_type=fit)
Tools  |  Operations  |  GIF
---|---|---
Inspect |  Adds a layer of highlighted polygons to your mesh and displays mesh data statistics. Edit your mesh by toggling options on and off. |
Normals |  Recomputes the [normals](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#normal) and opens tools to set Normals calculations by toggling options on and off, and set the Normals Topography. |
Tangents |  Opens a toolset to edit the mesh’s lines and tangents. |
Edit Attributes |  Opens a toolset to edit the mesh’s different attributes, UVs, and add new attributes as well. |
Generate PolyGroups |  Covers the mesh in a bright polygroup skin and opens tools to edit the PolyGroups of the selected mesh. |
Paint PolyGroups |  Enables users to paint PolyGroups onto a mesh using brushstrokes. |
Paint Maps |  Allows users to paint on specific weightmap layers, which first need to be generated with the Attribute Editor. |
Edit Materials |  Allows users to assign materials and new material elements to triangles selected via brushstrokes. |
##  Volumes
Edit and create volumes for your meshes, set collision and more with the Volumes toolset. The Volume toolset provides a way for you to set collisions for your mesh and edit the physics and geometry of your mesh.
[![Volume edit options.](https://dev.epicgames.com/community/api/documentation/image/ccaa302f-01d2-4fd9-824c-449bfc8ea69c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ccaa302f-01d2-4fd9-824c-449bfc8ea69c?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
Volume to Mesh |  Opens a tool to define and convert volume to a new mesh asset. |
Mesh To Volume |  Opens a toolset that defines the conversion of a mesh to a new volume object. |
Inspect Collision |  Opens a toolset to inspect physics geometry for the selected mesh. |
Mesh To Collision |  Convert selected meshes to **Simple Collision** geometry for the last selected mesh. Opens a toolset to define and edit the [collision](https://dev.epicgames.com/documentation/fortnite/unreal-editor-for-fortnite-glossary#collision) settings of the mesh. |
Collision To Mesh |  Opens a toolset that defines and converts **Simple Collision** geometry to a mesh. |
##  LODs
Edit, define, and create LODs for a new mesh or one you’ve edited. These tools decide the visual information your mesh generates depending on a player’s proximity to the mesh and the platform used to interact with the mesh in game.
[![LOD editing options.](https://dev.epicgames.com/community/api/documentation/image/7ddf7a87-f4dc-464c-8cd6-2a8edcfbb6b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ddf7a87-f4dc-464c-8cd6-2a8edcfbb6b4?resizing_type=fit)
Tool  |  Operation  |  GIF
---|---|---
LOD Manager |  Opens the LOD Manager to define and create LODs for the selected Static Mesh asset. |
AutoLOD |  Opens a toolset to generate and define Static Mesh LOD assets. |
