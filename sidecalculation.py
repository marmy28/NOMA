#0
def correlationdata(npzfilename, mode, showresults, foldername, newname, endname):
	import prody
	import os
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)
	try:
		open(bgn+foldername+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/')
		except (OSError):
			mer = 0

	if mode=='all' or mode=="'all'" or mode== ' all':
		x = 0
		x1 = len(npzmodel.getEigvals())
		while x < x1:
			correlationdataname = bgn+foldername+'/'+name+newname+'_mode'+str(x+1)+'.'+endname
			prody.writeArray(correlationdataname,prody.calcCrossCorr(npzmodel[x]),'%.18e')
			print correlationdataname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+correlationdataname)
			x +=1
	else:
		a = mode+' '
		b = [0]*len(a)
		i = 0
		j = 0
		b1 = 0
		while i < len(a):
			if a[i:i+1] ==' ' or a[i:i+1]==',':
				b[b1]=int(a[j:i])
				j = i+1
				i +=1
				b1 +=1
			else:
				i +=1
		del b[b1:]
		i=0
		while i < len(b):
			x = b[i]-1
			correlationdataname = bgn+foldername+'/'+name+newname+'_mode'+str(x+1)+'.'+endname
			prody.writeArray(correlationdataname,prody.calcCrossCorr(npzmodel[x]),'%.18e')
			print correlationdataname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+correlationdataname)
			i+=1

#1
def correlationplot(npzfilename, mode, showresults, foldername, newname, endname):
	import prody
	import os
	import matplotlib.pyplot as plt
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)
	try:
		open(bgn+foldername+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/')
		except (OSError):
			mer = 0

	if mode=='all' or mode=="'all'" or mode== ' all':
		x = 0
		x1 = len(npzmodel.getEigvals())
		while x < x1:
			plt.figure(figsize = (6,5))
			prody.showCrossCorr(npzmodel[x])
			correlationplotname = bgn+foldername+'/'+name+newname+'_mode'+str(x+1)+'.'+endname
			plt.savefig(correlationplotname,format = endname)
			print correlationplotname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+correlationplotname)
			x +=1
	else:
		a = mode+' '
		b = [0]*len(a)
		i = 0
		j = 0
		b1 = 0
		while i < len(a):
			if a[i:i+1] ==' ' or a[i:i+1]==',':
				b[b1]=int(a[j:i])
				j = i+1
				i +=1
				b1 +=1
			else:
				i +=1
		del b[b1:]
		i=0
		while i < len(b):
			x = b[i]-1
			plt.figure(figsize = (6,5))
			prody.showCrossCorr(npzmodel[x])
			correlationplotname = bgn+foldername+'/'+name+newname+'_mode'+str(x+1)+'.'+endname
			plt.savefig(correlationplotname,format = endname)
			print correlationplotname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+correlationplotname)
			i+=1
