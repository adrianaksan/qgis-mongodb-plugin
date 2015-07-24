# QGIS MongoDB Loader

#### Installation

Use the QGIS Plugins menu to install the MongoDB plugin.

#### Description

The MongoDB Loader allows a user to connect to a MongoDB using QGIS.

#### Dependencies

```pymongo, json, ast```

#### Loading Layers

Load MongoDB Layer plugin allows you to quickly and easily load point, linestring and polygon geometry along with the attributes in to a shapefile.
Unlike Mongoconnecter, no additional configuration is required and polygon geometry is loadable. Also, it lets you connect to any accessible external servers without a username/ password.

To load the layer simply type your MongoDB server name, db name, geometry field name and click CONNECT.

Example:

my.server.com.au
geos
geom

If the connection is successful, you should see a list of collections. You will only see collections that have geometry.
To load the collection, simply select the collection and click LOAD.

Additionally:

Under the SETTINGS tab you can also VIEW all of the attribute in your collection.
After viewing your attributes you can select an attribute and click DISTINCT. This will display a list of distinct values for that attribute.
To load your MongoDB layer using a specific attribute simply click SET.

Lastly switch back to the CONNECTION tab, tick the checkbox and select the field from the drop down list to filter what you would like QGIS to LOAD.
	

#### License

qgis-mongodb-plugin is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Copyright © 2010-2014 Pirmin Kalberer & Mathias Walker, Sourcepole AG

