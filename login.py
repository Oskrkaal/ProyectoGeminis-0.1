
from tkinter import *
from tkinter.ttk import Frame

class Ventana(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.CentrarVentana()


    def initUI(self):

        self.master.title("Bienvenido a Geminis-0.1")
        self.pack(fill=BOTH, expand=1)
        #self.master.geometry(0,0)
        self.CentrarVentana()
        self.Login()
       


    def CentrarVentana(self):

        w = 350
        h = 550

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.master.resizable(False,False)
        

    def Login(self):

        self.usuario = Label(self, text="Usuario", bd=5,bg="green", fg="white", font=("Rekha", 15, "bold"))
        self.usuario.grid(row=0,column=0, pady=15)

        self.usuarioEntrada = Entry(self,bg="white", fg="black",font=("Rekha", 15, "bold"))
        self.usuarioEntrada.grid(row=0,column=1, pady=15, padx=5, sticky="w")

        self.password = Label(self,text="Password", bd=5,bg="green", fg="white", font=("Rekha", 15, "bold"))
        self.password.grid(row=1,column=0, pady=15)
    
        self.passwordEntrada= Entry(self,bg="white", fg="black",font=("Rekha", 15, "bold"))
        self.passwordEntrada.grid(row=1,column=1, pady=15, padx=5, sticky="w")

        self.botonEntrar = Button(self, text="Ingresar", fg="white", font=("Rekha", 10, "bold"), anchor="center", relief="flat", activebackground="cyan2")
        self.botonEntrar.grid(row=2, column=0)


def main():

    root = Tk()
    ex = Ventana()
    root.mainloop()


if __name__ == '__main__':
    main()