#!/bin/sh
# ###
# Build using the PyInstaller.
#  * Recommended way for kivy
#  * Builds only for the current system
#    * i.e. need a sort-of buildfarm to build for multiple target platforms.
#    * Packs the current system's libraries.
#  * Relies on automatic dependencies detection.
#    * Can pack too much. Maybe needs tweaking.
# ###

set -e

# # Simple example (doesn't support Cython):
# python -m PyInstaller \
#   --name example_app_kivypkgtpl \
#   kivypkgtplapp/main.py \
#   "$@"

rm -r dist/example_app_kivypkgtpl || true

python -m PyInstaller example_app_kivypkgtpl.spec "$@"
