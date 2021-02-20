from tkinter import *
from tkinter import ttk
from Classes import backEnd

dataBack = backEnd()
dataBack.initialize()


root = Tk()
root.geometry("900x600")
frame_1 = Frame(master=root)
frame_2 = Frame(master=root)
frame_1.grid(row=1, column=1)
frame_2.grid(row=2, column=1)
#WIDGETS FOR FRAME 1
lbl_title = Label(master=frame_1, text="Luis' Checklist App  ")
lbl_title.grid(row=1, column=1)
lbl_date = Label(master=frame_1, text="Date", relief="groove")
lbl_date.grid(row=1, column=2)
date_entr = Entry(master=frame_1, width="15")
date_entr.grid(row=1, column=3)
date_gett = date_entr.get()
tsk_intro = Label(master=frame_1, text="Please check off all completed\n tasks: ", relief="groove")
tsk_intro.grid(row=2, column=1)


#WIDGETS FOR FRAME 2
lbl_task_mrn = Label(master=frame_2, text="Tasks for the morning:", relief="groove")
lbl_task_mrn.grid(row=1, column=1)

minute_wrkout = StringVar()
minute_check = Checkbutton(master=frame_2, text="Five minute workout", command= lambda : minute_wrkout.get(), variable=minute_wrkout, onvalue="Complete", offvalue="Not complete")
minute_check.grid(row=2, column=1)

tai_stretch = StringVar()
tai_check = Checkbutton(master=frame_2, text="     Tai-chi stretches ", command= lambda : tai_stretch.get(), variable=tai_stretch, onvalue="Complete", offvalue="Not complete" )
tai_check.grid(row=3, column=1)

bibl_stud = StringVar()
bible_check = Checkbutton(master=frame_2, text="     Bible studies       ", command= lambda : bibl_stud.get(),variable=bibl_stud, onvalue="Complete", offvalue="Not complete")
bible_check.grid(row=4, column=1)

tltc_book = StringVar()
toltec_check = Checkbutton(master=frame_2, text= "          10 Minutes\n       (4 agreements)", command= lambda : tltc_book.get(), variable=tltc_book, onvalue="Complete", offvalue="Not complete")
toltec_check.grid(row=5, column=1)

anon_bk = StringVar()
anon_check = Checkbutton(master=frame_2, text="12 Step study session", command= lambda : anon_bk.get(), variable=anon_bk, onvalue="Complete", offvalue="Not complete" )
anon_check.grid(row=6, column=1)

hlp_chores = StringVar()
hlp_check = Checkbutton(master=frame_2, text=" Help with moms work", command= lambda : hlp_chores.get(), variable=hlp_chores, onvalue="Complete", offvalue="Not complete")
hlp_check.grid(row=7, column=1)

#widget 2 right 
lbl_Test = Label(master=frame_2, text="\tevening tasks\t", relief="groove")
lbl_Test.grid(row=1, column=2)

cln_house = StringVar()
cln_house_chk = Checkbutton(master=frame_2, text="  Clean House\t" , command=lambda : cln_house.get(), variable=cln_house, onvalue="Complete", offvalue="Not complete")
cln_house_chk.grid(row=2, column=2)

medit_time = StringVar()
medit_check = Checkbutton(master=frame_2, text="  Meditation\t", command= lambda : medit_time.get(), variable=medit_time, onvalue="Complete", offvalue="Not complete" )
medit_check.grid(row=3, column=2)

medic_time = StringVar()
medic_Check = Checkbutton(master=frame_2, text= "  Took all three med \ndoses? ", command= lambda : medic_time.get(), variable=medic_time, onvalue="Complete", offvalue="Not complete")
medic_Check.grid(row=4, column=2)

hallow = StringVar()
hallow_chk = Checkbutton(master=frame_2, text="  Hallow session\t", command= lambda : hallow.get(), variable=hallow, onvalue="Complete", offvalue="Not complete")
hallow_chk.grid(row=5, column=2)

def add_values():
    dataBack.add_vals(date_entr.get(), minute_wrkout.get(), tai_stretch.get(), bibl_stud.get(), tltc_book.get(), anon_bk.get(), hlp_chores.get(), cln_house.get(), medit_time.get(), medic_time.get(), hallow.get())
    dataBack.confirm_Entry()

submitbtn = Button(master=frame_2, text="Submit data", command=add_values, width="20")
submitbtn.grid(row=8, column=1)


root.mainloop()