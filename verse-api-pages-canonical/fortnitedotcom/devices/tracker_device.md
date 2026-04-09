## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/tracker_device

# CreativeAnimation module
Learn technical details about the CreativeAnimation module.
Module import path: /Fortnite.com/Devices/CreativeAnimation
  * [`Fortnite.com`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom)
  * [`Devices`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices)
  * **`CreativeAnimation`**
    * [`InterpolationTypes`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/interpolationtypes)

## Classes and Structs
Name | Description
---|---
[`cubic_bezier_parameters`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/cubic_bezier_parameters) |  A structure for defining Bezier interpolation parameters. See https://en.wikipedia.org/wiki/B%C3%A9zier_curve for more info on Bezier curves.
[`keyframe_delta`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/keyframe_delta) |  Instead of specifying the actual keyframe positions, we specify the keyframe _deltas_. This allows us to treat the initial position of the prop as keyframe 0 and avoid the question of how to get the prop to its initial location. For a `animation_mode.Loop` animation, the net rotation and translation must both be zero. Each delta is interpreted as a world-space transformation to be concatenated onto the previous transform(s).
[`animation_controller`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/animation_controller) |  Used to move and animate the position of `creative_prop` objects.
  * See `creative_prop.GetAnimationController` for information on acquiring an instance of an `animation_controller` for a given `creative_prop`.
  * See `SetAnimation` for details on authoring movement and animations.

## Enumerations
Name | Description
---|---
[`animation_mode`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/animation_mode) |  Animation play modes.
[`animation_controller_state`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/animation_controller_state) |  `animation_controller` states.
---|---
[`await_next_keyframe_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/await_next_keyframe_result) |  Results for `animation_controller.AwaitNextKeyframe` function.
---|---
