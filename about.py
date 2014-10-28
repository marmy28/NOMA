from Tkinter import *
root=Tk()
def quit(event=None):
	root.destroy()
root.title("About NOMA...")
w=Canvas(root,width=200,height=100,bg='white')
w.pack(side='top')


w.create_line(10,60,12,56)
w.create_line(12,56,8,48)
w.create_line(8,48,12,40)
w.create_line(12,40,8,32)
w.create_line(8,32,12,24)
w.create_line(12,24,10,20)

w.create_line(10,20,15,24)
w.create_line(15,24,17,32)
w.create_line(17,32,27,40)
w.create_line(27,40,29,48)
w.create_line(29,48,39,56)
w.create_line(39,56,40,60)

w.create_line(40,60,42,56)
w.create_line(42,56,38,48)
w.create_line(38,48,42,40)
w.create_line(42,40,38,32)
w.create_line(38,32,42,24)
w.create_line(42,24,40,20)


w.create_oval(5,15,15,25,fill='green')
w.create_oval(5,55,15,65,fill='green')
w.create_oval(35,15,45,25,fill='green')
w.create_oval(35,55,45,65,fill='green')

w.create_oval(55,20,95,65,fill='yellow')


w.create_line(110,60,112,56)
w.create_line(112,56,108,48)
w.create_line(108,48,112,40)
w.create_line(112,40,108,32)
w.create_line(108,32,112,24)
w.create_line(112,24,110,20)

w.create_line(110,20,113.75,24)
w.create_line(113.75,24,113.25,32)
w.create_line(113.25,32,120.75,40)
w.create_line(120.75,40,120.25,48)
w.create_line(120.25,48,127.75,56)
w.create_line(127.75,56,127.5,60)

w.create_line(127.5,60,132.25,56)
w.create_line(132.25,56,130.75,48)
w.create_line(130.75,48,138.25,40)
w.create_line(138.25,40,137.75,32)
w.create_line(137.75,32,145.25,24)
w.create_line(145.25,24,145,20)

w.create_line(145,60,147,56)
w.create_line(147,56,143,48)
w.create_line(143,48,147,40)
w.create_line(147,40,143,32)
w.create_line(143,32,147,24)
w.create_line(147,24,145,20)


w.create_oval(105,15,115,25,fill='orange')
w.create_oval(105,55,115,65,fill='orange')
w.create_oval(122.5,55,132.5,65,fill='orange')
w.create_oval(140,15,150,25,fill='orange')
w.create_oval(140,55,150,65,fill='orange')

w.create_line(175,20,175.5,24)
w.create_line(175.5,24,168.5,32)
w.create_line(168.5,32,169.5,40)
w.create_line(169.5,40,162.5,48)
w.create_line(162.5,48,163.5,56)
w.create_line(163.5,56,160,60)

w.create_line(175,20,178.5,24)
w.create_line(178.5,24,177.5,32)
w.create_line(177.5,32,184.5,40)
w.create_line(184.5,40,183.5,48)
w.create_line(183.5,48,190.5,56)
w.create_line(190.5,56,190,60)

w.create_oval(170,15,180,25,fill='violet')
w.create_oval(170,45,180,55,fill='violet')
w.create_oval(155,55,165,65,fill='violet')
w.create_oval(185,55,195,65,fill='violet')


