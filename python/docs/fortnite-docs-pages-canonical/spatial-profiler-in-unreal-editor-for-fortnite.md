## https://dev.epicgames.com/documentation/en-us/fortnite/spatial-profiler-in-unreal-editor-for-fortnite

# Spatial Profiler

Use the spatial profiler to gather metrics on your UEFN islands.

![Spatial Profiler](https://dev.epicgames.com/community/api/documentation/image/902d89c3-2c2f-4969-b4f4-7ab9208f7126?resizing_type=fill&width=1920&height=335)

**Unreal Editor for Fortnite (UEFN)** gives you the tools you need to understand and improve the performance of your project. Since Fortnite runs on many platforms, knowing specific metrics for your project means that you can make any necessary adjustments to ensure smooth performance across your UEFN experiences.

The **Spatial Profiler** is a visualization widget that provides you with a 2D heatmap of Spatial Metrics. Here, you can also record, save, and load spatial metric samples. It collects data from the spatial metrics update function, meaning that data is updated periodically.

Jump to [Using the Spatial Profiler](https://dev.epicgames.com/documentation/fortnite/spatial-profiler-in-unreal-editor-for-fortnite#using-the-spatial-profiler) for a quick look at the workflow, or keep reading for an in-depth look at the **Spatial Profiler** tool.

[![](https://dev.epicgames.com/community/api/documentation/image/32f6bb99-df24-4eff-bb27-1232d1d268b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32f6bb99-df24-4eff-bb27-1232d1d268b5?resizing_type=fit)

Spatial Profiler in editor. UEFN Editor with the Spatial Profiler docked window.

## Useful Terms

A **Spatial Metric** is measured for any property that uses a 3D spatial position in a world. It consists of a certain number of spatial values, each having a number that corresponds to a measurement, with an associated coordinate that gives the spatial position where the value was measured within the world.

A **Spatial Value** is a concrete measurement of a spatial metric in a 3D location. Spatial values have three spatial coordinate values **X, Y, Z**, and a measurement result value. Spatial values are aggregated in a Spatial Metric Sample.

A **Spatial Metric Sample** is a measurement of a concrete spatial metric over a defined period. It may contain several spatial values measured with an associated result. A sample also includes other relevant data, such as the 3D bounds enclosing all the enclosing spatial values, the distance precision used, and the date it was taken.

The **Spatial Metric Properties** represent all the information included in a spatial metrics sample:

|  |  |
| --- | --- |
| **Property** | **Definition** |
| **Metric ID** | Defines the unique metric identifier, which is directly tied to the type of metric. |
| **Min Value** | The minimum value among the recorded spatial values. |
| **Max Value** | The maximum value among the recorded spatial values. |
| **Threshold Value** | The maximum value expected for the metric. |
| **Spatial Precision** | The 3D cell size used in world units, so all values contained contribute to the same spatial value. Usually, the highest value is selected. |
| **Unit** | The unit used by the recorded values, for example, milliseconds for time or meters for distance. |

## Using the Spatial Profiler

This section covers how to launch a live sampling session using the **Spatial Profiler** tool to monitor performance and memory usage during active sessions.

If a Spatial Profiler metric exceeds its threshold during gameplay, a performance warning icon appears in the viewport. There will be an Investigate button on this notification which opens Spatial Profiler.

1. Enable **Monitor Performance** from the [Launch Session](https://dev.epicgames.com/documentation/fortnite/user-interface-reference-for-unreal-editor-for-fortnite#8-live-edit-options) options in UEFN.
2. Open the **Spatial Profiler** window from either:

   - The **Performance** button in the bottom toolbar.

     - [![](https://dev.epicgames.com/community/api/documentation/image/efa3e832-7bc9-4415-a410-2bfc6ea8b01d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efa3e832-7bc9-4415-a410-2bfc6ea8b01d?resizing_type=fit)
   - **Tools > Spatial Profiler**.
   - The memory warning notification that pops up when a memory threshold is exceeded during a play session.
3. Launch a local play session.
4. In the game session, use your pawn to run around the island and play the game as intended to continuously capture performance and memory usage data. During gameplay the Spatial Profiler heatmap data updates in real time.

You can then click the **Memory Snapshot** button which will take a snapshot of the live assets loaded in memory, this will present a progress dialog to show a capture is happening. To learn more, see [Memory Snapshot](https://dev.epicgames.com/documentation/fortnite/memory-snapshot-in-unreal-editor-for-fortnite) .

## Save and Reopen Captures

You can save **Spatial Profiler** captures and reopen them later for additional review or comparison.

Spatial Profiler captures and Memory Snapshot insights are separate capture types and collect different profiling data.

Saved captures help you:

- Compare optimization changes
- Revisit previous profiling sessions
- Investigate performance regressions

To save a capture:

[![](https://dev.epicgames.com/community/api/documentation/image/1b8d5438-a735-4419-bdc6-439e400bbfd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b8d5438-a735-4419-bdc6-439e400bbfd3?resizing_type=fit)

To reopen a saved capture:

[![](https://dev.epicgames.com/community/api/documentation/image/461e771d-b0df-420e-b6ce-317b35354d2e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/461e771d-b0df-420e-b6ce-317b35354d2e?resizing_type=fit)

## Spatial Profiler UI

The **Spatial Profiler** is a dockable standalone widget divided into four areas:

[![](https://dev.epicgames.com/community/api/documentation/image/29e3474c-1840-443b-818f-6097f9257e39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29e3474c-1840-443b-818f-6097f9257e39?resizing_type=fit)

Spatial Profiler widget areas.

## Control Toolbar

This area contains the main interactive elements to operate the Spatial Profiler. It gives you the controls to produce, visualize, and save Spatial Metrics samples. You can use the samples you capture to generate data that can improve your UEFN experience.

[![](https://dev.epicgames.com/community/api/documentation/image/4d5ddd3c-12a0-4338-b936-ab2a8b0babcc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d5ddd3c-12a0-4338-b936-ab2a8b0babcc?resizing_type=fit)

Spatial Profiler control toolbar elements.

The control toolbar includes the following elements:

1. **Live Capture:** use this button to view the active live capture from the connected session. Live Capture displays spatial metric data in real time while profiling gameplay.
2. **Saved Captures:** this button opens a pre-existing sample file, which can contain multiple metrics. On opening, all loaded metrics are loaded into the metric browser so that you can assess the data.
3. **Save a sample to file:** you can use this button to save active profiling sessions. It opens a save-to-file dialog and proposes a file name with the sample timestamp by default. The Spatial Profiler saves all metrics in the current sampling session to the destination file.
4. **Start sampling:** this button starts the capture of the set of metrics the user selected. You have to be connected to a UEFN session for metrics to be sampled. During sampling, the heatmap automatically centers the view at the session’s player pawn location and focuses on the spatial values captured.
5. **Stop sampling:** this button stops the capture of the selected metrics.
6. **UEFN session selector:** You can have more than one client connected to a session. You can use the session selector to choose which session to connect and run metrics. The Spatial Profiler automatically connects to the client when launching a session, and then updates the session selector with the name of the user connected to that session.
7. **Take a Memory Snapshot:** use this button to capture a [Memory Snapshot](https://dev.epicgames.com/documentation/fortnite/memory-snapshot-in-unreal-editor-for-fortnite) from the connected session. Memory Snapshot displays an estimated memory usage breakdown for loaded assets, helping you identify assets contributing to high memory usage and investigate their impact on the island.
8. **Settings:** this button displays the Spatial Profiler preference settings. You can use this to toggle the visibility of certain widget elements.
9. **Connected Client:** this displays the name of the client currently connected to the active profiling session. A client is an instance of Fortnite connected to UEFN during a play session. The Connected Client element updates automatically when launching or switching sessions, and can also display Disconnected clients from previous profiling sessions.

## Metrics Tree View

You can select and deselect the metrics you want in your sampling session by clicking the check boxes to the left of the metrics. The **Search bar** can look up a specific metric.

[![](https://dev.epicgames.com/community/api/documentation/image/a9fb2313-80e8-4038-a257-a1459f6d3db7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9fb2313-80e8-4038-a257-a1459f6d3db7?resizing_type=fit)

When you click on a metric to select it, the Heatmap view updates to show any data samples, and Stats view updates to display the aggregate statistics for the data. The colored circles next to each metric represent their relative values based on the thresholds you set before the sampling session, showing your results at a glance.

[![](https://dev.epicgames.com/community/api/documentation/image/67207def-95b2-4ecb-9ebf-695f4aa188bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67207def-95b2-4ecb-9ebf-695f4aa188bb?resizing_type=fit)

Memory Usage selected and displays on the heatmap.

The following spatial metrics are available in the Spatial Profiler:

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Unit** |
| **Actor Count** | Tracks the number of actors in the world accounting for streaming events. This is especially useful for worlds with [World Partition](https://dev.epicgames.com/documentation/fortnite/streaming-and-hlods-in-unreal-editor-for-fortnite) streaming enabled. Seeing inconsistent actor counts in the level can highlight the most important areas of gameplay. However, really high actor counts can also indicate an excessive number of small actors and a potential stress point for the experience.  It is a good idea to evaluate this metric together with Game Update Time to evaluate game logic complexity, or with Render Time to evaluate render complexity. | Actors |
| **Scene Graph Entity** | Tracks the number of Scene Graph entities currently loaded in the world, accounting for streaming events and dynamically spawned entities. | Entities |
| **UObject Count** | Tracks the total number of Unreal Engine objects currently loaded in memory, including actors, components, assets, materials, and other engine systems used by the island. | UObjects |
| **Unique Collision Mesh Count** | Tracks the number of unique collision meshes currently loaded in memory. | Meshes |
| **Building Count** | A specialized version of the Actor Count metric that tracks the number of actors that have been categorized as buildings, and includes persistent static mesh actors. | Actors |
| **Loot Container Count** | A specialized version of the Actor Count metric that tracks the number of actors that have been categorized as loot containers. This category includes actors like chests, ammo boxes and other pickup spawners. | Actors |
| **Pickup Count** | A specialized version of the Actor Count metric that tracks the number of actors that have been categorized as pickups. This category includes lootable gameplay items. | Actors |
| **Available Memory** | Tracks the platform's available physical memory. You can use this to evaluate the memory requirements of each platform the experience has to run on.  Memory value display presets can be adjusted to use larger units when reviewing higher memory values. | Kilobytes |
| **Memory Usage** | Tracks the platform's executable memory usage. You can use this to evaluate the memory requirements of each platform the experience has to run on. | Kilobytes |
| **Texture Streaming Memory Usage** | Tracks memory usage from streamed textures. Texture streaming dynamically loads and unloads texture detail based on distance and screen size. | Mebibytes |
| **Draw Call Count** | Tracks the number of [draw calls](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#draw-call) on a single frame | Draw calls |
| **Primitive Count** | Tracks the number of primitives rendered on a single frame. Primitives are the basic drawing components used to render objects in 3D. | Primitives |
| **Shaders Loaded Count** | Tracks the number of shader variations currently loaded in memory. High counts may indicate too many unique materials or overly complex material settings. | Shaders |
| **Frame Time** | Tracks the total time required to update a single frame, including both Game Update Time and Render Time. Higher frame times can result in low FPS and less responsive gameplay. | Microseconds |
| **Game Update Time** | Tracks the platform’s game thread, measuring the time taken to update a single frame. | Microseconds |
| **GPU Time** | Tracks the platform's GPU time. | Microseconds |
| **Render Time** | Tracks the platform’s render thread, measuring the time taken to update a single frame. | Microseconds |
| **RHI Time** | Tracks the platform's Render Hardware Interface thread time. | Microseconds |

## Heatmap View

The Heatmap view displays a heatmap of your chosen metric, with an overlay of all the spatial values in the sample. Each spatial value is colored according to the sample’s data. You can quickly set cutoff values for each metric to define the range of expected values.

You can interact with the heatmap and customize it to your preferences using the four buttons at the top:

- Hamburger Menu
- Show Options
- Focus Player
- Focus Bounds

[![](https://dev.epicgames.com/community/api/documentation/image/16a3c299-f6a8-4c4c-a7df-089b90241d50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16a3c299-f6a8-4c4c-a7df-089b90241d50?resizing_type=fit)

Double-clicking on any location in the Heatmap view places the Editor camera at the corresponding location within the project. If a session is launched, the player pawn teleports to the location you double-click.

### Hamburger Menu

This button gives you access to the heatmap visualization options, containing two sections:

- Metric Settings
- Heatmap Color Settings

You can reset the settings in these sections by clicking the reset arrow button on the right side of each field.

[![](https://dev.epicgames.com/community/api/documentation/image/1d5136d8-e19e-49a1-a126-3a6b9c26c2ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d5136d8-e19e-49a1-a126-3a6b9c26c2ab?resizing_type=fit)

Spatial Profiler hamburger menu options.

#### Metric Settings

The **Metric Settings** group all the settings affecting visualization of the metrics.

|  |  |
| --- | --- |
| **Value** | **Definition** |
| **Profile** | Select the active profile for the source.   - Desktop - Console(Gen 8, 9, and Portable) - Mobile - Default |
| **Threshold** | A threshold value defines the expected maximum value for normal gameplay.  The Profile threshold values do not affect the Memory Usage values displayed in the Performance Monitor. |
| **Display Unit** | When specified, this option defines the preferred visualization unit for a metric. If left unspecified, the tool selects the best fitting unit for each metric. The Display Unit affects the units used by the Heatmap view and the Summary view. |
| **Cell Method** | This setting specifies the reduction method the tool uses to calculate each 2D cell value from the list of values that fall within each cell's boundaries. The available reduction methods are: |
| **Cell Size** | This setting changes the size of the grid and can increase or decrease the level of detail for a particular sampling area. |
| **Loading Range** | The streaming radius (in cm) used to show the loading behavior in the  [World Partition](https://dev.epicgames.com/documentation/fortnite/streaming-and-hlods-in-unreal-editor-for-fortnite)  .  The **Loading Range visualization** is not automatically synchronized with the **Loading Range values** configured in **World Settings**. If your World Settings values change, update the Loading Range setting manually to match your island configurations. |

#### Heatmap Color Settings

The **Heatmap Color Settings** contain all the settings affecting the visualization of the metrics.

The **Heat Colors** offer a readable color palette with considerations for colorblindness. You can define the key colors to customize the heatmap color range.

|  |  |
| --- | --- |
| **Value** | **Definition** |
| **Low** | This color represents the low spectrum of the heatmap color range, and maps to the minimum value in a metric sample. |
| **Midpoint** | This color represents the middle of the heatmap color range defined between the Minimum and the Threshold color. If a threshold value is not specified, it maps to the median spatial value in a sample. |
| **High** | This color represents all values that are above the set threshold. |
| **Max** | This color represents the maximum value. It is only displayed when you define a threshold value for the represented metric. When you specify a threshold value, the heatmap adds a range that exceeds the threshold, going from white to the color set for Maximum. |
| **Min Alpha** | The starting value given to spatial values. The alpha value of all spatial values in a sample increases according to their value, from the Minimum value (using Min Alpha) to the Maximum or Threshold values with maximum alpha. Using a low Min Alpha value highlights spatial values closer to the Maximum or Threshold values by making low spatial values less visible. |
| **Max Alpha** | The maximum starting value given to spatial values. |

The Alpha Settings show spatial values outside of the expected range. Adjusting these options becomes especially useful when looking at a metric sample with pockets of high-density spatial values, as you can review the metrics in more detail.

### Axes

This option toggles the visualization of the 3D axes on the bottom-left corner corresponding to the Heatmap view’s top-down orientation. This orientation is in parity with the client’s minimap view and not with the Editor's.

[![](https://dev.epicgames.com/community/api/documentation/image/689df15b-d008-46be-9320-655fc0c1ef1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/689df15b-d008-46be-9320-655fc0c1ef1e?resizing_type=fit)

Showing Heatmap axes

### Grid

Toggles the visualization of the 2D heatmap grid, subdividing the visible space into multiples of the sample value’s extents. The grid size can be modified in the hamburger menu.

![No Grid](https://dev.epicgames.com/community/api/documentation/image/5f70cae0-4324-44f1-b67d-d36bda3512fb?resizing_type=fit&width=1920&height=1080)

![Grid](https://dev.epicgames.com/community/api/documentation/image/ed386fe4-6076-4942-afbe-1e48fe5dedf6?resizing_type=fit&width=1920&height=1080)

### Heatmap Legend

This option turns the visualization of the heatmap’s color range legend on or off at the bottom right corner of the Heatmap view.

[![](https://dev.epicgames.com/community/api/documentation/image/eaa7557f-1476-40e6-9c0a-13175f99ad7f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eaa7557f-1476-40e6-9c0a-13175f99ad7f?resizing_type=fit)

Displaying Heatmap color palette legend

### Bounds

This option will toggle the 2D bounding box, which comprises all the spatial values in the sample.

[![](https://dev.epicgames.com/community/api/documentation/image/1768849a-1645-48fa-9a2d-be75abb2c677?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1768849a-1645-48fa-9a2d-be75abb2c677?resizing_type=fit)

Showing sample bounds (white) on the Heatmap

### Streaming Radius

This displays the streaming radius used to visualize how far [World Partition](https://dev.epicgames.com/documentation/fortnite/streaming-and-hlods-in-unreal-editor-for-fortnite) tiles load around the player during analysis.

The Streaming Radius map visualization is not automatically linked to the World Settings streaming radius values. To match your island configuration accurately, manually set the Streaming Radius map values to correspond with your World Partition streaming settings.

[![](https://dev.epicgames.com/community/api/documentation/image/34d923df-f680-4de9-aa26-1c22920b7f26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34d923df-f680-4de9-aa26-1c22920b7f26?resizing_type=fit)

### Sample Values

This displays the calculated value for each Heatmap cell based on the samples captured within that area. By default, each cell displays the median sampled value. The displayed value is determined by the selected [Cell Method](https://dev.epicgames.com/documentation/fortnite/spatial-profiler-in-unreal-editor-for-fortnite#metric-settings) reduction setting.

[![](https://dev.epicgames.com/community/api/documentation/image/921de887-ec11-4edd-94cd-f5884a09fdc8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/921de887-ec11-4edd-94cd-f5884a09fdc8?resizing_type=fit)

### Focus Player

Use the Focus Player options to control how the Spatial Profiler view tracks the connected session or editor viewport.

[![](https://dev.epicgames.com/community/api/documentation/image/013d97c5-c2f4-4d36-8a2c-e1fad3ad39da?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/013d97c5-c2f4-4d36-8a2c-e1fad3ad39da?resizing_type=fit)

The following tracking modes are available:

- **Off:** Disables automatic view tracking **(enabled by default)**
- **Track Player:** Continuously tracks the player’s viewpoint in the connected session.
- **Track Editor Camera:** Continuously tracks the editor viewport camera position.
- **Track Bounds:** Continuously fits the view to the bounds of the active spatial metric sample.

### Focus Bounds

This button centers the Heatmap view around the 2D bounding box.

[![](https://dev.epicgames.com/community/api/documentation/image/27350844-d68a-41af-a5e7-bfe3c9d6cf0d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27350844-d68a-41af-a5e7-bfe3c9d6cf0d?resizing_type=fit)

## Contextual Menu

You can access the contextual menu by right-clicking on the Heatmap view area. This menu contains the following options:

- Teleport
- Default View
- Focus Bounds

[![](https://dev.epicgames.com/community/api/documentation/image/6e114186-b146-4e1f-9c51-fee1e9d8708c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e114186-b146-4e1f-9c51-fee1e9d8708c?resizing_type=fit)

Spatial Profiler Heatmap View contextual menu

|  |  |
| --- | --- |
| **Option Name** | **Definition** |
| **Teleport** | You can use this option to bring both the camera view and the player pawn to a chosen right-clicked location in the Heatmap view. This action requires a connected session to teleport the player pawn. If no session is connected, it is the equivalent to double-clicking on any location in the Heatmap view, which places the Editor camera at the corresponding location within the project. |
| **Default View** | This option resets the Heatmap view focus and zoom values to their default settings. |
| **Focus Bounds** | You can use this option to focus the Heatmap view to include all sampled areas within the active spatial metric capture. This helps provide an overview of the full sampled region during analysis. |

## Histogram View

The **histogram** helps you visualize the data as it is being collected in real time. You can to go back through your test of the level and assess each metric at a specific point in your playtest. By scrolling through the open session's histogram you can identify the location of a particular reading that you want to investigate.

[![](https://dev.epicgames.com/community/api/documentation/image/e1dbcb78-1984-4bb8-8fd1-8458ecbcef79?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1dbcb78-1984-4bb8-8fd1-8458ecbcef79?resizing_type=fit)

Adjusting the values in the Hamburger menu will modify the various cutoff points displayed in the histogram.

Right-clicking the histogram you can select **Display Threshold Guidelines**, **Auto Scroll**, **Shade Values by Cell**, choose the Next and Previous values, and **Scale Histogram**. You can change the scale of the histogram by holding **Shift + Scrolling** the mouse wheel.

[![](https://dev.epicgames.com/community/api/documentation/image/b07af040-8507-4013-9407-305181260c3a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b07af040-8507-4013-9407-305181260c3a?resizing_type=fit)

Right-clicking the histogram displays the above options.

You can also zoom in and out of the histogram to get a more detailed look at your metrics.

![More Zoomed Out](https://dev.epicgames.com/community/api/documentation/image/7ad0004b-01c0-41d6-bc39-980667ba9fea?resizing_type=fit&width=1920&height=1080)

![More Zoomed In](https://dev.epicgames.com/community/api/documentation/image/fc07edaa-0362-4d1b-b24b-4092f659d1ef?resizing_type=fit&width=1920&height=1080)

When you hover over a segment of the sample, a tooltip will display its value.

[![](https://dev.epicgames.com/community/api/documentation/image/03845b97-d34c-44bf-90cd-6e54a9f5092a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/03845b97-d34c-44bf-90cd-6e54a9f5092a?resizing_type=fit)

Clicking on the sample segment highlights the location of the segment on the heatmap.

To the right of the histogram you can see a summary of statistics for the selected metric. It displays the following stats compiled from the sample’s spatial values:

|  |  |
| --- | --- |
| **Statistic** | **Definition** |
| **Values** | The total number of spatial values included in the sample. |
| **Outside** | The number of spatial values exceeding the threshold value, if defined. |
| **Min Value** | The smallest spatial value. |
| **Max Value** | The largest spatial value. |
| **Average Value** | Displays the average value across all collected samples during the capture session. |
| **Median Value** | Displays the middle sample value during the capture session. |