#2
def sqfluctdata(npzfilename, mode, showresults, separatevar, foldername, newname, endname):
	import prody
	import os
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)

	try:
		open(bgn+foldername+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/')
		except (OSError):
			mer = 0

	if separatevar!='0':
		try:
			pdbfilename = bgn+'../'+name+'.pdb'
			p38 = prody.parsePDB(pdbfilename)
		except:
			try:
				pdbfilename = bgn+'../'+name+'.pdb.gz'
				p38 = prody.parsePDB(pdbfilename)
			except:
				try:
					pdbfilename = bgn+name+'.pdb'
					p38=prody.parsePDB(pdbfilename)
				except:
					try:
						pdbfilename = bgn+name+'.pdb.gz'
						p38=prody.parsePDB(pdbfilename)
					except:
						import tkFileDialog
						pdbfilename = tkFileDialog.Open(initialdir='~',filetypes=[('PDB','.pdb'),('PDB gz','.pdb.gz'),('all files','*')]).show()
						p38 = prody.parsePDB(pdbfilename)



	numatom = npzmodel.numAtoms()
	if mode=='all' or mode=="'all'" or mode== ' all':
		yelp = 0
		yelp1=len(npzmodel.getEigvals())
		while yelp < yelp1:
			sqfluctdataname = bgn+foldername+'/'+name+newname+'_mode'+str(yelp+1)+'.'+endname
			fout = open(sqfluctdataname,'w')
			if separatevar=='0':
				a = 0
				while a < numatom:
					fout.write(str(a))
					fout.write("""	""")
					fout.write(str(prody.calcSqFlucts(npzmodel[yelp])[a]))
					fout.write("""
""")
					a +=1
			elif separatevar=='1':
				a=0
				while a <numatom:
					firstresnum=int(p38.getResnums()[0:1][0])
					origiresnum=int(p38.getResnums()[0:1][0])
					while firstresnum<(int(numatom*1.0/p38.numChains())+origiresnum):
						fout.write(str(firstresnum))
						fout.write('\t')
						fout.write(str(prody.calcSqFlucts(npzmodel[yelp])[a]))
						fout.write('\n')
						a+=1
						firstresnum+=1
					fout.write('&\n')
			fout.close()
			print sqfluctdataname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+sqfluctdataname)
			yelp+=1
	else:
		a = mode+' '
		b = [0]*len(a)
		i = 0
		j = 0
		b1 = 0
		while i < len(a):
			if a[i:i+1] ==' ' or a[i:i+1]==',':
				b[b1]=int(a[j:i])
				j = i+1
				i +=1
				b1 +=1
			else:
				i +=1
		del b[b1:]
		i=0
		while i < len(b):
			yelp = b[i]-1
			sqfluctdataname = bgn+foldername+'/'+name+newname+'_mode'+str(yelp+1)+'.'+endname
			fout = open(sqfluctdataname,'w')
			if separatevar=='0':
				a = 0
				while a < numatom:
					fout.write(str(a))
					fout.write("""	""")
					fout.write(str(prody.calcSqFlucts(npzmodel[yelp])[a]))
					fout.write("""
""")
					a +=1
			elif separatevar=='1':
				a=0
				while a <numatom:
					firstresnum=int(p38.getResnums()[0:1][0])
					origiresnum=int(p38.getResnums()[0:1][0])
					while firstresnum<(int(numatom*1.0/p38.numChains())+origiresnum):
						fout.write(str(firstresnum))
						fout.write('\t')
						fout.write(str(prody.calcSqFlucts(npzmodel[yelp])[a]))
						fout.write('\n')
						a+=1
						firstresnum+=1
					fout.write('&\n')
			fout.close()
			print sqfluctdataname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+sqfluctdataname)
			i+=1
#3
def sqfluctplot(npzfilename, mode, showresults,foldername, newname, endname):
	import prody
	import os
	import matplotlib.pyplot as plt
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)

	try:
		open(bgn+foldername+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/')
		except (OSError):
			mer = 0
	if mode=='all' or mode=="'all'" or mode== ' all':
		a=0
		a1=len(npzmodel.getEigvals())
		while a < a1:
			plt.figure(figsize=(5,4))
			prody.showSqFlucts(npzmodel[a])
			plt.grid()
			sqfluctplotname = bgn+foldername+'/'+name+newname+'_mode'+str(a+1)+'.'+endname
			plt.savefig(sqfluctplotname)
			print sqfluctplotname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+sqfluctplotname)
			a +=1
	else:
		a = mode+' '
		b = [0]*len(a)
		i = 0
		j = 0
		b1 = 0
		while i < len(a):
			if a[i:i+1] ==' ' or a[i:i+1]==',':
				b[b1]=int(a[j:i])
				j = i+1
				i +=1
				b1 +=1
			else:
				i +=1
		del b[b1:]
		i=0
		while i < len(b):
			a = b[i]-1
			plt.figure(figsize=(5,4))
			prody.showSqFlucts(npzmodel[a])
			plt.grid()
			sqfluctplotname = bgn+foldername+'/'+name+newname+'_mode'+str(a+1)+'.'+endname
			plt.savefig(sqfluctplotname)
			print sqfluctplotname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+sqfluctplotname)
			i+=1
