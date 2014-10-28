path="/usr/share/noma/"

from Tkinter import *
import tkFileDialog
import os
import time
import maincalculation
import sidecalculation
def readingsavedfile():
	hiddennomapath=os.path.join(os.path.expanduser('~'),'.noma/savefile.txt')
	try:
		fin = open(hiddennomapath,'r')
	except(IOError):
		try:
			os.makedirs(hiddennomapath[:-12])
		except (OSError):
			mer = 0
		os.system('noma default')
		fin = open(hiddennomapath,'r')
	global savedfile
	savedfile=fin.readlines()
	i=0
	a=len(savedfile)
	while i<a:
		savedfile[i]=savedfile[i][:-1]
		i+=1
	fin.close()
readingsavedfile()
def filenamefromterminal():
	hiddennomapath=os.path.join(os.path.expanduser('~'),'.noma/thefilename.txt')
	try:
		fin = open(hiddennomapath,'r')
		for line in fin:
			pair = line.split()
			newfilename=pair[0]
		if '.pdb' in newfilename:
			pdbfilename.set(newfilename)
		elif '.npz' in newfilename:
			npzfilename.set(newfilename)
			modelpage()
	except:
		mer=0

def maincalc1(event=None):
	root.config(cursor='watch')
	root.update()
	readingsavedfile()
	simulationinfo.set('Submitted '+pdbfilename.get()+' at '+time.asctime(time.localtime(time.time())))
	root.update_idletasks()
	a=[None]*2
	a=maincalculation.corepagecalculation(pdbfilename.get(),selatom_opt.cget('text'),noma_opt.cget('text'),nummodes.get(),savedfile[9],savedfile[10],savedfile[11],savedfile[12],savedfile[13],var10.get(),var11.get(),var12.get(),var13.get(),savedfile[7],var14.get(),modeens.get(),confens.get(),rmsdens.get(),var15.get(),modetra.get(),steptra.get(),rmsdtra.get(),savedfile[14],savedfile[41],savedfile[42],savedfile[43],savedfile[44],savedfile[45],savedfile[46],savedfile[47],savedfile[48],savedfile[49],savedfile[50], savedfile[58], savedfile[54], savedfile[55], savedfile[88], savedfile[87], savedfile[75], savedfile[76], savedfile[79], savedfile[80], savedfile[85], savedfile[86], crosscorr=var16.get(), corrfolder=savedfile[51], corrname=savedfile[59], corrend=savedfile[60], compmode01=compmode3.get(), compmode02=compmode4.get(), sqflucts=var17.get(), sqfluctsfolder=savedfile[52], sqfluctsname=savedfile[63], sqfluctsend=savedfile[64], separatevar1=sepchain.get(), temfac=var18.get(), temfacfolder=savedfile[56], temfacname=savedfile[81], temfacend=savedfile[82], fracovar=var19.get(), fraconame=savedfile[89], fracoend=savedfile[90], ovlap=var20.get(), ovlapfold=savedfile[53], ovlapname=savedfile[69], ovlapend=savedfile[70], ovlaptab=var21.get(), ovlaptabname=savedfile[73], ovlaptabend=savedfile[74], comppdbfilename=comparepdbfilename.get())# add savedfild[14] for modelnumber
	simulationinfo.set(a[0])
	if a[1]!='nofile':
		npzfilename.set(a[1])
	if a[2]!='nocoll':
		modelpagemode.set(a[2])
	root.config(cursor='')
def premaincalc1(event=None):
	if var0.get() == 1:
		selatom_var.set(selatom[0])
		noma_var.set(noma[0])
		maincalc1()
	if var1.get() == 1:
		selatom_var.set(selatom[0])
		noma_var.set(noma[1])
		maincalc1()
	if var2.get() == 1:
		selatom_var.set(selatom[1])
		noma_var.set(noma[0])
		maincalc1()
	if var3.get() == 1:
		selatom_var.set(selatom[1])
		noma_var.set(noma[1])
		maincalc1()
	if var4.get() == 1:
		selatom_var.set(selatom[2])
		noma_var.set(noma[0])
		maincalc1()
	if var5.get() == 1:
		selatom_var.set(selatom[2])
		noma_var.set(noma[1])
		maincalc1()
	if var6.get() == 1:
		selatom_var.set(selatom[3])
		noma_var.set(noma[0])
		maincalc1()
	if var7.get() == 1:
		selatom_var.set(selatom[3])
		noma_var.set(noma[1])
		maincalc1()
	if var8.get() == 1:
		selatom_var.set(selatom[4])
		noma_var.set(noma[0])
		maincalc1()
	if var9.get() == 1:
		selatom_var.set(selatom[4])
		noma_var.set(noma[1])
		maincalc1()

def maincalc2(event=None):
	root.config(cursor='watch')
	root.update()
	readingsavedfile()
	simulationinfo.set('Submitted '+pdbfilename.get()+' at '+time.asctime(time.localtime(time.time())))
	root.update_idletasks()
	a=[None]*3
	a=maincalculation.corepagecalculation(pdbfilename.get(),selatom_opt.cget('text'),noma_opt.cget('text'),nummodes.get(),savedfile[9],savedfile[10],savedfile[11],savedfile[12],savedfile[13],1,1,1,1,savedfile[7],0,modeens.get(),confens.get(),rmsdens.get(),0,modetra.get(),steptra.get(),rmsdtra.get(),'1', 'Ca_ANM', 'Ca_GNM', 'Heavy_ANM', 'Heavy_GNM', 'All_ANM' , 'All_GNM', 'Backbone_ANM', 'Backbone_GNM', 'Sidechain_ANM', 'Sidechain_GNM', 'NMD', 'Modes', 'Collectivity', savedfile[88], savedfile[87], savedfile[75], savedfile[76], savedfile[79], savedfile[80], savedfile[85], savedfile[86])
	simulationinfo.set(a[0])
	npzfilename.set(a[1])
	modelpagemode.set(a[2])
	root.config(cursor='')

def calcfromnotespage(event=None):
	if pagenumber.get()==6:
		switchorsave()
		notescalcfile=os.path.join(os.path.expanduser('~'),'.noma/notes.txt')
		fin = open(notescalcfile,'r')
		t1 = 0
		for line in fin:
			pair=line.split()
			if pair[0]=='#!':
				break
			pdbfilename.set(pair[0])
			if pair[1]=='C-alpha' or pair[1]=='ca' or pair[1]=='CA':
				selatom_var.set(selatom[0])
			elif pair[1]=='Heavy' or pair[1]=='heavy' or pair[1]=='noh':
				selatom_var.set(selatom[1])
			elif pair[1]=='All' or pair[1]=='all':
				selatom_var.set(selatom[2])
			elif pair[1]=='Backbone' or pair[1]=='backbone' or pair[1]=='bb':
				selatom_var.set(selatom[3])
			elif pair[1]=='Sidechain' or pair[1]=='sidechain' or pair[1]=='sc':
				selatom_var.set(selatom[4])
			if pair[2]=='ANM' or pair[2]=='anm':
				noma_var.set(noma[0])
			elif pair[2]=='GNM' or pair[2]=='gnm':
				noma_var.set(noma[1])
			nummodes.set(pair[3])
			try:
				if pair[4]=='new':
					maincalc1()
				else:
					maincalc2()
			except:
				maincalc2()
		fin.close()



root = Tk()
root.title("NOrmal Mode Analysis")
root.wm_iconbitmap("@"+path+"NOMA.xbm")
root["padx"]=10
root["pady"]=20
try:
	import prody
except(ImportError):
	import tkMessageBox
	tkMessageBox.askokcancel("ProDy","Check to see if you have to ProDy (1.1.0) package.")
def pdbbutton(event=None):
	readingsavedfile()
	if savedfile[8]=='0':
		firstpage()
	elif savedfile[8]=='1':
		simplepage()
def npzbutton(event=None):
	modelpage()
def notesbutton(event=None):
	notespage()
toppage1=Frame(root)
toppage1.pack(side='top')
pdbbutton1=Button(toppage1,text='PDB File',relief=FLAT,command=pdbbutton,bg='gray85')
pdbbutton1.pack(side='left')
npzbutton1=Button(toppage1,text='NPZ File',relief=SUNKEN,command=npzbutton,bg='gray70')
npzbutton1.pack(side='left')
notesbutton1=Button(toppage1,text='Notes',relief=SUNKEN,command=notesbutton,bg='gray70')
notesbutton1.pack(side='left')

toppage2=Frame(root)
Label(toppage2,text="Enter PDB file: ").pack(side='left')
pdbfilename=StringVar()
Entry(toppage2,width=30,textvariable=pdbfilename).pack(side='left')
def ldtmp1(event=None):
	filename1 = tkFileDialog.Open(initialdir='~',filetypes=[('PDB','.pdb'),('PDB','.pdb.gz'),('all files','*')]).show()
	if filename1 !='':
		pdbfilename.set(filename1)
