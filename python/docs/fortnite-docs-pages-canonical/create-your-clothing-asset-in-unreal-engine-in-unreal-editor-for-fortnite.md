## https://dev.epicgames.com/documentation/en-us/fortnite/create-your-clothing-asset-in-unreal-engine-in-unreal-editor-for-fortnite

# Create your Clothing Asset in Unreal Engine

Create a new Unreal Engine project and generate a new cloth asset.

![Create your Clothing Asset in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/167a3bad-3200-40ec-a6f1-6115af31ed4b?resizing_type=fill&width=1920&height=335)

The process of converting your cloth meshes into cloth assets is performed in Unreal Engine 5. In this section, we will import a USD file from Marvelous Designer. However, you can import assets from any external DCC package in FBX or USD formats.

As part of the Talisman: MetaHuman template, you can access several downloadable assets including an Unreal Engine project with the MetaHuman wearing Captain Roux’s jacket from the Talisman GDC demo. To learn how to access the downloadable files, see the [Talisman MetaHuman Template tutorial](talisman-metahuman-template-in-unreal-editor-for-fortnite).

Once you download the files, follow these steps to convert your meshes into a Cloth Asset:

### Create a New Unreal Engine Project

### Create the Cloth Asset

You can **download** the source files used in this guide by going to the [Talisman MetaHuman Template tutorial](talisman-metahuman-template-in-unreal-editor-for-fortnite). Once downloaded, go to **T > CaptainRoux_Cloth_Learning_Assets > CaptainRoux_Cloth_Learning_Assets > Cap_Jacket_SourceArt** to find the source files used in this tutorial.

[![Source assets available for download](https://dev.epicgames.com/community/api/documentation/image/25986183-f5a4-4a24-b1be-74f463d6b23b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25986183-f5a4-4a24-b1be-74f463d6b23b?resizing_type=fit)

In this section you will create a physics **cloth asset**. This asset contains the result of the cloth Dataflow graph which may include panel cloth data from Marvelous Designer or static and skeletal meshes. The cloth Dataflow graph includes the logic used to process the panel data and meshes so they can simulate during gameplay.

#### Navigate the Cloth Asset Panel Editor

The Cloth Asset Panel Editor has the following sections:

#### Import the Cloth Meshes

1. For this example, you will create the Dataflow graph from scratch.

   [![Select the USD file you exported from your DCC package](https://dev.epicgames.com/community/api/documentation/image/fa85678c-ace8-4ca9-ab1d-ac0263f361d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa85678c-ace8-4ca9-ab1d-ac0263f361d2?resizing_type=fit)
2. Drag from the **Collection** pin and search for then select **DeleteElement**.

   [![Add a DeleteElement node and enable Delete Render Mesh](https://dev.epicgames.com/community/api/documentation/image/a9e1573a-48e0-4545-a758-0e1d1ae53954?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9e1573a-48e0-4545-a758-0e1d1ae53954?resizing_type=fit)
3. Drag from the **Collection** pin and search for then select **TransformPositions**.

   [![Add a TransformPositions node, enable Transform 2D Sim Positions and set the SIM 2D Scale to 0.1 for X and Y](https://dev.epicgames.com/community/api/documentation/image/a26adc18-5f25-459b-9f65-2a200b181c23?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a26adc18-5f25-459b-9f65-2a200b181c23?resizing_type=fit)
4. Drag your custom render mesh FBX file to the **Content Browser** and select the appropriate import settings for your model, such as Generate Missing Collision and Create New Materials.

   [![Drag your custom render mesh FBX file to the Content Browse**r**](https://dev.epicgames.com/community/api/documentation/image/b4c55f2d-7c3d-40ce-a685-dfd8b33a3598?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b4c55f2d-7c3d-40ce-a685-dfd8b33a3598?resizing_type=fit)

   [![Select the appropriate import settings for your model](https://dev.epicgames.com/community/api/documentation/image/a3901f7d-3ce5-47ee-900e-a8080560408b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3901f7d-3ce5-47ee-900e-a8080560408b?resizing_type=fit)
5. Right click in the graph and search for then select **StaticMeshImport**.

   [![Add a StaticMeshImport node and add the imported Static Mesh and deselect Import Sim Mesh](https://dev.epicgames.com/community/api/documentation/image/e9e1ee06-029e-42f7-89b6-5318b703a3c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9e1ee06-029e-42f7-89b6-5318b703a3c3?resizing_type=fit)
6. Right click in the graph and search for then select **MergeClothCollections**.

   [![Add a MergeClothCollections node and right click and select Add Option Pin](https://dev.epicgames.com/community/api/documentation/image/84d29454-0f43-4beb-9715-c56a49a6fff0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/84d29454-0f43-4beb-9715-c56a49a6fff0?resizing_type=fit)

   [![Connect the Collection from the StaticMeshImport node to the MergeClothCollections** **node](https://dev.epicgames.com/community/api/documentation/image/eb24786a-8d4b-4715-b456-a3422afe0522?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eb24786a-8d4b-4715-b456-a3422afe0522?resizing_type=fit)

## Next step

- [![Configure the Clothing Asset Parameters](https://dev.epicgames.com/community/api/documentation/image/580b2e0e-f4cd-4de9-891f-bb1646f13ae4?resizing_type=fit&width=640&height=640)

  Configure the Clothing Asset Parameters

  Configure the parameters of the cloth asset to ensure proper functionality.](https://dev.epicgames.com/documentation/fortnite/configure-the-clothing-asset-parameters-in-unreal-editor-for-fortnite)
