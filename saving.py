import os
path=os.path.join(os.path.expanduser('~'),'.noma/')
fin = open(path+'savefile.txt','r')

savedfile=fin.readlines()
fin.close()
i=0
a=len(savedfile)
while i<a:
	savedfile[i]=savedfile[i][:-1]
	i+=1

from Tkinter import *
root = Tk()
root.title("Preferences")
####
def parabutton(event=None):
	firstpage()
def filenamebutton(event=None):
	secondpage()
def controlsbutton(event=None):
	thirdpage()
def miscbutton(event=None):
	fourthpage()
pagenumber=StringVar()

toppage1=Frame(root)
toppage1.pack(side='top')
parabutton1=Button(toppage1,text='Parameters',command=parabutton)
parabutton1.pack(side='left')
filenamebutton1=Button(toppage1,text='Save names',command=filenamebutton)
filenamebutton1.pack(side='left')
controlsbutton1=Button(toppage1,text='Controls',command=controlsbutton)
controlsbutton1.pack(side='left')
miscbutton1=Button(toppage1,text='Misc.',command=miscbutton)
miscbutton1.pack(side='left')
####

########################### Parameters page	First page
firstpage1=Frame(root)

Label(firstpage1,text='Start up',font='Times 14 underline').grid(row=0,column=1)
nummode=StringVar()
nummode.set(savedfile[0])
Entry(firstpage1,width=2,textvariable=nummode).grid(row=1,column=1)
Label(firstpage1,text='Number of modes').grid(row=1,column=2)

Label(firstpage1,text='Collectivity',font='Times 14 underline').grid(row=2,column=1)
massnomass=StringVar()
massnomass.set(savedfile[7])
Radiobutton(firstpage1,value=0,variable=massnomass).grid(row=3,column=1)
Label(firstpage1,text='with mass').grid(row=3,column=2)
Radiobutton(firstpage1,value=1,variable=massnomass).grid(row=4,column=1)
Label(firstpage1,text='without mass').grid(row=4,column=2)


Label(firstpage1,text='Sample Modes',font='Times 14 underline').grid(row=0,column=3)
modeens=StringVar()
modeens.set(savedfile[1])
Entry(firstpage1,width=4,textvariable=modeens).grid(row=1,column=3)
Label(firstpage1,text='modes').grid(row=1,column=4)
confens=StringVar()
confens.set(savedfile[2])
Entry(firstpage1,width=2,textvariable=confens).grid(row=2,column=3)
Label(firstpage1,text='n_confs').grid(row=2,column=4)
rmsdens=StringVar()
rmsdens.set(savedfile[3])
Entry(firstpage1,width=3,textvariable=rmsdens).grid(row=3,column=3)
Label(firstpage1,text='rmsd').grid(row=3,column=4)

Label(firstpage1,text='Traverse Mode',font='Times 14 underline').grid(row=0,column=6)
modetra=StringVar()
modetra.set(savedfile[4])
Entry(firstpage1,width=2,textvariable=modetra).grid(row=1,column=6)
Label(firstpage1,text='mode').grid(row=1,column=7)
steptra=StringVar()
steptra.set(savedfile[5])
Entry(firstpage1,width=3,textvariable=steptra).grid(row=2,column=6)
Label(firstpage1,text='n_steps').grid(row=2,column=7)
rmsdtra=StringVar()
rmsdtra.set(savedfile[6])
Entry(firstpage1,width=3,textvariable=rmsdtra).grid(row=3,column=6)
Label(firstpage1,text='rmsd').grid(row=3,column=7)


Label(firstpage1,text='Gamma\nCutoff',font='Times 14 underline').grid(row=0,column=9,columnspan=2)
gammacutoff=StringVar()
gammacutoff.set(savedfile[9])
Radiobutton(firstpage1,value=0,variable=gammacutoff).grid(row=1,column=8)
Label(firstpage1,text='dist^').grid(row=1,column=9)
gammadistdep=StringVar()
gammadistdep.set(savedfile[91])
Entry(firstpage1,width=3,textvariable=gammadistdep).grid(row=1,column=10)

