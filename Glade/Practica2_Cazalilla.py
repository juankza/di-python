#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import sqlite3
bd = "tEjercicio"
from gi.repository import Gtk

def userEntryChanged(self):
    print "on_userEntry_changed"

def pwdEntryChanged(self):
    print "on_pwdEntry_changed"

def emailEntryChanged():
    print "on_emailEntry_changed"

def nameEntryChanged():
    print "on_emailEntry_changed"

def surnameEntryChanged():
    print "on_emailEntry_changed"

def dirEntryChanged():
    print "on_emailEntry_changed"

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
    signals = { "on_userEntry_changed": userEntryChanged,"on_pwdEntry_changed": pwdEntryChanged,"on_emailEntry_changed": emailEntryChanged,"on_nameEntry_changed": nameEntryChanged,"on_surnameEntry_changed": surnameEntryChanged,"on_dirEntry_changed": dirEntryChanged,"on_cleanBtn_clicked": cleanBtnClicked,"on_cancelBtn_clicked": cancelBtnClicked,"on_okBtn_clicked": okBtnClicked,"gtk_main_quit": Gtk.main_quit }
    glade.connect_signals(signals)
    window = glade.get_object("mainWindow")
    window.show_all()
    Gtk.main()
    