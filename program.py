import os
hiddennomapath=os.path.join(os.path.expanduser('~'),'.noma/thefilename.txt')
fin = open(hiddennomapath,'r')
for line in fin:
	pair = line.split()
	try:
		newfilename=pair[0]
	except:
		newfilename=''
oldfilename=os.path.expanduser('~')
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

###############

bgn1='/usr/share/noma/Extra/'
dirList1=os.listdir(bgn1)
i=0
f1=[None]*len(dirList1)
for fname in dirList1:
	if '.py' in fname:
		f1[i]=fname
		i+=1
	else:
		mert=0
del f1[i:]
try:
	bgn2=os.path.join(os.path.expanduser('~'),'nomaaddon/')
	dirList2=os.listdir(bgn2)
	i=0
	f2=[None]*len(dirList2)
	for fname in dirList2:
		if '.py' in fname:
			f2[i]=fname
			i+=1
		else:
			mert=0
	del f2[i:]
except:
	mert=0
###############

if newfilename=='about':
	os.system('python /usr/share/noma/about.py')
elif newfilename=='help' or newfilename=='--help' or newfilename=='-h' or newfilename=='-help':
	print ''
	print 'Hello ',name,'!'
	print ''
	print 'noma [options|file]'
	print 'Can put PDB or NPZ file name after noma.'
	print ''
	print 'Commands'
	print '--------'
	print 'about		Brings up the about page'
	print 'manual		Brings up the manual'
	print 'calc		Brings up the calculator'
	print 'pref		Brings up the preferences'
	print '		if this has an error then default will fix it.'
	print 'default		May solve problem if noma is not working'
	print ''
	i=0
	while i<len(f1):
		print f1[i][:-3],'	Extra'
		i+=1
	try:
		i=0
		while i<len(f2):
			print f2[i][:-3],'	Personal'
			i+=1
	except:
		mert=0
	print ''


elif newfilename=='manual' or newfilename=='man':
	os.system('python /usr/share/noma/manual.py')
elif newfilename=='calculator' or newfilename=='calc':
	os.system('python /usr/share/noma/calculator.py')
elif newfilename=='preferences' or newfilename=='pref':
	os.system('python /usr/share/noma/saving.py')
elif newfilename=='default':
	hiddennomapath=os.path.join(os.path.expanduser('~'),'.noma/savefile.txt')
	fout=open(hiddennomapath,'w')
	fout.write("""20
7,8
12
3.0
7
5
3.0
0
0
0
100.0
1.0
13.0
0
1
1
Control-b
Return
Control-e
Control-s
Control-q
Control-Shift-O
Control-Shift-X
Control-Shift-V
Control-i
Control-a
Control-m
Control-Shift-C
Control-f
Control-n
Control-p
Control-Up
Control-Down
Control-Right
Control-Left
Up
Down




Ca_ANM
Ca_GNM
Heavy_ANM
Heavy_GNM
All_ANM
All_GNM
Backbone_ANM
Backbone_GNM
Sidechain_ANM
Sidechain_GNM
Correlation
SqFlucts
Overlap
Modes
Collectivity
Temp
PhiPsi
NMD
_correlation
txt
_correlation_plot
png
_sqflucts
txt
_sqflucts
png
_overlap
txt
_overlap
png
_overlap_table
txt
_overlap_table
png
_modes
txt
_mode
png
_collectivity
txt
_TempFactors
txt
average
txt
_sample
_traverse


_FractOfVariances
png
-2
1""")
	fout.close()
	print 'Default settings'
	print 'Try using noma now'