x=StringVar()
x.set('50')
velx=StringVar()
velx.set('1')
a=StringVar()
a.set('40')
b=StringVar()
b.set('90')
c=StringVar()
c.set('60')
d=StringVar()
d.set('70')
e=StringVar()
e.set('80')
f=StringVar()
f.set('100')
g=StringVar()
g.set('120')
h=StringVar()
h.set('140')
i=StringVar()
i.set('160')
j=StringVar()
j.set('170')
line1=w.create_line(30,80,float(a.get()),float(b.get()),width='2.0',fill='gray')
line2=w.create_line(float(a.get()),float(b.get()),float(c.get()),float(d.get()),width='2.0',fill='gray')
line3=w.create_line(float(c.get()),float(d.get()),float(e.get()),float(b.get()),width='2.0',fill='gray')
line4=w.create_line(float(e.get()),float(b.get()),float(f.get()),float(d.get()),width='2.0',fill='gray')
line5=w.create_line(float(f.get()),float(d.get()),float(g.get()),float(b.get()),width='2.0',fill='gray')
line6=w.create_line(float(g.get()),float(b.get()),float(h.get()),float(d.get()),width='2.0',fill='gray')
line7=w.create_line(float(h.get()),float(d.get()),float(i.get()),float(b.get()),width='2.0',fill='gray')
line8=w.create_line(float(i.get()),float(b.get()),170,80,width='2.0',fill='gray')
w.create_oval(10,70,30,90,fill='blue3',outline='blue4')
w.create_oval(12,72,23,83,fill='blue2',outline='blue3')
w.create_oval(14,74,21,81,fill='blue1',outline='blue2')
w.create_oval(16,76,19,79,fill='white',outline='blue1')
ball1=w.create_oval(170,70,190,90,fill='red3',outline='red4')
ball2=w.create_oval(172,72,183,83,fill='red2',outline='red3')
ball3=w.create_oval(174,74,181,81,fill='red1',outline='red2')
ball4=w.create_oval(176,76,179,79,fill='white',outline='red1')

def moveatom(event=None):
	if float(x.get())>157 or float(x.get())<50:
		velx.set(str(float(velx.get())*-1))
	deltax=float(velx.get())*.25
	x.set(str(float(x.get())+deltax))
	w.move(ball1,-deltax,0)
	w.move(ball2,-deltax,0)
	w.move(ball3,-deltax,0)
	w.move(ball4,-deltax,0)
	a.set(str(float(a.get())-float(velx.get())*7.5*.25/107))
	b.set(str(float(b.get())+float(velx.get())*3.9*.25/107))
	c.set(str(float(c.get())-float(velx.get())*22.5*.25/107))
	d.set(str(float(d.get())-float(velx.get())*3.9*.25/107))
	e.set(str(float(e.get())-float(velx.get())*37.5*.25/107))
	f.set(str(float(f.get())-float(velx.get())*52.5*.25/107))
	g.set(str(float(g.get())-float(velx.get())*67.5*.25/107))
	h.set(str(float(h.get())-float(velx.get())*82.5*.25/107))
	i.set(str(float(i.get())-float(velx.get())*97.5*.25/107))
	j.set(str(float(j.get())-float(velx.get())*105*.25/107))
	w.coords(line1,30,80,float(a.get()),float(b.get()))
	w.coords(line2,float(a.get()),float(b.get()),float(c.get()),float(d.get()))
	w.coords(line3,float(c.get()),float(d.get()),float(e.get()),float(b.get()))
	w.coords(line4,float(e.get()),float(b.get()),float(f.get()),float(d.get()))
	w.coords(line5,float(f.get()),float(d.get()),float(g.get()),float(b.get()))
	w.coords(line6,float(g.get()),float(b.get()),float(h.get()),float(d.get()))
	w.coords(line7,float(h.get()),float(d.get()),float(i.get()),float(b.get()))
	w.coords(line8,float(i.get()),float(b.get()),float(j.get()),80)
	w.after(10,moveatom)
ppoot=Frame(root)
ppoot.pack(side='top')
mylabel=Label(ppoot,text=u"""

Version 1.1.0

Computational Molecular Biophysics
Department of Physics
Creighton University


""")

mylabel.pack(side='top')
alphabet=StringVar()
alphabet.set('0')
def changebutton(event=None):
	if alphabet.get()=='0':
		alphabet.set('1')
		mylabel.config(text=u"""

Enjoy the program!

Computational Molecular Biophysics
Department of Physics
Creighton University


""")
		multibutton.config(text='Quit')
		moveatom()
	else:
		quit()
multibutton=Button(ppoot,text='Play',command=changebutton,cursor='gumby',width=6)
multibutton.pack(side='top')
root.bind('<Return>',changebutton)
root.bind('<Control-q>',quit)
root.mainloop()
