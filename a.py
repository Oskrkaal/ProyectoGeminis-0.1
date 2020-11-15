# -*- coding: utf-8 -*-
from tkinter import *

class Student:

    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Sistema de Inventario")
        self.ventana.geometry("1280x950+0+0")
        self.ventana.resizable(True, False)
        #Ventana General
        title=Label(self.ventana, text ="Sistema de Cajas", bd=10, relief=RAISED, font=("Arial", 40, "bold"), bg="green", fg="white")
        title.pack(side=TOP)

        #Area de registro
        Manage_Frame = Frame (self.ventana,bd=4, relief =RIDGE , bg="green")
        Manage_Frame.place(x=20,y=100, width=520, height=780)

        #Registros
        m_title= Label(Manage_Frame, text="Control de Cajas", bd=10, relief=RAISED, font=("Arial", 20, "bold"), bg="yellow", fg="black")
        m_title.grid(row=0, columnspan=10, pady=10)

        txt_Fecha = Label(Manage_Frame, text="Fecha", bg="Yellow", fg="red", font=("Arial",15,"bold"))
        txt_Fecha.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        FechaI= Entry(Manage_Frame,  font=("Arial",10,"bold"),bd=5, relief=GROOVE)
        FechaI.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        txt_Cod = Label(Manage_Frame, text="Código", bg="Yellow", fg="red", font=("Arial",15,"bold"))
        txt_Cod.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        CodI= Entry(Manage_Frame,  font=("Arial",10,"bold"),bd=5, relief=GROOVE)
        CodI.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        txt_Desc = Label(Manage_Frame, text="Descripción", bg="Yellow", fg="red", font=("Arial",15,"bold"))
        txt_Desc.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        CodI= Entry(Manage_Frame,  font=("Arial",10,"bold"),bd=5, relief=GROOVE)
        CodI.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        txt_Ingreso = Label(Manage_Frame, text="Cantidad a ingresar", bg="Yellow", fg="red", font=("Arial",15,"bold"))
        txt_Ingreso.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        ConIngr= Entry(Manage_Frame,  font=("Arial",10,"bold"),bd=5, relief=GROOVE)
        ConIngr.grid(row=4, column=1, pady=10, padx=20, sticky="w")



        #Details_Frame=Frame(self.ventana, bd=4, relief=RIDGE, bg="green")
        #Details_Frame.place(x=550,y=100, width=520, height=780)


ventana = Tk()
ob = Student(ventana)
ventana.mainloop()
