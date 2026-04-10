## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath

# SpatialMath module
Learn technical details about the SpatialMath module.
Module import path: /Verse.org/SpatialMath
  * [`Verse.org`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg)
  * **`SpatialMath`**

## Classes and Structs
Name | Description
---|---
[`rotation`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/rotation) |
[`transform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/transform) |  A combination of scale, rotation, and translation, applied in that order.
[`vector3`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/vector3) |  3-dimensional vector with `float` components.
## Functions
Name | Description
---|---
[`MakeRotationRadians`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makerotationradians) |  Makes a `rotation` from `Axis` and `Angle` in radians using a right-handed sign convention (e.g. a positive rotation around Up takes Forward to Left).
[`MakeRotationDegrees`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makerotationdegrees) |  Degrees version of `MakeRotationRadians`
[`MakeRotationFromYawPitchRollRadians`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makerotationfromyawpitchrollradians) |  Makes a `rotation` by applying a pre-rotation of `YawAngle` followed by `PitchAngle` and then `RollAngle`, in that order:
  * _yaw_ is right-handed rotation about the Down axis,
  * _pitch_ is right-handed rotation about the Right axis,
  * _roll_ is right-handed rotation about the Forward axis.

[`MakeRotationFromYawPitchRollDegrees`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makerotationfromyawpitchrolldegrees) |  Degrees version of `MakeRotationFromYawPitchRollRadians`
[`MakeRotationFromEulerRadians`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makerotationfromeulerradians) |  Makes a `rotation` by applying a post-rotation of `LeftAxisAngle` followed by `UpAxisAngle` and then `ForwardAxisAngle `in that order. Right-handed convention (e.g. a positive rotation around Up takes +Forward to Left).
[`MakeRotationFromEulerDegrees`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makerotationfromeulerdegrees) |  Degrees version of `MakeRotationFromEulerRadians`
[`IdentityRotation`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/identityrotation) |  Makes the identity `rotation`.
[`Distance`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/distance) |  Returns the distance between `Rotation1` and `Rotation2`. The result will be between:
  * `0.0`, representing equivalent rotations and
  * `1.0` representing rotations which are 180 degrees apart (i.e., the shortest rotation between them is 180 degrees around some axis).

[`AngularDistanceRadians`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/angulardistanceradians) |  Returns the smallest angular distance between `Rotation1` and `Rotation2` in radians.
[`AngularDistanceDegrees`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/angulardistancedegrees) |  Degrees version of `AngularDistanceRadians`.
[`operator'*'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorstar) |  Apply a `PreRotation` to `PostRotation` as `v * PreRotation * PostRotation`.
[`MakeShortestRotationBetween`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/makeshortestrotationbetween) |  Makes the smallest angular `rotation` from `InitialVector` to `FinalVector` two vectors of arbitrary length such that: `InitialVector * MakeShortestRotationBetween(InitialVector, FinalVector) = FinalVector` and `MakeShortestRotationBetween(InitialVector, FinalVector)?.GetAngleRadians()` is as small as possible.
[`Slerp`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/slerp) |  Used to perform spherical linear interpolation between `From` (when `Ratio = 0.0`) and `To` (when `Ratio = 1.0`). Expects `0.0 <= Ratio <= 1.0`.
[`operator'*'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorstar-1) |  Makes a `vector3` by applying `Rotation` to `Vector`.
[`ToString`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/tostring) |  Makes a `string` representation of `rotation` in axis/degrees format with a right-handed sign convention. `ToString(MakeRotationRadians(vector3{Left:=0.0, Up:=0.0, Forward:=1.0}, PiFloat/2.0))` produces the string: `"{Axis = {Left=0.000000, Up=0.000000, Forward=1.000000}, Angle = 90.000000}"`.
[`DegreesToRadians`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/degreestoradians) |  Returns radians from `Degrees`.
[`RadiansToDegrees`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/radianstodegrees) |  Returns degrees from `Radians`.
[`operator'*'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorstar-2) |  Makes a `vector3` by applying `InTransform` to `InVector`.
[`ToString`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/tostring-1) |  Makes a `string` representation of `InTransform` where the result is on the form. `"{Translation = {ToString(`InTransform.Translation`)}, Rotation = {ToString(`InTransform.Rotation`)}, Scale = {ToString(`InTransform.Scale`)}}".
[`ReflectVector`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/reflectvector) |  Makes a `vector3` by inverting the `SurfaceNormal` component of `Direction`.
[`DotProduct`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/dotproduct) |  Returns the dot product of `V1` and `V2`.
[`CrossProductLeftHanded`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/crossproductlefthanded) |  Returns the left-handed cross product of `V1` and `V2`.
[`CrossProduct`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/crossproduct) |  Returns the right-handed cross product of `V1` and `V2`.
[`Distance`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/distance-1) |  Returns the Euclidean distance between `V1` and `V2`.
[`DistanceSquared`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/distancesquared) |  Returns the squared Euclidean distance between `V1` and `V2`.
[`DistanceForwardLeft`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/distanceforwardleft) |  Returns the 2-D Euclidean distance between `V1` and `V2` by ignoring the difference in `Up`.
[`DistanceSquaredForwardLeft`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/distancesquaredforwardleft) |  Returns the squared 2-D Euclidean distance between `V1` and `V2` by ignoring their difference in `Up`.
[`ToString`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/tostring-2) |  Makes a `string` representation of `V`.
[`Lerp`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/lerp) |  Used to linearly interpolate/extrapolate between `From` (when `Parameter = 0.0`) and `To` (when `Parameter = 1.0`). Expects that all arguments are finite. Returns `From*(1 - Parameter) + To*Parameter`.
[`prefix'-'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/prefixminus) |  Makes a `vector3` by inverting the signs of `Operand`.
[`operator'+'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorplus) |  Makes a `vector3` by component-wise addition of `Left` and `Right`.
[`operator'-'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorminus) |  Makes a `vector3` by component-wise subtraction of `Right` from `Left`.
[`operator'*'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorstar-3) |  Makes a `vector3` by component-wise multiplication of `Left` and `Right`.
[`operator'*'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorstar-4) |  Makes a `vector3` by multiplying the components of `Left` by `Right`.
[`operator'*'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorstar-5) |  Makes a `vector3` by multiplying the components of `Right` by `Left`.
[`operator'/'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorslash) |  Makes a `vector3` by dividing the components of `Left` by `Right`.
[`operator'/'`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/operatorslash-1) |  Makes a `vector3` by component-wise division of `Left` by `Right`.
[`IsAlmostEqual`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/spatialmath/isalmostequal) |  Succeeds when each component of `V1` and `V2` are within `AbsoluteTolerance` of each other.