cutoff1=StringVar()
cutoff1.set(savedfile[10])
Entry(firstpage1,width=5,textvariable=cutoff1).grid(row=1,column=11)
Label(firstpage1,text=u'\u00C5').grid(row=1,column=12)
Radiobutton(firstpage1,value=1,variable=gammacutoff).grid(row=2,column=8)
gamma2=StringVar()
gamma2.set(savedfile[11])
Entry(firstpage1,width=3,textvariable=gamma2).grid(row=2,column=9)
cutoff2=StringVar()
cutoff2.set(savedfile[12])
Entry(firstpage1,width=5,textvariable=cutoff2).grid(row=2,column=11)
Label(firstpage1,text=u'\u00C5').grid(row=2,column=12)


Label(firstpage1,text='Model\nProtofibril',font='Times 14 underline').grid(row=3,column=8)
coordset=StringVar()
coordset.set(savedfile[14])
Entry(firstpage1,width=2,textvariable=coordset).grid(row=4,column=8)
Label(firstpage1,text='Coordinate\nset').grid(row=4,column=9)

########################### File name page	Second page
secondpage1=Frame(root)
Label(secondpage1,text='Folder Names',font='Times 14 underline').grid(row=0,column=0)
Label(secondpage1,text='Cannot be left blank').grid(row=1,column=0)
folder1=StringVar()
folder1.set(savedfile[41])
Entry(secondpage1,width=13,textvariable=folder1).grid(row=2,column=0)
Label(secondpage1,text='C-alpha ANM').grid(row=2,column=1)
folder2=StringVar()
folder2.set(savedfile[42])
Entry(secondpage1,width=13,textvariable=folder2).grid(row=3,column=0)
Label(secondpage1,text='C-alpha GNM').grid(row=3,column=1)
folder3=StringVar()
folder3.set(savedfile[43])
Entry(secondpage1,width=13,textvariable=folder3).grid(row=4,column=0)
Label(secondpage1,text='Heavy ANM').grid(row=4,column=1)
folder4=StringVar()
folder4.set(savedfile[44])
Entry(secondpage1,width=13,textvariable=folder4).grid(row=5,column=0)
Label(secondpage1,text='Heavy GNM').grid(row=5,column=1)
folder5=StringVar()
folder5.set(savedfile[45])
Entry(secondpage1,width=13,textvariable=folder5).grid(row=6,column=0)
Label(secondpage1,text='All ANM').grid(row=6,column=1)
folder6=StringVar()
folder6.set(savedfile[46])
Entry(secondpage1,width=13,textvariable=folder6).grid(row=7,column=0)
Label(secondpage1,text='All GNM').grid(row=7,column=1)
folder7=StringVar()
folder7.set(savedfile[47])
Entry(secondpage1,width=13,textvariable=folder7).grid(row=8,column=0)
Label(secondpage1,text='Backbone ANM').grid(row=8,column=1)
folder8=StringVar()
folder8.set(savedfile[48])
Entry(secondpage1,width=13,textvariable=folder8).grid(row=9,column=0)
Label(secondpage1,text='Backbone GNM').grid(row=9,column=1)
folder9=StringVar()
folder9.set(savedfile[49])
Entry(secondpage1,width=13,textvariable=folder9).grid(row=10,column=0)
Label(secondpage1,text='Sidechain ANM').grid(row=10,column=1)
folder10=StringVar()
folder10.set(savedfile[50])
Entry(secondpage1,width=13,textvariable=folder10).grid(row=11,column=0)
Label(secondpage1,text='Sidechain GNM').grid(row=11,column=1)
folder11=StringVar()
folder11.set(savedfile[51])
Entry(secondpage1,width=13,textvariable=folder11).grid(row=12,column=0)
Label(secondpage1,text='Correlation').grid(row=12,column=1)
folder12=StringVar()
folder12.set(savedfile[52])
Entry(secondpage1,width=13,textvariable=folder12).grid(row=13,column=0)
Label(secondpage1,text='SqFlucts').grid(row=13,column=1)
folder13=StringVar()
folder13.set(savedfile[53])
Entry(secondpage1,width=13,textvariable=folder13).grid(row=14,column=0)
Label(secondpage1,text='Overlap').grid(row=14,column=1)
folder14=StringVar()
folder14.set(savedfile[54])
Entry(secondpage1,width=13,textvariable=folder14).grid(row=15,column=0)
Label(secondpage1,text='Modes').grid(row=15,column=1)
folder15=StringVar()
folder15.set(savedfile[55])
Entry(secondpage1,width=13,textvariable=folder15).grid(row=16,column=0)
Label(secondpage1,text='Collectivity').grid(row=16,column=1)
folder16=StringVar()
folder16.set(savedfile[56])
Entry(secondpage1,width=13,textvariable=folder16).grid(row=17,column=0)
Label(secondpage1,text='TempFactors').grid(row=17,column=1)
folder17=StringVar()
folder17.set(savedfile[57])
Entry(secondpage1,width=13,textvariable=folder17).grid(row=18,column=0)
Label(secondpage1,text='PhiPsi').grid(row=18,column=1)
folder18=StringVar()
folder18.set(savedfile[58])
Entry(secondpage1,width=13,textvariable=folder18).grid(row=19,column=0)
Label(secondpage1,text='NMD').grid(row=19,column=1)



