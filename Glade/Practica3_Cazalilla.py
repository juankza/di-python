#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from gi.repository import Gtk


####################### FUNCTION #######################
def entryPrecioChanged(self):
    print "entryPrecioChanged"

def entryComboBoxChanged():
    print "entryComboBoxChanged"

def gtk_main_quit():
    Gtk.main_quit()


######################### MAIN #########################
if __name__ == "__main__":
    glade = Gtk.Builder()
    glade.add_from_file("Practica3_Cazalilla.glade")
    signals = { "on_entryPrecio_changed": entryPrecioChanged, "on_comboBoxEntry_changed": entryComboBoxChanged, "gtk_main_quit": Gtk.main_quit }
    glade.connect_signals(signals)
    window = glade.get_object("mainWindow")
    window.show_all()
    Gtk.main()

discount = [10, 20, 30, 40, 50]
comboBoxDescuento = glade.get_object("comboBoxDescuento")
for i in range(3):
    #comboBoxDescuento.append_text(discount[i])