#4,5,6,7
def overlapall(choice,npzfilename,comparefile,mode,compmode1,compmode2,showresults,foldername, newname4, endname4, newname5, endname5, newname6, endname6, newname7, endname7):
	import prody
	import os
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)

	comparemodel = prody.loadModel(comparefile)
	find = 0					#
	while find < len(comparefile):			#
		if comparefile[-(find+1):-find] == '/':	#
			bgn1 = len(comparefile)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name1 = comparefile[bgn1:-8]			#
	except (NameError):				#
		bgn1 = 0				#
		name1 = comparefile[bgn1:-8]			#
	try:							#
		open(bgn+foldername+'/')				# creates the folders
	except (IOError):					# where the files will
		try:						# be saved only if they
			os.makedirs(bgn+foldername+'/')		# are not there
		except (OSError):				#
			mer = 0
	if choice=='4':
		if mode=='all' or mode=="'all'" or mode== ' all':
			a=0
			a1=len(npzmodel.getEigvals())
			while a < a1:
				overlapname = bgn+foldername+'/'+name+'_'+name1+newname4+'_mode'+str(a+1)+'.'+endname4
				prody.writeArray(overlapname,prody.calcCumulOverlap(npzmodel[a],comparemodel),'%.18e')#,array=True
				print overlapname
				if showresults=='1':
					os.system('/usr/bin/gnome-open '+overlapname)
				a +=1
		else:
			a = mode+' '
			b = [0]*len(a)
			i = 0
			j0 = 0
			b1 = 0
			while i < len(a):
				if a[i:i+1] ==' ' or a[i:i+1]==',':
					b[b1]=int(a[j0:i])
					j0 = i+1
					i +=1
					b1 +=1
				else:
					i +=1
			del b[b1:]
			i=0
			while i < len(b):
				a = b[i]-1
				overlapname = bgn+foldername+'/'+name+'_'+name1+newname4+'_mode'+str(a+1)+'.'+endname4
				prody.writeArray(overlapname,prody.calcCumulOverlap(npzmodel[a],comparemodel),'%.18e')#,array=True
				print overlapname
				if showresults=='1':
					os.system('/usr/bin/gnome-open '+overlapname)
				i+=1
	elif choice=='5':
		import matplotlib.pyplot as plt
		if mode=='all' or mode=="'all'" or mode== ' all':
			a=0
			a1=len(npzmodel.getEigvals())
			while a < a1:
				plt.figure(figsize=(5,4))
				prody.showCumulOverlap(npzmodel[a],comparemodel)
				prody.showOverlap(npzmodel[a],comparemodel)
				plt.title('Overlap with Mode '+str(a+1)+' from '+name)
				plt.xlabel(name1+' mode index')
				overlapname = bgn+foldername+'/'+name+'_'+name1+newname5+'_mode'+str(a+1)+'.'+endname5
				plt.savefig(overlapname)
				print overlapname
				if showresults=='1':
					os.system('/usr/bin/gnome-open '+overlapname)
				a +=1
		else:
			a = mode+' '
			b = [0]*len(a)
			i = 0
			j0 = 0
			b1 = 0
			while i < len(a):
				if a[i:i+1] ==' ' or a[i:i+1]==',':
					b[b1]=int(a[j0:i])
					j0 = i+1
					i +=1
					b1 +=1
				else:
					i +=1
			del b[b1:]
			i=0
			while i < len(b):
				a = b[i]-1
				plt.figure(figsize=(5,4))
				prody.showCumulOverlap(npzmodel[a],comparemodel)
				prody.showOverlap(npzmodel[a],comparemodel)
				plt.title('Overlap with Mode '+str(a+1)+' from '+name)
				plt.xlabel(name1+' mode index')
				overlapname = bgn+foldername+'/'+name+'_'+name1+newname5+'_mode'+str(a+1)+'.'+endname5
				plt.savefig(overlapname)
				print overlapname
				if showresults=='1':
					os.system('/usr/bin/gnome-open '+overlapname)
				i+=1


	elif choice=='6':
		overlapname = bgn+foldername+'/'+name+'_'+name1+newname6+'.'+endname6
		prody.writeOverlapTable(overlapname,comparemodel[int(compmode1)-1:int(compmode2)],npzmodel[int(compmode1)-1:int(compmode2)])
		print overlapname
		if showresults=='1':
			os.system('/usr/bin/gnome-open '+overlapname)

	elif choice=='7':
		import matplotlib.pyplot as plt
		plt.figure(figsize=(5,4))
		prody.showOverlapTable(comparemodel,npzmodel)
		plt.xlim(int(compmode1)-1,int(compmode2))
		plt.ylim(int(compmode1)-1,int(compmode2))
		plt.title(name1+' vs '+name+' Overlap')
		plt.ylabel(name1)
		plt.xlabel(name)
		overlapname = bgn+foldername+'/'+name+'_'+name1+newname7+'.'+endname7
		plt.savefig(overlapname)
		print overlapname
		if showresults=='1':
			os.system('/usr/bin/gnome-open '+overlapname)