Button(toppage2, text = "Browse", command = ldtmp1, width = 8,underline=0).pack(side='left')
############################################################
firstpage1 = Frame(root)
var0 = IntVar()
Checkbutton(firstpage1, variable=var0).grid(row=0,column=0)
Label(firstpage1,text='Ca ANM').grid(row=0,column=1)
var1 = IntVar()
Checkbutton(firstpage1, variable=var1).grid(row=0,column=2)
Label(firstpage1,text='Ca GNM').grid(row=0,column=3)
var2 = IntVar()
Checkbutton(firstpage1, variable=var2).grid(row=1,column=0)
Label(firstpage1,text='Heavy ANM').grid(row=1,column=1)
var3 = IntVar()
Checkbutton(firstpage1, variable=var3).grid(row=1,column=2)
Label(firstpage1,text='Heavy GNM').grid(row=1,column=3)
var4 = IntVar()
Checkbutton(firstpage1, variable=var4).grid(row=2,column=0)
Label(firstpage1,text='All ANM').grid(row=2,column=1)
var5 = IntVar()
Checkbutton(firstpage1, variable=var5).grid(row=2,column=2)
Label(firstpage1,text='All GNM').grid(row=2,column=3)
var6 = IntVar()
Checkbutton(firstpage1, variable=var6).grid(row=3,column=0)
Label(firstpage1,text='Backbone ANM').grid(row=3,column=1)
var7 = IntVar()
Checkbutton(firstpage1, variable=var7).grid(row=3,column=2)
Label(firstpage1,text='Backbone GNM').grid(row=3,column=3)
var8 = IntVar()
Checkbutton(firstpage1, variable=var8).grid(row=4,column=0)
Label(firstpage1,text='Sidechain ANM').grid(row=4,column=1)
var9 = IntVar()
Checkbutton(firstpage1, variable=var9).grid(row=4,column=2)
Label(firstpage1,text='Sidechain GNM').grid(row=4,column=3)

Label(firstpage1,text='       ').grid(row=0,column=4)

############################################################
secondpage1 = Frame(root)
Label(secondpage1,text='       ').grid(row=0,column=1)
var16 = IntVar()
Checkbutton(secondpage1,variable=var16).grid(row=0,column=2)
Label(secondpage1, text='Cross-Correlation').grid(row=0,column=3)

var17 = IntVar()
Checkbutton(secondpage1,variable=var17).grid(row=0,column=4)
Label(secondpage1, text='Square Fluctuation').grid(row=0,column=5)
sepchain=StringVar()
sepchain.set('0')
Checkbutton(secondpage1,variable=sepchain,text='Split chain').grid(row=1,column=5)
var18 = IntVar()
Checkbutton(secondpage1,variable=var18).grid(row=2,column=2)
Label(secondpage1, text='Temp Factors').grid(row=2,column=3)

var19 = IntVar()
Checkbutton(secondpage1,variable=var19).grid(row=2,column=4)
Label(secondpage1, text='Fraction of Variance').grid(row=2,column=5)

var20 = IntVar()
Checkbutton(secondpage1,variable=var20).grid(row=3,column=2)
Label(secondpage1, text='Overlap').grid(row=3,column=3)

var21 = IntVar()
Checkbutton(secondpage1,variable=var21).grid(row=3,column=4)
Label(secondpage1, text='Overlap Table').grid(row=3,column=5)

Label(secondpage1,text='       ').grid(row=0,column=6)


secondpage2 = Frame(root)
compmode3=StringVar()
compmode3.set("7")
compmode4=StringVar()
compmode4.set("15")
Label(secondpage2,text='Evaluate mode ').pack(side='left')
Entry(secondpage2,width=2,textvariable=compmode3).pack(side='left')
Label(secondpage2,text=' through mode ').pack(side='left')
Entry(secondpage2,width=2,textvariable=compmode4).pack(side='left')

secondpage3 = Frame(root)
Label(secondpage3,text="Compare with: ").pack(side='left')
comparepdbfilename=StringVar()
Entry(secondpage3,width=30,textvariable=comparepdbfilename).pack(side='left')
def ldtmp6(event=None):
	filename6 = tkFileDialog.Open(initialdir='~',filetypes=[('PDB','.pdb'),('PDB','.pdb.gz'),('all files','*')]).show()
	if filename6 !='':
		comparepdbfilename.set(filename6)
Button(secondpage3, text = "Browse", command = ldtmp6, width = 8,underline=0).pack(side='left')
############################################################
############################################################
thirdpage1 = Frame(root)
Label(thirdpage1,text='       ').grid(row=0,column=1)
var10 = IntVar()
var10.set(1)
Checkbutton(thirdpage1, variable=var10).grid(row=0,column=2)
Label(thirdpage1,text='Save modes').grid(row=0,column=3)
var11 = IntVar()
var11.set(1)
Checkbutton(thirdpage1, variable=var11).grid(row=1,column=2)
Label(thirdpage1,text='Create NMD file').grid(row=1,column=3)
var12 = IntVar()
var12.set(1)
Checkbutton(thirdpage1, variable=var12).grid(row=2,column=2)
Label(thirdpage1,text='Create Model file').grid(row=2,column=3)
nummodes=StringVar()
nummodes.set(savedfile[0])
Entry(thirdpage1,width=2,textvariable=nummodes).grid(row=3,column=2)
Label(thirdpage1,text='Calculated modes').grid(row=3,column=3)
var13 = IntVar()
var13.set(1)
Checkbutton(thirdpage1, variable=var13).grid(row=4,column=2)
Label(thirdpage1,text='Collectivity').grid(row=4,column=3)

var14 = IntVar()
Checkbutton(thirdpage1, variable=var14).grid(row=0,rowspan=2,column=4)
Label(thirdpage1,text="""Sample
Modes""").grid(row=0,rowspan=2,column=5)
modeens=StringVar()
modeens.set(savedfile[1])
Entry(thirdpage1,width=4,textvariable=modeens).grid(row=2,column=5)
Label(thirdpage1,text='modes').grid(row=2,column=6)
confens=StringVar()
confens.set(savedfile[2])
Entry(thirdpage1,width=2,textvariable=confens).grid(row=3,column=5)
Label(thirdpage1,text='n_confs').grid(row=3,column=6)
rmsdens=StringVar()
rmsdens.set(savedfile[3])
Entry(thirdpage1,width=3,textvariable=rmsdens).grid(row=4,column=5)
Label(thirdpage1,text=u'rmsd (\u00C5)').grid(row=4,column=6)

var15 = IntVar()
Checkbutton(thirdpage1, variable=var15).grid(row=0,rowspan=2,column=7)
Label(thirdpage1,text="""Traverse
Mode""").grid(row=0,rowspan=2,column=8)
modetra=StringVar()
modetra.set(savedfile[4])
Entry(thirdpage1,width=2,textvariable=modetra).grid(row=2,column=8)
Label(thirdpage1,text='mode').grid(row=2,column=9)
steptra=StringVar()
steptra.set(savedfile[5])
Entry(thirdpage1,width=3,textvariable=steptra).grid(row=3,column=8)
Label(thirdpage1,text='n_steps').grid(row=3,column=9)
rmsdtra=StringVar()
rmsdtra.set(savedfile[6])
Entry(thirdpage1,width=3,textvariable=rmsdtra).grid(row=4,column=8)
Label(thirdpage1,text=u'rmsd (\u00C5)').grid(row=4,column=9)

Label(thirdpage1,text='       ').grid(row=0,column=10)
Button(thirdpage1,text="""


Submit


""",command=premaincalc1).grid(row=0,rowspan=5,column=11)
simulationinfo=StringVar()
thirdpage2=Frame(root)
Label(thirdpage2,textvariable=simulationinfo).pack(side='left')
############################################################
############################################################
############################################################
simplepage1=Frame(root)
Label(simplepage1,text='Selection of atoms: ').pack(side='left')
selatom=('C-alpha','Heavy','All','Backbone','Sidechain')
selatom_var = StringVar()
selatom_var.set(selatom[0])
selatom_opt=OptionMenu(simplepage1,selatom_var,*selatom)
selatom_opt.pack(side='left')

simplepage2=Frame(root)
Label(simplepage2,text="Normal Mode Analysis: ").pack(side='left')
noma=("Anisotropic Normal Mode","Gaussian Normal Mode")
noma_var = StringVar()
noma_var.set(noma[0])
noma_opt=OptionMenu(simplepage2,noma_var,*noma)
noma_opt.pack(side='left')

simplepage3 = Frame(root)
Label(simplepage3,text="Number of modes: ").pack(side='left')
Entry(simplepage3,width=4,textvariable=nummodes).pack(side='left')

simplepage4=Frame(root)
Button(simplepage4,text=' Submit ',command=maincalc2).pack(side='left')
simplepage5=Frame(root)
Label(simplepage5,textvariable=simulationinfo).pack(side='left')
############################################################
############################################################
############################################################
############################################################
def clearbottompage():
	correlationdatapage1.pack_forget()
	correlationdatapage2.pack_forget()
	correlationplotpage1.pack_forget()
	correlationplotpage2.pack_forget()
	sqfluctdatapage1.pack_forget()
	sqfluctdatapage2.pack_forget()
	sqfluctplotpage1.pack_forget()
	sqfluctplotpage2.pack_forget()
	optionsmenu.entryconfig(3,state='disabled')
	optionsmenu.entryconfig(4,state='disabled')
	overlappages1.pack_forget()
	overlapdatapage1.pack_forget()
	overlapdatapage2.pack_forget()
	overlapplotpage1.pack_forget()
	overlapplotpage2.pack_forget()
	overlaptabledatapage1.pack_forget()
	overlaptabledatapage2.pack_forget()
	overlaptableplotpage1.pack_forget()
	overlaptableplotpage2.pack_forget()
	modedatapage1.pack_forget()
	modedatapage2.pack_forget()
	modeplotpage1.pack_forget()
	modeplotpage2.pack_forget()
	collectivitydatapage1.pack_forget()
	collectivitydatapage2.pack_forget()
	tempfactorspage1.pack_forget()
	tempfactorspage2.pack_forget()
	viewnmdinvmdpage1.pack_forget()
	viewnmdinvmdpage2.pack_forget()
	fracofvarpage1.pack_forget()
	fracofvarpage2.pack_forget()
	calcphipsipage1.pack_forget()
	calcphipsipage2.pack_forget()
	saveconfirmation1.set("Type 'all' for all modes.")
	saveconfirmation2.set('')