Label(secondpage1,text='File Names',font='Times 14 underline').grid(row=0,column=5)
Label(secondpage1,text='Correlations Data').grid(row=2,column=4)
file1=StringVar()
file1.set(savedfile[59])
Entry(secondpage1,width=13,textvariable=file1).grid(row=2,column=5)
Label(secondpage1,text='.').grid(row=2,column=6)
file2=StringVar()
file2.set(savedfile[60])
Entry(secondpage1,width=3,textvariable=file2).grid(row=2,column=7)
#2
Label(secondpage1,text='Correlations Plot').grid(row=3,column=4)
file3=StringVar()
file3.set(savedfile[61])
Entry(secondpage1,width=13,textvariable=file3).grid(row=3,column=5)
Label(secondpage1,text='.').grid(row=3,column=6)
file4=StringVar()
file4.set(savedfile[62])
Entry(secondpage1,width=3,textvariable=file4).grid(row=3,column=7)
#2
Label(secondpage1,text='SqFlucts Data').grid(row=4,column=4)
file5=StringVar()
file5.set(savedfile[63])
Entry(secondpage1,width=13,textvariable=file5).grid(row=4,column=5)
Label(secondpage1,text='.').grid(row=4,column=6)
file6=StringVar()
file6.set(savedfile[64])
Entry(secondpage1,width=3,textvariable=file6).grid(row=4,column=7)
#2
Label(secondpage1,text='SqFlucts Plot').grid(row=5,column=4)
file7=StringVar()
file7.set(savedfile[65])
Entry(secondpage1,width=13,textvariable=file7).grid(row=5,column=5)
Label(secondpage1,text='.').grid(row=5,column=6)
file8=StringVar()
file8.set(savedfile[66])
Entry(secondpage1,width=3,textvariable=file8).grid(row=5,column=7)
#2
Label(secondpage1,text='Overlap Data').grid(row=6,column=4)
file9=StringVar()
file9.set(savedfile[67])
Entry(secondpage1,width=13,textvariable=file9).grid(row=6,column=5)
Label(secondpage1,text='.').grid(row=6,column=6)
file10=StringVar()
file10.set(savedfile[68])
Entry(secondpage1,width=3,textvariable=file10).grid(row=6,column=7)
#2
Label(secondpage1,text='Overlap Plot').grid(row=7,column=4)
file11=StringVar()
file11.set(savedfile[69])
Entry(secondpage1,width=13,textvariable=file11).grid(row=7,column=5)
Label(secondpage1,text='.').grid(row=7,column=6)
file12=StringVar()
file12.set(savedfile[70])
Entry(secondpage1,width=3,textvariable=file12).grid(row=7,column=7)
#2
Label(secondpage1,text='Overlap Table Data').grid(row=8,column=4)
file13=StringVar()
file13.set(savedfile[71])
Entry(secondpage1,width=13,textvariable=file13).grid(row=8,column=5)
Label(secondpage1,text='.').grid(row=8,column=6)
file14=StringVar()
file14.set(savedfile[72])
Entry(secondpage1,width=3,textvariable=file14).grid(row=8,column=7)
#2
Label(secondpage1,text='Overlap Table Plot').grid(row=9,column=4)
file15=StringVar()
file15.set(savedfile[73])
Entry(secondpage1,width=13,textvariable=file15).grid(row=9,column=5)
Label(secondpage1,text='.').grid(row=9,column=6)
file16=StringVar()
file16.set(savedfile[74])
Entry(secondpage1,width=3,textvariable=file16).grid(row=9,column=7)
#2
Label(secondpage1,text='Modes Data').grid(row=10,column=4)
file17=StringVar()
file17.set(savedfile[75])
Entry(secondpage1,width=13,textvariable=file17).grid(row=10,column=5)
Label(secondpage1,text='.').grid(row=10,column=6)
file18=StringVar()
file18.set(savedfile[76])
Entry(secondpage1,width=3,textvariable=file18).grid(row=10,column=7)
#2
Label(secondpage1,text='Modes Plot').grid(row=11,column=4)
file19=StringVar()
file19.set(savedfile[77])
Entry(secondpage1,width=13,textvariable=file19).grid(row=11,column=5)
Label(secondpage1,text='.').grid(row=11,column=6)
file20=StringVar()
file20.set(savedfile[78])
Entry(secondpage1,width=3,textvariable=file20).grid(row=11,column=7)
#2
Label(secondpage1,text='Collectivity').grid(row=12,column=4)
file21=StringVar()
file21.set(savedfile[79])
Entry(secondpage1,width=13,textvariable=file21).grid(row=12,column=5)
Label(secondpage1,text='.').grid(row=12,column=6)
file22=StringVar()
file22.set(savedfile[80])
Entry(secondpage1,width=3,textvariable=file22).grid(row=12,column=7)
#2
Label(secondpage1,text='Temp Factors').grid(row=13,column=4)
file23=StringVar()
file23.set(savedfile[81])
Entry(secondpage1,width=13,textvariable=file23).grid(row=13,column=5)
Label(secondpage1,text='.').grid(row=13,column=6)
file24=StringVar()
file24.set(savedfile[82])
Entry(secondpage1,width=3,textvariable=file24).grid(row=13,column=7)
#2
Label(secondpage1,text='Phi & Psi Data').grid(row=14,column=4)
file25=StringVar()
file25.set(savedfile[83])
Entry(secondpage1,width=13,textvariable=file25).grid(row=14,column=5)
Label(secondpage1,text='.').grid(row=14,column=6)
file26=StringVar()
file26.set(savedfile[84])
Entry(secondpage1,width=3,textvariable=file26).grid(row=14,column=7)
#2
Label(secondpage1,text='Sample').grid(row=15,column=4)
file27=StringVar()
file27.set(savedfile[85])
Entry(secondpage1,width=13,textvariable=file27).grid(row=15,column=5)
Label(secondpage1,text='.').grid(row=15,column=6)
Label(secondpage1,text='pdb').grid(row=15,column=7)
#1
Label(secondpage1,text='Traverse').grid(row=16,column=4)
file28=StringVar()
file28.set(savedfile[86])
Entry(secondpage1,width=13,textvariable=file28).grid(row=16,column=5)
Label(secondpage1,text='.').grid(row=16,column=6)
Label(secondpage1,text='pdb').grid(row=16,column=7)
#1
Label(secondpage1,text='NMD').grid(row=17,column=4)
file29=StringVar()
file29.set(savedfile[87])
Entry(secondpage1,width=13,textvariable=file29).grid(row=17,column=5)
Label(secondpage1,text='.').grid(row=17,column=6)
Label(secondpage1,text='nmd').grid(row=17,column=7)
#1
Label(secondpage1,text='Model').grid(row=18,column=4)
file30=StringVar()
file30.set(savedfile[88])
Entry(secondpage1,width=13,textvariable=file30).grid(row=18,column=5)
Label(secondpage1,text='.').grid(row=18,column=6)
Label(secondpage1,text='npz').grid(row=18,column=7)
#1
Label(secondpage1,text='Fraction of Variance').grid(row=19,column=4)
file31=StringVar()
file31.set(savedfile[89])
Entry(secondpage1,width=13,textvariable=file31).grid(row=19,column=5)
Label(secondpage1,text='.').grid(row=19,column=6)
file32=StringVar()
file32.set(savedfile[90])
Entry(secondpage1,width=3,textvariable=file32).grid(row=19,column=7)
#2

