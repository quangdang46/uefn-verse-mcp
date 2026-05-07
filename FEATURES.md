# Features checklist

Auto-generated inventory of MCP surfaces for **verse-mcp** (FastMCP server + UEFN `uefn_tools`). Update the **Status** column as you verify behavior in-editor.

## Status legend

| Value | Meaning |
| --- | --- |
| Untested | Not verified in this environment |
| Working | Verified OK |
| BUG | Broken or incorrect behavior (note in issue tracker) |

## Native MCP tools (~137)

Exposed directly on the MCP server (`server/main.py` + `server/tools/*.py`). Default status is **Untested**.

### Core tools (server/main.py)

| Tool | Category | Status |
| --- | --- | --- |
| `ping` | System | Untested |
| `get_status` | System | Untested |
| `execute_python` | System | Untested |
| `get_log` | System | Untested |
| `shutdown` | System | Untested |
| `get_all_actors` | Actors | Untested |
| `get_selected_actors` | Actors | Untested |
| `smart_spawn` | Actors | Untested |
| `delete_actors` | Actors | Untested |
| `set_actor_transform` | Actors | Untested |
| `get_actor_properties` | Actors | Untested |
| `set_actor_properties` | Actors | Untested |
| `select_actors` | Actors | Untested |
| `focus_selected` | Actors | Untested |
| `search_content_browser` | Assets | Untested |
| `list_device_aliases` | Devices | Untested |
| `refresh_device_catalog` | Devices | Untested |
| `list_assets` | Assets | Untested |
| `get_asset_info` | Assets | Untested |
| `get_selected_assets` | Assets | Untested |
| `rename_asset` | Assets | Untested |
| `delete_asset` | Assets | Untested |
| `duplicate_asset` | Assets | Untested |
| `does_asset_exist` | Assets | Untested |
| `save_asset` | Assets | Untested |
| `search_assets` | Assets | Untested |
| `get_project_info` | Project / level | Untested |
| `save_current_level` | Project / level | Untested |
| `get_level_info` | Project / level | Untested |
| `get_viewport_camera` | Viewport | Untested |
| `set_viewport_camera` | Viewport | Untested |
| `run_tool` | Escape hatch | Untested |
| `list_tools` | Escape hatch | Untested |
| `describe_tool` | Escape hatch | Untested |

### Extended tools (server/tools/*.py)

| Module | Tool count | Delegate via |
| --- | --- | --- |
| `editor_control` | 4 | `run_tool` |
| `materials` | 6 | `run_tool` |
| `verse` | 18 | `run_tool` |
| `devices` | 10 | `run_tool` |
| `lighting` | 4 | `run_tool` |
| `audio` | 3 | `run_tool` |
| `organization` | 9 | `run_tool` |
| `blueprints` | 3 | `run_tool` |
| `landscape` | 3 | `run_tool` |
| `vfx` | 3 | `run_tool` |
| `capture` | 6 | `run_tool` |
| `optimization` | 6 | `run_tool` |
| `sequencer` | 2 | `run_tool` |
| `procedural` | 5 | `run_tool` |
| `bulk_ops` | 5 | `run_tool` |
| `postprocess` | 2 | `run_tool` |
| `world` | 5 | `run_tool` |
| `text` | 3 | `run_tool` |
| `utility` | 10 | `run_tool` |

## `run_tool` registry (357)

Registered `uefn_tools` entries (invoke via MCP `run_tool` or `list_tools` / `describe_tool`). `registry.py` is excluded from discovery (documentation-only decorator examples).