def bottompage(event=None):
	readingsavedfile()
	if model_var.get()=='0':
		clearbottompage()
		correlationdatapage1.pack(side='top')
		correlationdatapage2.pack(side='top')
	elif model_var.get()=='1':
		clearbottompage()
		correlationplotpage1.pack(side='top')
		correlationplotpage2.pack(side='top')
	elif model_var.get()=='2':
		clearbottompage()
		sqfluctdatapage1.pack(side='top')
		sqfluctdatapage2.pack(side='top')
	elif model_var.get()=='3':
		clearbottompage()
		sqfluctplotpage1.pack(side='top')
		sqfluctplotpage2.pack(side='top')
	elif model_var.get()=='4':
		clearbottompage()
		optionsmenu.entryconfig(3,state='normal')
		optionsmenu.entryconfig(4,state='normal')
		overlappages1.pack(side='top')
		overlapdatapage1.pack(side='top')
		overlapdatapage2.pack(side='top')
	elif model_var.get()=='5':
		clearbottompage()
		optionsmenu.entryconfig(3,state='normal')
		optionsmenu.entryconfig(4,state='normal')
		overlappages1.pack(side='top')
		overlapplotpage1.pack(side='top')
		overlapplotpage2.pack(side='top')
	elif model_var.get()=='6':
		clearbottompage()
		optionsmenu.entryconfig(3,state='normal')
		optionsmenu.entryconfig(4,state='normal')
		overlappages1.pack(side='top')
		overlaptabledatapage1.pack(side='top')
		overlaptabledatapage2.pack(side='top')
	elif model_var.get()=='7':
		clearbottompage()
		optionsmenu.entryconfig(3,state='normal')
		optionsmenu.entryconfig(4,state='normal')
		overlappages1.pack(side='top')
		overlaptableplotpage1.pack(side='top')
		overlaptableplotpage2.pack(side='top')
	elif model_var.get()=='8':
		clearbottompage()
		modedatapage1.pack(side='top')
		modedatapage2.pack(side='top')
	elif model_var.get()=='9':
		clearbottompage()
		modeplotpage1.pack(side='top')
		modeplotpage2.pack(side='top')
	elif model_var.get()=='10':
		clearbottompage()
		collectivitydatapage1.pack(side='top')
		collectivitydatapage2.pack(side='top')
	elif model_var.get()=='11':
		clearbottompage()
		tempfactorspage1.pack(side='top')
		tempfactorspage2.pack(side='top')
	elif model_var.get()=='12':
		clearbottompage()
		viewnmdinvmdpage1.pack(side='top')
		viewnmdinvmdpage2.pack(side='top')
		if savedfile[15]=='1':
			find = 0					#
			a = npzfilename.get()
			while find < len(a):			#
				if a[-(find+1):-find] == '/':	#
					bgn = len(a)-find		#
					break				#
				else:					# helps in the
					find +=1			# saving of files
			try:						#
				name = a[bgn:-8]			#
			except (NameError):				#
				bgn = 0					#
				name = a[bgn:-8]			#
			bgn = a[:bgn]				# path for file
			nmdfilename.set(bgn+savedfile[58]+'/'+name+savedfile[87]+'.nmd')
	elif model_var.get()=='13':
		clearbottompage()
		fracofvarpage1.pack(side='top')
		fracofvarpage2.pack(side='top')
	elif model_var.get()=='14':
		clearbottompage()
		calcphipsipage1.pack(side='top')
		calcphipsipage2.pack(side='top')
		saveconfirmation2.set('Make sure PDB has chain identifiers.')
		if savedfile[15]=='1':
			find = 0					#
			a = npzfilename.get()
			while find < len(a):			#
				if a[-(find+1):-find] == '/':	#
					bgn = len(a)-find		#
					break				#
				else:					# helps in the
					find +=1			# saving of files
			try:						#
				name = a[bgn:-8]			#
			except (NameError):				#
				bgn = 0					#
				name = a[bgn:-8]			#
			bgn = a[:bgn]				# path for file
			phipsifilename.set(bgn+name+savedfile[85]+'.pdb')
	elif model_var.get()=='15':
		clearbottompage()
############################################################
############################################################
############################################################
############################################################
toppage3=Frame(root)
Label(toppage3,text="Enter NPZ file: ").pack(side='left')
npzfilename=StringVar()
Entry(toppage3,width=30,textvariable=npzfilename).pack(side='left')
def ldtmp2(event=None):
	filename2 = tkFileDialog.Open(initialdir='~',filetypes=[('Model','.npz'),('ANM Model','.anm.npz'),('GNM Model','.gnm.npz'),('all files','*')]).show()
	if filename2 !='':
		npzfilename.set(filename2)
Button(toppage3, text = "Browse", command = ldtmp2, width = 8,underline=0).pack(side='left')

modelpage1=Frame(root)
model_var = StringVar()

Radiobutton(modelpage1,value=0,variable=model_var,command=bottompage).grid(row=0,column=0)
def model0():
	model_var.set('0')
	bottompage()
Button(modelpage1,width=20,text='Cross-Correlation Data',command=model0,relief=FLAT).grid(row=0,column=1)
correlationdatapage1=Frame(root)
Label(correlationdatapage1,text='Mode: ').pack(side='left')
modelpagemode=StringVar()
modelpagemode.set('all')
Entry(correlationdatapage1,width=4,textvariable=modelpagemode).pack(side='left')
saveconfirmation1=StringVar()
saveconfirmation2=StringVar()
def correlationdatacommand(event=None):
	readingsavedfile()
	sidecalculation.correlationdata(npzfilename.get(), modelpagemode.get(), savedfile[13],savedfile[51],savedfile[59],savedfile[60])
	saveconfirmation1.set('File(s) saved in '+savedfile[51]+' folder.')
Button(correlationdatapage1,text=' Submit ',width=6,command=correlationdatacommand).pack(side='left')
correlationdatapage2=Frame(root)
Label(correlationdatapage2,textvariable=saveconfirmation1).pack(side='top')

Radiobutton(modelpage1,value=1,variable=model_var,command=bottompage).grid(row=0,column=2)
def model1():
	model_var.set('1')
	bottompage()
Button(modelpage1,width=20,text='Cross-Correlation Plot',command=model1,relief=FLAT).grid(row=0,column=3)
correlationplotpage1=Frame(root)
Label(correlationplotpage1,text='Mode: ').pack(side='left')
Entry(correlationplotpage1,width=4,textvariable=modelpagemode).pack(side='left')
def correlationplotcommand(event=None):
	readingsavedfile()
	sidecalculation.correlationplot(npzfilename.get(), modelpagemode.get(), savedfile[13],savedfile[51],savedfile[61],savedfile[62])
	saveconfirmation1.set('File(s) saved in '+savedfile[51]+' folder.')
Button(correlationplotpage1,text=' Submit ',width=6,command=correlationplotcommand).pack(side='left')
correlationplotpage2=Frame(root)
Label(correlationplotpage2,textvariable=saveconfirmation1).pack(side='top')

Radiobutton(modelpage1,value=2,variable=model_var,command=bottompage).grid(row=1,column=0)
def model2():
	model_var.set('2')
	bottompage()
Button(modelpage1,width=20,text='Square Fluctuation Data',command=model2,relief=FLAT).grid(row=1,column=1)
sqfluctdatapage1=Frame(root)
Label(sqfluctdatapage1,text='Mode: ').pack(side='left')
Entry(sqfluctdatapage1,width=4,textvariable=modelpagemode).pack(side='left')
def sqfluctdatacommand(event=None):
	readingsavedfile()
	sidecalculation.sqfluctdata(npzfilename.get(), modelpagemode.get(), savedfile[13],sepchain.get(),savedfile[52], savedfile[63], savedfile[64])
	saveconfirmation1.set('File(s) saved in '+savedfile[52]+' folder.')
Button(sqfluctdatapage1,text=' Submit ',width=6,command=sqfluctdatacommand).pack(side='left')
Checkbutton(sqfluctdatapage1,text='Separate chains',variable=sepchain).pack(side='left')
sqfluctdatapage2=Frame(root)
Label(sqfluctdatapage2,textvariable=saveconfirmation1).pack(side='top')

Radiobutton(modelpage1,value=3,variable=model_var,command=bottompage).grid(row=1,column=2)
def model3():
	model_var.set('3')
	bottompage()
