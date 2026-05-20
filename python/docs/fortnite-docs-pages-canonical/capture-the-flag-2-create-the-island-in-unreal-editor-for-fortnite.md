## https://dev.epicgames.com/documentation/en-us/fortnite/capture-the-flag-2-create-the-island-in-unreal-editor-for-fortnite

# 2. Create the Island

Build the bases, add colored elements to each base, and build the boundaries of your island.

![2. Create the Island](https://dev.epicgames.com/community/api/documentation/image/ccfd98f1-8102-4397-94c3-9eefb8f63a22?resizing_type=fill&width=1920&height=335)

**Devices used:**

- 4 x [Barrier](https://www.fortnite.com/en-US/creative/docs/using-barrier-devices-in-fortnite-creative)

You will need the following prefabs and galleries to build your base:

- **Castle Keep Prefab**: Navigate to **All > Fortnite > Prefabs > Castle** for this prefab. These are the buildings that will be the team bases. You'll need two.
- **Castle Gallery B**: Navigate to **All > Fortnite > Galleries** for the next items. These pieces have no snow, so they are useful for using indoors if you want to change how the inside of the castle prefab looks.
- **Castle Gallery C**: This gallery has some outdoor building pieces that have snow on them, but it also has walls and doors.
- **Castle Gallery D**: This gallery has castle building pieces that have snow on them, including ramps and stairs.
- **Military Gallery B Red, Military Gallery B Blue**: These have colored plaques to place on walls of bases to further identify the team each base belongs to.
- **Castle Prop Gallery**: Found in **All > Fortnite > Props > Castle**, this gallery contains props for the inside of the castle, such as furniture, torches, banners, and other decorations.
- **Ice House Gallery**: Found in **All > Fortnite > Props > Ice House**, this has the ice walls you need for the underground part of the map.

When using the [**Content Browser**](unreal-editor-for-fortnite-glossary#content-browser), hold down **Ctrl** and select multiple folders to display their contents at the same time.

Each base will have a basement and an underground path that connects the two bases. You will need to make a space for the underground part before placing the bases.

Remember to save your progress!

[![savegame](https://dev.epicgames.com/community/api/documentation/image/19f1a407-adc5-4f78-a08c-61d81b973203?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19f1a407-adc5-4f78-a08c-61d81b973203?resizing_type=fit)

## Add Colored Elements to Each Base

Next, add colored props and decorations that let the players know which base belongs to which team. The example uses red and blue, but you can choose any two colors. To follow this tutorial more easily, use red and blue.

[![Blue Base](https://dev.epicgames.com/community/api/documentation/image/8f934822-6bd4-43ba-9e7e-eb20db44b071?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f934822-6bd4-43ba-9e7e-eb20db44b071?resizing_type=fit)

The torches are customizable lights, so you can change the color of a light to red or blue depending on where you place it, then copy and paste the customized torch.

Use the elements in the blue and red Military Galleries to further identify each team’s base.

## Create Island Boundaries

Once your base is built out and you've added red and blue props to identify each side, you can place **Barrier devices** around the area. The play area includes the two bases and the courtyard area between them. The underground area has the same dimensions as the above-ground play area.

Place the Barrier devices against the outer walls of the play area so players can’t accidentally leave the play area or get stuck.

Configure the **User Options** for the first barrier as follows:

| Option | Value | Explanation |
| --- | --- | --- |
| **Barrier Material** | Choose one | The material you select is a matter of personal preference. |
| **Base Visible During Game** | False | The barrier device shouldn't be visible to players. |
| **Block Weapon Fire** | True | Weapon fire can't go through the barrier. |
| **Zone Shape** | Hollow Box | Players will spawn inside the barrier this way. |

[Playtest your island](playtesting-your-island-unreal-editor-for-fortnite) at any time by clicking the "Launch Session" button.

[![Launch Session](https://dev.epicgames.com/community/api/documentation/image/f72bd67a-e472-4dac-aeff-859616eb5abb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f72bd67a-e472-4dac-aeff-859616eb5abb?resizing_type=fit)

## Next Section

- [![3. Set Up Classes and Teams](https://dev.epicgames.com/community/api/documentation/image/5793afeb-2869-4a2b-9d1e-34a0ceac499b?resizing_type=fit&width=640&height=640)

  3. Set Up Classes and Teams

  Use Class Designer devices to set up classes and the Team Settings device to configure the teams.](https://dev.epicgames.com/documentation/fortnite/capture-the-flag-3-set-up-the-classes-and-teams-in-unreal-editor-for-fortnite)
