def gammaDistanceDependent(dist2, *args):

	if dist2 <= 10000:
		return dist2**(float(savedfile[91])/2.0)
	else:
		return 0.
def corepagecalculation(pdbfilename, selatom, noma1, nummodes, gamcut, cut1, gam2, cut2, showresults, smodes, snmd, smodel, scollec, massnomass, sample1, modeens, confens, rmsdens, traverse1, modetra, steptra, rmsdtra, modelnumber, caanm, cagnm, nohanm, nohgnm, allanm, allgnm, bbanm, bbgnm, scanm, scgnm, nmdfolder, modesfolder, collectivityfolder, modelnewname, nmdnewname, modesnewname, modesendname, collectivitynewname, collectivityendname, samplenewname, traversenewname, crosscorr=0, corrfolder='', corrname='', corrend='', compmode01='7', compmode02='15', sqflucts=0, sqfluctsfolder='', sqfluctsname='', sqfluctsend='', separatevar1='0', temfac=0, temfacfolder='', temfacname='', temfacend='', fracovar=0, fraconame='', fracoend='', ovlap=0, ovlapfold='', ovlapname='', ovlapend='', ovlaptab=0, ovlaptabname='', ovlaptabend='', comppdbfilename=''):
# modelnumber
	import prody
	import time
	import os
	import Tkinter
	root=Tkinter.Tk()
	root.title('Info')
	onlypage=Tkinter.Frame(root)
	onlypage.pack(side='top')
	Tkinter.Label(onlypage,text='File: '+pdbfilename).grid(row=0,column=0,sticky='w')
	Tkinter.Label(onlypage,text='Atoms: '+selatom).grid(row=1,column=0,sticky='w')
	Tkinter.Label(onlypage,text='Analysis: '+noma1).grid(row=2,column=0,sticky='w')
	path=os.path.join(os.path.expanduser('~'),'.noma/')
	fin = open(path+'savefile.txt','r')
	global savedfile
	savedfile=fin.readlines()
	fin.close()
	i=0
	a=len(savedfile)
	while i<a:
		savedfile[i]=savedfile[i][:-1]
		i+=1
	if gamcut=='0':
		Tkinter.Label(onlypage,text='Gamma: r^'+savedfile[91]).grid(row=3,column=0,sticky='w')
		Tkinter.Label(onlypage,text='Cutoff: '+cut1).grid(row=4,column=0,sticky='w')
	elif gamcut=='1':
		Tkinter.Label(onlypage,text='Gamma: '+gam2).grid(row=3,column=0,sticky='w')
		Tkinter.Label(onlypage,text='Cutoff: '+cut2).grid(row=4,column=0,sticky='w')



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
	mytimeis = time.asctime(time.localtime(time.time()))
	start = time.time()
	try:
		p38 = prody.parsePDB(pdbfilename,model=int(modelnumber))
	except:
		import tkMessageBox
		tkMessageBox.askokcancel("File Error","""This is not the correct path or name. Try entering /some/path/nameoffile.pdb
If you need help finding the path, open a new terminal and enter:
find -name 'filename.pdb'        use the output as the pdb input
If this doesn't work, make sure the file is in PDB format.""")
		p38 = prody.parsePDB(pdbfilename)
	print 'Submitted: '+pdbfilename+' at '+mytimeis
	Tkinter.Label(onlypage,text='Submitted at: '+mytimeis).grid(row=5,column=0,sticky='w')
	root.update()
	if selatom == "C-alpha" and noma1 == "Gaussian Normal Mode":
		folder = cagnm+'/'
		pro = p38.select('protein and name CA')	# selects only carbon alpahs
	elif selatom == "C-alpha" and noma1 == "Anisotropic Normal Mode":
		folder = caanm+'/'
		pro = p38.select('protein and name CA')
	elif selatom == "Heavy" and noma1 == "Gaussian Normal Mode":
		folder = nohgnm+'/'
		pro = p38.select('protein and not name "[1-9]?H.*"') # gets rid of all Hydrogens
	elif selatom == "Heavy" and noma1 == "Anisotropic Normal Mode":
		folder = nohanm+'/'
		pro = p38.select('protein and not name "[1-9]?H.*"')
	elif selatom == "All" and noma1 == "Gaussian Normal Mode":
		folder = allgnm+'/'
		pro = p38.select('protein')
	elif selatom == "All" and noma1 == "Anisotropic Normal Mode":
		folder = allanm+'/'
		pro = p38.select('protein')
	elif selatom == "Backbone" and noma1 == "Gaussian Normal Mode":
		folder = bbgnm+'/'
		pro = p38.select('protein and name CA C O N H')	# selects backbone
	elif selatom == "Backbone" and noma1 == "Anisotropic Normal Mode":
		folder = bbanm+'/'
		pro = p38.select('protein and name CA C O N H')	# selects backbone
	elif selatom == "Sidechain" and noma1 == "Gaussian Normal Mode":
		folder = scgnm+'/'
		pro = p38.select('protein and not name CA C O N H')	# selects sidechain
	elif selatom == "Sidechain" and noma1 == "Anisotropic Normal Mode":
		folder = scanm+'/'
		pro = p38.select('protein and not name CA C O N H')	# selects sidechain
	try:							#
		open(bgn+folder)				# creates the folders
	except (IOError):					# where the files will
		try:						# be saved only if they
			os.makedirs(bgn+folder)			# are not there
		except (OSError):				#
			mer = 0					#
	if noma1 == "Gaussian Normal Mode":
		print 'Building the Kirchhoff matrix'
		Tkinter.Label(onlypage,text='Building Kirchhoff').grid(row=6,column=0,sticky='w')
		root.update()
		anm = prody.GNM(name)###
		if gamcut=='0':
			anm.buildKirchhoff(pro,cutoff=float(cut1),gamma=gammaDistanceDependent)###
			anm.setKirchhoff(anm.getKirchhoff())
		elif gamcut=='1':
			anm.buildKirchhoff(pro,cutoff=float(cut2),gamma=float(gam2))###
		brat = 2
	elif noma1 == "Anisotropic Normal Mode":
		print 'Building the Hessian matrix'
		Tkinter.Label(onlypage,text='Building Hessian').grid(row=6,column=0,sticky='w')
		root.update()
		anm = prody.ANM(name)###
		if gamcut=='0':
			anm.buildHessian(pro,cutoff=float(cut1),gamma=gammaDistanceDependent)###
			anm.setHessian(anm.getHessian())###
		elif gamcut=='1':
			anm.buildHessian(pro,cutoff=float(cut2),gamma=float(gam2))###
		brat = 7
	print 'Calculating modes'
	Tkinter.Label(onlypage,text='Calculating modes').grid(row=7,column=0,sticky='w')
	root.update()
	anm.calcModes(int(nummodes),zeros = True)###
	numatom=anm.numAtoms()###
	eigval=anm.getEigvals()###
	atomname=pro.getNames()###
	if smodel==1:
		if brat==2:
			modelfilename=bgn+folder+name+modelnewname+'.gnm.npz'
		elif brat==7:
			modelfilename=bgn+folder+name+modelnewname+'.anm.npz'
		print 'Saving Model'
		Tkinter.Label(onlypage,text='Saving Model').grid(row=8,column=0,sticky='w')
		root.update()
		try:
			prody.saveModel(anm,bgn+folder+name+modelnewname,True)###
		except:
			print 'Matrix not saved due to size'
			Tkinter.Label(onlypage,text='Matrix not saved').grid(row=8,column=0,sticky='w')
			root.update()
			prody.saveModel(anm,bgn+folder+name+modelnewname)###
	if snmd==1:
		print 'Saving NMD'
		Tkinter.Label(onlypage,text='Saving NMD').grid(row=9,column=0,sticky='w')
		root.update()
		try:						#
			os.makedirs(bgn+folder+nmdfolder+'/')		#
		except (OSError):				#
			mer = 0					#
		prody.writeNMD(bgn+folder+nmdfolder+'/'+name+nmdnewname+'.nmd',anm[:len(eigval)],pro)###	# this can be viewed in VMD
	if smodes==1:
		print 'Saving Modes'
		Tkinter.Label(onlypage,text='Saving Modes').grid(row=10,column=0,sticky='w')
		root.update()
		try:						#
			os.makedirs(bgn+folder+modesfolder+'/')	#
		except (OSError):				#
			mer = 0					#
		modefile = bgn+folder+modesfolder+'/'+name+modesnewname+'.'+modesendname
		fout = open(modefile,'w')
		mer = 0
		while mer< len(eigval):
			slowest_mode = anm[mer]###
			r = slowest_mode.getEigvec()###
			p = slowest_mode.getEigval()###
			tq = 0
			tt = 0
			ttt = 1
			tttt = 2
			fout.write('MODE {0:3d}		{1:15e}'.format(mer+1,p))
			fout.write("""
-------------------------------------------------
""")
			if noma1 == "Gaussian Normal Mode":
				while tq < numatom:
					fout.write("""{0:4s}{1:15e}
""".format(atomname[tq],r[tq]))
					tq +=1
			elif noma1 == "Anisotropic Normal Mode":
				while tt < numatom*3:
					fout.write("""{0:4s}{1:15e}{2:15e}{3:15e}
""".format(atomname[tq],r[tt],r[ttt],r[tttt]))
					tq+=1
					tt +=3
					ttt+=3
					tttt+=3
			mer +=1
		fout.close()
		if showresults=='1':
			os.system('/usr/bin/gnome-open '+modefile)
	if scollec==1:
		print 'Saving collectivity'
		Tkinter.Label(onlypage,text='Saving collectivity').grid(row=11,column=0,sticky='w')
		root.update()
		try:						#
			os.makedirs(bgn+folder+collectivityfolder+'/')	#
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
			slowest_mode = anm[mer]###
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
			k[a]=prody.calcCollectivity(anm[a]),a+1
			a +=1


		collectivefile = bgn+folder+collectivityfolder+'/'+name+collectivitynewname+'.'+collectivityendname
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
		mostcollective= "Mode "+prut+" is the most collective."
		Tkinter.Label(onlypage,text='Mode '+prut+' is the most collective').grid(row=12,column=0,sticky='w')
		root.update()
		print mostcollective
		fin.close()

	if sample1 == 1:
		print 'Saving sample file'
		Tkinter.Label(onlypage,text='Saving sample file').grid(row=13,column=0,sticky='w')
		root.update()
		a = modeens+' '
		b = [0]*(len(a)+1)
		i = 0
		j = 0
		b1 = 0
		while i < len(a):
			if a[i:i+1] ==' ' or a[i:i+1]==',':
				try:
					b[b1]=int(a[j:i])-1
				except:
					if '1c' in a[j:i]:
						b[b1]=int(prut)-1
					elif '2c' in a[j:i]:
						b[b1]=int(prut)-1
						b1 +=1
						b[b1]=int(secoll)-1
					elif '3c' in a[j:i]:
						b[b1]=int(prut)-1
						b1 +=1
						b[b1]=int(secoll)-1
						b1 +=1
						b[b1]=int(thicoll)-1
					elif '4c' in a[j:i]:
						b[b1]=int(prut)-1
						b1 +=1
						b[b1]=int(secoll)-1
						b1 +=1
						b[b1]=int(thicoll)-1
						b1+=1
						b[b1]=int(foucoll)-1
				j = i+1
				i +=1
				b1 +=1
			else:
				i +=1
		del b[b1:]
		ensemble = prody.sampleModes(anm[b],pro, n_confs=int(confens), rmsd =float(rmsdens))
		p38ens=pro.copy()
		p38ens.delCoordset(0)
		p38ens.addCoordset(ensemble.getCoordsets())
		prody.writePDB(bgn+folder+name+samplenewname+'.pdb',p38ens)


	if traverse1 ==1:
		print 'Saving traverse file'
		Tkinter.Label(onlypage,text='Saving traverse file').grid(row=14,column=0,sticky='w')
		root.update()
		if modetra=='c':
			modefortra=int(prut)-1
		else:
			modefortra=int(modetra)-1
		trajectory=prody.traverseMode(anm[modefortra],pro,n_steps=int(steptra),rmsd=float(rmsdtra))
		prody.calcRMSD(trajectory).round(2)
		p38traj=pro.copy()
		p38traj.delCoordset(0)
		p38traj.addCoordset(trajectory.getCoordsets())
		prody.writePDB(bgn+folder+name+'_mode'+str(modefortra+1)+traversenewname+'.pdb',p38traj)
	if crosscorr==1:
		print 'Saving cross correlation'
		Tkinter.Label(onlypage,text='Saving cross-correlation').grid(row=15,column=0,sticky='w')
		root.update()
		try:						#
			os.makedirs(bgn+folder+corrfolder+'/')	#
		except (OSError):				#
			mer = 0
		i=int(compmode01)
		while i <= int(compmode02):
			x=i-1
			correlationdataname=bgn+folder+corrfolder+'/'+name+corrname+'_mode'+str(x+1)+'.'+corrend
			prody.writeArray(correlationdataname,prody.calcCrossCorr(anm[x]),'%.18e')
			print correlationdataname
			i+=1

