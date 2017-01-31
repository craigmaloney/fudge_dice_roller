#!/usr/bin/env python

# Fudge Dice Roller
# Based off of the Table example from the pygtk tutorial

import pygtk
pygtk.require('2.0')
import gtk
import random

class FudgeDice:
    dice = 4
    die = 6
    total = 0
    # Use a standard 6 sided die, but change the values as follows
    fudge = {
            1:-1, 2:-1,
            3:0, 4:0,
            5:1, 6:1
            }
    # Standard fudge notation uses -, [blank], and + for -1, 0, and 1
    fudge_notation = {
            -1:"-",
            0:" ",
            1:"+"
            }
    dice_button = range(1,dice+2)


    # Ignore button presses on the dice for now
    def callback(self, widget, data=None):
        pass

    # This callback will roll the dice
    def roll_callback(self,widget):
        self.total = 0

        for i in range(1,self.dice+1):
            roll  = self.fudge[random.randint(1,self.die)]
            self.total = self.total + roll
            self.dice_button[i].set_label(self.fudge_notation[roll])

        self.total_label.set_text("Total: " + str(self.total))

        return

    # This callback quits the program
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False


    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # Set the window title
        self.window.set_title("Fudge Dice")

        # Set a handler for delete_event that immediately
        # exits GTK.
        self.window.connect("delete_event", self.delete_event)

        # Sets the border width of the window.
        self.window.set_border_width(20)

        # Create a 4x3 table
        table = gtk.Table(3, 4, True)

        # Put the table in the main window
        self.window.add(table)

        # Position the dice as buttons on the table
        for i in range(1,self.dice+1):
            self.dice_button[i] = gtk.Button(' ')
            self.dice_button[i].connect("clicked", self.callback, "dice %d" % i)
            table.attach(self.dice_button[i], i-1, i, 0, 1)
            self.dice_button[i].show()

        # Add a label for the total
        self.total_label = gtk.Label("Total: 0")
        table.attach(self.total_label,0,4,1,2)
        self.total_label.show()

        # Create a "Roll" button
        button = gtk.Button("Roll")
        button.connect("clicked", self.roll_callback)
        table.attach(button, 0,2, 2,3)
        button.show()

        # Create "Quit" button
        button = gtk.Button("Quit")
        button.connect("clicked", lambda w: gtk.main_quit())
        table.attach(button, 3, 4, 2, 3)
        button.show()

        table.show()
        self.window.show()

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    FudgeDice()
    main()

