from Tkinter import *
def quit3(event=None):
	root3.destroy()
root3=Tk()
root3.title("Manual for NOMA...")
sss1=Scrollbar(root3)
T=Text(root3)
T.focus_set()
sss1.pack(side='right',fill='y')
T.pack(side='left',fill='y')
sss1.config(command=T.yview)
T.config(yscrollcommand=sss1.set)
T.insert(END,"""
If you use the application by clicking on the icon and miss the terminal:
Drag it onto the panel. Right-click it. Properties. Switch Type from
Application to Application in Terminal. Close. The next time it starts up
the terminal window will appear.

About NOMA for Linux can be reached through the menu or pressing <Ctrl-A>.
There is an icon that can play by pressing the Play button. The quit button
follows so double-click Play to quit.

Switching the main tabs can be accomplished by clicking on the Buttons on
top.

Switching between the tabs in NPZ file page can be accomplished by
holding Ctrl and any arrow. Or by clicking on the Radiobutton or text.

Browsing is <Ctrl-b> for all browsing options as long as you are on the
screen that you want. The program will allow <Ctrl-b> to work for the
comparison NPZ file only if the original NPZ file space is not blank.
The same goes for the browing for your NMD file.

Submitting anything is available by pressing <Return> or by clicking the
submit button.

Adding or subtracting modes is easy by using the <Up> or <Down> arrows.
When the modes go to 0, all is placed in return. Multiple modes can be
submitted by having a space or comma between the numbers. EX: if you want
to submit modes 7 and 8 you can put Modes: 7 8 or Modes: 7,8
You may also write all to get all the modes.

Using <Ctrl-n> or <Ctrl-p> will get you to the next or previous PDB or NPZ
file that is in the same folder that the PDB or NPZ file you are working on
is in. If there are no other PDB or NPZ files then it will not change.

Swapping NPZ files is available by pressing <Ctrl-s>. It is also available in
the menubar.

Find an NPZ comparison file by searching with the browser or pressing <Ctrl-f>.
This option is also in the menubar.

Items on the menubar (File, Start-up...etc.) can be
reached by pressing Alt and the letter underlined.


In the modes plot:

blue==x-component
green==y-component
red==z-component

The statistics of either the PDB or NPZ file can be found while using the
menubar.

To view your PDB file in vmd just select a file and press <Ctrl-Shift-V>.

To open a file in xmgrace press <Ctrl-Shift-X> and select a file from the
browser.

If you would rather submit your structure through the uiNMAall interface
just go to the Start-up menu select Interface and then select Old.
If you would like this interface for the start-up screen then go to File
Preferences and switch the interface to Old then Save & Quit.

The Preferences makes saving various inputs so it stays the same even if
you quit the program and start up again.

Collectivity now outputs collectivity with and without mass. The program
reads the one you choose in the Preferences.

In light of the new saving feature there is a notes page which you can
write whatever you would like and save it. This will be saved and will
be there when you log on next time.

In Sample Modes you can write 1c or 2c or 3c or 4c in the modes option
to the most collective modes. The Collectivity box needs to also be checked
for this option.

The Traverse Mode you can write c to do the most collective mode.

The calculator is available by pressing <Ctrl-Shift-C>.

On the notes screen you can execute many files. On the first lines of the
notes page write:
path/to/file/name.pdb select_atoms anm_or_gnm number_of_modes
Ex:
/home/matt/PDB/34290ps.pdb ca anm 20
/home/matt/PDB/two_fold_Ab.pdb heavy gnm 30

It allows you to do multiple files. You can also have it run with the new
interface settings by typing new after the number of modes so:
/home/matt/PDB/34290ps.pdb ca anm 20 new

This means if you want to do Sample Modes then check that box in the PDB
file frame.

To keep the notes that you had before just put #! on the line directly
underneath the commands.
Ex:
/home/matt/PDB/34290ps.pdb ca anm 20 new
/home/matt/PDB/two_fold_Ab.pdb heavy gnm 30
#!
I can keep my notes here!

Now to execute this you must save the file first, then press <Ctrl-E>
or by clicking the option in the Notes menu.
""")
root3.bind('<Control-q>',quit3)
root3.mainloop()
