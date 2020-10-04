# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:37:37 2020

@author: Roshan Singh RSR
"""
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import Tk
from tkinter import ttk
window=Tk()
window.geometry("750x400")
window.configure(bg='white')
window.title("Checking plagarism of document")
label1=Label(window,text="SELECT YOUR FILE : " ,font=("Arial Bold",10),padx=10,pady=10,fg="black",bg='white')
label1.grid(column=0,row=0)
txt=scrolledtext.ScrolledText(window,width=40,height=10,fg="black")
def filter_x(x):
    for j in x:
        if j==" " or j=='':
            x.remove(j)
        j.replace("\n","")
    return(x)
def check_plg(file,y):
    '''plagaris=0
    li=[]
    for line in file:
        a=line.split(" ")
        li=li+a[:]
    li1=[]
    plagarised_text=""
    file.close()
    test_file=open(y)
    check_file=open("file0.txt")
    for line in test_file:
        a=line.split(" ")
        for line1 in check_file:
            b=line1.split(" ")
            for j in a:
                if j in b and j not in li1:
                    li1.append(j)
                    plagarised_text=plagarised_text+" "+j
        if len(li1)>=int(2*len(a)/3):
            plagaris=plagaris+len(li1)
        check_file.close()
        check_file=open("file0.txt")
        li1=[]'''
    x=file.read().split(".")
    x=filter_x(x)
    li=[]
    j=0
    p=0
    for i in range(5):
        t_file=open("file"+str(i)+".txt")
        y=t_file.read().split('.')
        y=filter_x(y)
        for j in range(0,len(x)):
            
            for k in range(0,len(y)):
                
                if x[j] in y[k] and x[j] not in li:
                    li.append(x[j])
                
            
            
            '''if x[j] in y and x[j] not in li:
                li.append(x[j])
            j=j+1'''
        
                        
                        
                        
                        
                        
                
        t_file.close()
    print(li,len(x),len(li))
    plagarised_text=li[:]
    plag=float((100*len(li))/len(x))
    return (plag,plagarised_text)



def clicked():
    import time
    global btn
    file=filedialog.askopenfilename()
    label2=Label(window,text="SELECTED FILE NAME : " ,font=("Arial Bold",10),padx=10,pady=10,fg="green",bg='white')
    label2.grid(column=0,row=1)
    label3=Label(window,text=file ,font=("Arial Bold",10),padx=10,pady=10,fg="black",bg='white')
    label3.grid(column=1,row=1)
    btn.configure(state='disabled',fg="black",bd=0)
    x=file
    file=open(file)
    (plagarism,plagarised_text)=check_plg(file,x)
    label6=Label(window,text="Detecting Plagarism Of Document : ",font=("Arial Bold",10),padx=10,pady=10,fg="black",bg='white')
    label6.grid(column=0,row=2)
    progress_bar = ttk.Progressbar(window, orient="horizontal",
                              mode="determinate", maximum=100, value=0)
    progress_bar.grid(column=1,row=2)
    window.update()
    progress_bar['value'] = 0
    window.update()
 
    while progress_bar['value'] < int(plagarism):
        progress_bar['value'] += 1
        
        window.update()
        time.sleep(0.2)
        
    label4=Label(window,text="Plagarism of document : ",font=("Arial Bold",10),padx=10,pady=10,fg="black",bg='white')
    label4.grid(column=0,row=3)
    label4=Label(window,text=str(plagarism) ,font=("Arial Bold",10),padx=10,pady=10,fg="black",bg='white')
    label4.grid(column=1,row=3)
    label5=Label(window,text="Common Text : " ,font=("Arial Bold",10),padx=10,pady=10,fg="black",bg='white')
    label5.grid(column=0,row=4)
    a=plagarised_text
    txt.grid(column=1,row=4)
    txt.configure(bd=0,pady=10)
    for text in a:
        txt.insert(INSERT,text+" ")
    
        
        
btn=Button(window,text="call me",bg="black",fg="white",bd=0,command=clicked)
btn.grid(column=1,row=0)
window.mainloop()

    