########################### Controls page	Third page
thirdpage1=Frame(root)
button1=StringVar()
button1.set(savedfile[16])
Entry(thirdpage1,width=13,textvariable=button1).grid(row=0,column=0)
Label(thirdpage1,text='Browsing').grid(row=0,column=1)

button2=StringVar()
button2.set(savedfile[17])
Entry(thirdpage1,width=13,textvariable=button2).grid(row=2,column=0)
Label(thirdpage1,text='Submitting').grid(row=2,column=1)

button3=StringVar()
button3.set(savedfile[18])
Entry(thirdpage1,width=13,textvariable=button3).grid(row=3,column=0)
Label(thirdpage1,text='Execute notes').grid(row=3,column=1)

button4=StringVar()
button4.set(savedfile[19])
Entry(thirdpage1,width=13,textvariable=button4).grid(row=4,column=0)
Label(thirdpage1,text='Saving and switching').grid(row=4,column=1)

button5=StringVar()
button5.set(savedfile[20])
Entry(thirdpage1,width=13,textvariable=button5).grid(row=5,column=0)
Label(thirdpage1,text='Quit').grid(row=5,column=1)

button6=StringVar()
button6.set(savedfile[21])
Entry(thirdpage1,width=13,textvariable=button6).grid(row=6,column=0)
Label(thirdpage1,text='Open').grid(row=6,column=1)