##
	if sqflucts==1:
		print 'Saving square fluctuation'
		Tkinter.Label(onlypage,text='Saving square fluctuation').grid(row=16,column=0,sticky='w')
		root.update()
		try:						#
			os.makedirs(bgn+folder+sqfluctsfolder+'/')	#
		except (OSError):				#
			mer = 0
		i=int(compmode01)
		while i < int(compmode02):
			yelp = i-1
			sqfluctdataname = bgn+folder+sqfluctsfolder+'/'+name+sqfluctsname+'_mode'+str(yelp+1)+'.'+sqfluctsend
			fout = open(sqfluctdataname,'w')
			if separatevar1=='0':
				a = 0
				while a < numatom:
					fout.write(str(a))
					fout.write("""	""")
					fout.write(str(prody.calcSqFlucts(anm[yelp])[a]))
					fout.write("""
""")
					a +=1
			elif separatevar1=='1':
				a=0
				while a <numatom:
					firstresnum=int(p38.getResnums()[0:1][0])
					origiresnum=int(p38.getResnums()[0:1][0])
					while firstresnum<(int(numatom*1.0/p38.numChains())+origiresnum):
						fout.write(str(firstresnum))
						fout.write('\t')
						fout.write(str(prody.calcSqFlucts(anm[yelp])[a]))
						fout.write('\n')
						a+=1
						firstresnum+=1
					fout.write('&\n')
			fout.close()
			print sqfluctdataname
			i+=1
	if temfac==1:
		print 'Saving temperature factors'
		Tkinter.Label(onlypage,text='Saving temperature factors').grid(row=17,column=0,sticky='w')
		root.update()
		try:						#
			os.makedirs(bgn+folder+temfacfolder+'/')	#
		except (OSError):				#
			mer = 0

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
		sqf = prody.calcSqFlucts(anm)
		x = sqf/((sqf**2).sum()**.5)
		y = prody.calcTempFactors(anm,pro)
		a = 0
		tempfactorsdataname =bgn+folder+temfacfolder+'/'+name+temfacname+'.'+temfacend
		fout=open(tempfactorsdataname,'w')
		fout.write("""Atom	Residue	      TempFactor   TempFactor with exp beta
""")
		while a < numatom:
			fout.write("""{0:4s}	{1:4d}	{2:15f}	{3:15f}
""".format(d[a],a+1,x[a],y[a]))
			a +=1
		fout.close()
		print tempfactorsdataname
	if fracovar==1:
		try:
			import matplotlib.pyplot as plt
			print 'Saving Fraction of Variance'
			Tkinter.Label(onlypage,text='Saving Fraction of Variance').grid(row=18,column=0,sticky='w')
			root.update()
			try:						#
				os.makedirs(bgn+folder+modesfolder+'/')	#
			except (OSError):				#
				mer = 0					#
			plt.figure(figsize = (5,4))
			prody.showFractVars(anm)
			prody.showCumulFractVars(anm)
			fracvardataname =bgn+folder+modesfolder+'/'+name+fraconame+'.'+fracoend
			plt.savefig(fracvardataname)
			print fracvardataname
			if showresults=='1':
				os.system('/usr/bin/gnome-open '+fracvardataname)
		except:
			print 'Error: Fraction of Variance'
			Tkinter.Label(onlypage,text='Error: Fraction of Variance').grid(row=18,column=0,sticky='w')
			root.update()
			mer=0

	if ovlap==1 or ovlaptab==1:
		try:
			import matplotlib.pyplot as plt
			print 'Saving Overlap'
			Tkinter.Label(onlypage,text='Saving Overlap').grid(row=19,column=0,sticky='w')
			root.update()


			Tkinter.Label(onlypage,text='Comparison: '+comppdbfilename).grid(row=20,column=0,sticky='w')


