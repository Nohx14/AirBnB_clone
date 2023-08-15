#!/usr/bin/env python3
"""
the __init__ file indicating a python package
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
