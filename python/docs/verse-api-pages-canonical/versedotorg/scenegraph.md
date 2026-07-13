## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/scenegraph

# SceneGraph module

Learn technical details about the SceneGraph module.

- [`Verse.org`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg)
- **`SceneGraph`**

  - [`KeyframedMovement`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/keyframedmovement)
  - [`CollisionChannels`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collisionchannels)
  - [`CollisionProfiles`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collisionprofiles)

## Classes and Structs

| Name | Description |
| --- | --- |
| [`basic_interactable_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/basic_interactable_component) | An interactable component with a composable feature set. |
| [`interactable_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_component) | Used to handle general interaction. |
| [`interactable_cooldown`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_cooldown) | Used to set a cooldown when interacted. |
| [`interactable_cooldown_per_agent`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_cooldown_per_agent) | Used to set a cooldown per agent when interacted. |
| [`interactable_duration`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_duration) | Used to set an interaction duration. |
| [`interactable_success_limit`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_success_limit) | Used to set a limit of times to interact. |
| [`camera_body`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_body) | Camera body settings, e.g. sensor/film settings, shutter speed, etc |
| [`camera_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_component) | Represents the physical body, lens of the camera and other cinematographic qualities, such as sensor size, aspect ratio lock/constraint, focal length, focus distance, post-process settings, etc. |
| [`camera_director_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_director_component) | Responsible for selecting a camera and blending when the active camera changes. Also allows global settings to be shared between different cameras (such as post process settings) and modifications to the final blended camera state, such as camera shakes |
| [`camera_lens`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_lens) | Camera lens settings |
| [`camera_modifier_stack`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_modifier_stack) | Modifier stack for camera state. |
| [`camera_modifier`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_modifier) | Base class for objects that can modify camera state. |
| [`camera_state`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_state) |  |
| [`camera_transition`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_transition) | Controls how a camera mode transitions to another |
| [`camera_mode_blend`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_mode_blend) | Configurable blend between two camera modes |
| [`camera_mode_blend_pop`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_mode_blend_pop) | Instantly snap to target mode |
| [`camera_mode_blend_linear`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_mode_blend_linear) | Linear blend between camera modes |
| [`camera_mode_blend_smoothstep`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_mode_blend_smoothstep) | Camera mode blend that uses the smoothstep function to blend between the two camera modes |
| [`camera_mode_blend_smootherstep`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_mode_blend_smootherstep) | Camera mode blend that uses the smootherstep function to blend between the two camera modes |
| [`camera_mode_blend_orbit`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_mode_blend_orbit) | Configurable blend between two camera modes |
| [`orthographic_camera_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/orthographic_camera_component) | Simple orthographic camera. |
| [`perspective_camera_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/perspective_camera_component) | Simple perspective camera. |
| [`physical_camera_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/physical_camera_component) | Camera that is physically based, determining its view properties in a manner more consistent with a physical camera |
| [`skeletal_animation`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/skeletal_animation) | A modifier of skeletons, used to animate meshes using skeletal animation |
| [`play_skeletal_animation_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/play_skeletal_animation_result) |  |
| [`skeleton`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/skeleton) | Skeletons are collections of bones & sets/chains |
| [`easing_window`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/easing_window) | An easing function combined with a relative time window |
| [`capsule_light_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/capsule_light_component) | A `capsule_light_component` emits light in all directions into the scene from a capsule shaped source with a specified radius and length. A radius and length of 0 makes it a point light. You can use these to simulate any kind of light sources that emit in all directions and need an elongated source shape, such as a long light bulb. |
| [`directional_light_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/directional_light_component) | A `directional_light_component` simulates light that is being emitted from a source that is infinitely far away. This means that all shadows cast by this light will be parallel, making this the ideal choice for simulating sunlight. |
| [`light_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/light_component) | Base class for light components in the SceneGraph.  Dependencies:   - `transform_component` on the entity positions the light.   Examples of components implementing `light_component`:   - `directional_light_component` - `capsule_light_component` - `sphere_light_component` - `rect_light_component` - `spot_light_component` |
| [`mesh_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/mesh_component) | Used to render a `mesh` at the location of this entity. A mesh is a set of polygons that can be used to represent shapes in the world such as:   - foliage and terrain decorations - movers (for example, doors and lifts) - procedurally created buildings   Dependencies:   - `transform_component` on the entity positions the mesh. |
| [`particle_system_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/particle_system_component) | Used to spawn a `particle_system` at the location of this entity. The `particle_system` will simulate while the `particle_system_component` is in the scene.  Dependencies:   - `transform_component` on the entity positions the `particle_system`. |
| [`possessable_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/possessable_component) | Marks an entity that can be possessed by an agent. |
| [`rect_light_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/rect_light_component) | A `rect_light_component` emits light into the scene from a rectangular plane with a specified width and height. You can use these to simulate any kind of light sources that have rectangular areas, such as televisions or monitor screens, overhead lighting fixtures, or wall sconces. |
| [`sound_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/sound_component) |  |
| [`sphere_light_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/sphere_light_component) | A `sphere_light_component` emits light in all directions into the scene from a spherical source shape with a specified radius. A radius of 0 makes it a point light. You can use these to simulate any kind of light sources that emit in all directions, such as a light bulb. |
| [`spot_light_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/spot_light_component) | A `spot_light_component` emits light from a single point in a cone shape. The shape of the light is defined by two cones: the `InnerConeAngleDegrees` and `OuterConeAngleDegrees`. Within the `InnerConeAngleDegrees` the light achieves full brightness. As you go from the extent of the inner radius to the extents of the `OuterConeAngleDegrees` a falloff takes place, creating a penumbra, or softening around the `spot_light_component`'s disc of illumination. The Radius of the light defines the length of the cones. More simply, this will work like a flash light or stage can light. |
| [`float_range`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/float_range) | A range with a minimum and maximum value. For a value to fall inside of this range, the min value must be less than or equal to the max value. |
| [`collision_channel`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_channel) | Every volume has a collision channel as part of its collision_profile. It is used to determine how two volumes interact. See collision_profile. |
| [`collision_profile`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_profile) | A collision profile determines how a volume interacts with other volumes for Overlap queries, Sweep queries, and physics simulation. When two volumes are being tested to see how they interact, the algorithm looks like this: GetInteraction(A:collision_profile, B:collision_profile):collision_interaction = InteractionA = B.GetChannelInteraction(A.Channel) InteractionB = A.GetChannelInteraction(B.Channel) return Min(InteractionA, InteractionB) |
| [`overlap_hit`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/overlap_hit) | The results of an overlap query. See entity.FindOverlapHits(). We will get one overlap_hit for each intersection of any volume in SourceVolumes with any other volume. |
| [`sweep_hit`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/sweep_hit) | The results of a sweep query. See entity.FindSweepHits(). We will get one sweep_hit for each intersection of any volume in SourceVolumes with any other volume. |
| [`collision_volume`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_volume) | Collision Volumes represent the collision shapes of meshes. They can be detected by Overlap and Sweep queries and generate collisions in the physics simulation. |
| [`collision_element`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_element) | Base class for collision_volumes that consist of a single volume with a single collision_profile and collision_material for the whole volume. This covers most volume types used in queries and physics, except compound types like a mesh. A query will always return an element rather than a general volume. For example when colliding with a mesh, the element will be a collision_triangle, which is a collision_element and has a single material, rather than a collision_triangle_mesh, which is not an element and has a material palette. |
| [`collision_capsule`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_capsule) | A collision capsule aligned along the Z axis. |
| [`collision_sphere`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_sphere) | A collision sphere. |
| [`collision_point`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_point) | A collision point. |
| [`collision_box`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_box) | An axis-aligned collision box. |
| [`component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component) | Base class for authoring logic and data in the SceneGraph. Using components you can author re-usable building blocks of logic and data which can then be added to entities in the scene.  Components are a very low level building block which can be used in many ways. For example:   - Exposing engine level concepts like mesh or sound - Adding gameplay capabilities like damage or interaction - Storing an inventory for a character in the game   As components are generic there is no specific way that they must be used. It is up to the needs of your experience if you use one big game component or if you break up logic into many small components.  Classes deriving from component must also specify `<final_super>` to be added to entities. This ensures the class will always derive directly from `component`. Further subclassing of the initial derived component is allowed and does not require specifying `<final_super>` on the derived classes.  Only one instance of a component from each subclass group can be added to an entity at a time. For example, given this group of components, only one light_component can exist on a single entity. To create multiple lights you should use multiple entities.  light_component := class(component){} capsule_light_component := class(light_component){} directional_light_component := class(light_component){} spot_light_component := class(light_component){} sphere_light_component := class(light_component){} rect_light_component := class(light_component){}  ============================================================================== Component Lifetime  Components move through a series of lifetime functions as they are added to entities, added to the scene, and begin running in the simulation. Components should override these methods to perform setup and run their simulation.  As a component shuts down it will then move through shutdown version of these functions, giving users the opportunity to clean up any retained state on the component before it is disposed . Lifetime Methods: OnAddedToScene OnBeginSimulation -> OnSimulate OnEndSimulation OnRemovingFromScene ============================================================================== |
| [`entity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity) | Entities are the base object in the SceneGraph.   - Objects in experiences are constructed of one or more entities. - Entities are hierarchical. You can query your parent using `GetParent` and add child entities using `AddEntities`. - Behavior is added to entities through `component`s. You can add new components using `AddComponents`. - The structure and content of entities is dynamic and be changed at any time through your experience. Deriving from entity   In the SceneGraph system a class that derives from `entity` is also known as a prefab. Prefabs are useful when you want to spawn/re-use a collection of entities and components many times within your game. Primarily prefabs are authored through the editor, with their Verse classes generated as part of the build into the projects Assets.digest.verse file.  While you can create base prefabs for common game object types like a vehicle or character, we highly recommended that you do not add code directly to the entity class, and instead keep logic in components. Keeping logic and data in components allows you to restructure your prefabs throughout production of your experience, without needing to massively refactor your class structure. |
| [`entity_prefab`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity_prefab) | Reference type to editor defined prefab. Only generated digest code should reference this type. |
| [`icon_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/icon_component) | Component that holds an icon for an entity. |
| [`entity_origin`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity_origin) | class to provide alternative origin to the 'transform_component' as an entity |
| [`rarity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/rarity) | Rarity may be used by gameplay and presentation systems to classify and rank things. |
| [`common_rarity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/common_rarity) |  |
| [`uncommon_rarity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/uncommon_rarity) |  |
| [`rare_rarity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/rare_rarity) |  |
| [`epic_rarity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/epic_rarity) |  |
| [`legendary_rarity`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/legendary_rarity) |  |
| [`rarity_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/rarity_component) | Component that denotes the rarity of an entity. |
| [`stackable_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/stackable_component) | A component that when attached to an entity allows for it to merge or 'stack' with other entities with compatible components. |
| [`change_stack_size_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/change_stack_size_result) |  |
| [`change_max_stack_size_result`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/change_max_stack_size_result) |  |
| [`basic_stackable_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/basic_stackable_component) |  |
| [`tick_events`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/tick_events) | Describes discrete phases of a frame update. Subscribe to members of the tick_events object to run code before or after the physics system has updated your object, allowing you to affect or react to these updates. |
| [`transform_component`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/transform_component) | Stores the transforms for an entity, which are used to position the entity. |
| [`execution_listenable`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/execution_listenable) | Users to subscribe to, or await on, a DeltaTime based callback from one of the phases in a component's `TickEvents` object. |