Button(modelpage1,width=20,text='Square Fluctuation Plot',command=model3,relief=FLAT).grid(row=1,column=3)
sqfluctplotpage1=Frame(root)
Label(sqfluctplotpage1,text='Mode: ').pack(side='left')
Entry(sqfluctplotpage1,width=4,textvariable=modelpagemode).pack(side='left')
def sqfluctplotcommand(event=None):
	readingsavedfile()
	sidecalculation.sqfluctplot(npzfilename.get(), modelpagemode.get(), savedfile[13],savedfile[52], savedfile[65], savedfile[66])
	saveconfirmation1.set('File(s) saved in '+savedfile[52]+' folder.')
Button(sqfluctplotpage1,text=' Submit ',width=6,command=sqfluctplotcommand).pack(side='left')
sqfluctplotpage2=Frame(root)
Label(sqfluctplotpage2,textvariable=saveconfirmation1).pack(side='top')

overlappages1=Frame(root)
Label(overlappages1,text="Compare with: ").pack(side='left')
compnpzfilename=StringVar()
Entry(overlappages1,width=30,textvariable=compnpzfilename).pack(side='left')
def ldtmp3(event=None):
	filename3 = tkFileDialog.Open(initialdir='~',filetypes=[('Model','.npz'),('ANM Model','.anm.npz'),('GNM Model','.gnm.npz'),('all files','*')]).show()
	if filename3 !='':
		compnpzfilename.set(filename3)
Button(overlappages1, text = "Browse", command = ldtmp3, width = 8,underline=0).pack(side='left')

###############
def overlapcommand(event=None):
	readingsavedfile()
	sidecalculation.overlapall(model_var.get(),npzfilename.get(), compnpzfilename.get(), modelpagemode.get(), compmode1.get(), compmode2.get(), savedfile[13],savedfile[53], savedfile[67], savedfile[68], savedfile[69], savedfile[70], savedfile[71], savedfile[72], savedfile[73], savedfile[74])
	saveconfirmation1.set('File(s) saved in '+savedfile[53]+' folder.')
	saveconfirmation2.set('File saved in '+savedfile[53]+' folder.')
###############
Radiobutton(modelpage1,value=4,variable=model_var,command=bottompage).grid(row=2,column=0)
def model4():
	model_var.set('4')
	bottompage()
Button(modelpage1,width=20,text='Overlap Data',command=model4,relief=FLAT).grid(row=2,column=1)
overlapdatapage1=Frame(root)
Label(overlapdatapage1,text='Mode: ').pack(side='left')
Entry(overlapdatapage1,width=4,textvariable=modelpagemode).pack(side='left')
Button(overlapdatapage1,text=' Submit ',width=6,command=overlapcommand).pack(side='left')
overlapdatapage2=Frame(root)
Label(overlapdatapage2,textvariable=saveconfirmation1).pack(side='top')

Radiobutton(modelpage1,value=5,variable=model_var,command=bottompage).grid(row=2,column=2)
def model5():
	model_var.set('5')
	bottompage()
Button(modelpage1,width=20,text='Overlap Plot',command=model5,relief=FLAT).grid(row=2,column=3)
overlapplotpage1=Frame(root)
Label(overlapplotpage1,text='Mode: ').pack(side='left')
Entry(overlapplotpage1,width=4,textvariable=modelpagemode).pack(side='left')
Button(overlapplotpage1,text=' Submit ',width=6,command=overlapcommand).pack(side='left')
overlapplotpage2=Frame(root)
Label(overlapplotpage2,textvariable=saveconfirmation1).pack(side='top')

Radiobutton(modelpage1,value=6,variable=model_var,command=bottompage).grid(row=3,column=0)
def model6():
	model_var.set('6')
	bottompage()
Button(modelpage1,width=20,text='Overlap Table Data',command=model6,relief=FLAT).grid(row=3,column=1)
overlaptabledatapage1 = Frame(root)
compmode1=StringVar()
compmode1.set("7")
compmode2=StringVar()
compmode2.set("15")
Label(overlaptabledatapage1,text='Compare mode ').pack(side='left')
Entry(overlaptabledatapage1,width=2,textvariable=compmode1).pack(side='left')
Label(overlaptabledatapage1,text=' through mode ').pack(side='left')
Entry(overlaptabledatapage1,width=2,textvariable=compmode2).pack(side='left')
Label(overlaptabledatapage1,text=' in Overlap Table Data.').pack(side='left')
Button(overlaptabledatapage1,text=' Submit ',width=6,command=overlapcommand).pack(side='left')
overlaptabledatapage2=Frame(root)
Label(overlaptabledatapage2,textvariable=saveconfirmation2).pack(side='top')

Radiobutton(modelpage1,value=7,variable=model_var,command=bottompage).grid(row=3,column=2)
def model7():
	model_var.set('7')
	bottompage()
Button(modelpage1,width=20,text='Overlap Table Plot',command=model7,relief=FLAT).grid(row=3,column=3)
overlaptableplotpage1 = Frame(root)
Label(overlaptableplotpage1,text='Compare mode ').pack(side='left')
Entry(overlaptableplotpage1,width=2,textvariable=compmode1).pack(side='left')
Label(overlaptableplotpage1,text=' through mode ').pack(side='left')
Entry(overlaptableplotpage1,width=2,textvariable=compmode2).pack(side='left')
Label(overlaptableplotpage1,text=' in Overlap Table Plot.').pack(side='left')
Button(overlaptableplotpage1,text=' Submit ',width=6,command=overlapcommand).pack(side='left')
overlaptableplotpage2=Frame(root)
Label(overlaptableplotpage2,textvariable=saveconfirmation2).pack(side='top')

Radiobutton(modelpage1,value=8,variable=model_var,command=bottompage).grid(row=4,column=0)
def model8():
	model_var.set('8')
	bottompage()
Button(modelpage1,width=20,text='Modes Data',command=model8,relief=FLAT).grid(row=4,column=1)
modedatapage1=Frame(root)
Label(modedatapage1,text='Saves all eigenvectors and eigenvalues.').pack(side='left')
def modedatacommand(event=None):
	readingsavedfile()
	sidecalculation.modedata(npzfilename.get(),savedfile[13],savedfile[54], savedfile[75], savedfile[76])
	saveconfirmation2.set('File saved in '+savedfile[54]+' folder.')
Button(modedatapage1,text=' Submit ',width=6,command=modedatacommand).pack(side='left')
modedatapage2=Frame(root)
Label(modedatapage2,textvariable=saveconfirmation2).pack(side='top')

Radiobutton(modelpage1,value=9,variable=model_var,command=bottompage).grid(row=4,column=2)
def model9():
	model_var.set('9')
	bottompage()
Button(modelpage1,width=20,text='Modes Plot',command=model9,relief=FLAT).grid(row=4,column=3)
modeplotpage1=Frame(root)
Label(modeplotpage1,text='Mode: ').pack(side='left')
Entry(modeplotpage1,width=4,textvariable=modelpagemode).pack(side='left')
def modeplotcommand(event=None):
	readingsavedfile()
	sidecalculation.modeplot(npzfilename.get(), modelpagemode.get(), savedfile[13], savedfile[54], savedfile[77], savedfile[78])
	saveconfirmation1.set('File(s) saved in '+savedfile[54]+' folder.')
Button(modeplotpage1,text=' Submit ',width=6,command=modeplotcommand).pack(side='left')
modeplotpage2=Frame(root)
Label(modeplotpage2,textvariable=saveconfirmation1).pack(side='top')

Radiobutton(modelpage1,value=10,variable=model_var,command=bottompage).grid(row=5,column=0)
def model10():
	model_var.set('10')
	bottompage()
Button(modelpage1,width=20,text='Collectivity',command=model10,relief=FLAT).grid(row=5,column=1)
collectivitydatapage1=Frame(root)
Label(collectivitydatapage1,text='Saves collectivity.').pack(side='left')
def collectivitydatacommand(event=None):
	readingsavedfile()
	a=[None]*3
	a=sidecalculation.collectivitydata(npzfilename.get(),savedfile[13],savedfile[7],savedfile[55], savedfile[79], savedfile[80])
	saveconfirmation2.set("""File saved in """+savedfile[55]+""" folder.\n"""+a[1])
	modelpagemode.set(a[0])
Button(collectivitydatapage1,text=' Submit ',width=6,command=collectivitydatacommand).pack(side='left')
collectivitydatapage2=Frame(root)
Label(collectivitydatapage2,textvariable=saveconfirmation2).pack(side='top')

Radiobutton(modelpage1,value=11,variable=model_var,command=bottompage).grid(row=5,column=2)
def model11():
	model_var.set('11')
	bottompage()
Button(modelpage1,width=20,text='Temp Factors',command=model11,relief=FLAT).grid(row=5,column=3)
tempfactorspage1=Frame(root)
Label(tempfactorspage1,text='Saves temp factors.').pack(side='left')
def tempfactorsdatacommand(event=None):
	readingsavedfile()
	sidecalculation.tempfactorsdata(npzfilename.get(), savedfile[13],savedfile[56], savedfile[81],savedfile[82])
	saveconfirmation2.set('File saved in '+savedfile[56]+' folder.')
Button(tempfactorspage1,text=' Submit ',width=6,command=tempfactorsdatacommand).pack(side='left')
tempfactorspage2=Frame(root)
Label(tempfactorspage2,textvariable=saveconfirmation2).pack(side='top')

Radiobutton(modelpage1,value=12,variable=model_var,command=bottompage).grid(row=6,column=0)
def model12():
	model_var.set('12')
	bottompage()
