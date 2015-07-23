# QGIS MongoDB Loader

#### Installation

Use the QGIS Plugins menu to install the MongoDB plugin.

#### Description

The MongoDB Loader allows a user to connect to a MongoDB using QGIS.

#### Dependencies

```pymongo, json, ast```

#### Modify the GUI

- Download: [QT Creator](http://qt-project.org/downloads "QT Creator")


- Open the ```loadMongoDB_dialog_base.ui``` file using the QT creator


- Make the necessary changes to the GUI using the tool


- Open the terminal and use the following code to convert the .ui to a .py

	```pyuic4 -o ui_loadMongoDB_dialog_base.py loadMongoDB_dialog_base.ui```
	
	(If the ```pyuic4``` does not work, run ```brew install pyqt``` in the terminal)
	

#### License

qgis-mongodb-plugin is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Copyright © 2010-2014 Pirmin Kalberer & Mathias Walker, Sourcepole AG

