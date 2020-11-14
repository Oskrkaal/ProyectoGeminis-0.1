
from tkinter import *
from tkinter.ttk import Frame

class Ventana(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Bienvenido a Geminis-0.1")
        self.pack(fill=BOTH, expand=1)
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

    def Login(self):

        usuario = Label(self, text="Usuario")
        usuario.pack()
        usuarioEntrada = Entry(self)
        usuarioEntrada.pack()

        password = Label(self,text="Password")
        password.pack()
        passwordEntrada= Entry(self)
        passwordEntrada.pack()

        botonEntrar = Button(self, text="Ingresar")
        botonEntrar.pack()


def main():

    root = Tk()
    ex = Ventana()
    root.mainloop()


if __name__ == '__main__':
    main()