button7=StringVar()
button7.set(savedfile[22])
Entry(thirdpage1,width=13,textvariable=button7).grid(row=7,column=0)
Label(thirdpage1,text='Xmgrace').grid(row=7,column=1)

button8=StringVar()
button8.set(savedfile[23])
Entry(thirdpage1,width=13,textvariable=button8).grid(row=8,column=0)
Label(thirdpage1,text='VMD').grid(row=8,column=1)

button9=StringVar()
button9.set(savedfile[24])
Entry(thirdpage1,width=13,textvariable=button9).grid(row=9,column=0)
Label(thirdpage1,text='Preferences').grid(row=9,column=1)

button10=StringVar()
button10.set(savedfile[25])
Entry(thirdpage1,width=13,textvariable=button10).grid(row=10,column=0)
Label(thirdpage1,text='About').grid(row=10,column=1)

button11=StringVar()
button11.set(savedfile[26])
Entry(thirdpage1,width=13,textvariable=button11).grid(row=11,column=0)
Label(thirdpage1,text='Manual').grid(row=11,column=1)

button12=StringVar()
button12.set(savedfile[27])
Entry(thirdpage1,width=13,textvariable=button12).grid(row=12,column=0)
Label(thirdpage1,text='Calculator').grid(row=12,column=1)

button13=StringVar()
button13.set(savedfile[28])
Entry(thirdpage1,width=13,textvariable=button13).grid(row=13,column=0)
Label(thirdpage1,text='Find comparison').grid(row=13,column=1)

button14=StringVar()
button14.set(savedfile[29])
Entry(thirdpage1,width=13,textvariable=button14).grid(row=14,column=0)
Label(thirdpage1,text='Next file').grid(row=14,column=1)

button15=StringVar()
button15.set(savedfile[30])
Entry(thirdpage1,width=13,textvariable=button15).grid(row=15,column=0)
Label(thirdpage1,text='Previous file').grid(row=15,column=1)

button16=StringVar()
button16.set(savedfile[31])
Entry(thirdpage1,width=13,textvariable=button16).grid(row=16,column=0)
Label(thirdpage1,text='Up NPZ Option').grid(row=16,column=1)

button17=StringVar()
button17.set(savedfile[32])
Entry(thirdpage1,width=13,textvariable=button17).grid(row=17,column=0)
Label(thirdpage1,text='Down NPZ Option').grid(row=17,column=1)

button18=StringVar()
button18.set(savedfile[33])
Entry(thirdpage1,width=13,textvariable=button18).grid(row=18,column=0)
Label(thirdpage1,text='Right NPZ Option').grid(row=18,column=1)

button19=StringVar()
button19.set(savedfile[34])
Entry(thirdpage1,width=13,textvariable=button19).grid(row=19,column=0)
Label(thirdpage1,text='Left NPZ Option').grid(row=19,column=1)

