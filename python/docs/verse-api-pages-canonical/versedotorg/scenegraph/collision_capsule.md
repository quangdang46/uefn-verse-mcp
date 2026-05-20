## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/scenegraph/collision_capsule

# collision_capsule class

Learn technical details about the collision_capsule class.

A collision capsule aligned along the Z axis.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Verse.org/SceneGraph }` |

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `collision_volume`:

| Name | Description |
| --- | --- |
| [`collision_volume`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_volume) | Collision Volumes represent the collision shapes of meshes. They can be detected by Overlap and Sweep queries and generate collisions in the physics simulation. |
| [`collision_element`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_element) | Base class for collision_volumes that consist of a single volume with a single collision_profile and collision_material for the whole volume. This covers most volume types used in queries and physics, except compound types like a mesh. A query will always return an element rather than a general volume. For example when colliding with a mesh, the element will be a collision_triangle, which is a collision_element and has a single material, rather than a collision_triangle_mesh, which is not an element and has a material palette. |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `Collidable` | `?logic` | Enable/disable collision on this volume. |
| `CollisionProfile` | `?collision_profile` | The collision_profile for this volume. |
| `Length` | `?float` | The length of the capsule's cylindrical section (distance between the two end cap centers) |
| `Queryable` | `?logic` | Enable/disable spatial queries against this volume. |
| `Radius` | `?float` | The radius of the capsule |

### Functions

| Function Name | Description |
| --- | --- |
| [`GetLocalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_volume/getlocaltransform) | Get the transform of this volume in the space of its owner (usually a component on an entity) |
| [`SetLocalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_volume/setlocaltransform) | Set the transform of this volume in the space of its owner (usually a component on an entity) |
