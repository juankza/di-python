#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from gi.repository import Gtk
from gi.repository import Gdk


######################### GLADE #########################
class MyGlade():

  def __init__(self):
    self._gladeFile = "Practica3_Cazalilla.glade"
    self._glade = Gtk.Builder()
    self._glade.add_from_file(self._gladeFile)


######################### MAIN #########################
class MainWindow(MyGlade):

  def __init__(self):
    MyGlade.__init__(self)
    self._discounts = 5, 10, 15, 20, 25, 30, 50, 60, 70, 75, 80
    
    ### Widgets
    self.mainWindow = self._glade.get_object("mainWindow")
    self.entryPrecio = self._glade.get_object("entryPrecio")
    self.comboBoxDescuento = self._glade.get_object("comboBoxDescuento")
    self.labelRPrecio2 = self._glade.get_object("labelRPrecio2")
    self.labelRDescuento2 = self._glade.get_object("labelRDescuento2")

    self._fillComboBox()
    
    ### Signals
    self.mainWindow.connect("destroy", Gtk.main_quit)
    self.entryPrecio.connect("changed", self._entryPrecioChanged)
    self.comboBoxDescuento.connect("changed", self._displayDiscount)

    self.mainWindow.show_all()      

  def _fillComboBox(self):
    store = Gtk.ListStore(int)
    for discount in self._discounts:
      store.append([discount])

    crt = Gtk.CellRendererText()
    self.comboBoxDescuento.set_model(store)
    self.comboBoxDescuento.pack_start(crt, True)
    self.comboBoxDescuento.add_attribute(crt, "text", 0)

  def _entryPrecioChanged(self, obj):
    value = self.entryPrecio.get_text()
    if value and not isNumeric(value):
      self.labelRPrecio2.set_text("Invalid")
      self.labelRDescuento2.set_text("Invalid")
    else:
      self._displayDiscount(obj)


  def _displayDiscount(self, obj):
    hasData, price, discount = self._getData()
    if not hasData:
      self.labelRPrecio2.set_text("0.0 €")
      self.labelRDescuento2.set_text("0.0 €")
    else:
      discounted = float(price * discount / 100)
      self.labelRPrecio2.set_text("{0} €".format(price - discounted))
      self.labelRDescuento2.set_text("{0} €".format(discounted))

  def _getData(self):
    price = self.entryPrecio.get_text()
    treeIter = self.comboBoxDescuento.get_active_iter()

    if not price or not treeIter:
      return False, False, False
    else:
      return True, float(price), int(self.comboBoxDescuento.get_model()[treeIter][0])


######################### INIT #########################
def isNumeric(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

if __name__ == "__main__":
  mainWindow = MainWindow()
  Gtk.main()