elif newfilename=='upload':
	print 'Upload noma'
	print '0     about.py'
	print '1     calculator.py'
	print '2     maincalculation.py'
	print '3     manual.py'
	print '4     noma'
	print '5     NOMA1.png'
	print '6     noma.desktop'
	print '7     noma.py'
	print '8     NOMA.xbm'
	print '9     saving.py'
	print '10    sidecalculation.py'
	print '11    EXIT'
	a=input()
	while a!=11:
		if a==0:
			os.system('sudo cp /usr/share/noma/about.py /media/CRUZER/')
		elif a==1:
			os.system('sudo cp /usr/share/noma/calculator.py /media/CRUZER/')
		elif a==2:
			os.system('sudo cp /usr/share/noma/maincalculation.py /media/CRUZER/')
		elif a==3:
			os.system('sudo cp /usr/share/noma/manual.py /media/CRUZER/')
		elif a==4:
			os.system('sudo cp /usr/share/noma/noma /media/CRUZER/')
		elif a==5:
			os.system('sudo cp /usr/share/noma/NOMA1.png /media/CRUZER/')
		elif a==6:
			os.system('sudo cp /usr/share/noma/noma.desktop /media/CRUZER/')
		elif a==7:
			os.system('sudo cp /usr/share/noma/noma.py /media/CRUZER/')
		elif a==8:
			os.system('sudo cp /usr/share/noma/NOMA.xbm /media/CRUZER/')
		elif a==9:
			os.system('sudo cp /usr/share/noma/saving.py /media/CRUZER/')
		elif a==10:
			os.system('sudo cp /usr/share/noma/sidecalculation.py /media/CRUZER/')
		a=input()
elif newfilename=='update':
	print 'Update noma'
	print '0     about.py'
	print '1     calculator.py'
	print '2     maincalculation.py'
	print '3     manual.py'
	print '4     noma'
	print '5     NOMA1.png'
	print '6     noma.desktop'
	print '7     noma.py'
	print '8     NOMA.xbm'
	print '9     saving.py'
	print '10    sidecalculation.py'
	print '11    EXIT'
	a=input()
	while a!=11:
		if a==0:
			os.system('sudo rm /usr/share/noma/about.py')
			os.system('sudo cp /media/CRUZER/about.py /usr/share/noma/')
		elif a==1:
			os.system('sudo rm /usr/share/noma/calculator.py')
			os.system('sudo cp /media/CRUZER/calculator.py /usr/share/noma/')
		elif a==2:
			os.system('sudo rm /usr/share/noma/maincalculation.py')
			os.system('sudo cp /media/CRUZER/maincalculation.py /usr/share/noma/')
		elif a==3:
			os.system('sudo rm /usr/share/noma/manual.py')
			os.system('sudo cp /media/CRUZER/manual.py /usr/share/noma/')
		elif a==4:
			os.system('sudo rm /usr/share/noma/noma')
			os.system('sudo rm /usr/local/bin/noma')
			os.system('sudo cp /media/CRUZER/noma /usr/share/noma/')
			os.system('sudo cp /media/CRUZER/noma /usr/local/bin/')
			os.system('sudo chmod +x /usr/local/bin/noma')
		elif a==5:
			os.system('sudo rm /usr/share/noma/NOMA1.png')
			os.system('sudo cp /media/CRUZER/NOMA1.png /usr/share/noma/')
		elif a==6:
			os.system('sudo rm /usr/share/noma/noma.desktop')
			os.system('sudo rm /usr/share/applications/noma.desktop')
			os.system('sudo cp /media/CRUZER/noma.desktop /usr/share/noma/')
			os.system('sudo cp /media/CRUZER/noma.desktop /usr/share/applications/')
		elif a==7:
			os.system('sudo rm /usr/share/noma/noma.py')
			os.system('sudo cp /media/CRUZER/noma.py /usr/share/noma/')
		elif a==8:
			os.system('sudo rm /usr/share/noma/NOMA.xbm')
			os.system('sudo cp /media/CRUZER/NOMA.xbm /usr/share/noma/')
		elif a==9:
			os.system('sudo rm /usr/share/noma/saving.py')
			os.system('sudo cp /media/CRUZER/saving.py /usr/share/noma/')
		elif a==10:
			os.system('sudo rm /usr/share/noma/sidecalculation.py')
			os.system('sudo cp /media/CRUZER/sidecalculation.py /usr/share/noma/')
		a=input()
elif '.pdb' in newfilename or '.npz' in newfilename or newfilename=='':
	os.system('python /usr/share/noma/noma.py')
else:
	i=0
	while i <len(f1):
		if newfilename==f1[i][:-3]:
			os.system('python '+bgn1+f1[i])
			break
		else:
			i+=1
	try:
		i=0
		while i <len(f2):
			if newfilename==f2[i][:-3]:
				os.system('python '+bgn2+f2[i])
				break
			else:
				i+=1
	except:
		mer=0