Button(modelpage1,width=20,text='view NMD in VMD',command=model12,relief=FLAT).grid(row=6,column=1)
viewnmdinvmdpage1=Frame(root)
Label(viewnmdinvmdpage1,text="Enter NMD file: ").pack(side='left')
nmdfilename=StringVar()
Entry(viewnmdinvmdpage1,width=30,textvariable=nmdfilename).pack(side='left')
def ldtmp4(event=None):
	filename4 = tkFileDialog.Open(initialdir='~',filetypes=[('NMD','.nmd'),('all files','*')]).show()
	if filename4 !='':
		nmdfilename.set(filename4)
Button(viewnmdinvmdpage1, text = "Browse", command = ldtmp4, width = 8,underline=0).pack(side='left')
viewnmdinvmdpage2=Frame(root)
Label(viewnmdinvmdpage2,text='Hit submit to view the NMD in VMD.').pack(side='left')
def viewnmdinvmddata(event=None):
	fin = open(nmdfilename.get(),'r')
	firstline=fin.readline()
	fin.close()
	if firstline=='nmwiz_load '+nmdfilename.get()+"""
""":
		os.system('gnome-terminal -x bash -c "vmd -e '+nmdfilename.get()+';bash"')
	else:
		import tkMessageBox
		tkMessageBox.askokcancel("NMD","Open the NMD file and change the first line to the correct path and name of file.")
Button(viewnmdinvmdpage2,text=' Submit ',width=6,command=viewnmdinvmddata).pack(side='left')

Radiobutton(modelpage1,value=13,variable=model_var,command=bottompage).grid(row=6,column=2)
def model13():
	model_var.set('13')
	bottompage()
Button(modelpage1,width=20,text='Fraction of Variance',command=model13,relief=FLAT).grid(row=6,column=3)
fracofvarpage1=Frame(root)
Label(fracofvarpage1,text='Saves a plot of fraction of variance for all modes.').pack(side='left')
def fracvardatacommand(event=None):
	readingsavedfile()
	sidecalculation.fracvardata(npzfilename.get(), savedfile[13], savedfile[54], savedfile[89],savedfile[90])
	saveconfirmation2.set('File(s) saved in '+savedfile[54]+' folder.')
Button(fracofvarpage1,text=' Submit ',width=6,command=fracvardatacommand).pack(side='left')
fracofvarpage2=Frame(root)
Label(fracofvarpage2,textvariable=saveconfirmation2).pack(side='top')


Radiobutton(modelpage1,value=14,variable=model_var,command=bottompage).grid(row=7,column=0)
def model14():
	model_var.set('14')
	bottompage()
Button(modelpage1,width=20,text='calc Phi & Psi',command=model14,relief=FLAT).grid(row=7,column=1)
calcphipsipage1=Frame(root)
Label(calcphipsipage1,text="Enter PDB file: ").pack(side='left')
phipsifilename=StringVar()
Entry(calcphipsipage1,width=30,textvariable=phipsifilename).pack(side='left')
def ldtmp5(event=None):
	filename5 = tkFileDialog.Open(initialdir='~',filetypes=[('PDB','.pdb'),('PDB','.pdb.gz'),('all files','*')]).show()
	if filename5 !='':
		phipsifilename.set(filename5)
Button(calcphipsipage1, text = "Browse", command = ldtmp5, width = 8,underline=0).pack(side='left')
calcphipsipage2=Frame(root)
Label(calcphipsipage2,textvariable=saveconfirmation2).pack(side='left')
def calcphipsicommand(event=None):
	readingsavedfile()
	sidecalculation.calcphipsi(phipsifilename.get(), savedfile[13],savedfile[57], savedfile[83], savedfile[84])
	saveconfirmation2.set('Files saved in '+savedfile[57]+' folder.')
Button(calcphipsipage2,text=' Submit ',width=6,command=calcphipsicommand).pack(side='left')


# can add another backpage option here
# make sure to add the Frame(root) to bottompage() and clearbottompage()
# add to submittingreturn(event=None):
# also change bignumber!!

#####
bignumber=StringVar()
bignumber.set('14')###change if model_var is bigger than number in ' '
#####

############################################################
############################################################
############################################################
############################################################
############################################################
notespage1=Frame(root)
notesscroll=Scrollbar(notespage1)
notestext=Text(notespage1)
notestext.focus_set()
notesscroll.pack(side='right',fill='y')
notestext.pack(side='left',fill='y')
notesscroll.config(command=notestext.yview)
notestext.config(yscrollcommand=notesscroll.set)
try:
	notesfile=open(os.path.join(os.path.expanduser('~'),'.noma/notes.txt'),'r')
except:
	notesfile=open(os.path.join(os.path.expanduser('~'),'.noma/notes.txt'),'w')
	notesfile.write('You can write notes here!')
	notesfile.close()
	notesfile=open(os.path.join(os.path.expanduser('~'),'.noma/notes.txt'),'r')
for line in notesfile:
	notestext.insert(END,line)
def notessave(event=None):
	hiddennomapath=os.path.join(os.path.expanduser('~'),'.noma/notes.txt')
	notesfile1=open(hiddennomapath,'w')
	notesfile1.write(notestext.get(1.0,END))
	notesfile1.close()
notespage2=Frame(root)
Button(notespage2,text='Save',command=notessave).pack(side='left')
notespage3=Frame(root)
Label(notespage3,textvariable=simulationinfo).pack(side='left')
############################################################
############################################################
############################################################
############################################################
############################################################
############################################################
pagenumber=IntVar()
def clear():
	clearbottompage()
	toppage2.pack_forget()
	toppage3.pack_forget()
	firstpage1.pack_forget()
	secondpage1.pack_forget()
	secondpage2.pack_forget()
	secondpage3.pack_forget()
	thirdpage1.pack_forget()
	thirdpage2.pack_forget()
	simplepage1.pack_forget()
	simplepage2.pack_forget()
	simplepage3.pack_forget()
	simplepage4.pack_forget()
	simplepage5.pack_forget()
	toppage2.pack_forget()
	modelpage1.pack_forget()
	notespage1.pack_forget()
	notespage2.pack_forget()
	notespage3.pack_forget()
	menubar.entryconfig(2,state='disabled')
	menubar.entryconfig(3,state='disabled')
	menubar.entryconfig(4,state='disabled')
def firstpage(event=None):
	clear()
	menubar.entryconfig(2,state='normal')
	coremenu.entryconfig(3,state='disabled')
	coremenu.entryconfig(4,state='disabled')
	pdbbutton1.config(relief=FLAT,bg='gray85')
	npzbutton1.config(relief=SUNKEN,bg='gray70')
	notesbutton1.config(relief=SUNKEN,bg='gray70')
	pagenumber.set(1)
	toppage2.pack(side='top')
	firstpage1.pack(side='top')
def secondpage(event=None):
	clear()
	menubar.entryconfig(2,state='normal')
	coremenu.entryconfig(3,state='normal')
	coremenu.entryconfig(4,state='normal')
	pdbbutton1.config(relief=FLAT,bg='gray85')
	npzbutton1.config(relief=SUNKEN,bg='gray70')
	notesbutton1.config(relief=SUNKEN,bg='gray70')
	pagenumber.set(2)
	toppage2.pack(side='top')
	secondpage1.pack(side='top')
	secondpage2.pack(side='top')
	secondpage3.pack(side='top')
def thirdpage(event=None):
	clear()
	menubar.entryconfig(2,state='normal')
	coremenu.entryconfig(3,state='disabled')
	coremenu.entryconfig(4,state='disabled')
	pdbbutton1.config(relief=FLAT,bg='gray85')
	npzbutton1.config(relief=SUNKEN,bg='gray70')
	notesbutton1.config(relief=SUNKEN,bg='gray70')
	pagenumber.set(3)
	toppage2.pack(side='top')
	thirdpage1.pack(side='top')
	thirdpage2.pack(side='top')
def simplepage(event=None):
	clear()
	menubar.entryconfig(2,state='normal')
	pdbbutton1.config(relief=FLAT,bg='gray85')
	npzbutton1.config(relief=SUNKEN,bg='gray70')
	notesbutton1.config(relief=SUNKEN,bg='gray70')
	pagenumber.set(4)
	toppage2.pack(side='top')
	simplepage1.pack(side='top')
	simplepage2.pack(side='top')
	simplepage3.pack(side='top')
	simplepage4.pack(side='top')
	simplepage5.pack(side='top')
def modelpage(event=None):
	clear()
	menubar.entryconfig(3,state='normal')
	npzbutton1.config(relief=FLAT,bg='gray85')
	pdbbutton1.config(relief=SUNKEN,bg='gray70')
	notesbutton1.config(relief=SUNKEN,bg='gray70')
	pagenumber.set(5)
	toppage3.pack(side='top')
	modelpage1.pack(side='top')
	bottompage()
def notespage(event=None):
	clear()
	menubar.entryconfig(4,state='normal')
	notesbutton1.config(relief=FLAT,bg='gray85')
	npzbutton1.config(relief=SUNKEN,bg='gray70')
	pdbbutton1.config(relief=SUNKEN,bg='gray70')
	pagenumber.set(6)
	notespage1.pack(side='top')
	notespage2.pack(side='top')
	notespage3.pack(side='top')
Button(thirdpage1, text="""


<<


""",command=secondpage).grid(row=0,rowspan=5,column=0)

