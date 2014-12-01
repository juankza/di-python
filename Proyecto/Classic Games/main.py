#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
#import sqlite3 bd = "db/scoreboard.db"
from gi.repository import Gtk
from gi.repository import Gdk


######################### GLADE #########################
class MainGlade():

  def __init__(self):
    self._gladeFile = "glade/main.glade"
    self._glade = Gtk.Builder()
    self._glade.add_from_file(self._gladeFile)


######################### MAIN #########################
class MainWindow(MainGlade):

  def __init__(self):
    MainGlade.__init__(self)
    
    ### Widgets
    self.mainWindow = self._glade.get_object("mainWindow")
    #self.entryPrecio = self._glade.get_object("entryPrecio")
    #self.comboBoxDescuento = self._glade.get_object("comboBoxDescuento")
    #self.labelRPrecio2 = self._glade.get_object("labelRPrecio2")
    #self.labelRDescuento2 = self._glade.get_object("labelRDescuento2")

    #self._fillComboBox()
    
    ### Signals
    self.mainWindow.connect("destroy", Gtk.main_quit)
    #self.entryPrecio.connect("changed", self._entryPrecioChanged)
    #self.comboBoxDescuento.connect("changed", self._displayDiscount)

    self.mainWindow.show_all()


######################### INIT #########################
if __name__ == "__main__":
  mainWindow = MainWindow()
  Gtk.main()