#8
def modedata(npzfilename, showresults,foldername, newname, endname):
	import prody
	import os
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find	#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)

	try:
		open(bgn+foldername+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/')
		except (OSError):
			mer = 0
	modedataname = bgn+foldername+'/'+name+newname+'.'+endname
	fout = open(modedataname,'w')
	numatom = npzmodel.numAtoms()
	mer = 0
	while mer< len(npzmodel.getEigvals()):
		slowest_mode = npzmodel[mer]
		r = slowest_mode.getEigvec()
		p = slowest_mode.getEigval()
		tt = 0
		ttt = 1
		tttt = 2
		fout.write('MODE {0:3d}		{1:15e}'.format(mer+1,p))
		fout.write("""
-------------------------------------------------
""")
		if len(r)/numatom == 3:
			while tt < numatom*3:
				fout.write("""{0:15e}{1:15e}{2:15e}
""".format(r[tt],r[ttt],r[tttt]))	# better format for saving files
				tt +=3
				ttt+=3
				tttt+=3
		else:
			while tt < numatom:
				fout.write("""{0:15e}
""".format(r[tt]))	# nicer way to save files
				tt +=1
		mer +=1
	fout.close()
	print modedataname
	if showresults=='1':
		os.system('/usr/bin/gnome-open '+modedataname)
#9
def modeplot(npzfilename, mode, showresults,foldername, newname, endname):
	import prody
	import os
	import matplotlib.pyplot as plt
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find	#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)

	try:
		open(bgn+foldername+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/')
		except (OSError):
			mer = 0
	if mode=='all' or mode=="'all'" or mode== ' all':
		a=0
		a1=len(npzmodel.getEigvals())
		while a < a1:
			plt.figure(figsize = (6,4))
			prody.showMode(npzmodel[a])
			plt.grid()
			modeplotname = bgn+foldername+'/'+name+newname+str(a+1)+'.'+endname
			plt.savefig(modeplotname)
			print modeplotname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+modeplotname)
			a +=1
	else:
		a = mode+' '
		b = [0]*len(a)
		i = 0
		j = 0
		b1 = 0
		while i < len(a):
			if a[i:i+1] ==' ' or a[i:i+1]==',':
				b[b1]=int(a[j:i])
				j = i+1
				i +=1
				b1 +=1
			else:
				i +=1
		del b[b1:]
		i=0
		while i < len(b):
			a = b[i]-1
			plt.figure(figsize = (6,4))
			prody.showMode(npzmodel[a])
			plt.grid()
			modeplotname = bgn+foldername+'/'+name+newname+str(a+1)+'.'+endname
			plt.savefig(modeplotname)
			print modeplotname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+modeplotname)
			i+=1