button20=StringVar()
button20.set(savedfile[35])
Entry(thirdpage1,width=13,textvariable=button20).grid(row=20,column=0)
Label(thirdpage1,text='Add to modes').grid(row=20,column=1)

button21=StringVar()
button21.set(savedfile[36])
Entry(thirdpage1,width=13,textvariable=button21).grid(row=21,column=0)
Label(thirdpage1,text='Subtract from modes').grid(row=21,column=1)

button22=StringVar()
button22.set(savedfile[37])
Entry(thirdpage1,width=13,textvariable=button22).grid(row=22,column=0)
Label(thirdpage1,text='Right on main tab').grid(row=22,column=1)

button23=StringVar()
button23.set(savedfile[38])
Entry(thirdpage1,width=13,textvariable=button23).grid(row=23,column=0)
Label(thirdpage1,text='Left on main tab').grid(row=23,column=1)

button24=StringVar()
button24.set(savedfile[39])
Entry(thirdpage1,width=13,textvariable=button24).grid(row=24,column=0)
Label(thirdpage1,text='Stat. PDB').grid(row=24,column=1)

button25=StringVar()
button25.set(savedfile[40])
Entry(thirdpage1,width=13,textvariable=button25).grid(row=25,column=0)
Label(thirdpage1,text='Stat. NPZ').grid(row=25,column=1)



#############################	MISC PAGE
fourthpage1=Frame(root)

Label(fourthpage1,text='User Interface',font='Times 14 underline').grid(row=5,column=1)
startpage=StringVar()
startpage.set(savedfile[8])
Radiobutton(fourthpage1,value=0,variable=startpage).grid(row=6,column=1)
Label(fourthpage1,text='New').grid(row=6,column=2)
Radiobutton(fourthpage1,value=1,variable=startpage).grid(row=7,column=1)
Label(fourthpage1,text='Old').grid(row=7,column=2)

Label(fourthpage1,text='Auto-name',font='Times 14 underline').grid(row=5,column=5)
autoname=StringVar()
autoname.set(savedfile[15])
Radiobutton(fourthpage1,value=1,variable=autoname).grid(row=6,column=5)
Label(fourthpage1,text='Yes').grid(row=6,column=6)
Radiobutton(fourthpage1,value=0,variable=autoname).grid(row=7,column=5)
Label(fourthpage1,text='No').grid(row=7,column=6)

Label(fourthpage1,text='Show Results',font='Times 14 underline').grid(row=5,column=8)
showresults=StringVar()
showresults.set(savedfile[13])
Radiobutton(fourthpage1,value=1,variable=showresults).grid(row=6,column=8)
Label(fourthpage1,text='Yes').grid(row=6,column=9)
Radiobutton(fourthpage1,value=0,variable=showresults).grid(row=7,column=8)
Label(fourthpage1,text='No').grid(row=7,column=9)



#############################	COMMANDS