Button(secondpage1, text="""


<<


""",command=firstpage).grid(row=0,rowspan=5,column=0)
Button(secondpage1, text="""


>>


""",command=thirdpage).grid(row=0,rowspan=5,column=7)

Button(firstpage1, text="""


>>


""",command=secondpage).grid(row=0,rowspan=5,column=5)
def pagenumberpage():
	if pagenumber.get()==1:
		firstpage()
	elif pagenumber.get()==2:
		secondpage()
	elif pagenumber.get()==3:
		thirdpage()
	elif pagenumber.get()==4:
		simplepage()
	elif pagenumber.get()==5:
		modelpage()
	elif pagenumber.get()==6:
		notespage()
def pagenumberright(event=None):
	if pagenumber.get()==6:
		pagenumber.set(1)
	else:
		pagenumber.set(pagenumber.get()+1)
	pagenumberpage()
def pagenumberleft(event=None):
	if pagenumber.get()==1:
		pagenumber.set(6)
	else:
		pagenumber.set(pagenumber.get()-1)
	pagenumberpage()
try:
	root.bind('<'+savedfile[37]+'>',pagenumberright)
except:
	mer=0
try:
	root.bind('<'+savedfile[38]+'>',pagenumberleft)
except:
	mer=0

def browsing(event=None):
	if pagenumber.get()==1 or pagenumber.get()==3 or pagenumber.get()==4:
		ldtmp1()
	elif pagenumber.get()==2:
		if pdbfilename.get()!='':
			ldtmp6()
		else:
			ldtmp1()
	elif pagenumber.get()==5:
		if npzfilename.get()!='':
			if model_var.get=='4' or model_var.get()=='5' or model_var.get()=='6' or model_var.get()=='7':
				ldtmp3()
			elif model_var.get()=='12':
				ldtmp4()
			elif model_var.get()=='14':
				ldtmp5()
			else:
				ldtmp2()
		else:
			ldtmp2()
try:
	root.bind('<'+savedfile[16]+'>',browsing)
except:
	mer=0
def submittingreturn(event=None):
	if pagenumber.get()==1:
		secondpage()
	elif pagenumber.get()==2:
		thirdpage()
	elif pagenumber.get()==3:
		premaincalc1()
	elif pagenumber.get()==4:
		maincalc2()
	elif pagenumber.get()==5:
		if model_var.get()=='0':
			correlationdatacommand()
		elif model_var.get()=='1':
			correlationplotcommand()
		elif model_var.get()=='2':
			sqfluctdatacommand()
		elif model_var.get()=='3':
			sqfluctplotcommand()
		elif model_var.get()=='4':
			overlapcommand()
		elif model_var.get()=='5':
			overlapcommand()
		elif model_var.get()=='6':
			overlapcommand()
		elif model_var.get()=='7':
			overlapcommand()
		elif model_var.get()=='8':
			modedatacommand()
		elif model_var.get()=='9':
			modeplotcommand()
		elif model_var.get()=='10':
			collectivitydatacommand()
		elif model_var.get()=='11':
			tempfactorsdatacommand()
		elif model_var.get()=='12':
			viewnmdinvmddata()
		elif model_var.get()=='13':
			fracvardatacommand()
		elif model_var.get()=='14':
			calcphipsicommand()
try:
	root.bind('<'+savedfile[17]+'>',submittingreturn)
except:
	mer=0
try:
	root.bind('<'+savedfile[18]+'>',calcfromnotespage)
except:
	mer=0
def switchorsave(event=None):
	if pagenumber.get()==2:
		one=pdbfilename.get()
		two=comparepdbfilename.get()
		pdbfilename.set(two)
		comparepdbfilename.set(one)
	elif pagenumber.get()==5:
		if model_var.get()=='4' or model_var.get()=='5' or model_var.get()=='6' or model_var.get()=='7':
			one=npzfilename.get()
			two=compnpzfilename.get()
			npzfilename.set(two)
			compnpzfilename.set(one)
	elif pagenumber.get()==6:
		notessave()
try:
	root.bind('<'+savedfile[19]+'>',switchorsave)
except:
	mer=0