## Interfaces

| Name | Description |
| --- | --- |
| [`has_camera_modifier`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/has_camera_modifier) | Interface for classes that own a camera modifier stack. |
| [`easeable`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/easeable) | Interface used to trigger easing behaviors |
| [`scene_event`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/scene_event) | An event which can be sent through the scene graph. |
| [`origin`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/origin) | Interface to provide alternative origin to an entity which is defaulted to its parent. See `transform_component` |
| [`has_merge_rules`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/has_merge_rules) | Merge Rules Interface. Implemented by components that want to participate in entity mergeability checks. |

## Enumerations

| Name | Description |
| --- | --- |
| [`camera_projection_mode`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_projection_mode) |  |

|  |  |
| --- | --- |
| [`camera_transition_initial_orientation`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_transition_initial_orientation) | Controls how a camera mode transitions to another |

|  |  |
| --- | --- |
| [`entity_streaming_policy`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity_streaming_policy) | Entity client streaming modes |

|  |  |
| --- | --- |
| [`children_streaming_policy`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/children_streaming_policy) | Child entities client streaming modes |

|  |  |
| --- | --- |
| [`collision_interaction`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_interaction) | Specifies how a collision volume pair should interact. See collision_profile. |

## Data

| Name | Description |
| --- | --- |
| `GlobalModifierPosition` |  |

|  |  |
| --- | --- |
| `VisualModifierPosition` |  |
