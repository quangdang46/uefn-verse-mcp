"""Material tools — create instances, apply presets, swap, list."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register material tools on the MCP server."""

    @mcp.tool()
    def create_material_instance(
        parent_path: Annotated[str, Field(description="Content path to the parent Material (e.g. '/Game/Materials/M_Master').")],
        instance_name: Annotated[str, Field(description="Name for the new MaterialInstanceConstant asset.")],
        destination: Annotated[str, Field(description="Content Browser folder for the new MI.")] = "/Game/Materials",
        scalar_params: Annotated[Optional[dict], Field(description="Scalar parameters {name: float} e.g. {'Roughness': 0.2}.")] = None,
        vector_params: Annotated[Optional[dict], Field(description="Vector parameters {name: [r,g,b,a]} e.g. {'BaseColor': [1,0,0,1]}.")] = None,
        texture_params: Annotated[Optional[dict], Field(description="Texture parameters {name: asset_path} e.g. {'DiffuseTex': '/Game/T_Rock'}.")] = None,
    ) -> str:
        """Create a MaterialInstanceConstant from a parent material with optional parameters."""
        params = {
            "parent_path": parent_path,
            "instance_name": instance_name,
            "destination": destination,
        }
        if scalar_params:
            params["scalar_params"] = scalar_params
        if vector_params:
            params["vector_params"] = vector_params
        if texture_params:
            params["texture_params"] = texture_params
        return str(bridge.send_command("create_material_instance", params))

    @mcp.tool()
    def import_asset(
        source_file: Annotated[str, Field(description="Absolute path to the file to import (FBX, PNG, WAV, etc.).")],
        destination_path: Annotated[str, Field(description="Content Browser destination folder (e.g. '/Game/Meshes').")],
        replace_existing: Annotated[bool, Field(description="Replace existing asset if name collides.")] = True,
        automated: Annotated[bool, Field(description="Skip import dialogs.")] = True,
        save: Annotated[bool, Field(description="Save the imported asset immediately.")] = True,
    ) -> str:
        """Import an external file (FBX, PNG, WAV, etc.) into the Content Browser."""
        return str(bridge.send_command("import_asset", {
            "source_file": source_file,
            "destination_path": destination_path,
            "replace_existing": replace_existing,
            "automated": automated,
            "save": save,
        }))

    @mcp.tool()
    def material_list_presets() -> str:
        """List all saved material presets available for quick application."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "material_list_presets",
            "kwargs": {},
        }))

    @mcp.tool()
    def material_apply_preset(
        preset: Annotated[str, Field(description="Preset name to apply (e.g. 'chrome', 'neon', 'glass').")],
    ) -> str:
        """Apply a material preset to selected actors."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "material_apply_preset",
            "kwargs": {"preset": preset},
        }))

    @mcp.tool()
    def material_bulk_swap(
        old_material: Annotated[str, Field(description="Content path of the material to replace.")],
        new_material: Annotated[str, Field(description="Content path of the replacement material.")],
    ) -> str:
        """Swap materials across all actors in the level that use the old material."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "material_bulk_swap",
            "kwargs": {"old_material": old_material, "new_material": new_material},
        }))

    @mcp.tool()
    def material_randomize_colors(
        saturation: Annotated[float, Field(description="Color saturation 0.0-1.0.")] = 0.8,
        brightness: Annotated[float, Field(description="Color brightness 0.0-1.0.")] = 0.7,
    ) -> str:
        """Randomize material colors on selected actors for quick prototyping."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "material_randomize_colors",
            "kwargs": {"saturation": saturation, "brightness": brightness},
        }))
