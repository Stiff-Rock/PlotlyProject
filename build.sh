#!/bin/bash

# Clean previous build files
echo "Cleaning previous builds..."
rm -rf build/
rm -rf dist/
rm -f *.spec

# Run PyInstaller
echo "Running PyInstaller..."
pyinstaller -w -F --add-data "app/templates:templates" --add-data "app/static:static" run.py

echo "Build complete!"
