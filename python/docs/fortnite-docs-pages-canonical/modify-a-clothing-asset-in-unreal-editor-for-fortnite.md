## https://dev.epicgames.com/documentation/en-us/fortnite/modify-a-clothing-asset-in-unreal-editor-for-fortnite

# Modify a Clothing Asset in UEFN

A guide on modifying a clothing asset inside Unreal Editor for Fortnite.

![Modify a Clothing Asset in UEFN](https://dev.epicgames.com/community/api/documentation/image/cb9cd423-718e-4e76-8547-cdbf9d53f6c5?resizing_type=fill&width=1920&height=335)

In this guide, you will learn how to modify your clothing material to add additional color variety to the same asset. In addition, we will explain how to modify the material textures outside of UEFN to achieve a similar effect.

Import your MetaHuman into UEFN and set up a clothing asset by following the steps outlined in the [**Import your Clothing Assets to UEFN**](import-your-clothing-asset-to-unreal-editor-for-fortnite) guide.

## Modify the Clothing Material

Follow these steps to modify the material associated with your clothing asset:

1. Open your **MetaHuman Blueprint** and select the **ChaosCloth component** in the **Components** window.

   [![Open your MetaHuman Blueprint and select the ChaosCloth component](https://dev.epicgames.com/community/api/documentation/image/31273017-0d8f-4cd6-925e-654bab81fa58?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/31273017-0d8f-4cd6-925e-654bab81fa58?resizing_type=fit)
2. Go to the **Details** panel and scroll down to the **Materials** section.
3. Double click the material to open it. This will open the **Material Editor** where you can edit the node graph that creates the final material applied to your clothing asset. To learn more about materials, please see the [Materials](https://dev.epicgames.com/documentation/fortnite/materials-in-unreal-editor-for-fortnite) documentation for UEFN.

   [![Double click the material to open it](https://dev.epicgames.com/community/api/documentation/image/7cddf809-993d-4e42-96ce-bc9effe20143?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7cddf809-993d-4e42-96ce-bc9effe20143?resizing_type=fit)
4. Move the **Texture Sample** node to make space, right click in the **Material Graph**, and search for then select **Constant3Vector**.

   [![Right click in the Material Graph, and search for then select Constant 3 Vector](https://dev.epicgames.com/community/api/documentation/image/93e9aed8-a0bb-4515-b9a4-8d164f9ba95f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93e9aed8-a0bb-4515-b9a4-8d164f9ba95f?resizing_type=fit)
5. With the node selected, go to the **Details** panel and click the **Constant** to open the **Color Picker.** Set the color to white and click **OK.**

   [![Click the Constant to open the Color Picker, set the color to white and click OK](https://dev.epicgames.com/community/api/documentation/image/0cf0fc79-e4b5-44dd-8bec-545741a21212?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0cf0fc79-e4b5-44dd-8bec-545741a21212?resizing_type=fit)
6. Right click in the **Node Graph** and search for then select **Multiply.**

   [![Right click in the Node Graph and search for then select Multiply](https://dev.epicgames.com/community/api/documentation/image/47b40c83-d931-4122-8ad9-60b03fa99705?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47b40c83-d931-4122-8ad9-60b03fa99705?resizing_type=fit)
7. Connect the **Texture Sample** node and the **Constant3** node to the **A** and **B** pins of the **Multiply** node. Connect the **Multiply** node to the **Base Color** pin of the **Material** node.

   [![Connect the Texture Sample and Constant 3 nodes to the Multiply node. Connect the Multiply node to the Material node](https://dev.epicgames.com/community/api/documentation/image/75305c27-e7c3-4aa4-8a52-0302dfe9bf6b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75305c27-e7c3-4aa4-8a52-0302dfe9bf6b?resizing_type=fit)
8. Right click on the **Constant3** node and select **Convert to Parameter**. Enter **Tint** as the name and click **Save**.

   [![Right click on the Constant 3 node and select Convert to Parameter](https://dev.epicgames.com/community/api/documentation/image/d7a0b794-da69-46da-be9f-a887c9c947a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7a0b794-da69-46da-be9f-a887c9c947a0?resizing_type=fit)

   [![Enter Tint as the name of the node](https://dev.epicgames.com/community/api/documentation/image/3194870b-bb7f-4c93-b012-98053c0688c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3194870b-bb7f-4c93-b012-98053c0688c5?resizing_type=fit)

   [![Click Save](https://dev.epicgames.com/community/api/documentation/image/a7b6df07-1e36-4de3-92e2-a54861882941?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7b6df07-1e36-4de3-92e2-a54861882941?resizing_type=fit)
9. Go back to the **Content Browser**, right click on the material and select **Create Material Instance.** Name the asset. In this example, we named it **MI_Cap_Jacket.**

   [![Right click on the material and select Create material instance](https://dev.epicgames.com/community/api/documentation/image/06011eb8-eb1c-4904-b745-a640c168d994?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06011eb8-eb1c-4904-b745-a640c168d994?resizing_type=fit)

   [![Name the asset MI_Cap_Jacket.](https://dev.epicgames.com/community/api/documentation/image/e665c9d8-d811-438e-b531-1bd4f4f1ef1b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e665c9d8-d811-438e-b531-1bd4f4f1ef1b?resizing_type=fit)
10. Go back to the **MetaHuman Blueprint**, select the **ChaosCloth component** and go to the **Materials** section in the **Details** panel.
11. Open the **material instance**, expand the **Global Vector Parameters** section and **enable** the **Tint** checkbox.

    [![Open the material instance, expand the Global Vector Parameters section and enable the Tint checkbox](https://dev.epicgames.com/community/api/documentation/image/48d1275c-b60a-42ae-ac3b-83cf449a0c5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48d1275c-b60a-42ae-ac3b-83cf449a0c5a?resizing_type=fit)
12. Click the **Tint** color to open the **Color Picker**. You can now select the color you want and see the changes update instantly. Pick a color and click **OK**.

    [![Click the Tint color to open the Color Picker. Pick a color and click OK](https://dev.epicgames.com/community/api/documentation/image/3074f77f-edea-4fd5-a803-f8d24caa7c21?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3074f77f-edea-4fd5-a803-f8d24caa7c21?resizing_type=fit)
13. You can right click on the **material instance** and select **Duplicate** to create multiple versions of the clothing material instance. In the example below, we created 3 versions of the jacket by duplicating the material instance and selecting a different tint.

    [![Duplicate the material instances to create different versions of the jacket](https://dev.epicgames.com/community/api/documentation/image/99bd545d-a3b9-423b-bdec-28015bd0b4a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99bd545d-a3b9-423b-bdec-28015bd0b4a2?resizing_type=fit)

## Modify the Textures Outside of UEFN

You can also add variety to your clothing asset by modifying the material's textures directly. You can export the desired textures and modify them in an external image editing software, like Photoshop. This method is more elaborate, but offers you more control over the final result.

Follow these steps to locate and export a texture from the material:

If you imported a new texture file, go back to the material and select the **Texture Sample** node. Go to the **Details** panel and scroll down to the **Material Expression Texture Base** section and replace the **Texture** with your new one.

[![Scroll down to the Material Expression Texture Base section and replace the Texture with your new one](https://dev.epicgames.com/community/api/documentation/image/f7781dc0-a667-4aec-9f67-ef359acf4b43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7781dc0-a667-4aec-9f67-ef359acf4b43?resizing_type=fit)

For your convenience, the **Cloth Learning Assets** available from the link in UEFN include the base texture and a Photoshop file with a Selective Color layer so you can quickly modify the texture for this example. To learn how to access the downloadable files, see the [Talisman MetaHuman Template tutorial](talisman-metahuman-template-in-unreal-editor-for-fortnite).

[![Download the Cloth Learning Assets and open the Cap_Jacket_Textures folder](https://dev.epicgames.com/community/api/documentation/image/cbb26084-a7ea-415b-b45b-99a4733a3a03?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cbb26084-a7ea-415b-b45b-99a4733a3a03?resizing_type=fit)
