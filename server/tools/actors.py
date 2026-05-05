"""Actor commands."""
from server import bridge

def get_all_actors() -> str:
    """Get all actors in the current level."""
    return str(bridge.send_command("get_all_actors"))

def get_selected_actors() -> str:
    """Get currently selected actors."""
    return str(bridge.send_command("get_selected_actors"))

def spawn_actor(class_path: str, location: list = None, rotation: list = None) -> str:
    """Spawn an actor from a class or object path."""
    params = {"class_path": class_path}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    return str(bridge.send_command("spawn_actor", params))

def delete_actors(actor_labels: list) -> str:
    """Delete actors by their labels."""
    return str(bridge.send_command("delete_actors", {"actor_labels": actor_labels}))

def set_actor_transform(actor_label: str, location: list = None, rotation: list = None, scale: list = None) -> str:
    """Set actor transform (location, rotation, scale)."""
    params = {"actor_label": actor_label}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    if scale:
        params["scale"] = scale
    return str(bridge.send_command("set_actor_transform", params))

def get_actor_properties(actor_label: str) -> str:
    """Get properties of an actor."""
    return str(bridge.send_command("get_actor_properties", {"actor_label": actor_label}))

def set_actor_properties(actor_label: str, properties: dict) -> str:
    """Set properties of an actor."""
    return str(bridge.send_command("set_actor_properties", {"actor_label": actor_label, "properties": properties}))

def select_actors(actor_labels: list) -> str:
    """Select actors in the viewport."""
    return str(bridge.send_command("select_actors", {"actor_labels": actor_labels}))

def focus_selected() -> str:
    """Focus the viewport on selected actors."""
    return str(bridge.send_command("focus_selected"))