#10
def collectivitydata(npzfilename,showresults,massnomass,foldername, newname, endname):
	import prody
	import os
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	if 'ANM' in bgn:
		brat=7
	elif 'GNM' in bgn:
		brat=2
	else:
		brat=1
	npzmodel = prody.loadModel(npzfilename)
	numatom=npzmodel.numAtoms()###
	eigval=npzmodel.getEigvals()###
	try:
		pdbfilename = bgn+'../'+name+'.pdb'
		p38 = prody.parsePDB(pdbfilename)
	except:
		try:
			pdbfilename = bgn+'../'+name+'.pdb.gz'
			p38 = prody.parsePDB(pdbfilename)
		except:
			try:
				pdbfilename = bgn+name+'.pdb'
				p38=prody.parsePDB(pdbfilename)
			except:
				try:
					pdbfilename = bgn+name+'.pdb.gz'
					p38=prody.parsePDB(pdbfilename)
				except:
					import tkFileDialog
					pdbfilename = tkFileDialog.Open(initialdir='~',filetypes=[('PDB','.pdb'),('PDB gz','.pdb.gz'),('all files','*')]).show()
					p38 = prody.parsePDB(pdbfilename)
	anohc = 0
	numatom = npzmodel.numAtoms()		# number of atoms
	while anohc < 5:
		if anohc == 0:
			calphas = p38.select('protein')
		elif anohc == 1:
			calphas = p38.select('protein and not name "[1-9]?H.*"')
		elif anohc == 2:
			calphas = p38.select('protein and name CA')
		elif anohc == 3:
			calphas = p38.select('protein and name CA C O N H')
		elif anohc == 4:
			calphas = p38.select('protein and not name CA C O N H')
		atomname = calphas.getNames()
		if numatom != len(atomname):
			anohc +=1
		else:
			break
	try:							#
		open(bgn+foldername+'/')					# creates the folders
	except (IOError):
		try:						#
			os.makedirs(bgn+foldername+'/')	#
		except (OSError):				#
			mer = 0					#
	mer = 0
	xx = [0]*(numatom) # sets the array to zero and other initial conditions
	i = 0
	aa = 0
	no = 0
	var3 = 0
	sss = [0]*(len(eigval))
	while mer< len(eigval):
		slowest_mode = npzmodel[mer]###
		r = slowest_mode.getEigvec()###
		p = slowest_mode.getEigval()###
		a = 0
		tt = 0
		ttt = 1
		tttt = 2
		while a < numatom:
			atom = atomname[a]
			mass = 0
			while mass < 2:
				if atom[mass] == "N": # all nitrogen
					m = 14.0067
					break
				elif atom[mass] == 'H': # all hydrogen
					m = 1.00794
					break
				elif atom[mass] == "C" : # all carbon
					m = 12.0107
					break
				elif atom[mass] == "O" : # all oxygen
					m = 15.9994
					break
				elif atom[mass] == 'S': # all sulfur
					m = 32.065
					break
				elif atom[mass] == 'P' : # all phosphorus
					m = 30.973762
					break
				else:
					if mass == 0:
						mass +=1
						try:
							atom[mass]
						except (IndexError):
							m = 1
							if no == 0:
								print 'Enter atom '+atom+' in to the system. Its mass was set to 1 in this simulation.'
								no +=1
							break
					else:
						m = 1
						if no == 0:
							print 'Enter atom '+atom+' in to the system. Its mass was set to 1 in this simulation'
							no +=1
						break
			if len(r)/numatom == 3:
				xx[i] = (r[tt]**2 + r[ttt]**2 + r[tttt]**2)/m
				i +=1
				tt +=3
				ttt+=3
				tttt+=3
			else:
				xx[i] = (r[tt]**2)/m
				i +=1
				tt +=1
			a +=1
		var3 = 0
		j = 0
		loop = 1
		while loop == 1:
			if sum(xx) == 0: # need this because you can't divide by 0
				loop = 0
			elif j <(numatom):
				var1 = xx[j]/sum(xx)
				if var1 == 0:
					var2 = 0
				elif var1 != 0:
					from math import log # this means natural log
					var2 = var1* log(var1)
				var3 += var2
				j +=1
			else:
				from math import exp
				k = exp(-var3)/numatom
				sss[aa] = k, aa+1
				aa +=1
				mer +=1
				loop = 0
				i = 0
				xx = [0]*(numatom)  # goes through all this until the big loop is done
	a = 0
	k=[0]*(len(eigval))
	while a < len(eigval):
		k[a]= prody.calcCollectivity(npzmodel[a]),a+1
		a +=1


	collectivefile = bgn+foldername+'/'+name+newname+'.'+endname
	fout = open(collectivefile,'w')
	if massnomass=='0':
		fout.write('MODE      COLLECTIVITY(mass)')
		fout.write("""
---------------------------
""")
		for h in sorted(sss,reverse=True):
			fout.write(str(h)[-3:-1]+'        '+str(h)[1:19]+"""
""")
		fout.write("""

MODE      COLLECTIVITY(without mass)""")
		fout.write("""
---------------------------
""")
		for hh in sorted(k,reverse=True):
			fout.write(str(hh)[-3:-1]+'        '+str(hh)[1:19]+"""
""")
	elif massnomass=='1':
		fout.write('MODE      COLLECTIVITY(without mass)')
		fout.write("""
---------------------------
""")
		for hh in sorted(k,reverse=True):
			fout.write(str(hh)[-3:-1]+'        '+str(hh)[1:19]+"""
""")
		fout.write("""

MODE      COLLECTIVITY(mass)""")
		fout.write("""
---------------------------
""")
		for h in sorted(sss,reverse=True):
			fout.write(str(h)[-3:-1]+'        '+str(h)[1:19]+"""
""")
	fout.close()
	if showresults=='1':
		os.system('/usr/bin/gnome-open '+collectivefile)

	fin = open(collectivefile,'r')
	lst = fin.readlines()
	hi0 = 2
	looop = 1
	prut=0
	secoll=0
	thicoll=0
	while looop == 1:
		fine = lst[hi0]
		if int(fine[0:2]) >= brat:
			if prut==0:
				prut=fine[0:2]
			elif secoll==0:
				secoll=fine[0:2]
			elif thicoll==0:
				thicoll=fine[0:2]
			else:
				foucoll=fine[0:2]
				looop = 0
		else:
			hi0 +=1
	print "Mode "+prut+" is the most collective."
	return (prut,"Mode "+prut+" is the most collective.")
	fin.close()








