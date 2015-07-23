# QGIS MongoDB Loader

#### Installation

Use the QGIS Plugins menu to install the MongoDB plugin.

#### Description

The MongoDB Loader allows a user to connect to a MongoDB using QGIS.

#### Dependencies

```pymongo, json, ast```

#### Loading Layers

The Load MongoDB Layer plugin allows you to quickly and easily load Point, Linestring and Polygon geometry and their attributes into a shapefile. Unlike Mongoconnecter, no additional configuration is required and Polygon geometry is loadable. 

To load the layer simply type the your mongo db server name, db name, geometry field name and click CONNECT.

Example:
my.server.com.au 
geos 
geom

If the connection is successful, you should see a list of your collections that contain geometry with the geometry type. To load the collection, simply select the collection and click LOAD. Under the settings tab you can also VIEW all of the attribute in your collection. After viewing your attributes select an attribute and click DISTINCT. This will display a list of distinct value for that attribute. To load your mongoDB layer using a specific attribute simply click SET. 

Now go back to the CONNECTION tab and tick the checkbox and select the field from the drop down list that you would like to load.
	

#### License

qgis-mongodb-plugin is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Copyright © 2010-2014 Pirmin Kalberer & Mathias Walker, Sourcepole AG

