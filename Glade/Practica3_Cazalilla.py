#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from gi.repository import Gtk


####################### FUNCTION #######################
def entryPrecioChanged():
    print "entryPrecioChanged"

def comboBoxDescuentoChanged():
    print "comboBoxDescuentoChanged"

def gtk_main_quit():
    Gtk.main_quit()

def fillComboBox():
    discounts = 10, 20, 30, 40, 50
    store = Gtk.ListStore(int)
    for discount in discounts:
        store.append([discount])
    cellRendererText = Gtk.CellRendererText()
    comboBoxDescuento.set_model(store)
    comboBoxDescuento.pack_start(cellRendererText, True)
    comboBoxDescuento.add_attribute(cellRendererText, "text", 0)


######################### MAIN #########################
if __name__ == "__main__":
    glade = Gtk.Builder()
    glade.add_from_file("Practica3_Cazalilla.glade")
    signals = { "on_entryPrecio_changed": entryPrecioChanged, "on_comboBoxDescuento_changed": comboBoxDescuentoChanged, "gtk_main_quit": Gtk.main_quit }
    glade.connect_signals(signals)
    window = glade.get_object("mainWindow")

    comboBoxDescuento = glade.get_object("comboBoxDescuento")
    fillComboBox()

    window.show_all()
    Gtk.main()