#11
def tempfactorsdata(npzfilename,showresults,foldername, newname, endname):
	import prody
	import os
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)
	try:							#
		open(bgn+foldername+'/')					# creates the folders
	except (IOError):					# where the files will
		try:						# be saved only if they
			os.makedirs(bgn+foldername+'/')		# are not there
		except (OSError):				#
			mer = 0					#
	try:
		pdbfilename = bgn+'../'+name+'.pdb'
		p38 = prody.parsePDB(pdbfilename)
	except:
		try:
			pdbfilename = bgn+'../'+name+'.pdb.gz'
			p38 = prody.parsePDB(pdbfilename)
		except:
			try:
				pdbfilename = bgn+name+'.pdb'
				p38=prody.parsePDB(pdbfilename)
			except:
				try:
					pdbfilename = bgn+name+'.pdb.gz'
					p38=prody.parsePDB(pdbfilename)
				except:
					import tkFileDialog
					pdbfilename = tkFileDialog.Open(initialdir='~',filetypes=[('PDB','.pdb'),('PDB gz','.pdb.gz'),('all files','*')]).show()
					p38 = prody.parsePDB(pdbfilename)
	anohc = 0
	numatom = npzmodel.numAtoms()		# number of atoms
	while anohc < 5:
		if anohc == 0:
			calphas = p38.select('protein')
		elif anohc == 1:
			calphas = p38.select('protein and not name "[1-9]?H.*"')
		elif anohc == 2:
			calphas = p38.select('protein and name CA')
		elif anohc == 3:
			calphas = p38.select('protein and name CA C O N H')
		elif anohc == 4:
			calphas = p38.select('protein and not name CA C O N H')
		atomname = calphas.getNames()
		if numatom != len(atomname):
			anohc +=1
		else:
			break
	fin=open(pdbfilename,'r')
	d = [None]*len(atomname)
	e = 0
	for line in fin:
		pair = line.split()
		if 'ATOM  ' in line and e < len(atomname):
			if str(pair[2]) == str(atomname[e]):
				d[e]=str(pair[1])
				e+=1
			else:
				e+=0
		else:
			continue
	fin.close()
	sqf = prody.calcSqFlucts(npzmodel)
	x = sqf/((sqf**2).sum()**.5)
	y = prody.calcTempFactors(npzmodel,calphas)
	a = 0
	tempfactorsdataname =bgn+foldername+'/'+name+newname+'.'+endname
	fout=open(tempfactorsdataname,'w')
	fout.write("""Atom	Residue	      TempFactor   TempFactor with exp beta
""")
	while a < npzmodel.numAtoms():
		fout.write("""{0:4s}	{1:4d}	{2:15f}	{3:15f}
""".format(d[a],a+1,x[a],y[a]))
		a +=1
	fout.close()
	print tempfactorsdataname
	if showresults=='1':
		os.system('/usr/bin/gnome-open '+tempfactorsdataname)
