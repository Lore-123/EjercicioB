#EJERCICIO B SPOTIFY
#MARIA JENNIFER CARBAJAL MARTINEZ 41S
#LORENZO HERNANDEZ HERNANDEZ 41s
from tkinter import*
from PIL import ImageTk,Image
root= Tk()

ventanaprincipal=Frame(root)
ventanaprincipal.grid()
contras=StringVar()
confirmo=StringVar()


def contraseñas():
    if contras.get()==confirmo.get():
        print("section started")
        ventanaprincipal.config(bg="#0099FF")
    
    else:
        print("incorrect password")
        ventanaprincipal.config(bg="#CC3300")

img=Image.open("C:\\Users\\nisha\\OneDrive\\Escritorio\\TECNOLOGICO\\4to Semestre\\PROGRA VIS\\gm.png")
imagen=img.resize((150,100))
imag=ImageTk.PhotoImage(imagen)
Titulog=Label(ventanaprincipal,image=imag)
Titulog.grid(row=1,column=1,padx=10,pady=20,columnspan=2,rowspan=2)

titulo=Label(ventanaprincipal,text="LOG IN",font=("Glossy Sheen",20))
titulo.grid(row=3,column=1,columnspan=2)

NAME=Label(ventanaprincipal,text="NAME:",font=("Purple Smile",15)).grid(row=4,column=1,padx=30,pady=30)
textonombre=Entry(ventanaprincipal,font=("Glossy Sheen",10)).grid(row=4,column=2,padx=15,pady=15)
CONTRA=Label(ventanaprincipal,text="password:",font=("Purple Smile",15)).grid(row=5,column=1,padx=15,pady=30)
textocontra=Entry(ventanaprincipal,font=("Glossy Sheen",10),textvariable=contras).grid(row=5,column=2,padx=30,pady=15)
CONFIRM=Label(ventanaprincipal,text="confirm password:",font=("Purple Smile",15)).grid(row=6,column=1,padx=15,pady=30)
textoconfir=Entry(ventanaprincipal,font=("Glossy Sheen",10),textvariable=confirmo).grid(row=6,column=2,padx=30,pady=15)
control1=IntVar()
Man=Checkbutton(ventanaprincipal, text="Man",variable=control1,font=("Purple Smile",15))
Man.grid(row=7,column=1)
control2=IntVar()
Woman=Checkbutton(ventanaprincipal, text="Woman",variable=control2,font=("Purple Smile",15))
Woman.grid(row=7,column=2)
control3=IntVar()
ACEPT=Checkbutton(ventanaprincipal, text="I accept terms",variable=control3,font=("Purple Smile",15))
ACEPT.grid(row=8,column=1,columnspan=2)
Start=Button(ventanaprincipal,text="Start",command=contraseñas,width=20,height=2).grid(row=9,column=1,columnspan=2)


root.mainloop()