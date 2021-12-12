# Pipeline-Work
Final Work for pipeline - One plugin that shares methods with 3 DCC's.

## Supported DCC's:
* Maya
* Houdini
* Nuke

## Dependencies:

* Nuke API
* Houdini API for python 3
* Maya CMDS for python 3
* Pyside2

## Methods: 

`crear_esfera( )`: Adds a polygonal sphere to the scene with a custom name. *Available in: Maya, Houdini, Nuke*

`crear_cubo( )`: Adds a polygonal cube to the scene with a custom name. *Available in: Maya, Houdini, Nuke*

`guardar_escena( )`: Saves the current scene to desired folder and a custom name. *Available in: Maya, Houdini, Nuke*

`guardar_metadata( )`: Saves basic metadata of the scene in a json and saves it in the same folder as the scene. *Available in: Maya, Houdini, Nuke*

`exportar_alembic( )`: Exports the alembic of the scene. Uses Ogawa format as default. *Available in: Maya, Houdini, Nuke*

`crear_video( )`: Creates a video given the path of a folder with an image sequence. Default format is .mov using h.264 codec, 24 frames per second. *Available only in Nuke*
`crear_resumen()`: Creates a txt file with a summary of the files in the directory for production.

## Console functions:

This package can create a simple sphere and save the scene without opening maya though the console(CMD).

How to:
- Open the console (CMD) and navigate to the location of this package in the console
- type: `python esferaCMD.py` 
- Done!, the new scene created will be in the Main folder used by this plugin. 
