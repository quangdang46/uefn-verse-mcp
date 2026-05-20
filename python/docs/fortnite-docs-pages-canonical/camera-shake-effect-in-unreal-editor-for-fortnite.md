## https://dev.epicgames.com/documentation/en-us/fortnite/camera-shake-effect-in-unreal-editor-for-fortnite

# Camera Shake Effect

Add a camera shake to your level sequence to create a distinct cinematic mood for your project.

![Camera Shake Effect](https://dev.epicgames.com/community/api/documentation/image/2370fc11-f6d8-412e-84d7-05d70c5c6bc4?resizing_type=fill&width=1920&height=335)

Add a tension-building camera shake to a [level sequence](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#sequencer) or [actor](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#actor) using a **camera shake effect**.

You can add a camera shake during the sequence editing process, or after a sequence has been created.

Create a camera shake using a Blueprint class. You can then attach the camera shake Blueprint class to an actor in your [project](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#project) or a sequence during the editing process.

[![An example of camera shake applied to a level sequence.](https://dev.epicgames.com/community/api/documentation/image/738d0829-38ed-4be4-bac2-d901ba3394e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/738d0829-38ed-4be4-bac2-d901ba3394e9?resizing_type=fit)

There are 4 different **camera shake patterns**:

Both the Perlin Noise Camera Shake Pattern and the Wave Oscillator Camera Shake Pattern are created by determining the amplitude and frequency for the camera shake effect’s location, rotation, and field of view (FOV). You can edit it further by determining the duration of the effect and the blend in and out time to fade it in and out.

The camera’s rotation is determined by roll, yaw, and pitch (X, Y, Z).

[![Rotation directions.](https://dev.epicgames.com/community/api/documentation/image/183621f2-36ec-4f3b-b500-970a5172bb47?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/183621f2-36ec-4f3b-b500-970a5172bb47?resizing_type=fit)

## Creating the Blueprint Object

1. Right-click in the **Content Browser** and select **Blueprint Class**.

   [![Right-click in the Content Browser to create a blueprint class.](https://dev.epicgames.com/community/api/documentation/image/e74899fc-9eb5-4038-b338-e1386977c255?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e74899fc-9eb5-4038-b338-e1386977c255?resizing_type=fit)
2. Go to **CameraShakeBase** > **Select**.

   [![Select camera shake base.](https://dev.epicgames.com/community/api/documentation/image/7bf955d0-69ba-45e9-b917-26266858b90c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7bf955d0-69ba-45e9-b917-26266858b90c?resizing_type=fit)
3. Name the **Camera Shake** Blueprint object.

   [![Name the camera shake class.](https://dev.epicgames.com/community/api/documentation/image/75577eba-abf2-4679-a91a-2a25be12eb95?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75577eba-abf2-4679-a91a-2a25be12eb95?resizing_type=fit)
4. Double-click the **Camera Shake** thumbnail to open the shake editor.
5. Select the **Perlin Noise Camera Shake Pattern** from the **Root Shake Pattern** dropdown menu. The camera shake editor opens once a shake pattern is selected.

   [![Select a camera shake pattern from the Root Shake Pattern drop down menu.](https://dev.epicgames.com/community/api/documentation/image/697b39ff-fb6b-44d9-92f8-67dc8a26c8ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/697b39ff-fb6b-44d9-92f8-67dc8a26c8ad?resizing_type=fit)
6. Set the **Location Amplitude Multiplier** to **20** and the **Location Frequency Multiplier** to **5**.
7. Set the **Duration** to **20**.
8. Click **Compile** > **Save**.

The camera will shake at an amplitude of 20. A frequency of 5 means that it will reach the peak (a location move of 20 units) about 5 times per second, so it will shake about a hundred times over the 20 seconds.

The effect will fade in and out for 0.2 seconds (the default fade in and out). The higher the amplitude, the more vigorous the shake will be. This can be a problem for players who have issues with seizures.

The lower the amplitude, the less likely the camera shakes will be an issue for players. An amplitude range of 2–75 should be enough for a sequence that contains a camera shake pattern.

### Adding a Camera Shake Effect to a Sequence

Create a sequence with a camera shake effect to add a sense of urgency or size to a boss character or gameplay.

1. Create a sequence by right-clicking in the **Content Browser** and selecting **Cinematics** > **Level Sequence**.

   [![Create a level sequence.](https://dev.epicgames.com/community/api/documentation/image/824baabc-d661-4f6a-b835-7447e24e2670?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/824baabc-d661-4f6a-b835-7447e24e2670?resizing_type=fit)
2. Name the sequence thumbnail.

   [![Name the level sequence thumbnail.](https://dev.epicgames.com/community/api/documentation/image/3d3516cf-0ece-4096-a139-6b185ea15c20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d3516cf-0ece-4096-a139-6b185ea15c20?resizing_type=fit)
3. Double-click the sequence thumbnail to open the sequence editor.
4. Follow the direction in the [**Sequencer and Control Rig**](sequencer-and-control-rig-in-unreal-editor-for-fortnite) document to create a sequence.
5. Click the **Track icon** next to the **CineCameraActor** and select **Camera Shake** > **Blueprint Class** (the camera shake effect you created).

   [![Add the camera shake effect you created to the sequence.](https://dev.epicgames.com/community/api/documentation/image/963806e4-766b-46d2-9017-76e9c6b461bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/963806e4-766b-46d2-9017-76e9c6b461bc?resizing_type=fit)
6. Move the Blueprint camera shake class into the sequence and stretch the camera shake to the duration you want the shake to take effect for during the sequence.

   [![Move and edit the camera shake in the sequence.](https://dev.epicgames.com/community/api/documentation/image/936396c3-fd3d-4530-885e-09151e7652b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/936396c3-fd3d-4530-885e-09151e7652b0?resizing_type=fit)
7. Click **Save**.

Your level sequence has the camera shake effect applied to the sequence.

You can even add the camera shake effect to the sequence while editing your sequence. It works much like the workflow above.

This adds the camera shake to your project and plays for the duration set in the camera shake effect Duration settings.

### Adding a Camera Shake Effect to an Actor

Make the camera shake activate for a player based on their proximity to an actor.

A thumbnail is created for the Blueprint Class associated with the actor in your project.

[![An example of a Blueprint Class thumbnail.](https://dev.epicgames.com/community/api/documentation/image/2e0fd8c3-4c9f-41ca-bd26-02454ae5624c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e0fd8c3-4c9f-41ca-bd26-02454ae5624c?resizing_type=fit)

Playtest your project to see the camera shake based on how far away the player is from the actor in the scene. If you want the camera to shake only when a player is close, change the Inner and Outer Attenuation Radius settings to an amount less than 10.
