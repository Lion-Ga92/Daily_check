import sqlite3
from tkinter import *
from tkinter import ttk

class backEnd():
    def __init__(self):
        self = self

    def initialize(self):
        o = 1
        self.conn = sqlite3.connect("day_check.db")

        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS dayCheck ('date' TEXT, 'workout' TEXT, 'tai-chi' TEXT, 'bible-Studies' TEXT, '4_agreements' TEXT, '12_Step' TEXT, 'Hlp_mom' TEXT, 'Cln_house' TEXT, 'Meditation' TEXT, 'meds_Dose' TEXT, 'Hallow' TEXT);""")

        self.conn.commit()

        o = 1

        while o != 1:
            self.conn.close()

    def add_vals(self, a, b, z, d, e, f, g, h, i, j, k):
        self.a = a
        self.b = b
        self.z = z
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h 
        self.i = i
        self.j = j
        self.k = k
        self.c = self.conn.cursor()
        self.data = (a, b, z, d, e, f, g, h, i, j, k)
        self.query = """INSERT INTO dayCheck VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        self.c.execute(self.query, self.data)
        self.conn.commit()
        o = 1

    def confirm_Entry(self):    
        window_2 = Tk()
        frame_1 = Frame(window_2)
        frame_2 = Frame(window_2)
        frame_1.pack()
        frame_2.pack()
        lbl_one = Label(frame_1, text="Your values have been added to the database, you can close this app now!!")
        lbl_one.pack()     
        enter_button = Button(frame_2, text="Close", command=lambda : exit())
        enter_button.pack()
 