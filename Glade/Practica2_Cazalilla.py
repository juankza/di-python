#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import sqlite3
bd = "tEjercicio"
from gi.repository import Gtk


def cleanBtnClicked(self):
    print "cleanBtnClicked"
    # Entry Cleaner Function
    glade.get_object("userEntry").set_text("")
    glade.get_object("pwdEntry").set_text("")
    glade.get_object("emailEntry").set_text("")
    glade.get_object("nameEntry").set_text("")
    glade.get_object("surnameEntry").set_text("")
    glade.get_object("dirEntry").set_text("")

def cancelBtnClicked():
    print "cancelBtnClicked"

def okBtnClicked():
    print "okBtnClicked"

def gtk_main_quit():
    Gtk.main_quit()


######################### MAIN #########################
if __name__ == "__main__":
    glade = Gtk.Builder()
    glade.add_from_file("Practica2_Cazalilla.glade")
    signals = { "on_cleanBtn_clicked": cleanBtnClicked,"on_cancelBtn_clicked": cancelBtnClicked,"on_okBtn_clicked": okBtnClicked,"gtk_main_quit": Gtk.main_quit }
    glade.connect_signals(signals)
    window = glade.get_object("mainWindow")
    window.show_all()
    Gtk.main()
    