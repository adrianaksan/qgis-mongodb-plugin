# -*- coding: utf-8 -*-
"""
/*!
 * MongoDB to QGIS Loader
 *
 * GUI/ Layer Loader
 * @author Adrian Aksan <adrian.aksan@gmail.com>
 * @created 15/09/2014
 */
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Initialize Qt resources from file resources.py
import resources_rc, os.path
# Import the code for the dialog
from loadMongoDB_dialog import loadMongoDBDialog

# test requirements
try:
    import json

except ImportError as e:
    QMessageBox.critical(iface.mainWindow(),
                         "Missing module",
                         "Json module is required",
                         QMessageBox.Ok)

class loadMongoDB:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'loadMongoDB_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = loadMongoDBDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Load MongoDB Layers')

        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'loadMongoDB')
        self.toolbar.setObjectName(u'loadMongoDB')


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('loadMongoDB', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the InaSAFE toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    # append the new server details to the cache.txt file
    def save_server_cache(self):

        server = self.dlg.ui.serverName.currentText().strip()
        db = self.dlg.ui.dbName.currentText().strip()
        geom = self.dlg.ui.geom_field.currentText().strip()
        query = self.dlg.ui.query_field.currentText().strip()

        if len(server) == 0 or len(db) == 0 or len(geom) == 0:
            return

        for field, value in {'servers': server, 'db': db, 'geom': geom, 'query': query}.items():
            if value not in self.user_details[field]:
                self.user_details[field].append(value)


        if geom not in self.user_details["geom"]:
            self.user_details["geom"].append(geom)

        json.dump(self.user_details, open(str(os.path.abspath(__file__ + "/../../")) + "/qgis-mongodb-loader/cache.txt",'w'))


    # attempt a connection to the server when the user presses "CONNECT"
    def button_clicked(self):
        self.dlg.ui.load_field.clear()
        if len(self.dlg.ui.dbName.currentText()) != 0 and len(self.dlg.ui.serverName.currentText()) != 0 and len(self.dlg.ui.geom_field.currentText()) != 0:
            # self.dlg.ui.groupBox.setTitle(str(self.dlg.ui.serverName.currentText()).upper())
            self.dlg.show_mdb_collection(self.dlg.ui.dbName.currentText(), self.dlg.ui.serverName.currentText(), self.dlg.ui.geom_field.currentText())
            self.save_server_cache()


    # attempt to load the collection when the user presses "LOAD"
    def on_click_check(self):
        self.user_details["checkbox"] = self.dlg.ui.checkBox.isChecked()
        if len(self.dlg.ui.dbName.currentText()) != 0 and len(self.dlg.ui.serverName.currentText()) != 0 and len(self.dlg.ui.geom_field.currentText()) != 0:
            self.dlg.on_click_load()
            self.save_server_cache()


    #
    def load_file_cache(self):

        try:
            self.user_details = json.load(open(str(os.path.abspath(__file__ + "/../../")) + "/qgis-mongodb-loader/cache.txt"))
            if 'query' not in self.user_details:
                self.user_details['query'] = []

        except:
            self.user_details = {"geom": [], "db": [], "checkbox": False, "servers": [], 'query': []}


    #
    def populate_fields(self):

        if self.user_details == None:
            return

        server_name_list = self.user_details["servers"]
        db_name_list = self.user_details["db"]
        geom_name_list = self.user_details["geom"]
        query_name_list = self.user_details.get('query', [])

        self.dlg.ui.serverName.clear()
        self.dlg.ui.dbName.clear()
        self.dlg.ui.geom_field.clear()
        self.dlg.ui.query_field.clear()

        self.dlg.ui.serverName.addItems(list(set(server_name_list)))
        self.dlg.ui.dbName.addItems(list(set(db_name_list)))
        self.dlg.ui.geom_field.addItems(list(set(geom_name_list)))
        self.dlg.ui.query_field.addItems(list(set(query_name_list)))


    def initGui(self):

        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/loadMongoDB/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Load MongoDb Layers'),
            callback=self.run,
            parent=self.iface.mainWindow())

        QObject.connect(self.dlg.ui.load_collection, SIGNAL("clicked()"), self.on_click_check)
        QObject.connect(self.dlg.ui.createFile, SIGNAL("clicked()"), self.button_clicked)
        QObject.connect(self.dlg.ui.view_button, SIGNAL("clicked()"), self.dlg.view_all_attributes)
        QObject.connect(self.dlg.ui.distinct_button, SIGNAL("clicked()"), self.dlg.view_distinct)
        QObject.connect(self.dlg.ui.set_button, SIGNAL("clicked()"), self.dlg.set_attribute)

        # the list will store the server details
        self.server_details_list = []

        # load the server details from the cache.txt file upon loading
        self.load_file_cache()
        self.populate_fields()


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Load MongoDB Layers'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):

        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()

        self.load_file_cache()
        self.populate_fields()
        # Run the dialog event loop
        result = self.dlg.exec_()

        # See if OK was pressed
        if result == 1:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
