from tkinter import *
from random import sample

window=Tk()
#تقوم باضافة البوتنز  ومن ثم   خصائصها  
img=PhotoImage(file="logo.png")
run=Button(window,text="Run",relief="ridge",width=10,height=4)
reset=Button(window,text="Reset",relief="ridge",width=8,height=3)
logo=Label(window,image=img)

Label1=Label(window,text="welcome",relief='flat',width=8,height=6)
Label2=Label(window,relief='sunken',width=10,height=10)
Label3=Label(window,relief='sunken',width=10,height=10)
Label4=Label(window,text='.',relief='sunken',width=10,height=10)
Label5=Label(window,text='.',relief='sunken',width=10,height=10)
Label6=Label(window,relief='sunken',width=10,height=10)

img3=PhotoImage(file="min.png")
img4=PhotoImage(file="64.png")
kalb=Button(window,image=img3)
img5=PhotoImage(file="zom.png")
Zoom=Button(window,image=img5)
img2=PhotoImage(file="32x32.png")
exitt=Label(window,image=img2)
Exitt=Button(window,image=img4)
#بترسم الزازير علي الواجهة وتحدد مكانها عليها 
logo.grid(row=1)
Label1.grid(row=1,column=3,padx=1)
Label2.grid(row=3,column=2,padx=5)
Label3.grid(row=3,column=3,padx=3)
Label4.grid(row=3,column=4,padx=4)
Label5.grid(row=3,column=5,padx=5)
Label6.grid(row=3,column=6,padx=6)
exitt.grid(row=4,column=6,padx=6)
Exitt.grid(row=6,column=6,padx=6)
kalb.grid(row=1,column=5,padx=6)
Zoom.grid(row=1,column=6,padx=6)
#لو عاوز تعدل علي خصائص الزارير طريقة كونفج
Label6.configure(text=".")
Label3.configure(text='.')
Label2.configure(text=".")
run.grid(row=5,column=4,padx=3)
reset.grid(row=6,column=4,padx=3)

def runnums():
    numms=sample(range(1,100),5)
    Label2.configure(text=numms[0])
    Label3.configure(text=numms[1])
    Label4.configure(text=numms[2])
    Label5.configure(text=numms[3])
    Label6.configure(text=numms[4])

    run.configure(state=DISABLED)
    reset.configure(state=NORMAL)


def resetnums():
    Label2.configure(text='.')
    Label3.configure(text='.')
    Label4.configure(text='.')
    Label5.configure(text='.')
    Label6.configure(text='.')
    
    reset.configure(state=DISABLED)
    run.configure(state=NORMAL)

def zom():
    #window.state('zoomed')
    window.geometry("800x800")
    Zoom.configure(state=DISABLED)

def zomout():
    window.geometry("500x500")
    kalb.configure(state=DISABLED)
    
def getout():
    exit()
    
run.configure(command=runnums)
reset.configure(command=resetnums)
Zoom.configure(command=zom)
kalb.configure(command=zomout)
Exitt.configure(command=getout)  
    

#خصائص النافذة
window.title("Numbers_Game")
window.resizable(False,False)
window.mainloop()
