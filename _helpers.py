"""
Shared helper for the test files in this directory.

The exercise files are named like "01_find_largest.py" — a leading
digit makes that an invalid Python identifier, so they can't be
imported with a normal `import` statement. load_module() loads them
by file path instead.
"""

import importlib.util
import pathlib


def load_module(filename: str):
    """Load and execute filename (relative to this directory) as a module."""
    path = pathlib.Path(__file__).parent / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
