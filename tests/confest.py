"""Pytest configuration for abhiprime."""

def pytest_collection_modifyitems(config, items):
    """Remove imported test_prime from test collection."""
    items[:] = [item for item in items 
                if not (hasattr(item, 'name') and item.name == 'test_prime')]