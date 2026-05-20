## https://dev.epicgames.com/documentation/en-us/fortnite/upgrading-legacy-lighting-in-multilevel-projects-in-unreal-editor-for-fortnite

# Upgrading Legacy Lighting in Multi-Level Projects

Upgrade out-of-date world lighting in multi-level projects.

![Upgrading Legacy Lighting in Multi-Level Projects](https://dev.epicgames.com/community/api/documentation/image/2919d9b0-f02c-4822-95ef-0ec1b8c94c57?resizing_type=fill&width=1920&height=335)

With the deprecation of the old time of day manager’s (TODM) day and night cycle and the Skydome device, it is recommended to convert all islands you wish to preserve to the new TODM. 
All islands using the Skydome device will retain their gameplay, volume data, and positional data, but the island lighting will default to Chapter 5 lighting and ignore any settings used with the Skydome device.

The upgrade guarantees:

- More realistic lighting with Lumen and Nanite.
- Parity with the UEFN TODM and future TODM updates.

This also affects UEFN projects that use multi-level instances, or multiple maps. To ensure that you can publish your island and reduce the possibility of running into problems, you need to convert all lighting in your additional levels.

## Default Level

You will always have a default level, which is what is loaded when you launch a session. You can change which level is the default level at any time through the **GameFeatureData** asset by doing the following:

By default, when you open a UEFN project the “default map” loads, but you can load any additional levels by:

## Manual Lighting Upgrade

In order to upgrade the lighting on a particular level, it is recommended to open up all secondary levels that have legacy lighting and upgrade the TODM and Skydome devices individually. Once a map is loaded, you can convert the map and adjust the visuals to ensure the conversion is working properly for you.

### Time of Day Manager (TODM)

The easiest way to tell if a map is using legacy lighting is to look at the World Settings. To check your what TODM a map is using:

## Skydome and Day Sequence Devcie

If the legacy TODM was used in your map, you may also have old Skydome devices.  In which case it’s important to also upgrade your Skydome devices to the new [Day Sequence device](https://dev.epicgames.com/documentation/en-us/uefn/using-day-sequence-devices-in-unreal-editor-for-fortnite), since the Skydome device is not compatible with the latest Ch5 TODM.

To check if a map is using the Skydome device, do the following:

For any Skydome devices being used, replace them with the Day Sequence devices.  You can find the Day Sequence device in the **Fortnite** > **Devices** > **Environment** folders in the content hierarchy of the Content Browser.

[![Replace all Skydome devices with the Day Sequence device.](https://dev.epicgames.com/community/api/documentation/image/9b0b7a95-6a96-4d0b-bd03-fd3e2b9e8156?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b0b7a95-6a96-4d0b-bd03-fd3e2b9e8156?resizing_type=fit)

Day Sequence device

Add any number of Day Sequence devices, and tweak the visuals to taste.

The parameters are different between the Skydome and Day Sequence devices, so it’s important to become familiar with the new features.  Please see the [Day Sequence device](https://dev.epicgames.com/documentation/en-us/uefn/using-day-sequence-devices-in-unreal-editor-for-fortnite) document for more details on creating world lighting.