def statPDB(event=None):
	oldfilename=pdbfilename.get()
	find = 0					#
	while find < len(oldfilename):			#
		if oldfilename[-(find+1):-find] == '/':	#
			bgn = len(oldfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		float(bgn)				#
	except (NameError):				#
		bgn = 0					#
	name=oldfilename[bgn:len(oldfilename)]
	p38 = prody.parsePDB(oldfilename)
	numatom=[0]*5
	i = 0
	while i<5:
		if i == 0:
			pro = p38.select('protein')
		elif i == 1:
			pro = p38.select('protein and name CA')
		elif i == 2:
			pro = p38.select('protein and not name "[1-9]?H.*"')
		elif i == 3:
			pro = p38.select('protein and name CA C O N H')	# selects backbone
		elif i == 4:
			pro = p38.select('protein and not name CA C O N H')	# selects sidechain
		numatom[i] = pro.numAtoms()		# number of atoms
		i+=1
	if savedfile[9]=='0':
		ba='dist dependent'
		ca=savedfile[10]
	elif savedfile[9]=='1':
		ba=savedfile[11]
		ca=savedfile[12]
	global root4
	root4=Tk()
	root4.title("PDB Stats")
	Label(root4,text=name,font='Times 14 underline').grid(row=0)
	Label(root4,text=str(numatom[0])+' atoms').grid(row=1,sticky=W)
	Label(root4,text=str(numatom[1])+' C-alpha atoms').grid(row=2,sticky=W)
	Label(root4,text=str(numatom[2])+' heavy atoms').grid(row=3,sticky=W)
	Label(root4,text=str(numatom[3])+' backbone atoms').grid(row=4,sticky=W)
	Label(root4,text=str(numatom[4])+' sidechain atoms').grid(row=5,sticky=W)
	Label(root4,text=ba+' gamma').grid(row=6,sticky=W)
	Label(root4,text=ca+u' \u00C5 cutoff').grid(row=7,sticky=W)
try:
	root.bind('<'+savedfile[39]+'>',statPDB)
except:
	mer=0
def statNPZ(event=None):
	oldfilename = npzfilename.get()
	find = 0					#
	while find < len(oldfilename):			#
		if oldfilename[-(find+1):-find] == '/':	#
			bgn = len(oldfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		float(bgn)				#
	except (NameError):				#
		bgn = 0					#
	name=oldfilename[bgn:len(oldfilename)]
	npzmodel = prody.loadModel(oldfilename)
	a = len(npzmodel.getEigvals())
	b = npzmodel.numAtoms()
	c = str(npzmodel.getCutoff())
	if c == 'None':
		c = 'N/A'
	d = str(npzmodel.getGamma())
	if d == 'None':
		d = 'dist dependent'
	global root5
	root5=Tk()
	root5.title("NPZ Stats")
	Label(root5,text=name,font='Times 14 underline').grid(row=0)
	Label(root5,text=str(a)+' modes').grid(row=1,sticky=W)
	Label(root5,text=str(b)+' atoms').grid(row=2,sticky=W)
	Label(root5,text=c+u' \u00C5 cutoff').grid(row=3,sticky=W)
	Label(root5,text=d+' gamma').grid(row=4,sticky=W)
try:
	root.bind('<'+savedfile[40]+'>',statNPZ)
except:
	mer=0
def quit(event=None):
	root.destroy()
	try:
		import matplotlib.pyplot as plt
		plt.close('all')
	except:
		mer=0
try:
	root.bind('<'+savedfile[20]+'>',quit)
except:
	mer=0
def openingfromnoma(event=None):
	filename = tkFileDialog.Open(filetypes=[('all files','*')]).show()
	os.system('/usr/bin/gnome-open '+filename)
try:
	root.bind("<"+savedfile[21]+">",openingfromnoma)
except:
	mer=0
def xmgracefromnoma(event=None):
	filename = tkFileDialog.Open(filetypes=[('all files','*')]).show()
	os.system('xmgrace '+filename)
try:
	root.bind("<"+savedfile[22]+">",xmgracefromnoma)
except:
	mer=0
def vmdfromnoma(event=None):
	os.system('gnome-terminal -x bash -c "vmd '+pdbfilename.get()+';bash"')
try:
	root.bind("<"+savedfile[23]+">",vmdfromnoma)
except:
	mer=0
def saving(event=None):
	os.system('python '+path+'saving.py')
try:
	root.bind('<'+savedfile[24]+'>',saving)
except:
	mer=0
def about(event=None):
	os.system('python '+path+'about.py &')
try:
	root.bind('<'+savedfile[25]+'>',about)
except:
	mer=0
def manual(event=None):
	os.system('python '+path+'manual.py &')
try:
	root.bind('<'+savedfile[26]+'>',manual)
except:
	mer=0
#################################################################
def myfileiscool(event=None):####################################
	pdbfilename.set('/home/matt/new/34290ps.pdb')############
	npzfilename.set('/home/matt/new/Ca_ANM/34290ps.anm.npz')# DELETE
root.bind('<Control-k>',myfileiscool)############################
#################################################################
def calculator(event=None):
	os.system('python '+path+'calculator.py &')
try:
	root.bind('<'+savedfile[27]+'>',calculator)
except:
	mer=0


###
def find(event=None):
	if pagenumber.get()==5 and (model_var.get()=='4' or model_var.get()=='5' or model_var.get()=='6' or model_var.get()=='7'):
		oldfilename = npzfilename.get()
		npzmodel = prody.loadModel(oldfilename)
		numatom=npzmodel.numAtoms()
		find = 0					#
		while find < len(oldfilename):			#
			if oldfilename[-(find+1):-find] == '/':	#
				bgn = len(oldfilename)-find		#
				break				#
			else:					# helps in the
				find +=1			# saving of files
		try:						#
			float(bgn)				#
		except (NameError):				#
			bgn = 0					#
		name=oldfilename[bgn:len(oldfilename)]
		bgn = oldfilename[:bgn]				# path for file
		dirList=os.listdir(bgn)
		i =0
		f = [None]*len(dirList)
		for fname in dirList:
			if '.npz' in fname:
				f[i]=fname
				i+=1
			else:
				mert=0
		del f[i:]
		i=0
		while i < len(f):
			if prody.loadModel(bgn+f[i]).numAtoms() == numatom and bgn+f[i] != oldfilename and bgn+f[i] != compnpzfilename.get():
				j = i
				compnpzfilename.set(bgn+f[j])
				saveconfirmation1.set('Comparison found!')
				saveconfirmation2.set('Comparison found!')
				break
			else:
				saveconfirmation1.set('Comparison not found.')
				saveconfirmation2.set('Comparison not found.')
				compnpzfilename.set('')
				i +=1
		root.update_idletasks()
	elif pagenumber.get()==2:#####################$%^%$&#&%^&%$%^
		oldfilename = pdbfilename.get()
		npzmodel = prody.parsePDB(oldfilename)
		numatom=npzmodel.numAtoms()
		find = 0					#
		while find < len(oldfilename):			#
			if oldfilename[-(find+1):-find] == '/':	#
				bgn = len(oldfilename)-find		#
				break				#
			else:					# helps in the
				find +=1			# saving of files
		try:						#
			float(bgn)				#
		except (NameError):				#
			bgn = 0					#
		name=oldfilename[bgn:len(oldfilename)]
		bgn = oldfilename[:bgn]				# path for file
		dirList=os.listdir(bgn)
		i =0
		f = [None]*len(dirList)
		for fname in dirList:
			if '.pdb' in fname:
				f[i]=fname
				i+=1
			else:
				mert=0
		del f[i:]
		i=0
		while i < len(f):
			if prody.parsePDB(bgn+f[i]).numAtoms() == numatom and bgn+f[i] != oldfilename and bgn+f[i] != comparepdbfilename.get():
				j = i
				comparepdbfilename.set(bgn+f[j])
				break
			else:
				comparepdbfilename.set('')
				i +=1
try:
	root.bind('<'+savedfile[28]+'>',find)
except:
	mer=0
#####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def next(event=None):
	if pagenumber.get()==1 or pagenumber.get()==2 or pagenumber.get()==3 or pagenumber.get()==4:
		oldfilename = pdbfilename.get()
	elif pagenumber.get()==5 and model_var.get()=='14':
		oldfilename = phipsifilename.get()
	elif pagenumber.get()==5:
		oldfilename = npzfilename.get()
	find = 0					#
	while find < len(oldfilename):			#
		if oldfilename[-(find+1):-find] == '/':	#
			bgn = len(oldfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		float(bgn)				#
	except (NameError):				#
		bgn = 0					#
	name=oldfilename[bgn:len(oldfilename)]
	bgn = oldfilename[:bgn]				# path for file
	dirList=os.listdir(bgn)
	i =0
	f = [None]*len(dirList)
#
	if pagenumber.get()==1 or pagenumber.get()==2 or pagenumber.get()==3 or pagenumber.get()==4 or (pagenumber.get()==5 and model_var.get()=='14'):
		for fname in dirList:
			if '.pdb' in fname:
				f[i]=fname
				i+=1
			else:
				mert=0
	elif pagenumber.get()==5:
		for fname in dirList:
			if '.npz' in fname:
				f[i]=fname
				i+=1
			else:
				mert=0
#
	del f[i:]
	i=0
	while i < len(f):
		if f[i] == name:
			j = i +1
			break
		else:
			i +=1
#
	if pagenumber.get()==1 or pagenumber.get()==2 or pagenumber.get()==3 or pagenumber.get()==4:
		try:
			pdbfilename.set(bgn+f[j])
		except:
			pdbfilename.set(bgn+f[0])
	elif pagenumber.get()==5 and model_var.get()=='14':
		try:
			phipsifilename.set(bgn+f[j])
		except:
			phipsifilename.set(bgn+f[0])
	elif pagenumber.get()==5:
		try:
			npzfilename.set(bgn+f[j])
		except:
			npzfilename.set(bgn+f[0])
try:
	root.bind('<'+savedfile[29]+'>',next)
except:
	mer=0
def previous(event=None):
	if pagenumber.get()==1 or pagenumber.get()==2 or pagenumber.get()==3 or pagenumber.get()==4:
		oldfilename = pdbfilename.get()
	elif pagenumber.get()==5 and model_var.get()=='14':
		oldfilename = phipsifilename.get()
	elif pagenumber.get()==5:
		oldfilename = npzfilename.get()

	find = 0					#
	while find < len(oldfilename):			#
		if oldfilename[-(find+1):-find] == '/':	#
			bgn = len(oldfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		float(bgn)				#
	except (NameError):				#
		bgn = 0					#
	name=oldfilename[bgn:len(oldfilename)]
	bgn = oldfilename[:bgn]				# path for file
	dirList=os.listdir(bgn)
	i =0
	f = [None]*len(dirList)
	if pagenumber.get()==1 or pagenumber.get()==2 or pagenumber.get()==3 or pagenumber.get()==4 or (pagenumber.get()==5 and model_var.get()=='14'):
		for fname in dirList:
			if '.pdb' in fname:
				f[i]=fname
				i+=1
			else:
				mert=0
	elif pagenumber.get()==5:
		for fname in dirList:
			if '.npz' in fname:
				f[i]=fname
				i+=1
			else:
				mert=0

	del f[i:]
	i=0
	while i < len(f):
		if f[i] == name:
			j = i-1
			break
		else:
			i +=1
	if pagenumber.get()==1 or pagenumber.get()==2 or pagenumber.get()==3 or pagenumber.get()==4:
		try:
			pdbfilename.set(bgn+f[j])
		except:
			pdbfilename.set(bgn+f[len(f)])
	elif pagenumber.get()==5 and model_var.get()=='14':
		try:
			phipsifilename.set(bgn+f[j])
		except:
			phipsifilename.set(bgn+f[len(f)])
	elif pagenumber.get()==5:
		try:
			npzfilename.set(bgn+f[j])
		except:
			npzfilename.set(bgn+f[len(f)])
try:
	root.bind('<'+savedfile[30]+'>',previous)
except:
	mer=0
#####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###

def movingup(event=None):
	if pagenumber.get()==5:
		if model_var.get()=='0':
			model_var.set(bignumber.get())
		elif model_var.get()=='1':
			model_var.set(str(int(bignumber.get())-1))
		else:
			model_var.set(str(int(model_var.get())-2))
		bottompage()
def movingdown(event=None):
	if pagenumber.get()==5:
		if int(model_var.get())>=int(bignumber.get()):
			model_var.set('0')
		elif model_var.get()==str(int(bignumber.get())-1):
			model_var.set('1')
		else:
			model_var.set(str(int(model_var.get())+2))
		bottompage()
def movingright(event=None):
	if pagenumber.get()==5:
		if int(model_var.get())>=int(bignumber.get()):
			model_var.set('0')
		else:
			model_var.set(str(int(model_var.get())+1))
		bottompage()
def movingleft(event=None):
	if pagenumber.get()==5:
		if model_var.get()=='0':
			model_var.set(bignumber.get())
		else:
			model_var.set(str(int(model_var.get())-1))
		bottompage()
try:
	root.bind('<'+savedfile[31]+'>',movingup)
except:
	mer=0
try:
	root.bind('<'+savedfile[32]+'>',movingdown)
except:
	mer=0
try:
	root.bind('<'+savedfile[33]+'>',movingright)
except:
	mer=0
try:
	root.bind('<'+savedfile[34]+'>',movingleft)
except:
	mer=0
def add(event=None):
	if pagenumber.get()== 3 or pagenumber.get()==4:
		nummodes.set(str(int(nummodes.get())+1))
	elif pagenumber.get()== 5:
		if modelpagemode.get()=='all' or modelpagemode.get()=="'all'":
			modelpagemode.set('1')
		else:
			try:
				modelpagemode.set(str(int(modelpagemode.get())+1))
			except:
				mer=0
def subtract(event=None):
	if pagenumber.get()== 3 or pagenumber.get()==4:
		if nummodes.get()=='1':
			nummodes.set('1')
		else:
			nummodes.set(str(int(nummodes.get())-1))
	elif pagenumber.get()== 5:
		if modelpagemode.get()=='1' or modelpagemode.get()=='all' or modelpagemode.get()=="'all'":
			modelpagemode.set('all')
		else:
			try:
				modelpagemode.set(str(int(modelpagemode.get())-1))
			except:
				mer=0
try:
	root.bind('<'+savedfile[35]+'>',add)
except:
	mer=0
try:
	root.bind('<'+savedfile[36]+'>',subtract)
except:
	mer=0
i=16
while i<41:
	import string
	try:
		savedfile[i]=string.capwords(savedfile[i],'-')
		savedfile[i]=string.replace(savedfile[i],'Control','Ctrl')
	except:
		mer=0
	i+=1
menubar=Menu(root)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="About NOMA",command=about,accelerator=savedfile[25])
filemenu.add_command(label="Open...",command=openingfromnoma,accelerator=savedfile[21])
filemenu.add_separator()
filemenu.add_command(label="Preferences",command=saving,accelerator=savedfile[24])
filemenu.add_command(label="Browse",accelerator=savedfile[16],command=browsing)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=quit,accelerator=savedfile[20])

menubar.add_cascade(label='File',menu=filemenu,underline=0)

coremenu=Menu(menubar,tearoff=0)
coremenu.add_command(label="Next PDB file",accelerator=savedfile[29],command=next)
coremenu.add_command(label="Previous PDB file",accelerator=savedfile[30],command=previous)
coremenu.add_separator()
coremenu.add_command(label='Switch PDB files',command=switchorsave,accelerator=savedfile[19])
coremenu.add_command(label='Find comparison file',accelerator=savedfile[28],command=find)
coremenu.add_separator()
coremenu.add_command(label="Statistics of PDB file",command=statPDB,accelerator=savedfile[39])
coremenu.add_command(label="View in VMD",command=vmdfromnoma,accelerator=savedfile[23])

moremenu=Menu(coremenu,tearoff=0)
moremenu.add_command(label="New",command=firstpage)
moremenu.add_command(label="Old",command=simplepage)

coremenu.add_cascade(label='Interface',menu=moremenu)

menubar.add_cascade(label='Start-up',menu=coremenu,underline=0)

optionsmenu=Menu(menubar,tearoff=0)
optionsmenu.add_command(label="Next NPZ file",accelerator=savedfile[29],command=next)
optionsmenu.add_command(label="Previous NPZ file",accelerator=savedfile[30],command=previous)
optionsmenu.add_separator()
optionsmenu.add_command(label='Switch NPZ files',command=switchorsave,accelerator=savedfile[19])
optionsmenu.add_command(label='Find comparison file',accelerator=savedfile[28],command=find)
optionsmenu.add_separator()
optionsmenu.add_command(label="Statistics of NPZ file",command=statNPZ,accelerator=savedfile[40])
optionsmenu.add_command(label="View in xmgrace",command=xmgracefromnoma,accelerator=savedfile[22])

menubar.add_cascade(label='Model',menu=optionsmenu,underline=0)

notesmenu=Menu(menubar,tearoff=0)
notesmenu.add_command(label='Save notes',command=switchorsave,accelerator=savedfile[19])
notesmenu.add_command(label='Execute notes',accelerator=savedfile[18],command=calcfromnotespage)

menubar.add_cascade(label='Notes',menu=notesmenu,underline=0)

def newoptions(self,name,begn,progcom,progend):
	if progend=='.c' or progend=='.cpp':
		firstcom=progcom+' '+begn+name+progend
		secondcom=os.path.join(os.getcwd(),'a.out')
		self.add_command(label=name, command=(lambda: os.system(firstcom+';'+secondcom)))
	else:
		self.add_command(label=name,command=(lambda: os.system(progcom+' '+begn+name+progend)))
bgn1=path+'Extra/'
dirList1=os.listdir(bgn1)
i=0
f1=[None]*len(dirList1)
for fname in dirList1:
	if fname[-3:]=='.py':
		f1[i]=fname
		i+=1
	else:
		mert=0
del f1[i:]
dirList3=os.listdir(bgn1)
i=0
f3=[None]*len(dirList3)
for fname in dirList3:
	if fname[-3:]=='.pl':
		f3[i]=fname
		i+=1
	else:
		mert=0
del f3[i:]
dirList4=os.listdir(bgn1)
i=0
f4=[None]*len(dirList4)
for fname in dirList4:
	if fname[-4:]=='.csh':
		f4[i]=fname
		i+=1
	else:
		mert=0
del f4[i:]
extramenu=Menu(menubar,tearoff=0)
i=0
while i < len(f1):
	newoptions(extramenu,f1[i][:-3],bgn1,'python','.py')
	i+=1
i=0
while i < len(f3):
	newoptions(extramenu,f3[i][:-3],bgn1,'perl','.pl')
	i+=1
i=0
while i < len(f4):
	newoptions(extramenu,f4[i][:-4],bgn1,'csh','.csh')
	i+=1

#####
dirList7=os.listdir(bgn1)
i=0
f7=[None]*len(dirList7)
for fname in dirList7:
	if fname[-3:]=='.sh':
		f7[i]=fname
		i+=1
	else:
		mert=0
del f7[i:]
dirList9=os.listdir(bgn1)
i=0
f9=[None]*len(dirList9)
for fname in dirList9:
	if fname[-4:]=='.cpp':
		f9[i]=fname
		i+=1
	else:
		mert=0
del f9[i:]
dirList11=os.listdir(bgn1)
i=0
f11=[None]*len(dirList11)
for fname in dirList11:
	if fname[-2:]=='.c':
		f11[i]=fname
		i+=1
	else:
		mert=0
del f11[i:]

i=0
while i < len(f7):
	newoptions(extramenu,f7[i][:-3],bgn1,'sh','.sh')
	i+=1
i=0
while i < len(f9):
	newoptions(extramenu,f9[i][:-4],bgn1,'g++','.cpp')
	i+=1
i=0
while i < len(f11):
	newoptions(extramenu,f11[i][:-2],bgn1,'g++','.c')
	i+=1
#####


menubar.add_cascade(label='Extra',menu=extramenu)

personalmenu=Menu(menubar,tearoff=0)
try:
	bgn1=os.path.join(os.path.expanduser('~'),'nomaaddon/')
	dirList1=os.listdir(bgn1)
	i=0
	f1=[None]*len(dirList1)
	for fname in dirList1:
		if fname[-3:]=='.py':
			f1[i]=fname
			i+=1
		else:
			mert=0
	del f1[i:]

	i=0
	while i < len(f1):
		newoptions(personalmenu,f1[i][:-3],bgn1,'python','.py')
		i+=1
except:
	mert=0
try:
	bgn1=os.path.join(os.path.expanduser('~'),'nomaaddon/')
	dirList5=os.listdir(bgn1)
	i=0
	f5=[None]*len(dirList5)
	for fname in dirList5:
		if fname[-3:]=='.pl':
			f5[i]=fname
			i+=1
		else:
			mert=0
	del f5[i:]

	i=0
	while i < len(f5):
		newoptions(personalmenu,f5[i][:-3],bgn1,'perl','.pl')
		i+=1
except:
	mert=0
try:
	bgn1=os.path.join(os.path.expanduser('~'),'nomaaddon/')
	dirList6=os.listdir(bgn1)
	i=0
	f6=[None]*len(dirList6)
	for fname in dirList6:
		if fname[-4:]=='.csh':
			f6[i]=fname
			i+=1
		else:
			mert=0
	del f6[i:]

	i=0
	while i < len(f6):
		newoptions(personalmenu,f6[i][:-4],bgn1,'csh','.csh')
		i+=1
except:
	mert=0

####
try:
	bgn1=os.path.join(os.path.expanduser('~'),'nomaaddon/')
	dirList8=os.listdir(bgn1)
	i=0
	f8=[None]*len(dirList8)
	for fname in dirList8:
		if fname[-3:]=='.sh':
			f8[i]=fname
			i+=1
		else:
			mert=0
	del f8[i:]

	i=0
	while i < len(f8):
		newoptions(personalmenu,f8[i][:-3],bgn1,'sh','.sh')
		i+=1
except:
	mert=0
try:
	bgn1=os.path.join(os.path.expanduser('~'),'nomaaddon/')
	dirList10=os.listdir(bgn1)
	i=0
	f10=[None]*len(dirList10)
	for fname in dirList10:
		if fname[-4:]=='.cpp':
			f10[i]=fname
			i+=1
		else:
			mert=0
	del f10[i:]

	i=0
	while i < len(f10):
		newoptions(personalmenu,f10[i][:-4],bgn1,'g++','.cpp')
		i+=1
except:
	mert=0
try:
	bgn1=os.path.join(os.path.expanduser('~'),'nomaaddon/')
	dirList12=os.listdir(bgn1)
	i=0
	f12=[None]*len(dirList12)
	for fname in dirList12:
		if fname[-2:]=='.c':
			f12[i]=fname
			i+=1
		else:
			mert=0
	del f12[i:]

	i=0
	while i < len(f12):
		newoptions(personalmenu,f12[i][:-2],bgn1,'g++','.c')
		i+=1
except:
	mert=0
####


menubar.add_cascade(label='Personal',menu=personalmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Manual",command=manual,accelerator=savedfile[26])

menubar.add_cascade(label='Help',menu=helpmenu,underline=0)

root.config(menu=menubar)


model_var.set(str(int(bignumber.get())+1))

if savedfile[8]=='0':
	firstpage()
elif savedfile[8]=='1':
	simplepage()
filenamefromterminal()
root.mainloop()
writeblankfile=os.path.join(os.path.expanduser('~'),'.noma/thefilename.txt')
fout=open(writeblankfile,'w')
fout.write('')
fout.close()

