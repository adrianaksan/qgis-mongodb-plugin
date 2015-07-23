# QGIS MongoDB Loader

#### Description

The MongoDB Loader allows a user to connect to a MongoDB using QGIS.

#### Modify the GUI

- Download: [QT Creator](http://qt-project.org/downloads "QT Creator")


- Open the ```loadMongoDB_dialog_base.ui``` file using the QT creator


- Make the necessary changes to the GUI using the tool


- Open the terminal and use the following code to convert the .ui to a .py

	```pyuic4 -o ui_loadMongoDB_dialog_base.py loadMongoDB_dialog_base.ui```
	
	(If the ```pyuic4``` does not work, run ```brew install pyqt``` in the terminal)

#### Dependencies

```pymongo, json, ast```

