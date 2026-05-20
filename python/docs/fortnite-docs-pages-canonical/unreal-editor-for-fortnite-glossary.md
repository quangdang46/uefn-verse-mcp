## https://dev.epicgames.com/documentation/en-us/fortnite/unreal-editor-for-fortnite-glossary

# Glossary for Unreal Editor for Fortnite

Knowing what the words mean is key to understanding how things work. Level up your island design with UEFN. This glossary is here to help!

![Glossary for Unreal Editor for Fortnite](https://dev.epicgames.com/community/api/documentation/image/fa572493-5f6f-4e16-a809-ac9c85dd2f75?resizing_type=fill&width=1920&height=335)

This glossary contains terms specific to **Unreal Editor for Fortnite (UEFN)**.

For **Fortnite Creative** terminology, see the **[Fortnite Creative Glossary](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary)**.

For terms related to the **Verse** programming language, see the **[Verse Glossary](https://dev.epicgames.com/documentation/fortnite/verse-glossary)**. For those who are interested, the Verse Glossary also contains a number of basic programming terms with definitions designed for those who are learning programming for the first time.

0 dB
:   A 0 dB does not represent no sound. Think of 0 dB as maximum volume. For example, if your receiver reads -25 dB, it means that the volume of the signal has been attenuated by 25 dB (made 25 dB quieter than the loudest it could possibly be) before being output to your speakers.

2D audio
:   Sound that plays without [spatialization](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#spatialization). This means that the sound does not change as a player moves through the game. Compare to [3D audio](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#3d-audio).

3D audio
:   Sounds that are [spatialized](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#spatialized), or located audibly in three-dimensional or virtual space.

actor
:   An actor is any object that can be placed on a level. This is a generic class of objects that supports 3D transformations such as translation, rotation and scale. Actors can be created (spawned) and destroyed through gameplay code.

air dodge
:   In Rocket Racing, you can use an air dodge to transition from driving on the ground to driving on the wall or the ceiling, or to land more quickly on the ground. This maneuver basically flips the car over.

albedo
:   The base color of an object with no shadows or highlights.

aliasing
:   A digital image distortion that can appear as a jagged or saw-toothed outline in a low-resolution monitor.

alpha channel
:   The alpha channel controls the transparency or opacity of a color. The alpha channel is what you use to remove the background from an image. A PNG image, for example, has an alpha channel that lets you set the background to be transparent.

ambient lighting
:   The amount of light in scene that has no source and no real direction. Ambient lighting illuminates the entire area evenly. Changing the color value on an ambient light can change the mood of the scene.

angle pitch
:   With camera devices, this measures how much the camera points up or down while framing its [target](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#target).

angle yaw
:   With camera devices, this measures how much the camera turns left or right while framing its [target](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#target).

Animation Blueprint
:   A node-based interface that captures the animations of the MetaHuman character.

AOE
:   Area of effect, or AOE, is an area where an effect — positive or negative — is applied to a player. This would include effects like explosive, healing, or poison/toxic.

aperture
:   A setting on a camera that controls the brightness of an image (to some degree) and more importantly, [depth of field](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#depthoffield). It is usually indicated by **f/** followed by a number, where the **f** stands for focal length, and the number indicates the length. The smaller the number, the more out of focus the background will be.

AR
:   Augmented reality, or AR, is an interactive experience where the real world is enhanced by computer-generated information that most commonly includes visual, audio, and haptic (vibrations or other motion).

articulate
:   When sections of something are connected by joints that can bend, they articulate. For example, think of an arm. It articulates at the elbow, and again at the wrist. sections connected by joints.

artificial intelligence
:   **1.**Artificial intelligence, or AI. In Fortnite, an AI is a programmed opponent, ally or other type of non-player character.

    **2.** More broadly, AI is the ability of a computer system or systems to learn, solve problems, reason, perceive information, and make decisions without the direct intervention of a human agent. It involves creating intelligent machines and software capable of simulating human cognitive functions, analyzing data, recognizing patterns, and adapting to new information to achieve specific goals.

asset reflection
:   You can expose your UEFN assets in Verse to use them from your Verse code. This is called asset reflection, and you can use it to insert images in your custom UI or change meshes for your custom props in Verse.

attack
:   The time it takes from the start of a sound for it to reach maximum volume. Compare to [release](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#release).

attenuation
:   A change in the strength or volume of a sound. Attenuation is usually tied in to proximity of the listener to the source of the sound, or how close the listener is.

audio effect

audio envelope
:   In audio, an envelope describes how a sound changes over time. The most common stages of an audio envelope are known as ADSR: [attack](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#attack), [decay](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#decay), [sustain](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#sustain), and [release](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#release). While attack, decay, and release refer to time, sustain refers to volume.

audio file
:   An audio file is a file in which sounds are saved. A sound is an audio asset.

    You can import an audio file into UEFN as a .wav .slac, .ogg, or .aif. The editor can recognize and use any of these files directly, or you can save them as [sound cues](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#soundcue), which give additional functionality.

audio generator
:   In Patchwork, this is any device that generates audio data that can be played by a speaker or other output. Examples would include the [Drum Player](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworkdrumplayer), the [Instrument Player](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworkinstrumentplayer) and the [Omega Synth](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworkomegasynth).

audio signal processing
:   An audio signal is an electronic representation of a sound. Audio signal processing is how these signals are manipulated.

    For an example in **Fortnite Creative**, in Patchwork, the [Echo Effect](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworkechoeffect) device uses audio signal processing to create and modify an echo effect.

Automatic Bounding Box
:   When this field is enabled under the World Settings tab in [UEFN](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealeditorforfortnite), the editor automatically sets collision bounds based on the collision primitives applied to the [Static Mesh](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#staticmesh) shape.

axis
:   An axis is a a fixed reference line for the measurement of coordinates.

    Fortnite takes place in three dimensions, so to locate something in the space, you need three points of reference, or three axes. These points are called the **Left**, or **L-axis** (formerly the **Y-axis**), the **Up**, or **U-axis** (formerly the **Z-axis**), and the **Forward**, or **F-axis** (formerly the **X-axis**). Collectively, these coordinates are called **LUF**.

    Imagine you are looking over a flat plane. Place a dot in the center of the plane. This is your **0** point for all dimensions. Draw a line from north to south (away from you and toward you) and make sure it goes through the 0 point. This is **F**. Now draw a line that crosses at the 0 point, but goes east to west, (left to right). This is **L**. Draw a third line that also goes through the 0 point, crossing where the other two lines cross, but going straight up and down. This is **U**. Using those three lines, you can position any object in a three-dimensional space.

    **X-axis** and **Y-axis** are still used, but only for coordinates limited to two dimensions —   such as in reference to UI content. The X-axis refers to a location left of the origin (negative values) or right of the origin (positive values). The Y-axis refers to a location down from the origin (negative values) or up from the origin (positive values).

back-solve
:   A backward solve has to do with the control rig driving a character's animation. When a control is manipulated, it looks at how the movement will affect the controls down the chain (a forward solve) and well as how its movement affects controls higher in the chain (backward solve), basically double-checking the work. Some animations and features rely on the forward or backward solve in order to add effects or motion to the character at [runtime](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#runtime).

backface
:   The back side of a mesh. This side doesn't face the camera, so it can be discarded to save memory.

bake
:   To embed pre-computed information into an asset to optimize rendering.

bark
:   You can use the Audio Player device to set use dialog lines from guards. In game development, these lines are often referred to as barks.

barn door
:   In photograph or film lighting, barn doors are hinged metal flaps you can add to a light to adjust where and how much light illuminates the camera subject. In UEFN, the same principle can be applied to lights to control a light source from the light's Details panel.

base-16
:   Hexadecimal (from hexa-, meaning six, and decimal, meaning ten), base-16 (often shortened to hex), is a numbering system that uses 16 symbols, instead of the more familiar 10 symbols in base-10.

BGM
:   You can use background music (BGM) to create or shift a mood in your UEFN experience.

bidirectional
:   Functioning in two directions.

bit
:   A unit of computer information based on a binary choice: 0 or 1, yes or no, on or off. Also see [byte](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#byte).

bite
:   A control on the [Omega Synth](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworkomegasynth) device that gives sounds a harsher, choppier feel.

bitmap
:   A bitmap is an image file format used to create and store computer graphics. A bitmap file displays the image in small dots that create an overall image. It is abbreviated as BMP, and a bitmap file has the extension **.bmp**.

Boolean operation
:   In 3D modeling, a Boolean operation refers to the creation of intersections and unions of objects, and the subtraction of one object from another. For example, if you wanted to make a round disk with a hole in the middle, you could overlap a smaller disk with a larger one, then subtract the smaller disk with a Boolean operation.

boom collision
:   In film, a boom jib is an apparatus that holds the camera. Boom operators can move and orient the camera with levers and wheels to get the shot they desire. You can use the Boom Collision properties for a fixed-angle camera device to determine the behavior of that camera when an object in the scene gets between the camera and its target.

bound

bounding box
:   A container for all collision properties that can be set on a [Static Mesh](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#staticmesh). When you import a Static Mesh into [UEFN](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealeditorforfortnite), the editor generates [collisionprimitives](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#collisionprimitive) to control how that mesh will render and interact with physics. Bounding boxes are used for things like [rendering](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#render), [culling](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#cull), lighting, and [physics](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#physics).

BPM
:   Short for beats per minute, this is the tempo that music plays at. For example, 60 bpm is a slow, relaxing tempo, while 150 bpm is much more lively.

branching logic
:   With branching logic, a computer program sends new instructions based on specific conditions being met by the player. Also see [logic](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#logic).

bug

byte
:   A unit of computer information made up of eight [bits](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#bit).

camera offset
:   With a camera device, the camera view normally centers on its [target](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#target). The offset is how far from the center the camera view is. The camera can have an offset amount on the L-, U-, or F-axis, and on more than one [axis](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#axis) at a time.

camera transition
:   When you're using multiple camera devices, a **transition** controls the image change as you move from one camera view to another. Different **transition types** influence the shift between [keyframes](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#keyframe):

    - Linear The camera view shifts cleanly from one camera to the next, at a constant pace between frames.
    - Ease In Makes the transition start slowly then gain speed.
    - Ease Out This option slows down the transition before it stops.
    - Ease In-Out Combines Ease In and Ease Out, so slow at start, speeding up, then slow to stop at end.

canvas
:   A canvas is a container [widget](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#widget) that holds other widgets. You can position other widgets within the canvas using canvas slots to design a custom UI for a player. When a canvas widget is at the top of the UI [hierarchy](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#hierarchical), it represents the whole screen.

cell
:   A subdivision in the [World Partition](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#worldpartition) that is loaded and unloaded based on the location of the [streaming source](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#streamingsource). Cells are based on grid size.

chamfered edge
:   A transitional edge between two surfaces to ease the appearance of a sharp line or edge. A type of bevel, it uses a 45° angle where the surfaces meet.

child entity
:   An [entity](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#entity) that is nested under another entity (its parent entity) in the [entity hierarchy](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#entityhierarchy).

chromatic aberration
:   Refraction is when light bends as it passes from one transparent substance into another, and affects how objects are perceived. For example. rainbows are the result of refraction. Chromatic aberration is the effect from refraction when different wavelengths of light pass through slightly different angles, resulting in a failure to focus. Depending on the amount of chromatic aberration used in a post-process volume, you will either end up with some blurring around the edges of the scene, or with blurring throughout the entire scene.

cinematic sequence
:   A sequence is a series of shots that are edited together. A cinematic sequence tells a short story or glimpse into a story much like a movie would.

click-through rate
:   See [CTR](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#ctr).

collision
:   If an [asset](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#asset) has collision enabled, this means it is solid to the player's character and the character cannot pass through it. For example, if you place a Barrier around the edge of an island, players are blocked and can't fall off the edge. You can also use collision settings for things you want a player or character to interact with. You can't attack something that doesn't have collision enabled, for example. You can't pick up something that doesn't have collision either — a character's hand just passes through it.

collision primitive
:   A simple, primitive shape, such as a box or sphere, that can be used to set collision boundaries and other object behaviors.

color channel
:   Digital images are composed of combinations of the primary light colors red, green, and blue (RGB). Each of these colors can be viewed separately on a channel. A black and white image has only one channel.

color grading
:   Color grading is an effect that you can use to create a mood by subtly altering the appearance of colors. Color grading differs from color correction, which attempts to adjust images to real life colors.

color space
:   A way of defining how [RGB](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#rgb) colors are represented on a monitor or device. The color space used can determine how vibrant the colors are, how deep the darks are and how bright the lights and whites are. Compare to [gamut](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#gamut).

color temperature
:   In light, color temperature is measured in [Kelvins (K)](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#kelvinscale). The higher the number, the cooler (whiter or bluer) the light appears. The lower the number, the warmer (more yellow) it appears. Cooler light can appear brighter, even though Kelvins don't measure actual light output.

command line interface
:   A way of bypassing a GUI (graphical user interface) and sending a command directly to a program from a command line prompt. Some applications (UEFN is one) also have a command line interface that accepts command lines. Command lines are most often used by programmers, where it's faster to enter a command directly than to navigate through one or more GUIs.

commit
:   A commit is when you record a set of changes in code to a [version control](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#versioncontrol) system.

     In Verse, a commit is when code effects of a [failable expression](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#failableexpression) are made permanent after that expression succeeds.

communication framework
:   A way of sharing data between different components. In [UEFN](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealeditorforfortnite), this is a communication framework that passes or shares data between components, including a [Fortnite DS](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#fortniteds), a [PC game client](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#client), an [uncooked editor server](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#uncookededitorserver), and the Fortnite Editor.

competitive race
:   In Rocket Racing, a competitive race is where all players are on the track at the same time, doing the same number of laps, and the player whose vehicle crosses the finish line first is the winner.

component
:   Components have editable properties that can be physical, like a static mesh and particle system, or logical, like a gameplay tag or custom Verse code that defines the movement of a platform. By default, all entities have a transform component to specify where the entity exists in the world.

    In Verse, a function or group of related functions in a program that can be reused.

container
:   In UEFN, a container is a [class](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#class) that contains properties that can be applied to multiple objects.

    In Verse,  a container is a way of organizing data in code. See [container type](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#containertype) for more info.

Content Browser
:   The primary area of UEFN used for creating, importing, organizing, viewing, and modifying content assets within the editor. The Content Browser provides a way to manage content folders.

    You can also perform other useful operations on assets, such as renaming, moving, copying, and viewing references. The Content Browser can search for and interact with all assets in the game.

    In the Content Browser, you can search and sort assets by type, and you can filter your view of the assets either by choosing specific types of assets in the Filters dropdown list, or by typing text in the Search Assets box.

Content Drawer
:   The Content Drawer is a special instance of the Content Browser that automatically minimizes when it loses focus (that is, when you click away from it). To keep it open, click the Dock in Layout button in the top-right corner of the Content Drawer. This creates a new instance of the Content Browser, but you can still open a new Content Drawer.

Content Drawer button
:   This button opens the [Content Drawer](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#contentdrawer), from which you can access all of the assets in your project. This button is located in the bottom left corner of the screen.

Content Library
:   A plugin in UEFN with third-party assets that you can download for free.

content service
:   The feature that makes it possible to import content from UEFN into Creative.

contrast
:   In lighting, contrast describes how highlights transition into shadows. The brightest areas of the image are the highlights. The darkest areas are the shadows. In between, the image will have lights, midtones, and darks.

control bus
:   A [modulation source](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#modulationsource) that can be added to an audio source or effect. Assets sent to the same control bus can be modulated as a group by using a [control bus mix](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#controlbusmix). In UEFN, the control bus is a way to control certain parameters for one or more sounds.

control bus mix
:   A mix used to drive values utilized by [control buses](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#controlbus). In UEFN, can be used to control the volume of groups of sounds when added to an Audio Mixer device.

Control Rig
:   A suite of animation tools you can use to rig and animate characters directly in UEFN

cook
:   To convert data to a format that can be used on a specific platform. Cooked data is data that is basically ready to ship.

    A final build is run through a process where the data is organized, and combined into large chunks, compressed, and so on, so that it loads fast. Editor and debug data is not included when data is cooked.

cooked editor
:   The editor in [UEFN](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealeditorforfortnite) where you can create, import and edit props. This is called a "cooked" editor because it uses cooked data, or data that has been converted to run in real time.

cosmetic track
:   Cosmetic tracks in Rocket Racing island templates can be alternate tracks, like [secondary tracks](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#secondarytrack), or used just to achieve a particular cosmetic look. Players do not spawn on cosmetic tracks, and travel on a cosmetic track doesn't determine play position through a lap. There is no limit to how many cosmetic tracks you use. In Edit mode, these are identified by their color, white.

Creative Edit
:   Creative Edit the act of playtesting your project in Fortnite Creative without leaving UEFN. You can use all of your tools to edit your island. You do this by clicking Launch Session, then Play. This is the equivalent of [Create mode](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#createmode) in Fortnite Creative in that any edits made to the project are automatically saved.

Creative Play
:   To start the game in the [Fortnite client](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#client) so you can test the player version of an island. This is done by pressing START GAME in Creative. This is the equivalent of [Play mode](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#playmode) in Fortnite Creative in that no edits are saved.

CTR
:   Click-through rate (CTR) is the ratio of clicks over impressions, measured as a percentage for how many impressions resulted in a click. For example, if your island has 100 impressions and 5 clicks, that is a 5% CTR. CTR measures the effectiveness of your thumbnail and title at capturing player attention and getting players to click.

cubemap
:   A cubemap is a simple method of environment mapping, in which distant scenery, such as sckies and surrounding environments, is mapped to a panoramic texture.

cull
:   To increase performance by reducing the number of objects of any kind from the current view. The [bounds](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#boundingbox) of an object are used to test whether it is currently [rendered](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#render) within the frame. Objects that are removed include objects made of [polygons](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#polygon), along with their materials, lights, and shadows.

CVar
:   Console variables, or CVars, are [variables](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#variable) that can be set in an [.ini file](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#inifile).

dB
:   Short for decibel, a unit used to measure relative loudness of sound. Also see [0dB](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#0db).

DCC
:   Digital content creation, or DCC, refers to applications like 3ds Max, Maya, or Blender that you can use to create 3D content.

deadlock
:   A deadlock is when computer programs sharing the same resource prevent each other from accessing the resource, causing the programs to stop functioning.

deadzone
:   When you're using a camera device, this is the area where the [target](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#target) can move without affecting the camera. When the target moves to the edge of the deadzone, the camera will start following the target into the new area.

debugging
:   The process of identifying and resolving errors in your code.

decay
:   The time it takes from a sound reaching its maximum volume until it reaches its [sustain](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#sustain) volume.

delay
:   A time interval that controls how long a device will wait before producing a sound or other output.

deleted island
:   Deleted Islands are islands that have been deleted.

depot
:   Where files are stored when [revision control](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#revisioncontrol) is used.

depth of field
:   Depth of field, or DoF, describes how much of an image is in focus, and how much of the background is out of focus. When using the [Replay](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#replay) mode to capture images or videos from your island, the DoF is controlled by the [aperture](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#aperture) settings.

Details panel
:   The Details panel in the level editor contains information about the properties for various elements. This includes [transform](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#transform) edit boxes for moving, rotating, and scaling Actors, editable properties for the selected Actors, and quick access to additional editing functionality (depending on the types of Actors selected in the viewport).

developer
:   Someone who uses Fortnite tools to author (develop) an island in Fortnite, especially when using UEFN. This term includes Fortnite island developers, artists, and architects.

device
:   Devices are [objects](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#object) in Fortnite that perform specific tasks intended to control gameplay.

    A device, like a prop, is something you can place on your island. But devices are different from [props](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#prop) in that you use them to create player interactions. Different devices do different things, but they all do *something*.

    Think of a device as a package of game mechanics with specific features that can be customized to support your gameplay. Most devices can be customized, but all of them have default settings that determine how they behave even if you don't customize them.

    In Verse, a device is the basic building block used to construct game mechanics. A device drives player interactions that control gameplay.

device chain
:   What you get when you patch two or more devices together in Patchwork.

diatonic scale
:   In music, a diatonic scale uses seven notes, instead of the twelve notes used in a [chromatic scale](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#chromaticscale).

diffuse
:   Diffuse reflection scatters light when reflecting off an object. Compare to [specular](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#specular) and [normal](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#normal).

diffuse shadows
:   In UEFN, the premise is that a small but intense light source will provide sharp edges on a shadow, while a larger area light source will have smoother, softer edges.

direct event binding
:   See [binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#binding).

disabled island
:   Disabled islands are islands that cannot be played, opened, or playtested.

Discover Score
:   Attraction, engagement, and satisfaction metrics are combined to create a holistic Discover Score that influences **For You** and **Recommendations** in Discover. This score aggregates the following metrics over a 96-hour period: uniique players per impression, minutes per player, and fun survey scores.

distortion
:   An [audio effect](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#audioeffect) that can simulate the warm sound of a signal being [overdriven](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#overdrive) through an analog tube amp, or an unsettling digital processing and warping.

    Different styles of distortion shape the feel of your audio in different ways, evoking various moods and music genres. In Patchwork, the [Distortion Effect](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#patchworkdistortioneffect) device is one way you can customize your sound.

draw call
:   A draw call tells the graphics [API](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#api) what to draw and how to draw it. Each draw call contains all the information the graphics API needs to draw on the screen, such as information about textures, shaders, and buffers. Draw calls can be resource-intensive, but often the preparation for a draw call is more resource-intensive than the draw call itself. For more info, see [Reducing Draw Calls](https://dev.epicgames.com/documentation/fortnite/reducing-draw-calls-in-fortnite).

draw distance
:   In computer graphics, **draw distance** (sometimes called **render** or **view distance**) is the maximum distance of objects in a three-dimensional scene that the rendering engine will draw. [Polygons](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#polygon) that lie beyond the draw distance will not be drawn on the screen.

    Draw distance requires a limit because a processor that's expected to render objects to an infinite distance would slow the application to an unacceptable speed because of the computing power it uses.

drive
:   When an amp is pushed past the point of clean sound by increasing the [gain](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#gain).

dry
:   In audio, a dry signal or sound refers to a sound before any effects are applied. Compare to [wet](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#wet).

ducking
:   Audio ducking is the process of [compressing](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#compression) (ducking down) the volume of an [audio signal](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#audiosignalprocessing) when another signal goes above a certain threshold. This technique makes it possible to get more clarity from both audio signals.

    In Patchwork, as an example, the SFX ducking control on the [Speaker](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworkspeaker) device determines how much the volume will reduce when the speaker is playing.

echo
:   In [audio signal processing](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#audiosignalprocessing), an echo is a reflection of sound that arrives to the listener with a [delay](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#delay) after the source sound.

edge
:   A line, or two connected [vertices](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#vertices).

Edit mode
:   In UEFN, when you playtest an island, the views of each are distinguished by **Edit mode** (the view of the UEFN viewport where you make changes, or edits) and **Play mode** (where the island appears in the Creative client).

editor
:   An editor is an interface used by a developer to create program code that makes a program work. In [UEFN](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealeditorforfortnite), a tool is a dialog or panel used to perform a specific set of actions or to display information about one or more actors or assets, and an editor is a collection of tools used to edit one or more specific types of assets.

emissive material
:   A self-illuminated [material](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#material). Material emission is a material property that is written directly into the scene color buffer.

emitter
:   A key component in a visual effects system, an emitter defines the properties for what will be used to emit (simulate) certain kinds of visual phenomena, like smoke, rain, or explosions.

empty emitter
:   An [emitter](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#emitter) that has not yet had its properties defined.

engagement
:   For a Fortnite developer, engagement refers to the amount of time players spend on your game, and how often they return to play again.

    Engagement metrics focus on how often players return to an island and how long their play lasts. It is measured by daily and weekly retention, minutes played per player, number of unique players, and social play time spent in social parties.

    The more player engagement your island gets, the more successful you've been in your design and execution.

entity
:   An entity is the base object present in [Scene Graph](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#scenegraph). This is a lightweight class containing two key elements: components and child entities.

entity hierarchy
:   Grouping [entities](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#entity) under one [parent entity](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#parententity) creates a hierarchical structure with child entities under the parent entity, and causes the parent entity to control the [lifetime](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#lifetimemanagement) of all the entities nested beneath it.

Environment Lighting Rig device
:   A device in UEFN that that you can use for individual lighting rig sets to create custom lighting, volumetric clouds, time of day lighting, and so on.

event
:   Events are things that trigger functions. Functions are things that devices do when triggered. This is the basis of the mechanics you use to create gameplay.

    Compare to [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function).

    **In Verse**, an event is an action or occurrence that can be identified. For example, the Button device has the `InteractedWithEvent`, which occurs whenever a player interacts with the button. You can define behavior that results for a specific event by subscribing with an [event handler](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event-handler).

event handler
:   An event handler is what responds to a [bound](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#bind) event. For example, binding a function to a Button device's InteractedWithEvent will call the event handler every time the button is interacted with.

ExperienceSettings
:   See [Island Settings](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#islandsettings).

exposure compensation
:   A way to control how dark or light a scene is.

extrude
:   When you extrude a model, you are extending the top face in a direction.

F-axis
:   In a 3D space (real or virtual), the F-axis represents horizontal forward/backward (or north/south) movement. Also see axis.

face
:   A surface comprised of three or more connected edges. The side of a cube can contain a single face, or multiple faces. Each face can be [extruded](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#extrude).

falloff
:   A gradual reduction in something over space or time. This term could apply to lighting, terrain, or sound, for example.

FBX
:   FBX (Filmbox) is a proprietary file format (.fbx) developed by Kaydara and owned by Autodesk since 2006. It is used to provide interoperability between digital content creation applications. FBX is also part of Autodesk Gameware, a series of video game middleware.

field of view
:   Field of view, or FOV for short, is how much of the world a player can see at any given moment.

    With a camera device, **field of view** refers to what the camera (and by extension, the player) can actually see. The field of view is represented as an angle, and is measured in degrees. Angles are two lines that join at a point called the **vertex**. With cameras, the vertex is the lens (virtual in this case) of the camera. The arms of the angle spread up and down (the vertical axis) from that vertex. The higher the number of degrees, the wider the angle, and the more the camera can see.

fill light
:   A secondary source of light in a scene that doesn't change the character of the [key light](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#keylight). Fill lights are used primarily to lighten shadows.

filter
:   In audio signal processing, a filter determines which sound frequencies are heard. Different filters process audio in different ways. For example, a low-pass filter allows lower frequencies to be heard while reducing or eliminating higher frequencies.

first person mode
:   In first person mode, the player's perspective is as though they were looking through their avatar's eyes. With this camera mode, the player usually can't see their avatar's body, but can see their hands or weapons.

first-person shooter
:   A type of shooter game where the player plays from a first-person perspective in a three-dimensional space. in an FPS, the player can move within the space.

FK rigging
:   FK (Forward Kinematics) is how the positions for different parts of a model at specified times are calculated for both position and orientation. FK refers to the effect on the child nodes as the parent moves or rotates. Compare to [IK rigging](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#ikrigging).

float value
:   A float value is a value based on a floating point number. This is a positive or negative whole number with a decimal point. For example, 5.1, 0.25, and -122.333 are all floating point numbers, but 76 and 0 are not. These are called floating point numbers because the decimal point can "float" to any position necessary.

Foley
:   Sound effects created in post for film, video, or gaming. It's capitalized out of respect for Jack Foley, the man who invented many of the techniques still used.

Fortnite DS
:   A Fortnite-dedicated server is a technical component for UEFN. Downloading projects directly from Creative is possible when a dedicated server is live with the project.

FOV
:   See [field of view](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#fieldofview).

frame rate
:   Frame rate, or fps (frames per second) for short, is the number of frames that appear in any kind of streaming content per second. While streaming videos and broadcast TV usually use a frame rate of 24 fps, streaming games usually use a higher rate of 30 or 60 fps. You can adjust the frame rate in Creative by pressing the Tab key, then under Menu, clicking Settings > Video > Frame Rate Limit, and selecting a different frame rate.

gain
:   While gain and volume are closely related, there are differences. Volume is how loud something is, while gain is how much an audio signal is increased by an amplifier. Adjusting the volume does not affect the [waveform](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#waveform). However, increasing the gain does, and this can cause [distortion](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#distortion).

Game Data folder
:   Game data includes any game or user info that's generated through use. The Game Data folder is where this info is stored.

gameboard
:   The surface on which a game is played. Traditionally, the term gameboard has applied to tabletop games. However, it is becoming more common to use it to describe video game levels. In video game development, gameboard levels can be split into different areas or zones, with different shapes, arrangements or terrains. As with tabletop gameboards, players can move characters or objects around the board (level) to progress through the game.

gameplay tag
:   Gameplay tags are conceptual, hierarchical labels with user-defined names. These tags can have any number of hierarchical levels, separated by the "." character; for example, a gameplay tag with three levels would take the form of "Family.Genus.Species", with "Family" being the broadest identifier in the hierarchy, and "Species" being the most specific.

    For more info, see [Gameplay Tags](https://dev.epicgames.com/documentation/en-us/uefn/gameplay-tags-in-verse).

gamut
:   Color gamut is a way of describing a range of colors that can be used within a [color space](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#colorspace). Available gamuts are determined in part by the number of colors a monitor can display. A **wide gamut** is a larger color space.

geometry
:   See [level geometry](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#levelgeometry).

glide
:   Glide determines how long it takes to blend to a new pitch when a note is played.

global illumination
:   Provides more realistic lighting in your scene by using algorithms that account for both light originating from a light source and reflections off of nearby objects.

glTF
:   This file format name comes from Graphics Language Transmission Format. It is a standard file format for 3D scenes and models. A glTF file uses one of two possible file extensions: .gltf (JSON/ASCII) or .glb (binary). Both .gltf and .glb files can reference external binary and texture resources. Alternatively, both formats may be self-contained by directly embedding binary data buffers (as base64-encoded strings in .gltf files or as raw byte arrays in .glb files). This is an open standard developed and maintained by the Khronos Group, and it supports 3D model geometry, appearance, scene graph hierarchy, and animation.

golden path
:   A golden path is a procedure that doesn't go off in unexpected directions. Think of it as the straightest line from point A to point B.

    Another definition for golden path is playing or testing a game using [cooked](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#cook) data with a [dedicated server](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#fortniteds) and [client](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#client) running separately, not via play-in-editor (PIE). This is the closest you can get to testing exactly what will happen in-game.

grayboxing
:   Grayboxing (also known as blockout) is the process of making a playable rough draft of a level to get a sense of its gameplay before polishing its look. It's common for level designers to graybox a game environment to test its layout for gameplay purposes.

greybox
:   See [grayboxing](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#grayboxing).

grid
:   A level is marked with lines in a grid pattern. You can use these grid lines to position [props](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#prop) and [devices](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#device), and to measure distances. Each grid area is called a tile. Grids are measured in [UUs](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealunits), and one tile equals 512 UU.

grid plane
:   A grid plane is an area that cannot be edited, but that you can place objects on. If you're going to create custom terrains, you need to remove the grid plane(s) in your project before you can do this. To select a grid plane, make sure you're in Selections Mode, then click on the grid. It will now have a yellow border. To remove the selected grid plane, press the **Delete** key. Also see [Landscape Streaming Proxy](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#landscapestreamingproxy).

grid snap
:   UEFN inherits its grid-snapping values, known as [**Unreal Units (UU)**](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealunits), from Unreal Engine (UE) for all [actors](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#actor). Inside UE, 1 UU is equal to 1 centimeter (CM). This means smaller snap values cause the actor to snap in smaller increments, or alternatively, larger snap values cause actors to snap in larger increments. This is the opposite of how grid snapping works in Fortnite, where the smaller the grid-snapping value, the larger the incremental snap.

    However, Building Actors do use the Fortnite grid snapping values. You can enable and disable Fortnite grid-snapping properties in **World Settings** by toggling **Editor Cell Snap** on and off for Building Actors. Changing your grid snapping levels does not affect non-Building Actors.

harmony
:   A combination of notes played at the same time that make up a [chord](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#chordprogression). Compare to [melody](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#melody).

heightmap
:   A raster image (two dimensional) used for elevation modeling. Each pixel stores values, such as surface elevation data, for display in 3D computer graphics. Heightmaps are widely used in terrain rendering software and modern video games, and are ideal for storing digital terrain elevations; compared to a regular polygonal mesh, they require substantially less memory for a given level of detail.

hierarchical
:   Having clear levels or hierarchies of rank, importance, or control. Common hierarchical relationships are parent/child or superclass/subclass.

Hierarchical Level of Detail
:   Hierarchical Level of Detail (HLOD) decreases the amount of detail on assets as the player camera moves further away from them. This contributes to managing memory more effectively. Also see [LOD](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#lod).

HLOD
:   Hierarchical Level of Detail (HLOD) decreases the amount of detail on assets as the player camera moves further away from them. This contributes to managing memory more effectively. Also see [LOD](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#lod).

horizontal composition
:   In [adaptive music](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#adaptivemusic), horizontal composition, or resequencing, is where segments of music can be resequenced based on player actions or other triggers. Unlike [vertical composition](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#verticalcomposition), where a basic music track plays continuously while other elements are added to or removed from it, the musical segments used in horizontal composition are separate from each other.

hotfix
:   A small piece of code that can be replaced directly in a live game or playtest. These are usually things like [CVars](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#cvar).

HUD message
:   A customized message that displays on the [HUD](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#hud) at a specific point in the game.

IK rigging
:   Kinematics is the study of motion. Inverse Kinematics, or IK, is the process in 3D animation that uses joint articulation to create both poses and movement. Rigging is how these poses and movements are mapped to a skeletal mesh.

impression
:   An impression is a player view of your island thumbnail. To be counted as an impression, your island's thumbnail must be 100% visible on the screen and viewable for two seconds or more. If a player clicks your thumbnail, even if it's not fully visible or does not appear for the full two seconds, the impression will still count as an impression based on the click-through result.

impressions-to-clicks-to-plays
:   The impressions-to-clicks-to-plays flow for an island involves generating awareness (impressions), capturing interest (clicks), and driving action (plays).

in-game resolution
:   Resolution is the number of pixels per inch that display on a monitor. While different consoles have different resolution settings, a video game runs at its own in-game resolution regardless of console settings. What this means is that the in-game resolution directly affects performance. Higher in-game resolution causes the GPU to work harder to render more pixels, resulting in lower frame rates. Console resolution does not affect gaming performance.

INI file
:   A file that contains configuration information for computer software. INI is short for initialization, which is the assignment of an initial value when a program launches.

instance
:   Think of an instance as a unique copy of an [asset](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#asset). The original asset determines the default properties of any new instance you create. Changes you make to the properties for an instance don't affect the original asset. For example, you can change a [material](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#material) to have a different appearance without changing the master material. This would be a material instance.

    In Verse, an instance is to create a [variable](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#variable), specify its [identifier](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#identifier) and [type](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#type), which is called [declaring a variable](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#declare), and assign a value to the variable, which is called **initializing**.

instantiate
:   To create an instance of something.

    In Verse, instantiate is to to create an [instance](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#instance) or value of a data structure or type such as a class or structure. Also see [archetype instantiation](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#archetypeinstantiation).

interval
:   The difference in pitch between two notes. From C to D would be a step interval, or one step up in the scale. From C to E would be a skip interval, skipping a step from one note to the next.

island
:   In Unreal Editor for Fortnite, you are building islands. In UEFN, these islands are sometimes called [levels](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#level).

island template
:   In Unreal Editor for Fortnite, an island template is basically an empty island with terrain or other environmental features, much like the starter islands available in Fortnite. These templates are available on the **Project Browser** screen in UEFN.

jump
:   In Rocket Racing, the jump button causes the vehicle to jump off the ground.

K-DOP
:   K-DOP is a type of bounding [volume](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#volume) where **K** is the number of axis-aligned planes, and **DOP** stands for **discrete oriented polytope**. It takes K axis-aligned planes and pushes them as close to the mesh as possible.

    This should not be confused with K-pop, an internationally known, high-energy musical genre.

Kelvin scale
:   The Kelvin (K) scale is used in lighting to measure the color temperature of light. Lower K numbers mean yellower (warmer) light. Higher numbers mean whiter or bluer (cooler) light.

key
:   The first note in an [octave](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#octave). For example, the key of C starts with the C note, while the key of G starts with the G note.

key light
:   The **key light** is the primary light source. It's called this because it's usually the main light source, and the point around which other lighting can be designed. This can apply to both interior and exterior lighting.

keyframe
:   In animation, a key or keyframe is a record of a given value or values at a point on an audio or video timeline. Keyframes are used to mark the beginning or end of a transition.

keyword matching search
:   keyword matching search

    Search is an important way for players to find specific islands and genres within Fortnite, and Discover uses a hybrid approach that combines two algorithms: **keyword matching** and **semantic search**. Keyword matching returns islands that contain text that exactly matches the user’s query. Semantic search returns islands that are semantically similar to a user’s query.

L-axis
:   In a 3D space (real or virtual), the L-axis represents horizontal left/right (or east/west) movement. Also see [axis](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#axis).

landscape mode
:   A set of tools in UEFN used specifically for editing terrain. You can use this toolset to add mountains and hills, bodies of water, caves and tunnels, and foliage.

Landscape Streaming Proxy
:   When you delete a [grid plane](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#gridplane), you're left with a proxy (substitute) for the grid plane. The primary difference between a grid plane and a proxy is that you can use the [Landscape Mode](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#landscapemode) tools on a proxy to build custom terrains.

large language model
:   See [LLM](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#llm).

LEGO Elements
:   These are any of the LEGO Fortnite assets that look like they're built with real-life bricks from your LEGO sets, and that are for use exclusively on LEGO Islands. This includes prefabs, devices, tools, and so on. All LEGO assets, from [Minifigures](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#minifigure) to prefabricated buildings (prefabs), are scaled at half the size of Fortnite assets to match the Minifigure scale. Unlike Fortnite assets, LEGO assets cannot be scaled or resized in any way. Tiny but mighty!

LEGO Island
:   A LEGO Island uses LEGO assets and [Minifigures](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#minifigure). Templates for these islands can be found when you interact with the console on the Creative hub, click Create New, and select the LEGO tab, or in the Project Browser when launching UEFN. Dream big, build small!

LEGO llama
:   A llama that works just like a Fortnite loot llama, but is scaled down and outfitted to match the LEGO environment. LEGO llamas can also be used as piñatas. *¡Dale, Dale, Dale!*

LEGO Styles
:   The LEGO [Minifigures](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#minifigure)version of a Fortnite outfit.

lerp
:   Short for linear interpolation. Interpolation is the creation of new values that lie between known values. Linear interpolation is the most simple form of interpolation, based on the assumption of a straight line between two points.

level
:   In UEFN, a level is a user-defined area of gameplay. Levels are created, viewed, and modified by placing, transforming, and editing the properties of the [actors](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#actor) it contains. Multiple levels can be saved within a single [project](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#project). You can also think of a level as a container that can have a dedicated landscape, and can hold actors (devices, props, custom assets, and so on).

    The term **level** is synonymous with **island**.

level design
:   Level design is another way of saying game design.

Level Editor
:   When you launch a project, it opens in the Level Editor. Different content editors become available based on the mode you choose to work in.

level geometry
:   When a designer talks about geometry, they are talking about what the computer uses to define objects in three dimensions. Level geometry includes not only location and size of objects, but also colors and textures. Also see [polygon](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#polygon).

level instance
:   If an [instance](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#instance) is a unique copy of an asset, then a level instance would be a unique copy of a [level](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#level) (a collection of assets) that can be modified without changing the original level. New level instances can be generated from selected [Actors](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#actor) in the [viewport](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#viewport). Also see [packed level instance](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#packedlevelinstance) and [level instance device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-level-instance-devices-in-fortnite-creative).

Level Save Record
:   The save file for the Creative island file, which specifies all the data necessary to recreate a customized island. This is a collection of template records that hold actor class and specific property settings, and instance records that hold a reference to a template record, including the location and rotation for where an actor was placed. A LSR will have some template records and many instance records.

lifetime management
:   Nested [entities](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#entity) exist as long as the [parent entity](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#parententity) exists. If the parent entity is destroyed, then so are all the child entities below it.

Link Code
:   See [Project Link Code](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#projectlinkcode).

live build
:   The version of Fortnite Creative or UEFN that is in release and available without requiring any special permissions.

Live Edit
:   A feature in UEFN that provides a live connection between UEFN and an island in Edit mode. Changes you make in the editor automatically update in Creative.

LLM
:   A large language model, or LLM, is a computer program trained to process and output natural language through text. You can view the model as learned knowledge from a library of resources (database) on the topic of language. Some training material sets are small while others are large. Through the training, the model can predict a string of text it should produce in response to a prompt, making it appear as though it were aware and thinking.

    The language model can generate human language through text using [algorithms](https://dev.epicgames.com/documentation/en-us/fortnite/verse-glossary#:~:text=you%20need%20here!-,algorithm,-An%20algorithm%20is) to learn pattern recognition and relationships between words from the training material. This system of training is called [machine learning](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#machine-learning). Typically, a user can interact with the LLM through some interface.

local exposure
:   Local exposure is an effect in post processing that automatically applies adjustments to exposure within user-controlled parameters to preserve both highlight and shadow detail on top of existing global exposure. This is useful for projects with challenging high dynamic range scenes using dynamic lighting, in which applying a single global exposure adjustment is not enough to avoid blown out highlights and completely dark shadows.

local position
:   The position of a pixel or vertex relative to an object.

local space
:   This is the space that is relative to an object with no rotation or transformation.

LOD
:   Short for **level of detail**. This refers to the level of detail that shows in a Static Mesh based on distance away from it. If a player is close to a complex mesh, you would want more detail viewable, but this can slow performance. If a player is further away, the LOD can be reduced to improve performance.

LOD bias
:   A setting in UEFN that affects [level of detail (LOD)](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#lod) with a bias toward less detail but improved performance.

look-at location
:   Where the camera is looking at any time. It might be something other than the player.

LSR
:   See [Level Save Record](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#levelsaverecord).

LTM
:   Short for limited time mode, meaning there is a time limit to how long the game lasts.

Lumen
:   A dynamic global illumination and reflections system designed for next-generation consoles.

machine learning
:   Machine learning (ML) is a part of artificial intelligence (AI) that helps a system improve performance over time without requiring every task to be programmed. ML models use algorithms to identify patterns in datasets, make predictions, and adjust their approach to improve methods based on that learning.

map template
:   See [island template](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#islandtemplate).

material
:   A material is an asset that can be applied to a mesh to control the visual look of the scene. At a high level, it is easiest to think of a material as the “paint” that’s applied to an object. But even that can be misleading, since a material literally defines the type of surface from which your object appears to be made. You can define its color, shininess, transparency, and much more. In more technical terms, when light from the scene hits the surface, a material is used to calculate how that light interacts with that surface. These calculations use incoming data that is input to the material from a variety of images (textures) and math expressions, as well as from various property settings inherent to the material itself.

    Unreal Engine utilizes a physically based shading model. This means that rather than defining a material using arbitrary properties (such as diffuse color and specular power), you instead use properties more easily relatable to the real world. These include base color, metallic, specular, and roughness.

material function
:   A way of grouping a node graph so that it can be used as a single node. Material functions are little snippets of material graphs that can be saved in packages and reused across multiple materials.

    Applying complex math to define how a texture appears on a [material](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#material).

material graph
:   A material graph is used for the configuration of material nodes used to make a [material](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#material).

melody
:   A sequence of single notes grouped together. The melody is the main concept in a musical composition, and usually the most memorable aspect of a song. It's the tune that plays or repeats that you can use to identify that song. Compare to [harmony](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#harmony).

mesh
:   A set of locations, or [vertices](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#vertices) that are connected at their edges. There are different types of mesh. Static Mesh, used to map the surface of an unanimated 3D object, and Skeletal Mesh, used to map the surface of an animated object, are most common.

mesh surface integrity
:   An asset should be watertight, with no holes in the [mesh](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#mesh) that show a [backface](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#backface). This increases the prop's usefulness, as variation can be introduced by rotating and scaling a single prop, or placing the prop different ways. However, if the asset is meant to be stationary, or there are other reasons to allow holes, this is acceptable.

metadata
:   Data that provides information about other data. Special sets of metadata, or tags, are used in digital searches to find specific objects or text. Search engines use metadata to match a user's search with what they're looking for.

MetaHuman
:   A complete framework that gives to the power to create and use fully rigged, photorealistic humans. Also see [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#animationblueprint).

metaverse
:   The metaverse is an online social entertainment experience in real time, where people play and connect in a 3D world.

Minifigure
:   Brick-built characters on LEGO Islands. These represent players and non-player characters (NPC). Minifigures are half the size of the usual Fortnite character, so everything on a LEGO Island is scaled down to half size to match. Half the size but twice the cute!

Minifigure-compatible
:   This can apply to props, items, tools, devices, and any other assets. It means that the asset has been scaled down to match the [Minifigures](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#minifigure) used on a LEGO Island.

minutes per player
:   **Minutes per player** is similar to the attraction metric of [Minutes played per impression](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#minutes-played-per-impression), but instead shows a more refined view of an island's actual engagement on a per player basis

mode
:   UEFN has a number of editing modes for specific types of assets. For example, Landscape Mode is used specifically for quickly editing terrain.

moderation
:   When you submit your island for publishing, the island goes through a review process, after which it either gets approved and published, or rejected. This process is called moderation.

modularity
:   If an asset imported into UEFN includes elements that could be used separately, it should be modular. For example, an asset could be a market stall with baskets and fruit. It could be one complete unit, or you could make the baskets and fruit as separate meshes that could be used on their own.

    This term also refers to architectural assets that can be used together to create a building and rooms within the building.

modulation
:   To **modulate** means to change or control. In audio, modulation usually refers to sound elements like volume and pitch, which can be adjusted with a modulator.

modulation parameter
:   A modulation parameter provides the context for how a value associated with a [control bus](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#controlbus) is displayed, mixed, and transformed. In UEFN, only the volume modulation parameter is supported on [control buses](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#controlbus).

modulation source
:   Any source that modulates a [parameter](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#modulationparameter). In UEFN, this is limited to control buses.

News menu
:   A menu screen that appears when you first launch UEFN. This screen contains links to info on what's new for the UEFN community, and other relevant UEFN info.

Niagara
:   Niagara is the visual effects system in [Unreal Engine](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealengine) used for creating and previewing particle effects in real time. Niagara is also included in UEFN.

node
:   In **UEFN**, a node is a fundamental unit within a graph-based system that represents a specific function, operation, or data point. In the context of node graphs, a node is an individual component that processes or routes audio signals, such as a sound source, effect (like reverb or delay), mixer, or output.

    For **Verse**, see [linked list node](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#linkedlistnode).

node graph
:   A visual representation of an interconnected system of audio processing [nodes](https://dev.epicgames.com/documentation/fortnite/node) used to generate, modify, and route sound in a game engine.

    Each **node** in the graph represents a functional component, such as an audio source, filter, effect, mixer, or output. These nodes are connected by links that define the flow of audio signals. In **UEFN**, an audio node graph enables dynamic and procedural sound design by allowing developers to build complex audio behaviors, such as spatialization, reverb, and real-time audio effects.

normal
:   A normal vector is a type of texture which is used to add significant physical detail to a surface without adding additional polygons to a mesh. This is achieved by modifying the "normal" or facing direction of each pixel.

    Compare to [specular](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#specular) and [diffuse](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#diffuse).

number of unique players

OBJ
:   A file format developed by Wavefront Technologies and now available as an open format used by many 3D graphics application vendors. The format supports [geometry](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#levelgeometry) elements like points, lines, and texture [vertices](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#vertices), but does not support animation or lighting information.

object
:   In UEFN, an object is another word for [asset](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#asset).

    In Verse, an [instance](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#instance) of a [class](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#class) is an object. An instance has the same behaviors defined by its class [type](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#type) but with real [values](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#value).

    The terms **instance** and **object** are synonymous.

octave
:   A range of musical notes in the interval between (and including) two notes, where the first note has twice the frequency of vibration of the other. It's called an octave because it includes eight notes, represented by C, D, E, F, G, A, B, C. An octave can start at any note. Also see [pitch](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#pitch).

octave offset
:   The shift of a scale to a different [key](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#key).

offline progression
:   With offline progression, some aspect of a game will continue to progress while closed as though the player were still in the game. For example, in a farming game that uses this mechanic, crops would continue to grow while the player is logged out of the game. There is usually a time limit for how long offline progression continues. Also see [persistence](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#persistence).

orthographic
:   A 2D representation of a 3D object or space. In an orthographic view, all objects appear at the same scale, unlike a perspective view, where distant objects are scaled smaller.

Outliner panel
:   The Outliner panel, or Outliner for short, displays all [actors](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#actor) within a scene in a hierarchical tree view. In the panel, you also have an option to search for an actor element in the level, and to create folders to group actor elements together.

overdrive
:   A type of [distortion](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#distortion) usually caused by pushing an amp past what it can produce as a clean tone.

oversteer
:   When a vehicle steers into sharper turn than expected, which can have the effect of shoving the rear of the vehicle to the outside of the curve. This effect, where the back wheels slide while the driver maintains control of the front wheels is called drifting.

owner
:   The user that owns or controls a team or project in the [Creator Portal](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#creatorportal).

packed level instance
:   This is a [level instance](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#levelinstance) where a compact collection of [Actors](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#actor) are grouped together into a single Actor. You can move, copy, and paste it as a single asset, but you can also open it and edit the parts inside individually. This is roughly the equivalent of a [prefab](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#prefab) in Fortnite.

panel
:   In Unreal Editor for Fortnite, a panel is one or more areas on the screen that contain information about your level. A panel can be moved, docked, or dragged into a separate window. Examples include the Details panel and the Content Browser.

parent entity
:   An [entity](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#entity) that has at least one other entity nested under it (its child entity) in the [entity hierarchy](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#entityhierarchy).

particle system
:   Particle systems use lots of tiny sprites to generate special effects that don't have well-defined shapes — dust, smoke, moving water, explosions, and so on.

Pawn
:   A Pawn is a subclass of Actor, and serves as an in-game avatar or persona such as a character in a game. Pawns can be controlled by a player or by the game's AI in the form of non-player characters (NPCs).

    When a Pawn is controlled by a human or AI player, it is considered possessed. When a Pawn is not controlled by a human or AI player, it is considered unpossessed.

persistence
:   When player data is saved from a session and reloaded into the next session for that game, this is called persistence.

perspective
:   In a perspective view, objects that are far away are smaller than those nearby while in [orthographic](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#orthographic) view, all objects appear in the same scale.

photobashing
:   Photobashing is a technique where artists merge & blend photographs or 3D assets together while painting and compositing them into one finished piece.

ping pong
:   To reverse direction back and forth.

PingPong animation mode
:   To reverse the direction of an animation when the final keyframe is reached, and to play again in the opposite direction.

pitch

pitch-yaw-roll
:   Pitch, yaw and roll are terms originating in aviation. They refer to the three different types of rotation a plane can perform when moving. These terms were adopted into 3D design and game development to more precisely define a virtual 3D environment and how things are moved in that virtual space. **Pitch** is the up-and-down movement of an object relative to its original position. **Yaw** is the horizontal left or right movement relative to its original position. **Roll** is a tilt to the left or right relative to its original position.

    These terms are also used with camera devices to describe movements of the camera.

    Also see [axis](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#axis).

pivot point
:   The point that controls how an object rotates and scales. Any transformation of size or orientation for an object is relative to the object's pivot point.

pixel
:   A unit of graphic information based on two dimensions. From picture element, or **pix** and **el**. Compare to [voxel](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#voxel).

platform
:   A platform is a system that runs software on different kinds of hardware. Fortnite runs on different platforms. These platforms fall into one of three categories: desktops or laptops that use Microsoft Windows or macOS, traditional mobile devices (like phones or tablets), and handheld devices or consoles.

Play button
:   The **Play** button on the Level Editor toolbar opens a Fortnite [client](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#client) where you can playtest your island.

play-in-editor
:   Play-in-editor, or PIE, is running a game from the editor. PIE does not use [cooked](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#cook) data.

playhead
:   When editing audio or video, the playhead is a vertical line in the timeline that represents the position, or frame, of the track.

playtest
:   To test how the island you've built plays before inviting others to join you there

    To test a new game or version of software for bugs and design flaws by getting users to play it before it is released.

playtest build
:   A prerelease build that can only be accessed with special permission. Compare to [live build](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#livebuild).

playtest code
:   A private code for use by the individuals in a [playtest group](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#playtestgroup).

playtest group
:   A set of users defined in the Creator Portal that can recieve a private playtest code

plugin
:   Plugins provide tools to add entirely new features, and to modify built-in functionality without modifying the engine code directly. A plugin might add new menu items and toolbar commands to the editor, or even add entirely new features.

point light
:   A point light sends light in all directions equally from a single point.

polygon
:   Triangles are used in 3D graphics to build three-dimensional things. While **polygon** actually means **many angles**, the most common polygon in gaming graphics is a triangle, because it is the simplest shape that still fits the definition of a plane with multiple sides and angles, and with no lines crossing other lines.

populate
:   To add content to something.

post process volume
:   Post-processing refers to customizable filters that you can use to improve visual effects. Post-processing filters primarily affect lighting.

post processing
:   Post-processing effects are customizable filters that allow you to quickly enrich the visuals of your island or level. Using the post-processing effect objects in lighting or a camera, you can simulate a camera viewing a bright light and exaggerate its glow ([bloom](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#bloom)).

power of two
:   Powers of two are based on a binary numeral system, which is what computer machine language uses. This basically means successive doublings, such as 1, 2, 4, 8, 16, 32, 64, and so on. One practical application of this concept is when working with textures in UEFN. Graphics hardware across platforms works best with textures that conform to the power of two in their original dimensions. This results in graphics that perform better and are easier to [render](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#render)

primary track
:   In Rocket Racing island templates, this is the main track for a race. It is also the track on which players spawn. In Edit mode, these are identified by their color, green.

primitives
:   For a LEGO Island, primitives refers to a collection of basic geometrical shapes that look like real-life LEGO bricks. These props can be used with other elements to build just about anything you can imagine. Start simple, then build an empire!

priority system
:   When using camera devices, if multiple cameras are assigned to a player, the camera's priority determines which camera is active at any point in time. Priorities can be set in the device options. If two cameras are tied for the highest priority, the most recently added camera will become active, or take priority.

project
:   A project contains a collection of [assets](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#asset) and the data needed for [sharing](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#share) and testing those assets. Users can edit a project and its assets in UEFN and in Creative [Create mode](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#createmode) where applicable.

    A project can have multiple assets. It can also have multiple levels (or no levels), and meshes, textures, sounds, and other characteristics, depending on the needs and intent of the project the user is building.

    You could also say that a project is a single source of truth for a game or [content library](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#contentlibrary).

project content
:   Island content developed in or imported to UEFN.

Project ID
:   See [Project Link Code](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#projectlinkcode).

Project Link Code
:   UEFN creates a Project Link Code when you share a project for playtesting. You may need this code to access the project into Creative if it doesn't automatically show up in your Downloads tab.

project template
:   Any template in UEFN that can be used to start a project.

    A project template contains devices that can demonstrate various types of game mechanics available in UEFN. These templates are available on the Project Browser screen in UEFN.

prop
:   A prop is a [mesh](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#mesh) [Actor](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#actor) with parameters that are not exposed, or shown, to the user in Creative. Because of this, you cannot change the behavior of a prop, but only its size (scale), location (coordinates), or rotation (axis). Props are placed in the environment to make it more interesting visually.

Props folder
:   A folder in UEFN where props are stored, and from where they can be accessed.

publish
:   Any project, asset, object, or prop that's available to the broad public is **published**. The word **public** means exposed to general view, and **publish**, which comes from the same root, means to make public. In UEFN, it's possible to [share](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#share) a project, or some aspect of the project, with specific [developers](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#developer) or players for testing purposes without fully publishing the project.

quantize
:   In music, quantization is like snapping notes to the beat. If a note is played a little early or late, quantization moves it to the nearest beat or rhythm spot, making the timing more exact. It helps the music sound more on time and organized.Quantization in music is like snapping notes to the beat. If a note is played a little early or late, quantization moves it to the nearest beat or rhythm spot, making the timing more exact. It helps the music sound more on time and organized.

ragdoll physics
:   A type of limp and lifeless animation applied to a character after a fall from a great height or after being knocked out by another character or object.

raise
:   When a [function](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#function) emits a signal, it raises an event. Interested parties are notified that an event occurred, such as interacting with a button, and all the [event handlers](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#eventhandler) are called.

rarity
:   In UEFN, the way to tell a weapon's rarity is by the naming convention with _C, _UC, _R, _VR, _SR for Common, Uncommon, Rare, Very Rare, and Super Rare.

rectangle light
:   A rectangular light (RectLight) provides a way to light a large area evenly and generate [diffuse shadows](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#diffuseshadows) based on the area it covers. RectLights are great for imitating fluorescent ceiling lights and for studio lighting setups.

refraction
:   The bending of a wave when it moves at an angle from one medium into another in which its speed is different. For example, when light passes from air into water, it refracts.

release
:   If [attack](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#attack) is the time it takes from the start of a sound for it to reach maximum volume, then release is the time it takes for the sound to no longer be heard after it stops being generated.

render
:   Rendering is the process of using a computer program to make a 2D or 3D image. The result of rendering is called a **render**. A rendered image contains a number of different elements, including texture, lighting, shading, and one or more points from which it can be viewed. The complexity of the render determines how much of your computer's resources will be used.

reverse camera
:   In Rocket Racing, this vehicle action reverses the camera view so you can see what your competitors are doing behind you.

revert
:   With [revision control](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#revisioncontrol) to revert means to discard recent changes on assets that have been checked out but not submitted.

revision
:   In UEFN, this refs to a specific version of a file. Also see [revision control](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#revisioncontrol).

revision control
:   Revision control (also known as source code control or version control), is a way to track and manage changes to software code. This is useful when you have teams of programmers working on the same project. If someone makes a mistake, version control makes it possible to compare earlier versions of the code to find and correct the problem without interrupting everyone else’s work.

RGB
:   The colors in light that make up other colors. RGB stands for red, green, and blue.

rigging
:   A technique used in skeletal animation for a 3D character model using a series of interconnected digital bones. Rigging is the process of creating the bone structure of a 3D model, which can then be used to animate the character the way you would a puppet.

rocket drift
:   In Rocket Racing, a rocket drift happens when you turn very sharply and accelerate, causing the back tires to slide. Also see [oversteer](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#oversteer).

runtime error
:   An error that occurs while a program is running. Runtime errors are informally called [bugs](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#bug).

runtime session
:   When you click the **Launch Session** button in UEFN, this launches the server that runs Fortnite Creative on top of UEFN.

sample library
:   A sample library is a collection of sounds stored in a file.

sample rate
:   Sampling is when you turn an audio source into a digital file. This is done by taking **samples** of the audio source. How often these samples are taken determines the **sample rate**.

    Sample rates are measured per second, using kilohertz (kHz) per second. CDs are usually recorded at 44.1kHz — with 44,100 samples taken every second.

satisfaction
:   The satisfaction metric is based on player experience with your island, and includes factors like how much fun players had, how they rate your game, and if they **favorite** or **recommend** the island.

saturation
:   The level of color intensity. High saturation provides bright colors, while low saturation appears more muted.

    In lighting, saturation describes the amount of brightness a color appears to have on an island. In Contrast, lightness tells how dark or light a specific color is. Color saturation can mute colors which yields a grayscale or black-and-white appearance, or it can over-saturate a specific color or range of colors making them more vivid.

scale
:   The size of something compared to something else. For example, if you have a box that is one unit in every direction, if you scale it up to twice the size, it will be two units in every direction.

    In music, a scale is a graduated sequence of notes that divides an [octave](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#octave).

scale degree
:   The scale degree represents the relative relationships between notes in an octave. These are called the first, second, and so on, through seventh, and are represented by Roman numerals: I, II, III, IV, V, VI, and VII. A basic chord is made up of I, III, and V, regardless of the [key](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#key) used. For example, a chord in the key of C would use C, D, and F, while a chord in the key of F would use F, A, and C.

scalloping
:   Scalloping is a pattern of convex curves that look like the edge of a scallop shell as it repeats. A scalloped effect can be created with a series of spot lights placed at intervals along a wall or similar surface. This effect can be an intentional or unintentional, but either way, it can add visual interest to a space. The more [diffuse](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#diffuse) the light source is, the softer the scallop will be.

Screen Size Value
:   The Screen Size Value determines how much space an [asset](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#asset) should occupy on the screen before the asset drops to a lower [level of detail](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#lod). As you move away from an asset, its screen size value shrinks.

secondary track
:   A secondary track in Rocket Racing is an alternate path or route along the [primary track](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#primarytrack). There's no limit to how many secondary tracks you can use. In Edit mode, these are identified by their color, green.

section
:   The size of a single [Landscape Steaming Proxy](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#landscapestreamingproxy). A section is made up of [components](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#component). A camera can only render a limited number of components within a section at a time.

semantic search
:   See [keyword matching search](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#keyword-matching-search).

Sequencer
:   Sequencer is a multi-track editor in Unreal Engine and UEFN that you can use to create and preview [cinematic sequences](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#cinematicsequence) in real time.

series
:   A game built as a part of an ongoing series of islands.

server
:   UEFN is accessed through a dedicated server that connects Fortnite clients for editing and playtesting.

shading path switch
:   A type of material node you can use to select between different behaviors within a single material. This is commonly used to combine behaviors for low end and high end platforms within a material.

simulation entity
:   The simulation entity is the [entity](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#entity) that sits at the root of your project to represent the simulation.

Skeletal Mesh
:   A Skeletal Mesh Actor is a special type of actor that is used to display complex animation data that was created in a 3D content creation software. Skeletal Meshes are made up of two parts: A set of polygons composed to make up the surface of the Skeletal Mesh, and a hierarchical set of interconnected bones which can be used to animate the vertices of the polygons. Skeletal Meshes are often used in Unreal Engine to represent characters or other animating objects. The 3D models, rigging and animations are created in an external modeling and animation application (3DSMax, Maya, Softimage, etc), and are then imported into Unreal Engine 4 and saved into packages by using the Unreal Editor Content Browser.

Sketchfab
:   The leading platform for web-based 3D and augmented reality (AR). You can use Sketchfab to create and manage 3D assets.

snapshot
:   A **snapshot** captures all of the information for your project in the instant that you submit changes for revision control.

socket
:   A socket is a point where something connects with something else. Sockets can be used on a Static Mesh or a Skeletal Mesh to attach lights, particle effects or even other meshes.

soft deadzone
:   The area inside of the [deadzone](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#deadzone) where the camera starts to accelerate to follow the player. This area blends the [look-at location](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#look-atlocation) between remaining stationary and following the target.

soft source radius
:   You can use this effect to blur a shadow edge that is too sharp. See [source radius](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#sourceradius) for more info.

sophistication score
:   The sophistication score uses the same statistical approach as the [Discover Score](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#discover-score), but focuses on the content within an island and the development effort spent building and updating the island. It includes metrics that focus on the use of devices, animation, sequencers, Verse code, textures, and many other features. As new features are added to UEFN, they may be integrated into future calculations.

sound
:   See [audio file](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#audiofile).

sound cue
:   A sound cue is an audio object that encapsulates complex sound design tasks in a [sound graph](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#soundgraph).

    You can use a sound cue to modify an existing audio file by using audio nodes on the graph. Some of the things you can do with a sound cue include creating audio loops, fading sounds based on player distance from the source, and creating an audio sequence by using multiple sounds in a single cue.

    UEFN provides a number of sound cues, but you can also create your own.

sound graph
:   An sound graph is used to configure sounds using nodes.

sound source
:   What you hear in-game when the audio engine renders a sound.

sound wave
:   An audio file that can be imported into UEFN.

source length
:   Source length is the distance over which a light projects. The length runs down the X-axis for the light source.

source radius
:   This simulates the size of a small light source, such as LEDs, throwing off sharp shadows. This is especially apparent when the light source is close to a surface.

spatial values
:   A concrete measurement of a spatial metric in a 3D location. Spatial values are composed of three spatial coordinate values {X, Y, X}, and a measurement result value {V}. Spatial values are aggregated in a Spatial Metric Sample.

spatialization
:   An audio effect that gives a listener the impression that a sound is coming from a specific direction or location.

spatialized
:   Sound that has been recorded and/or processed to create an impression of spherical (3D) sound.

specular
:   Specular reflection uses the same angle to reflect light off an object as the angle the light strikes the object with. Compare to [diffuse](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#diffuse) and [normal](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#normal).

speed run race
:   In Rocket Racing, a speed run can be played solo or with multiple players, but instead of racing against others, the player is racing to beat their own best time in a session, with the result logged against global learderboards.

spline
:   In computer graphics, a spline is a smooth curve that runs through a series of given points.

spline node
:   A point on a path, track, or rail that controls its placement. These nodes can be used to shape, reshape or extend the path, track or rail.

sprite
:   A sprite is a two-dimensional [bitmap](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#bitmap) that's used in computer graphics. The term goes all the way back to the first arcade video games from the early Seventies.

spriting
:   Creating [sprites](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#sprite) by hand is a form of pixel art and is sometimes called spriting.

sRGB
:   sRGB stands for Standard Red Green Blue. This is a [color space](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#colorspace), or a set of specific colors, that sets a standard for the colors on electronic displays. sRGB is the most popular color space used today and the default used in games. Also see [RGB](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#rgb).

starter content
:   Content provided for use in a template to get a project going quickly.

Static Mesh
:   A Static Mesh is a 3D object drawn inside a level without animations. At most, it can have a transform modification that applies to the whole object.

step rate
:   In Patchwork, the pace at which a device moves through its output steps.

    Step rate controls are used for setting the output speed value for the [Step Modulator](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworkstepmodulator), for going through the columns on the Note Sequencer [note grid](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#notegrid), and for moving between [transpositions](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#transpose) applied by the [Note Progressor](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#patchworknoteprogressor).

stinger
:   A stinger (also called bumper or sounder) is a short audio clip used to introduce, link, or end other audio clips. In addition to music, stingers can also incorporate voiceover or sound effects.

streaming proxy
:   A part of the Landscape that can be loaded and unloaded independently, based on distance from player.

streaming source
:   Streaming sources are components that define a position in the world and trigger the loading of cells around them. Player Controllers are a streaming source. Other streaming sources can be added to the world using the [World Partition](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#worldpartition) Streaming Source component. For example, a streaming source component can be activated at the location that a player will teleport to, so it can load the cells there. Once the grid cells are loaded, the player teleports to the location and the streaming source component is deactivated. Since there is no longer a streaming source at the player's previous location, those grid cells would be unloaded. UEFN currently has the player as the only streaming source.

subscribe
:   Subscribing is a way to specify the [function](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#function) you want to [call](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#call) when an [event](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#event) is [raised](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#raise). This is referred as **binding to an event**. The [bound](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#bind) function is referred to as a [handler](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#handler).

sustain
:   The steady volume level of a held note following its [attack](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#attack) and [decay](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#decay). How long a note holds a steady volume.

sync content
:   A way of ensuring in UEFN that your project files are the most current when using [revision control](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#revisioncontrol).

tame
:   Taming is a way of filtering [distortion](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#distortion) in Patchwork that reduces or increases the distortion. A higher tame value increases the [filter](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#filter), which reduces the distortion.

target
:   When using camera devices, the target is the player the camera is following or focused on.

team
:   A group of users defined in Creator Portal that have shared access to one or more projects.

team member
:   A user who's been added to a team in the Creator Portal for the purpose of collaboration on a project.

tempo
:   How fast or slow something plays. Also known as beats per minute, or bpm. Different tempos can create different moods. For example, a 60-bpm tempo is a slow, relaxing tempo, while a 150-bpm tempo is much more energetic.

testing in Discover
:   For Discover, a test is defined as receiving 50,000 [impressions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#impression), ideally within a 20–60-minute period.  
    Discover algorithms analyze an island's attraction, engagement, and satisfaction during the test window. Islands with particularly high [sophistication scores](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#sophistication-score) may be tested multiple times in their first week post launch.

texel
:   Short for **tex**-ture **el**-ement, a texel is the smallest unit of a texture map. Texels are similar to [pixels](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#pixel) but they are the smallest units in texture space, compared to pixels in screen space.

texture
:   A texture is an image that is mapped to the surface that a [material](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#material) is applied to. A texture can be applied directly, or the values of the texture's pixels (called [texels](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#texel)) can be used within the material as masks or for other calculations. For the most part, textures are created in an image-editing application, such as Photoshop, then imported into UEFN through the Content Browser.

texture mapping
:   Texture mapping is a method for defining the appearance of a 3D model. This reduces the number of polygons needed to define surface color, texture or other details, which improves performance.

texture mask
:   A texture mask is a grayscale texture, or a single [R, G, B](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#rgb) or [Alpha](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#alphachannel) [channel](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#colorchannel) of a texture, used to limit the area of an effect inside of a [material](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#material).

title screen
:   A screen that displays while an item is loading.

TODM
:   Time of Day Manager

tool
:   In [UEFN](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#unrealeditorforfortnite), a tool is a dialog or panel used to perform a specific set of actions or to display information about one or more Actors or Assets, and an editor is a collection of tools used to edit one or more specific types of Assets.

transact
:   An action that is transacted can be reversed in the editor.

transform
:   References moving (translating), scaling, and rotating collectively.

transform gizmo
:   A viewport icon that you can use to quickly choose an axis or combination of axes when [transforming](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#transform) a selected object.

translate
:   To move an object from one place to another in three dimensions.

translation
:   Translation is when you move an object from one position to another in a three-dimensional space.

transpose
:   To shift a sequence of notes to a different key without changing the note pattern.

turbo
:   In Rocket Racing, the turbo button gives a vehicle a burst of speed.

UMG
:   Unreal Motion Graphics, or UMG, is a feature that provides a way to create an interactive user-interface using [widgets](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#widget) for a [project](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#project). It is the user-interface creation and editing suite inside of Unreal Engine (UE) and Unreal Editor for Fortnite (UEFN).

uncooked editor server
:   A server dedicated to validating, processing, and cooking data. The uncooked editor server is currently on the same machine as the dedicated server.

Unreal Engine
:   A complete suite of integrated tools for anyone working with real-time technology. In addition to the Unreal Editor interface for creating and editing content, this is the engine that runs the games and other experiences you create in the Unreal Editor.

Unreal Units
:   An Unreal Unit (UU, or unit) is the basic unit of length in Creative. The grid is based on UUs. On a Creative island, one meter equals 100 UU, and a [grid](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#grid) tile is 512 UU.

USD
:   USD stands for Universal Scene Description.The .usd file format is used for passing data between digital content creation applications. Developed by Pixar, it can interchange elemental assets like models or animation.

UV island
:   A group of connected [polygons](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#polygon) in a [UV map](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#uvmapping).

UV mapping
:   A way to project a 2D texture onto a 3D model. U and V name the axes used for the texture since X, Y and Z are used to name the axes of the 3D model.

validation
:   The checks run over the project content to verify it conforms to the rules of UEFN.

variable
:   A value that can be changed while a program is running. It's called a variable because it can vary.

Verse
:   Verse is a [statically-checked](https://dev.epicgames.com/documentation/en-us/uefn/verse-glossary#staticchecking) programming language with an emphasis on gameplay programming.

Verse file
:   A file in UEFN that contains Verse code.

version control
:   See [revision control](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#revisioncontrol).

vertex
:   A single point. Also see [vertices](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#vertices).

vertical composition
:   In [adaptive music](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#adaptivemusic), vertical composition, or reorchestration, is a technique in which a track continues to play throughout a section of a game, but as game parameters change, individual elements of the music track are added and removed.

    For example, it is common in games to have a simple orchestral track that plays while the player explores an island, but with additional percussion that plays only when the player is in combat. The combat-triggered percussion is added in dynamically when the player enters combat, and is removed when combat is finished, all while the original track continues to play.

    Compare to [horizontal composition](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#horizontalcomposition).

vertices
:   In 3D graphics, models are usually represented by an array of triangles called vertex sets, or vertices. A vertex can have coordinates that represent its position, color, texture, and other attributes.

verts
:   See [vertices](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#vertices).

VFX
:   Short for visual effects, VFX is digital art that is used for things that are not characters or objects. This includes things like, explosions, dust, water, and so on. A VFX object would be an object that includes visual effects.

vibrato
:   Small, rapid variations in pitch. Vibrato gives extra warmth and expression to a vocal or instrumental tone.

vibrato rate
:   The speed with which a vibrato tone varies.

viewport
:   The viewport is a visual representation of your level in the editor. While working on your level, you can use a 3D viewport, 2D viewports, or a combination.

    The viewport contains a variety of tools to help you see the exact data you need. Viewports are your windows into the things you create. They can be navigated just as you would in a game, or used in a more schematic design sense as you would for an architectural blueprint.

vignette
:   An effect that simulates darkening in a real-world camera lenses. High-quality lens try to compensate for this effect. Vignetting is mostly noticeable near the edges of the image.

Virtual Shadow Map
:   Virtual Shadow Map (VSM) is a shadow-mapping method that delivers consistent, high-resolution shadowing.

voxel
:   A unit of graphic information based on three dimensions. From **vo** lume and **el** ement. Compare to [pixel](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#pixel) and [texel](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#texel).

waveform
:   A graphical representation of a signal. A waveform shows changes of intensity over time.

weight map
:   A weight map is a way to paint varying strengths on a texture that is mapped to terrain. This, in turn, can be used by a material to control how the terrain appears.

wet
:   In audio, a wet signal or sound has effects added to it, such as reverb. This refers to any effects you can apply to sound. Compare to [dry](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#dry).

white balance
:   A setting that tells the camera how to register color temperature by adjusting the value of the whites in an image so the whites actually appear white.

    White balance acts to balance the [color temperature](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#colortemperature) in a game environment by adding the opposite color to the image in an attempt to bring the color temperature back to a natural-looking neutral. Instead of whites appearing blue (cool) or orange (warm), they should appear white after correct white balancing.

widget
:   An element of a graphical user interface (GUI) that displays information, or provides a specific way for a user to interact with the application.

wireframe
:   A model created by [vertices](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#vertices) to represent a single object, character, or a piece of terrain. A wireframe is typically three-dimensional and is un-textured, exposing all vertices in a see-through fashion.

World Partition
:   The magic behind building large experiences, the World Partition feature in UEFN automatically divides the world into [cells](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#cell), and [streams](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#streamingsource) only the necessary [cells](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#cell) based on player location and [HLOD](https://dev.epicgames.com/documentation/en-us/uefn/unreal-editor-for-fortnite-glossary#hlod).

world position
:   World position is the location where a vertex or pixel is being rendered.

world position offset
:   This is the additional offset applied to a vertex position from its base position, and is controlled by the material.

World Settings Glossary
:   Each level can have unique settings applied to it from the World Settings panel that override other settings.

world space
:   World space is relative to the world origin, with a position of 0, 0, and 0 across the X-, Y- and Z-axes.

X-axis
:   See [axis](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#axis).

Y-axis
:   See [axis](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#axis).

Z-axis
:   See **[axis](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#axis)**.

z-score
:   In statistical analysis, a z-score is a way to measure how far from the **mean** (average) any data value is based on a standardized scale. Z-scores identify **outliers** in a dataset by finding those values (the outliers) that are unusually distant from the mean.
