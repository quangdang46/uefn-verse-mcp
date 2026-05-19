## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/cubic_bezier_parameters

# cubic_bezier_parameters struct
Learn technical details about the cubic_bezier_parameters struct.
A structure for defining Bezier interpolation parameters. See https://en.wikipedia.org/wiki/B%C3%A9zier_curve for more info on Bezier curves.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices/CreativeAnimation }`
## Members
This struct has data members, but no functions.
### Data
Data Member Name | Type | Description
---|---|---
`X0` | `float` |  X value of the P1 control point. `0.0 <= X0 <= 1.0` or an error will be generated when calling `animation_controller.SetAnimation`.
`Y0` | `float` |  Y value of the P1 control point.
`X1` | `float` |  X value of the P2 control point. `0.0 <= X1 <= 1.0 or an error will be generated when calling `animation_controller.SetAnimation`.
`Y1` | `float` |  Y value of the P2 control point.
