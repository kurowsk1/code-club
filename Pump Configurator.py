from tkinter import *

# CREATE A WINDOW WITH SOME BASIC PROPERTIES
root = Tk()
# assigns the basic window class to the variable root
root.title('SciLog Expert Pump Configurator')
root.minsize(300, 300)
root.geometry("800x800")
# assigns some basic properties to the root window


# CREATE SOME FRAMES WITHIN THE ROOT WINDOW
oneFrame = Frame(root)
# makes a frame (a borderless box that objects can be dropped into) within the 'root' basic window.  This will not display unless accompanied by some sort of spatial instruction.  For this we'll just use pack again.
oneFrame.pack()
twoFrame = Frame(root)
twoFrame.pack()
threeFrame = Frame(root)
threeFrame.pack()
xFrame = Frame(root)
xFrame.pack(side=BOTTOM)
# The top frame will be packed into the available space (probably anchored to the top left of the available space by default).  The bottom frame has this extra spatial parameter to anchor it underneath


# CREATE FRAME LABELS
pumpSelect = Label(root, text="Select Pump Type")
# tells the program to insert some text (called a label) into the window named 'root'.
pumpSelect.pack()  # packs it in

motorSelect = Label(twoFrame, text="Select Motor Speed")
motorSelect.pack()

pheadSelect = Label(threeFrame, text="Select Pump Head")
pheadSelect.pack()

part_no_output_1 = Label(xFrame, text='200-')    # create the label
part_no_output_1.config(font=("Courier", 44))
part_no_output_1.pack(side=LEFT)    # say where to put it

# CREATE AND ORIENTATE THE BUTTONS IN THE FIRST FRAME
btn_pureTec = Button(oneFrame, text="PureTec", fg="red")
btn_chemTec = Button(oneFrame, text="ChemTec", fg="blue")
btn_labTec = Button(oneFrame, text="LabTec", fg="green")
btn_mabTec = Button(oneFrame, text="MABTec", fg="brown")
btn_filterTec = Button(oneFrame, text="FilterTec", fg="purple")
btn_ftPlus = Button(oneFrame, text="FilterTec Plus", fg="purple")
btn_pureTec.pack(side=LEFT)
btn_chemTec.pack(side=LEFT)
btn_labTec.pack(side=LEFT)
btn_mabTec.pack(side=LEFT)
btn_filterTec.pack(side=LEFT)
btn_ftPlus.pack(side=LEFT)
# since it is the only thing in this frame, you don't really need to say where, but...
# The format with basic GUIs is that you need to create the widget (above), but they won't display until you say where.


# DEFINE BUTTON BEHAVIOUR


def ptclick():
    part_no_output_2a = Label(xFrame, text='PURE-')
    part_no_output_2a.config(font=("Courier", 44))
    part_no_output_2a.pack(side=LEFT)


btn_pureTec["command"] = ptclick

def ctclick():
    part_no_output_2b = Label(xFrame, text='CHEM-')
    part_no_output_2b.config(font=("Courier", 44))
    part_no_output_2b.pack(side=LEFT)


btn_chemTec["command"]=ctclick


def ltclick():
    part_no_output_2c = Label(xFrame, text='LABT-')
    part_no_output_2c.config(font=("Courier", 44))
    part_no_output_2c.pack(side=LEFT)


btn_labTec["command"]=ltclick

def mtclick():
    part_no_output_2d = Label(xFrame, text='MABT-')
    part_no_output_2d.config(font=("Courier", 44))
    part_no_output_2d.pack(side=LEFT)


btn_mabTec["command"]=mtclick

def ftclick():
    part_no_output_2e = Label(xFrame, text='FILT-')
    part_no_output_2e.config(font=("Courier", 44))
    part_no_output_2e.pack(side=LEFT)


btn_filterTec["command"]=ftclick

def ftpclick():
    part_no_output_2f = Label(xFrame, text='FILT-')
    part_no_output_2f.config(font=("Courier", 44))
    part_no_output_2f.pack(side=LEFT)


btn_ftPlus["command"]=ftpclick



# CREATE & ORIENTATE THE BUTTONS IN THE SECOND FRAME
btn_eightRpm = Button(twoFrame, text="8RPM", fg="red")
btn_onesixtyRpm = Button(twoFrame, text="160RPM", fg="blue")
btn_sixhundredRpm = Button(twoFrame, text="600RPM", fg="green")
btn_threethosixhunRpm = Button(twoFrame, text="3600RPM", fg="brown")
btn_eightRpm.pack(side=LEFT)
btn_onesixtyRpm.pack(side=LEFT)
btn_sixhundredRpm.pack(side=LEFT)
btn_threethosixhunRpm.pack(side=LEFT)


# DEFINE BUTTON BEHAVIOUR


def eightRpmclick():
    part_no_output_3a = Label(xFrame, text='10')
    part_no_output_3a.config(font=("Courier", 44))
    part_no_output_3a.pack(side=LEFT)


btn_eightRpm["command"]=eightRpmclick


def onesixtyRpmclick():
    part_no_output_3b = Label(xFrame, text='11')
    part_no_output_3b.config(font=("Courier", 44))
    part_no_output_3b.pack(side=LEFT)


btn_onesixtyRpm["command"]=onesixtyRpmclick


def sixhundredRpmclick():
    part_no_output_3c = Label(xFrame, text='16')
    part_no_output_3c.config(font=("Courier", 44))
    part_no_output_3c.pack(side=LEFT)


btn_sixhundredRpm["command"]=sixhundredRpmclick


def threethosixhunRpmclick():
    part_no_output_3d = Label(xFrame, text='13')
    part_no_output_3d.config(font=("Courier", 44))
    part_no_output_3d.pack(side=LEFT)


btn_threethosixhunRpm["command"]=threethosixhunRpmclick


# CREATE & ORIENTATE BUTTONS IN THE THIRD FRAME
btn_tandem81 = Button(threeFrame, text="Tandem 1801", fg="red")
btn_tandem82 = Button(threeFrame, text="Tandem 1082", fg="blue")
btn_masflex_thin = Button(threeFrame, text="Masterflex Thin", fg="green")
btn_masflex_thick = Button(threeFrame, text="Masterflex Thick", fg="brown")
btn_tandem81.pack(side=LEFT)
btn_tandem82.pack(side=LEFT)
btn_masflex_thin.pack(side=LEFT)
btn_masflex_thick.pack(side=LEFT)

#DEFINE BUTTON BEHAVIOUR


def tandem81click():
    part_no_output_4a = Label(xFrame, text='81')
    part_no_output_4a.config(font=("Courier", 44))
    part_no_output_4a.pack(side=LEFT)


btn_tandem81["command"]=tandem81click


def tandem82click():
    part_no_output_4b = Label(xFrame, text='82')
    part_no_output_4b.config(font=("Courier", 44))
    part_no_output_4b.pack(side=LEFT)


btn_tandem82["command"]=tandem82click


def masflex_thinclick():
    part_no_output_4c = Label(xFrame, text='22')
    part_no_output_4c.config(font=("Courier", 44))
    part_no_output_4c.pack(side=LEFT)


btn_masflex_thin["command"]=masflex_thinclick


def masflex_thickclick():
    part_no_output_4d = Label(xFrame, text='23')
    part_no_output_4d.config(font=("Courier", 44))
    part_no_output_4d.pack(side=LEFT)


btn_masflex_thick["command"] = masflex_thickclick


root.mainloop()
# infinite loop to keep the window open, until it's closed