##
			find = 0
			while find < len(comppdbfilename):
				if comppdbfilename[-(find+1):-find] == '/':
					bgn1 = len(comppdbfilename)-find
					break
				else:
					find +=1
			try:
				float(bgn1)
			except (NameError):
				bgn1 = 0
			find = 0
			while bgn1+find<len(comppdbfilename):
				if comppdbfilename[bgn1+find:bgn1+find+1] == '.':
					end1 = len(comppdbfilename)-(bgn1+find)
					break
				else:
					find +=1
			try:
				name1 = comppdbfilename[bgn1:-end1]
			except (NameError):
				name1 = comppdbfilename[bgn1:len(comppdbfilename)]
			bgn1 = comppdbfilename[:bgn1]
			p381 = prody.parsePDB(comppdbfilename,model=int(modelnumber))
			if selatom == "C-alpha" and noma1 == "Gaussian Normal Mode":
				pro1 = p381.select('protein and name CA')
			elif selatom == "C-alpha" and noma1 == "Anisotropic Normal Mode":
				pro1 = p381.select('protein and name CA')
			elif selatom == "Heavy" and noma1 == "Gaussian Normal Mode":
				pro1 = p381.select('protein and not name "[1-9]?H.*"')
			elif selatom == "Heavy" and noma1 == "Anisotropic Normal Mode":
				pro1 = p381.select('protein and not name "[1-9]?H.*"')
			elif selatom == "All" and noma1 == "Gaussian Normal Mode":
				pro1 = p381.select('protein')
			elif selatom == "All" and noma1 == "Anisotropic Normal Mode":
				pro1 = p381.select('protein')
			elif selatom == "Backbone" and noma1 == "Gaussian Normal Mode":
				pro1 = p381.select('protein and name CA C O N H')
			elif selatom == "Backbone" and noma1 == "Anisotropic Normal Mode":
				pro1 = p381.select('protein and name CA C O N H')
			elif selatom == "Sidechain" and noma1 == "Gaussian Normal Mode":
				pro1 = p381.select('protein and not name CA C O N H')
			elif selatom == "Sidechain" and noma1 == "Anisotropic Normal Mode":
				pro1 = p381.select('protein and not name CA C O N H')
			if noma1 == "Gaussian Normal Mode":
				print 'Building the Kirchhoff matrix'
				Tkinter.Label(onlypage,text='Building Kirchhoff').grid(row=21,column=0,sticky='w')
				root.update()
				anm1 = prody.GNM(name1)
				if gamcut=='0':
					anm1.buildKirchhoff(pro1,cutoff=float(cut1),gamma=gammaDistanceDependent)
					anm1.setKirchhoff(anm1.getKirchhoff())
				elif gamcut=='1':
					anm1.buildKirchhoff(pro1,cutoff=float(cut2),gamma=float(gam2))
				brat = 2
			elif noma1 == "Anisotropic Normal Mode":
				print 'Building the Hessian matrix'
				Tkinter.Label(onlypage,text='Building Hessian').grid(row=21,column=0,sticky='w')
				root.update()
				anm1 = prody.ANM(name1)
				if gamcut=='0':
					anm1.buildHessian(pro1,cutoff=float(cut1),gamma=gammaDistanceDependent)
					anm1.setHessian(anm1.getHessian())
				elif gamcut=='1':
					anm1.buildHessian(pro1,cutoff=float(cut2),gamma=float(gam2))
				brat = 7
			print 'Calculating modes'
			Tkinter.Label(onlypage,text='Calculating modes').grid(row=22,column=0,sticky='w')
			root.update()
			anm1.calcModes(int(nummodes),zeros = True)