def save(event=None):
	fout=open(path+'savefile.txt','w')
	fout.write(nummode.get()+"""
"""+modeens.get()+"""
"""+confens.get()+"""
"""+rmsdens.get()+"""
"""+modetra.get()+"""
"""+steptra.get()+"""
"""+rmsdtra.get()+"""
"""+massnomass.get()+"""
"""+startpage.get()+"""
"""+gammacutoff.get()+"""
"""+cutoff1.get()+"""
"""+gamma2.get()+"""
"""+cutoff2.get()+"""
"""+showresults.get()+"""
"""+coordset.get()+"""
"""+autoname.get()+"""
"""+button1.get()+"""
"""+button2.get()+"""
"""+button3.get()+"""
"""+button4.get()+"""
"""+button5.get()+"""
"""+button6.get()+"""
"""+button7.get()+"""
"""+button8.get()+"""
"""+button9.get()+"""
"""+button10.get()+"""
"""+button11.get()+"""
"""+button12.get()+"""
"""+button13.get()+"""
"""+button14.get()+"""
"""+button15.get()+"""
"""+button16.get()+"""
"""+button17.get()+"""
"""+button18.get()+"""
"""+button19.get()+"""
"""+button20.get()+"""
"""+button21.get()+"""
"""+button22.get()+"""
"""+button23.get()+"""
"""+button24.get()+"""
"""+button25.get()+"""
"""+folder1.get()+"""
"""+folder2.get()+"""
"""+folder3.get()+"""
"""+folder4.get()+"""
"""+folder5.get()+"""
"""+folder6.get()+"""
"""+folder7.get()+"""
"""+folder8.get()+"""
"""+folder9.get()+"""
"""+folder10.get()+"""
"""+folder11.get()+"""
"""+folder12.get()+"""
"""+folder13.get()+"""
"""+folder14.get()+"""
"""+folder15.get()+"""
"""+folder16.get()+"""
"""+folder17.get()+"""
"""+folder18.get()+"""
"""+file1.get()+"""
"""+file2.get()+"""
"""+file3.get()+"""
"""+file4.get()+"""
"""+file5.get()+"""
"""+file6.get()+"""
"""+file7.get()+"""
"""+file8.get()+"""
"""+file9.get()+"""
"""+file10.get()+"""
"""+file11.get()+"""
"""+file12.get()+"""
"""+file13.get()+"""
"""+file14.get()+"""
"""+file15.get()+"""
"""+file16.get()+"""
"""+file17.get()+"""
"""+file18.get()+"""
"""+file19.get()+"""
"""+file20.get()+"""
"""+file21.get()+"""
"""+file22.get()+"""
"""+file23.get()+"""
"""+file24.get()+"""
"""+file25.get()+"""
"""+file26.get()+"""
"""+file27.get()+"""
"""+file28.get()+"""
"""+file29.get()+"""
"""+file30.get()+"""
"""+file31.get()+"""
"""+file32.get()+"""
"""+gammadistdep.get()+"""
"""+pagenumber.get()+"""
""")
	fout.close()
def default(event=None):
	nummode.set('20')
	modeens.set('7,8')
	confens.set('12')
	rmsdens.set('3.0')
	modetra.set('7')
	steptra.set('5')
	rmsdtra.set('3.0')
	massnomass.set('0')
	startpage.set('0')
	gammacutoff.set('0')
	cutoff1.set('100.0')
	gamma2.set('1.0')
	cutoff2.set('13.0')
	showresults.set('0')
	coordset.set('1')
	autoname.set('1')
	button1.set('Control-b')
	button2.set('Return')
	button3.set('Control-e')
	button4.set('Control-s')
	button5.set('Control-q')
	button6.set('Control-Shift-O')
	button7.set('Control-Shift-X')
	button8.set('Control-Shift-V')
	button9.set('Control-i')
	button10.set('Control-a')
	button11.set('Control-m')
	button12.set('Control-Shift-C')
	button13.set('Control-f')
	button14.set('Control-n')
	button15.set('Control-p')
	button16.set('Control-Up')
	button17.set('Control-Down')
	button18.set('Control-Right')
	button19.set('Control-Left')
	button20.set('Up')
	button21.set('Down')
	button22.set('')
	button23.set('')
	button24.set('')
	button25.set('')
	folder1.set('Ca_ANM')
	folder2.set('Ca_GNM')
	folder3.set('Heavy_ANM')
	folder4.set('Heavy_GNM')
	folder5.set('All_ANM')
	folder6.set('All_GNM')
	folder7.set('Backbone_ANM')
	folder8.set('Backbone_GNM')
	folder9.set('Sidechain_ANM')
	folder10.set('Sidechain_GNM')
	folder11.set('Correlation')
	folder12.set('SqFlucts')
	folder13.set('Overlap')
	folder14.set('Modes')
	folder15.set('Collectivity')
	folder16.set('Temp')
	folder17.set('PhiPsi')
	folder18.set('NMD')
	file1.set('_correlation')
	file2.set('txt')
	file3.set('_correlation_plot')
	file4.set('png')
	file5.set('_sqflucts')
	file6.set('txt')
	file7.set('_sqflucts')
	file8.set('png')
	file9.set('_overlap')
	file10.set('txt')
	file11.set('_overlap')
	file12.set('png')
	file13.set('_overlap_table')
	file14.set('txt')
	file15.set('_overlap_table')
	file16.set('png')
	file17.set('_modes')
	file18.set('txt')
	file19.set('_mode')
	file20.set('png')
	file21.set('_collectivity')
	file22.set('txt')
	file23.set('_TempFactors')
	file24.set('txt')
	file25.set('average')
	file26.set('txt')
	file27.set('_sample')
	file28.set('_traverse')
	file29.set('')
	file30.set('')
	file31.set('_FractOfVariances')
	file32.set('png')
	pagenumber.set('1')
	gammadistdep.set('-2')

