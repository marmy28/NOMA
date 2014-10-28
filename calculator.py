def tree(event=None):
	a=T.get(1.0,INSERT)+"""
"""
	i=0
	for line in a:
		if """
""" in line:
			i+=1
	g=float(i-1)+.0
	h = float(i-1)+.99
	a= T.get(g,h).lower()
	i=0
	if """		""" in a:
		T.insert(INSERT,a.replace("""		""",''))
		i=2
	if """		""" in T.get(g+2,h+2) and i != 2:
		T.delete(g+2,g+3)
		i = 1
	a=a.replace('^','**')
	a=a.replace(u'\u221A','sqrt')
	a=a.replace(u'\u03C0','pi')
	a=a.replace('log(','log10(')
	a=a.replace('ln(','log(')
	a=a.replace('arctan(','atan(')
	a=a.replace('arccos(','acos(')
	a=a.replace('arcsin(','asin(')
	a=a.replace('arccot(','acot(')
	a=a.replace('arccsc(','acsc(')
	a=a.replace('arcsec(','asec(')
	a=a.replace('arctanh(','atanh(')
	a=a.replace('arccosh(','acosh(')
	a=a.replace('arcsinh(','asinh(')
	a=a.replace('arccoth(','acoth(')
	a=a.replace('arccsch(','acsch(')
	a=a.replace('arcsech(','asech(')
	a=a.replace('/','*1.0/')
	try:
		ans=eval(a)
		if i == 0:
			T.insert(INSERT,"""		"""+str(ans)+"""
""")
		elif i==1:
			T.insert(INSERT,"""		"""+str(ans))
	except:
		ans=a
		if i == 0:
			T.insert(INSERT,"""		"""+str(ans)+"""
""")
		elif i==1:
			T.insert(INSERT,"""		"""+str(ans))
def sqr():
	T.insert(INSERT,u'\u221A(')
def pie():
	T.insert(INSERT,u'\u03C0')
def hJs():
	T.insert(INSERT,'6.62606896*10^-34')
def heVs():
	T.insert(INSERT,'4.13566733*10^-15')
def cms():
	T.insert(INSERT,'2.99792458*10^8')
def kbJK():
	T.insert(INSERT,'1.38065*10^-23')
def kbeVK():
	T.insert(INSERT,'8.61773324*10^-5')
def mekg():
	T.insert(INSERT,'9.910938215*10^-31')
def mpkg():
	T.insert(INSERT,'1.672621637*10^-27')
def mnkg():
	T.insert(INSERT,'1.67492711*10^-27')
def qC():
	T.insert(INSERT,'1.602176487*10^-19')
def epsCJm():
	T.insert(INSERT,'8.85419*10^-12')
def muNA():
	T.insert(INSERT,u'4*\u03C0*10^-7')
def mhkg():
	T.insert(INSERT,'1.673532499*10^-27')
def rJmolK():
	T.insert(INSERT,'8.314472')
def namol():
	T.insert(INSERT,'6.02214179*10^23')
from Tkinter import *
from math import *
root=Tk()
root.title("NOMA Calculator")
T=Text(root,font=('Times',14))
T.focus_set()
T.pack(side='left',fill='y')
Button(root,text=u'\u221A',command=sqr).pack(side='top')
Button(root,text=u'\u03C0',command=pie).pack(side='top')
Button(root,text='h (J s)',command=hJs).pack(side='top')
Button(root,text='h (eV s)',command=heVs).pack(side='top')
Button(root,text='c (m/s)',command=cms).pack(side='top')
Button(root,text='k_b (J/K)',command=kbJK).pack(side='top')
Button(root,text='k_b (eV/K)',command=kbeVK).pack(side='top')
Button(root,text=u'm\u2091 (kg)',command=mekg).pack(side='top')
Button(root,text=u'm_p (kg)',command=mpkg).pack(side='top')
Button(root,text=u'm_n (kg)',command=mnkg).pack(side='top')
Button(root,text='q (C)',command=qC).pack(side='top')
Button(root,text=u'\u03B5\u2080 (C\u00B2/[J m])',command=epsCJm).pack(side='top')
Button(root,text=u'\u03BC\u2080 (N/A\u00B2)',command=muNA).pack(side='top')
Button(root,text='m_h (kg)',command=mhkg).pack(side='top')
Button(root,text='R (J/[mol K])',command=rJmolK).pack(side='top')
Button(root,text=u'N\u2090 (/mol)',command=namol).pack(side='top')
root.bind('<Return>',tree)
def quit(event=None):
	root.destroy()
root.bind('<Control-q>',quit)
root.mainloop()