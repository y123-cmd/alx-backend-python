
"""Utilities module with access_nested_map function."""


def access_nested_map(nested_map, path):
    """Accesses a value in a nested dictionary using a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map