##
			try:
				os.makedirs(bgn+folder+ovlapfold+'/')
			except (OSError):
				mer = 0
			if ovlap==1:
				i=int(compmode01)
				while i < int(compmode02):
					a = i-1
					plt.figure(figsize=(5,4))
					prody.showCumulOverlap(anm[a],anm1)
					prody.showOverlap(anm[a],anm1)
					plt.title('Overlap with Mode '+str(a+1)+' from '+name)
					plt.xlabel(name1+' mode index')
					overlapname = bgn+folder+ovlapfold+'/'+name+'_'+name1+ovlapname+'_mode'+str(a+1)+'.'+ovlapend
					plt.savefig(overlapname)
					print overlapname
					i+=1
			if ovlaptab==1:
				plt.figure(figsize=(5,4))
				prody.showOverlapTable(anm1,anm)
				plt.xlim(int(compmode01)-1,int(compmode02))
				plt.ylim(int(compmode01)-1,int(compmode02))
				plt.title(name1+' vs '+name+' Overlap')
				plt.ylabel(name1)
				plt.xlabel(name)
				overlapname = bgn+folder+ovlapfold+'/'+name+'_'+name1+ovlaptabname+'.'+ovlaptabend
				plt.savefig(overlapname)
				print overlapname
		except:
			mer=0


	root.destroy()
	mynewtimeis = float(time.time()-start)
	if mynewtimeis <= 60.00:
		timeittook= "The calculations took %.2f s."%(mynewtimeis)
	elif mynewtimeis > 60.00 and mynewtimeis <= 3600.00:
		timeittook= "The calculations took %.2f min."%((mynewtimeis/60.00))
	else:
		timeittook= "The calculations took %.2f hrs."%((mynewtimeis/3600.00))
	print timeittook
	if smodel==1 and scollec==1:
		return (timeittook,modelfilename,str(int(prut)))
	elif scollec==1:
		return (timeittook,'nofile',str(int(prut)))
	elif smodel==1:
		return (timeittook,modelfilename,'nocoll')
	else:
		return (timeittook,'nofile','nocoll')

