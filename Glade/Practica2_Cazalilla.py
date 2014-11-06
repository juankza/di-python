#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from gi.repository import Gtk
glade = Gtk.Builder()
glade.add_from_file("Practica2_Cazalilla.glade")
window = glade.get_object("mainWindow")
window.show_all()
Gtk.main()

##### MAIN CLASS
class MainWin:

	def __init__(self):
		self.widgets = gtk.glade.XML("Practica2_Cazalilla.glade")

        signals = { "on_userEntry_changed": self.on_userEntry_changed,
        			"on_pwdEntry_changed": self.on_pwdEntry_changed,
        			"on_emailEntry_changed": self.on_emailEntry_changed,
        			"on_nameEntry_changed": self.on_nameEntry_changed,
        			"on_surnameEntry_changed": self.on_surnameEntry_changed,
        			"on_dirEntry_changed": self.on_dirEntry_changed,
        			"on_cleanBtn_clicked": self.on_cleanBtn_clicked,
        			"on_cancelBtn_clicked": self.on_cancelBtn_clicked,
        			"on_okBtn_clicked": self.on_okBtn_clicked,
        			"gtk_main_quit": gtk.main_quit }

        self.widgets.signal_autoconnect(signals)

    def on_cleanBtn_clicked(self, widget):
    	# Entry Cleaner Function
    	self.userEntry = self.widgets.get_object("userEntry")
    	self.pwdEntry = self.widgets.get_object("pwdEntry")
    	self.emailEntry = self.widgets.get_object("emailEntry")
    	self.nameEntry = self.widgets.get_object("nameEntry")
    	self.surnameEntry = self.widgets.get_object("surnameEntry")
    	self.dirEntry = self.widgets.get_object("dirEntry")

    	self.userEntry.set_text("")
   		self.pwdEntry.set_text("")
   		self.emailEntry.set_text("")
   		self.nameEntry.set_text("")
   		self.surnameEntry.set_text("")
   		self.dirEntry.set_text("")

   		self.on_userEntry_changed(self)
   		self.on_pwdEntry_changed(self)
   		self.on_emailEntry_changed(self)
   		self.on_nameEntry_changed(self)
   		self.on_surnameEntry_changed(self)
   		self.on_dirEntry_changed(self)

######################### MAIN #########################
if __name__ == "__main__":
	MainWin()
	gtk.main()