"""Asset commands."""
from .. import bridge

def list_assets(directory: str = "/", recursive: bool = True, class_filter: str = "") -> str:
    """List assets in a directory."""
    params = {"directory": directory, "recursive": recursive}
    if class_filter:
        params["class_filter"] = class_filter
    return str(bridge.send_command("list_assets", params))

def get_asset_info(asset_path: str) -> str:
    """Get detailed info about an asset."""
    return str(bridge.send_command("get_asset_info", {"asset_path": asset_path}))

def get_selected_assets() -> str:
    """Get assets currently selected in the Content Browser."""
    return str(bridge.send_command("get_selected_assets"))

def rename_asset(old_path: str, new_path: str) -> str:
    """Rename or move an asset."""
    return str(bridge.send_command("rename_asset", {"old_path": old_path, "new_path": new_path}))

def delete_asset(asset_path: str) -> str:
    """Delete an asset."""
    return str(bridge.send_command("delete_asset", {"asset_path": asset_path}))

def duplicate_asset(source_path: str, dest_path: str) -> str:
    """Duplicate an asset to a new path."""
    return str(bridge.send_command("duplicate_asset", {"source_path": source_path, "dest_path": dest_path}))

def does_asset_exist(asset_path: str) -> str:
    """Check if an asset exists."""
    return str(bridge.send_command("does_asset_exist", {"asset_path": asset_path}))

def save_asset(asset_path: str) -> str:
    """Save a modified asset."""
    return str(bridge.send_command("save_asset", {"asset_path": asset_path}))

def search_assets(class_name: str = "", directory: str = "/", recursive: bool = True) -> str:
    """Search assets using the Asset Registry."""
    return str(bridge.send_command("search_assets", {"class_name": class_name, "directory": directory, "recursive": recursive}))

def get_project_info() -> str:
    """Get project info."""
    return str(bridge.send_command("get_project_info"))

def save_current_level() -> str:
    """Save the current level."""
    return str(bridge.send_command("save_current_level"))

def get_level_info() -> str:
    """Get level info."""
    return str(bridge.send_command("get_level_info"))

def get_viewport_camera() -> str:
    """Get viewport camera position."""
    return str(bridge.send_command("get_viewport_camera"))

def set_viewport_camera(location: list = None, rotation: list = None) -> str:
    """Set viewport camera position."""
    params = {}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    return str(bridge.send_command("set_viewport_camera", params))