| Tool | Category | Status |
| --- | --- | --- |
| `actor_attach_to_parent` | Actor Organization | Untested |
| `actor_chain_place` | Proximity Tools | Untested |
| `actor_cluster_to_folder` | Proximity Tools | Untested |
| `actor_copy_to_positions` | Proximity Tools | Untested |
| `proximity_find` | Proximity Tools | Untested |
| `actor_detach` | Actor Organization | Untested |
| `actor_duplicate_offset` | Proximity Tools | Untested |
| `actor_folder_list` | Actor Organization | Untested |
| `actor_hide` | Visibility | Untested |
| `actor_isolate` | Visibility | Untested |
| `actor_lock` | Visibility | Untested |
| `actor_match_transform` | Actor Organization | Untested |
| `actor_set_label` | Actor Organization | Untested |
| `actor_move_to_folder` | Actor Organization | Untested |
| `actor_move_to_root` | Actor Organization | Untested |
| `actor_place_next_to` | Proximity Tools | Untested |
| `actor_rename_folder` | Actor Organization | Untested |
| `actor_replace_class` | Proximity Tools | Untested |
| `actor_select_by_class` | Actor Organization | Untested |
| `actor_select_by_folder` | Actor Organization | Untested |
| `actor_select_same_folder` | Actor Organization | Untested |
| `actor_show` | Visibility | Untested |
| `actor_show_all` | Visibility | Untested |
| `actor_unlock` | Visibility | Untested |
| `align_to_grid_two_points` | Alignment | Untested |
| `align_to_reference` | Alignment | Untested |
| `align_to_surface` | Alignment | Untested |
| `anim_create_montage` | Animation | Untested |
| `anim_list_blend_spaces` | Animation | Untested |
| `anim_list_montages` | Animation | Untested |
| `anim_list_sequences` | Animation | Untested |
| `anim_list_skeletons` | Animation | Untested |
| `api_crawl_level_classes` | API Explorer | Untested |
| `api_crawl_selection` | API Explorer | Untested |
| `api_export_full` | API Explorer | Untested |
| `api_generate_stubs` | API Explorer | Untested |
| `api_inspect` | API Explorer | Untested |
| `api_list_subsystems` | API Explorer | Untested |
| `api_search` | API Explorer | Untested |
| `api_sync_master` | API Explorer | Untested |
| `api_verse_get_schema` | Verse Helpers | Untested |
| `api_verse_refresh_schemas` | Verse Helpers | Untested |
| `arena_generate` | Procedural | Untested |
| `audio_list` | Audio | Untested |
| `audio_list_metasounds` | Audio | Untested |
| `audio_list_sound_classes` | Audio | Untested |
| `audio_list_sound_cues` | Audio | Untested |
| `audio_list_sound_mixes` | Audio | Untested |
| `audio_list_synesthesia` | Audio | Untested |
| `audio_place` | Audio | Untested |
| `audio_set_radius` | Audio | Untested |
| `audio_set_volume` | Audio | Untested |
| `blueprint_audit` | Blueprints | Untested |
| `blueprint_compile_folder` | Blueprints | Untested |
| `blueprint_inspect` | Blueprints | Untested |
| `blueprint_list` | Blueprints | Untested |
| `bulk_align` | Bulk Ops | Untested |
| `bulk_distribute` | Bulk Ops | Untested |
| `bulk_face_camera` | Bulk Ops | Untested |
| `bulk_mirror` | Bulk Ops | Untested |
| `bulk_normalize_scale` | Bulk Ops | Untested |
| `bulk_randomize` | Bulk Ops | Untested |
| `bulk_reset` | Bulk Ops | Untested |
| `bulk_snap_to_grid` | Bulk Ops | Untested |
| `bulk_stack` | Bulk Ops | Untested |
| `config_get` | Utilities | Untested |
| `config_list` | Utilities | Untested |
| `config_reset` | Utilities | Untested |
| `config_set` | Utilities | Untested |
| `convert_to_hism` | Optimization | Untested |
| `cooker_mark_batch` | Optimization | Untested |
| `cooker_mark_selection` | Optimization | Untested |
| `cooker_open` | Optimization | Untested |
| `cooker_scan` | Optimization | Untested |
| `cooker_unmark_all` | Optimization | Untested |
| `core_safety_audit` | System | Untested |
| `curve_create` | Curves | Untested |
| `curve_export` | Curves | Untested |
| `curve_inspect` | Curves | Untested |
| `curve_list` | Curves | Untested |
| `data_layer_assign_selection` | World Partition | Untested |
| `data_layer_create` | World Partition | Untested |
| `data_layer_list` | World Partition | Untested |
| `datatable_audit` | DataTable | Untested |
| `datatable_export` | DataTable | Untested |
| `datatable_inspect` | DataTable | Untested |
| `datatable_list` | DataTable | Untested |
| `datatable_row_names` | DataTable | Untested |
| `debug_audit_verse_assets` | Utilities | Untested |
| `debug_dump_verse_actor` | Utilities | Untested |
| `device_call_method` | Verse Helpers | Untested |
| `device_catalog_scan` | API Explorer | Untested |
| `device_set_property` | Verse Helpers | Untested |
| `distribute_with_gap` | Alignment | Untested |
| `entity_list_kits` | Entities | Untested |
| `entity_spawn_kit` | Entities | Untested |
| `folder_hide` | Visibility | Untested |
| `folder_show` | Visibility | Untested |
| `foliage_audit_brushes` | Environmental | Untested |
| `foliage_convert_selected_to_actor` | Environmental | Untested |
| `geometry_boolean_intersect` | Geometry | Untested |
| `geometry_boolean_subtract` | Geometry | Untested |
| `geometry_boolean_union` | Geometry | Untested |
| `geometry_compute_normals` | Geometry | Untested |
| `geometry_fill_holes` | Geometry | Untested |
| `geometry_generate_lightmap_uvs` | Geometry | Untested |
| `geometry_remove_degenerate` | Geometry | Untested |
| `geometry_weld_edges` | Geometry | Untested |
| `import_fbx` | Assets | Untested |
| `import_fbx_folder` | Assets | Untested |
| `import_image_from_clipboard` | Pipeline | Untested |
| `import_image_from_url` | Pipeline | Untested |
| `input_create_action` | Enhanced Input | Untested |
| `input_inspect_context` | Enhanced Input | Untested |
| `input_list_actions` | Enhanced Input | Untested |
| `input_list_contexts` | Enhanced Input | Untested |
| `label_attach` | Text & Signs | Untested |
| `landscape_audit` | Landscape | Untested |
| `landscape_info` | Landscape | Untested |
| `landscape_list` | Landscape | Untested |
| `landscape_set_material` | Landscape | Untested |
| `level_health_open` | Utilities | Untested |
| `level_health_report` | Utilities | Untested |
| `light_cinematic_preset` | Lighting | Untested |
| `light_list` | Lighting | Untested |
| `light_place` | Lighting | Untested |
| `light_randomize_sky` | Lighting | Untested |
| `light_set` | Lighting | Untested |
| `lod_audit_folder` | Assets | Untested |
| `lod_auto_generate_folder` | Assets | Untested |
| `lod_auto_generate_selection` | Assets | Untested |
| `lod_set_collision_folder` | Assets | Untested |
| `match_spacing` | Alignment | Untested |
| `material_apply_preset` | Materials | Untested |
| `material_bulk_swap` | Materials | Untested |
| `material_color_harmony` | Materials | Untested |
| `material_glow_pulse_preview` | Materials | Untested |
| `material_gradient_painter` | Materials | Untested |
| `material_list_presets` | Materials | Untested |
| `material_parent_audit` | Optimization | Untested |
| `material_pattern_painter` | Materials | Untested |
| `material_randomize_colors` | Materials | Untested |
| `material_save_preset` | Materials | Untested |
| `material_team_color_split` | Materials | Untested |
| `mcp_restart` | MCP Bridge | Untested |
| `mcp_start` | MCP Bridge | Untested |
| `mcp_status` | MCP Bridge | Untested |
| `mcp_stop` | MCP Bridge | Untested |
| `measure_distance` | Measurement | Untested |
| `measure_travel_time` | Measurement | Untested |
| `memory_autofix_lods` | Optimization | Untested |
| `memory_scan` | Optimization | Untested |
| `memory_scan_meshes` | Optimization | Untested |
| `memory_scan_textures` | Optimization | Untested |
| `memory_top_offenders` | Optimization | Untested |
| `mesh_merge_selection` | Bulk Ops | Untested |
| `movie_render_apply_preset` | Cinematic | Untested |
| `movie_render_queue_sequence` | Cinematic | Untested |
| `movie_render_status` | Cinematic | Untested |
| `nanite_audit` | Static Meshes | Untested |
| `nanite_enable_folder` | Static Meshes | Untested |
| `nanite_enable_selection` | Static Meshes | Untested |
| `niagara_bulk_set_parameter` | VFX | Untested |
| `niagara_clear_systems` | VFX | Untested |
| `niagara_list_systems` | VFX | Untested |
| `niagara_spawn_system` | VFX | Untested |
| `organize_assets` | Assets | Untested |
| `organize_open` | Project | Untested |
| `organize_smart_categorize` | Project | Untested |
| `pattern_arc` | Prop Patterns | Untested |
| `pattern_circle` | Prop Patterns | Untested |
| `pattern_clear` | Prop Patterns | Untested |
| `pattern_grid` | Prop Patterns | Untested |
| `pattern_helix` | Prop Patterns | Untested |
| `pattern_line` | Prop Patterns | Untested |
| `pattern_radial_rows` | Prop Patterns | Untested |
| `pattern_spiral` | Prop Patterns | Untested |
| `pattern_wave` | Prop Patterns | Untested |
| `pcg_execute_graph` | Procedural | Untested |
| `pcg_list_graphs` | Procedural | Untested |
| `pcg_refresh_all` | Procedural | Untested |
| `pcg_set_seed` | Procedural | Untested |
| `physics_add` | Physics | Untested |
| `physics_list` | Physics | Untested |
| `physics_remove` | Physics | Untested |
| `plugin_export_manifest` | Utilities | Untested |
| `plugin_list_custom` | Utilities | Untested |
| `plugin_validate_all` | Utilities | Untested |
| `postprocess_preset` | Post-Process | Untested |
| `postprocess_set` | Post-Process | Untested |
| `postprocess_spawn` | Post-Process | Untested |
| `prefab_export_to_disk` | Asset Management | Untested |
| `prefab_export_within_project` | Asset Management | Untested |
| `prefab_parse_refs` | Asset Management | Untested |
| `prefab_resolve_deps` | Asset Management | Untested |
| `procedural_volume_scatter` | Procedural | Untested |
| `procedural_wire_create` | Procedural | Untested |
| `project_setup` | Project Admin | Untested |
| `publish_audit` | Project Admin | Untested |
| `ref_audit_duplicates` | Reference Auditor | Untested |
| `ref_audit_orphans` | Reference Auditor | Untested |
| `ref_audit_redirectors` | Reference Auditor | Untested |
| `ref_audit_unused_textures` | Reference Auditor | Untested |
| `ref_delete_orphans` | Reference Auditor | Untested |
| `ref_fix_redirectors` | Reference Auditor | Untested |
| `ref_full_report` | Reference Auditor | Untested |
| `rename_dry_run` | Assets | Untested |
| `rename_enforce_conventions` | Assets | Untested |
| `rename_report` | Assets | Untested |
| `rename_strip_prefix` | Assets | Untested |
| `rogue_actor_scan` | Optimization | Untested |
| `rotate_around_pivot` | Alignment | Untested |
| `save_all_dirty` | Project Admin | Untested |
| `scaffold_delete_template` | Project | Untested |
| `scaffold_generate` | Project | Untested |
| `scaffold_list_templates` | Project | Untested |
| `scaffold_organize_loose` | Project | Untested |
| `scaffold_preview` | Project | Untested |
| `scaffold_save_template` | Project | Untested |
| `scatter_along_path` | Procedural | Untested |
| `scatter_avoid` | Procedural | Untested |
| `scatter_clear` | Procedural | Untested |
| `scatter_export_manifest` | Procedural | Untested |
| `scatter_hism` | Procedural | Untested |
| `scatter_props` | Procedural | Untested |
| `scatter_road_edge` | Procedural | Untested |
| `screenshot_focus_selection` | Screenshot | Untested |
| `screenshot_open_folder` | Screenshot | Untested |
| `screenshot_take` | Screenshot | Untested |
| `screenshot_timed_series` | Screenshot | Untested |
| `select_by_property` | Selection | Untested |
| `select_by_verse_tag` | Selection | Untested |
| `select_in_radius` | Selection | Untested |
| `selection_list` | Selection | Untested |
| `selection_restore` | Selection | Untested |
| `selection_save` | Selection | Untested |
| `seq_actor_to_spline` | Sequencer | Untested |
| `seq_batch_keyframe` | Sequencer | Untested |
| `sign_batch_edit` | Text & Signs | Untested |
| `sign_batch_rename` | Text & Signs | Untested |
| `sign_batch_set_text` | Text & Signs | Untested |
| `sign_clear` | Text & Signs | Untested |
| `sign_list` | Text & Signs | Untested |
| `sign_spawn_bulk` | Text & Signs | Untested |
| `sim_generate_proxy` | Simulation | Untested |
| `sim_trigger_method` | Simulation | Untested |
| `skel_audit` | Skeletal Mesh | Untested |
| `skel_list` | Skeletal Mesh | Untested |
| `skel_list_sockets` | Skeletal Mesh | Untested |
| `skel_set_physics_asset` | Skeletal Mesh | Untested |
| `sky_set_time` | Lighting | Untested |
| `smoke_test` | Utilities | Untested |
| `snapshot_compare_live` | Level Snapshot | Untested |
| `snapshot_delete` | Level Snapshot | Untested |
| `snapshot_diff` | Level Snapshot | Untested |
| `snapshot_export` | Level Snapshot | Untested |
| `snapshot_import` | Level Snapshot | Untested |
| `snapshot_list` | Level Snapshot | Untested |
| `snapshot_restore` | Level Snapshot | Untested |
| `snapshot_save` | Level Snapshot | Untested |
| `sound_asset_audit` | Sound Assets | Untested |
| `sound_asset_list` | Sound Assets | Untested |
| `sound_attenuation_list` | Sound Assets | Untested |
| `sound_class_list` | Sound Assets | Untested |
| `spline_clear_props` | Procedural | Untested |
| `spline_export_json` | Verse Helpers | Untested |
| `spline_measure` | Measurement | Untested |
| `spline_place_props` | Procedural | Untested |
| `spline_to_verse_patrol` | Verse Helpers | Untested |
| `spline_to_verse_points` | Verse Helpers | Untested |
| `spline_to_verse_zone_boundary` | Verse Helpers | Untested |
| `stamp_delete` | Stamps | Untested |
| `stamp_export` | Stamps | Untested |
| `stamp_import` | Stamps | Untested |
| `stamp_info` | Stamps | Untested |
| `stamp_list` | Stamps | Untested |
| `stamp_place` | Stamps | Untested |
| `stamp_save` | Stamps | Untested |
| `system_backup_project` | Project Admin | Untested |
| `system_build_verse` | System | Untested |
| `system_get_last_build_log` | System | Untested |
| `system_optimize_background_cpu` | System | Untested |
| `system_perf_audit` | Project Admin | Untested |
| `tag_add` | Asset Tagger | Untested |
| `tag_export` | Asset Tagger | Untested |
| `tag_list_all` | Asset Tagger | Untested |
| `tag_remove` | Asset Tagger | Untested |
| `tag_search` | Asset Tagger | Untested |
| `tag_show` | Asset Tagger | Untested |
| `text_apply_translation` | Localization | Untested |
| `text_clear_folder` | Text & Signs | Untested |
| `text_color_cycle` | Text & Signs | Untested |
| `text_export_manifest` | Localization | Untested |
| `text_label_selection` | Text & Signs | Untested |
| `text_list_styles` | Text & Signs | Untested |
| `text_paint_grid` | Text & Signs | Untested |
| `text_place` | Text & Signs | Untested |
| `text_render_texture` | Generative | Untested |
| `text_save_style` | Text & Signs | Untested |
| `text_voxelize_3d` | Generative | Untested |
| `texture_apply_preset` | Textures | Untested |
| `texture_audit` | Textures | Untested |
| `texture_set_compression` | Textures | Untested |
| `texture_set_group` | Textures | Untested |
| `texture_set_srgb` | Textures | Untested |
| `theme_get` | Utilities | Untested |
| `theme_list` | Utilities | Untested |
| `theme_set` | Utilities | Untested |
| `toolbelt_activity_clear` | System | Untested |
| `toolbelt_activity_log` | System | Untested |
| `toolbelt_activity_stats` | System | Untested |
| `toolbelt_integration_test` | Tests | Untested |
| `ui_icon_import_file` | Asset Management | Untested |
| `ui_icon_import_open` | Asset Management | Untested |
| `uv_add_channel` | Static Meshes | Untested |
| `uv_generate_box` | Static Meshes | Untested |
| `uv_generate_planar` | Static Meshes | Untested |
| `uv_list_channels` | Static Meshes | Untested |
| `verse_build_status` | System | Untested |
| `verse_bulk_set_property` | Verse Helpers | Untested |
| `verse_export_report` | Verse Helpers | Untested |
| `verse_find_project_path` | Verse Helpers | Untested |
| `verse_gen_custom` | Verse Helpers | Untested |
| `verse_gen_device_declarations` | Verse Helpers | Untested |
| `verse_gen_elimination_handler` | Verse Helpers | Untested |
| `verse_gen_game_skeleton` | Verse Helpers | Untested |
| `verse_gen_prop_spawner` | Verse Helpers | Untested |
| `verse_gen_scoring_tracker` | Verse Helpers | Untested |
| `verse_list_devices` | Verse Helpers | Untested |
| `verse_list_snippets` | Verse Helpers | Untested |
| `verse_open_snippets_folder` | Verse Helpers | Untested |
| `verse_patch_errors` | System | Untested |
| `verse_select_by_class` | Verse Helpers | Untested |
| `verse_select_by_name` | Verse Helpers | Untested |
| `verse_template_deploy` | Verse Helpers | Untested |
| `verse_template_get` | Verse Helpers | Untested |
| `verse_template_list` | Verse Helpers | Untested |
| `verse_write_file` | Verse Helpers | Untested |
| `viewport_bookmark_jump` | Viewport | Untested |
| `viewport_bookmark_list` | Viewport | Untested |
| `viewport_bookmark_save` | Viewport | Untested |
| `viewport_camera_get` | Viewport | Untested |
| `viewport_focus_actor` | Viewport | Untested |
| `viewport_goto` | Viewport | Untested |
| `viewport_move_to_camera` | Viewport | Untested |
| `viewport_showflag` | Viewport | Untested |
| `viewport_orbit` | Viewport | Untested |
| `world_partition_status` | World Partition | Untested |
| `world_settings_set` | Post-Process | Untested |
| `world_state_export` | API Explorer | Untested |
| `zone_fill_scatter` | Zone Tools | Untested |
| `zone_list` | Zone Tools | Untested |
| `zone_move_contents` | Zone Tools | Untested |
| `zone_resize_to_selection` | Zone Tools | Untested |
| `zone_select_contents` | Zone Tools | Untested |
| `zone_snap_to_selection` | Zone Tools | Untested |
| `zone_spawn` | Zone Tools | Untested |

---

Regenerate: `python scripts/gen_features_md.py`