#13
def fracvardata(npzfilename,showresults,foldername,newname, endname):
	import prody
	import os
	import matplotlib.pyplot as plt
	find = 0					#
	while find < len(npzfilename):			#
		if npzfilename[-(find+1):-find] == '/':	#
			bgn = len(npzfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		name = npzfilename[bgn:-8]			#
	except (NameError):				#
		bgn = 0					#
		name = npzfilename[bgn:-8]			#
	bgn = npzfilename[:bgn]				# path for file
	npzmodel = prody.loadModel(npzfilename)
	try:							#
		open(bgn+foldername+'/')					# creates the folders
	except (IOError):					# where the files will
		try:						# be saved only if they
			os.makedirs(bgn+foldername+'/')		# are not there
		except (OSError):				#
			mer = 0					#

	plt.figure(figsize = (5,4))
	prody.showFractVars(npzmodel)
	prody.showCumulFractVars(npzmodel)
	fracvardataname =bgn+foldername+'/'+name+newname+'.'+endname
	plt.savefig(fracvardataname)
	print fracvardataname
	if showresults=='1':
		os.system('/usr/bin/gnome-open '+fracvardataname)
#14
def add(letter):
	if letter=='A':
		return 'B'
	elif letter=='B':
		return 'C'
	elif letter=='C':
		return 'D'
	elif letter=='D':
		return 'E'
	elif letter=='E':
		return 'F'
	elif letter=='F':
		return 'G'
	elif letter=='G':
		return 'H'
	elif letter=='H':
		return 'I'
	elif letter=='I':
		return 'J'
	elif letter=='J':
		return 'K'
	elif letter=='K':
		return 'L'
	elif letter=='L':
		return 'M'
	elif letter=='M':
		return 'N'
	elif letter=='N':
		return 'O'
	elif letter=='O':
		return 'P'
	elif letter=='P':
		return 'Q'
	elif letter=='Q':
		return 'R'
	elif letter=='R':
		return 'S'
	elif letter=='S':
		return 'T'
	elif letter=='T':
		return 'U'
	elif letter=='U':
		return 'V'
	elif letter=='V':
		return 'W'
	elif letter=='W':
		return 'X'
	elif letter=='X':
		return 'Y'
	elif letter=='Y':
		return 'Z'
	elif letter=='Z':
		return 'A'

def calcphipsi(pdbfilename,showresults,foldername,newname,endname):
	import prody
	import os
	find = 0					#
	while find < len(pdbfilename):			#
		if pdbfilename[-(find+1):-find] == '/':	#
			bgn = len(pdbfilename)-find		#
			break				#
		else:					# helps in the
			find +=1			# saving of files
	try:						#
		float(bgn)				#
	except (NameError):				#
		bgn = 0					#
	find = 0					#
	while bgn+find<len(pdbfilename):			#
		if pdbfilename[bgn+find:bgn+find+1] == '.':	#
			end = len(pdbfilename)-(bgn+find)	#
			break				#
		else:					#
			find +=1			#
	try:						#
		name = pdbfilename[bgn:-end]			#
	except (NameError):				#
		name = pdbfilename[bgn:len(pdbfilename)]		# name of the file
	bgn = pdbfilename[:bgn]				# path for file
	try:
		open(bgn+foldername+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/')
		except (OSError):
			mer = 0
	try:
		open(bgn+foldername+'/'+name+'/')
	except (IOError):
		try:
			os.makedirs(bgn+foldername+'/'+name+'/')
		except (OSError):
			mer = 0
	pdb=prody.parsePDB(pdbfilename)
	lenchain=pdb.numResidues()
	nummodels=pdb.numCoordsets()
	nummodels1=1
	psi=[0]*(lenchain*nummodels)
	phi=[0]*(lenchain*nummodels)
	endres=int(lenchain*1.0/len(pdb.getHierView()))
	oldchain='A'
	firstresnum=int(pdb.getResnums()[0:1][0])
	while nummodels1<=nummodels:
		newpdb=prody.parsePDB(pdbfilename,model=nummodels1)
		pdbchain='A'
		pdbresnum=1
		pdbresnum1=firstresnum
		while pdbresnum<=lenchain:
			if pdbresnum1==int(int(pdb.getResnums()[-2:-1][0])+1):
				pdbresnum1=firstresnum
			try:
				phi[pdbresnum-1]=prody.calcPhi(newpdb[pdbchain,pdbresnum1])
			except:
				mer=0
			if pdbresnum%endres==0:
				oldchain=pdbchain
				pdbchain=add(pdbchain)
			try:
				psi[pdbresnum-1]=prody.calcPsi(newpdb[pdbchain,pdbresnum1])
			except:
				mer=0
			if pdbresnum%endres==0:
				modelsname = bgn+foldername+'/'+name+'/'+oldchain+str(pdbresnum)+'.txt'
			else:
				modelsname = bgn+foldername+'/'+name+'/'+pdbchain+str(pdbresnum)+'.txt'
			if nummodels1==1:
				fout=open(modelsname,'w')
			else:
				fout=open(modelsname,'a')
			fout.write('{0:3d}\t {1:10f}\t {2:10f}\n'.format(nummodels1,phi[pdbresnum-1],psi[pdbresnum-1]))
			fout.close()
			pdbresnum+=1
			pdbresnum1+=1
		nummodels1+=1
	pdbchain='A'
	pdbresnum=1
	sampleavgname=bgn+foldername+'/'+name+'/'+newname+'.'+endname
	fout=open(sampleavgname,'w')
	phiarray=[0]*nummodels
	psiarray=[0]*nummodels
	import numpy
	while pdbresnum<=lenchain:
		if pdbresnum%endres==0:
			modelsname = bgn+foldername+'/'+name+'/'+pdbchain+str(pdbresnum)+'.txt'
			oldchain=pdbchain
			pdbchain=add(pdbchain)
		else:
			modelsname = bgn+foldername+'/'+name+'/'+pdbchain+str(pdbresnum)+'.txt'
		fin=open(modelsname,'r')
		nummodels1=0
		for line in fin:
			pair=line.split()
			phiarray[nummodels1]=float(pair[1])
			psiarray[nummodels1]=float(pair[2])
			nummodels1+=1
		fin.close()
		if pdbresnum%endres==0:
			fout.write('{0:1s} {1:3d}\t {2:10f} +/- {3:10f}\t {4:10f} +/- {5:10f}\n'.format(oldchain,pdbresnum,numpy.average(phiarray),numpy.std(phiarray),numpy.average(psiarray),numpy.std(psiarray)))
		else:
			fout.write('{0:1s} {1:3d}\t {2:10f} +/- {3:10f}\t {4:10f} +/- {5:10f}\n'.format(pdbchain,pdbresnum,numpy.average(phiarray),numpy.std(phiarray),numpy.average(psiarray),numpy.std(psiarray)))
		pdbresnum+=1
	fout.close()
	print sampleavgname
	if showresults=='1':
		os.system('/usr/bin/gnome-open '+sampleavgname)


#### can add to backpage definitions here

