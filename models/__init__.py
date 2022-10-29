#!/usr/bin/python3
"""The __init__ module constructor"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