def quit(event=None):
	root.destroy()
try:
	root.bind('<'+savedfile[20]+'>',quit)
except:
	mer=0
try:
	root.bind('<'+savedfile[19]+'>',save)
except:
	mer=0
def clear():
	firstpage1.pack_forget()
	secondpage1.pack_forget()
	thirdpage1.pack_forget()
	fourthpage1.pack_forget()

def firstpage():
	clear()
	pagenumber.set('1')
	parabutton1.config(relief=FLAT,bg='gray85')
	filenamebutton1.config(relief=SUNKEN,bg='gray70')
	controlsbutton1.config(relief=SUNKEN,bg='gray70')
	miscbutton1.config(relief=SUNKEN,bg='gray70')
	firstpage1.pack(side='left')
def secondpage():
	clear()
	pagenumber.set('2')
	filenamebutton1.config(relief=FLAT,bg='gray85')
	parabutton1.config(relief=SUNKEN,bg='gray70')
	miscbutton1.config(relief=SUNKEN,bg='gray70')
	controlsbutton1.config(relief=SUNKEN,bg='gray70')
	secondpage1.pack(side='left')
def thirdpage():
	clear()
	pagenumber.set('3')
	controlsbutton1.config(relief=FLAT,bg='gray85')
	miscbutton1.config(relief=SUNKEN,bg='gray70')
	parabutton1.config(relief=SUNKEN,bg='gray70')
	filenamebutton1.config(relief=SUNKEN,bg='gray70')
	thirdpage1.pack(side='left')
def fourthpage():
	clear()
	pagenumber.set('4')
	miscbutton1.config(relief=FLAT,bg='gray85')
	filenamebutton1.config(relief=SUNKEN,bg='gray70')
	controlsbutton1.config(relief=SUNKEN,bg='gray70')
	parabutton1.config(relief=SUNKEN,bg='gray70')
	fourthpage1.pack(side='left')
#
Button(firstpage1,text='Save',command=save).grid(row=6,column=3,rowspan=2,columnspan=2)
Button(firstpage1,text='Default',command=default).grid(row=6,column=5,rowspan=2)
Button(firstpage1,text='Quit',command=quit).grid(row=6,column=6,rowspan=2,columnspan=2)
#
Button(secondpage1,text='Save',command=save).grid(row=20,column=0)
Button(secondpage1,text='Default',command=default).grid(row=20,column=2)
Button(secondpage1,text='Quit',command=quit).grid(row=20,column=5)
#
Button(thirdpage1,text='Save',command=save).grid(row=26,column=0)
Button(thirdpage1,text='Default',command=default).grid(row=26,column=1)
Button(thirdpage1,text='Quit',command=quit).grid(row=26,column=2)
#
Button(fourthpage1,text='Save',command=save).grid(row=9,column=3,rowspan=2,columnspan=2)
Button(fourthpage1,text='Default',command=default).grid(row=9,column=5,rowspan=2)
Button(fourthpage1,text='Quit',command=quit).grid(row=9,column=6,rowspan=2,columnspan=2)
#

def pagenumberpage():
	if pagenumber.get()=='2':
		secondpage()
	elif pagenumber.get()=='3':
		thirdpage()
	elif pagenumber.get()=='4':
		fourthpage()
	else:
		firstpage()
def pagenumberright(event=None):
	if pagenumber.get()=='4':
		pagenumber.set('1')
	else:
		pagenumber.set(str(int(pagenumber.get())+1))
	pagenumberpage()
def pagenumberleft(event=None):
	if pagenumber.get()=='1':
		pagenumber.set('4')
	else:
		pagenumber.set(str(int(pagenumber.get())-1))
	pagenumberpage()
try:
	root.bind('<'+savedfile[37]+'>',pagenumberright)
except:
	mer=0
try:
	root.bind('<'+savedfile[38]+'>',pagenumberleft)
except:
	mer=0
pagenumber.set(savedfile[92])
pagenumberpage()
root.mainloop()
