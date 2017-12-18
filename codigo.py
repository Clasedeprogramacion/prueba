# coding: utf-8
"""El siguiente código permite al usuario subir y clonar repositorios a github
Para ello primero debe hacer ciertos procedimientos para que sea posible usar
este programa. Los procedimientos se anexan al código
"""

from Tkinter import *
import subprocess  # permite usar la terminal del sistema operativo desde python


class Widgets:
    def __init__(self):
        window = Tk()  # creación de la ventana
        window.title("Suba aquí su repositorio :D")  # título de la ventana
        window.resizable(0, 0)  # no reescalable

        frame1 = Frame(window)  # cuadro 1
        frame1.pack()
        M1 = Message(frame1, text="Antes de usar este programa lea las \
instrucciones. Por favor ingrese los siguientes datos",
                     width=400)
        M1.grid(row=1, column=1, columnspan=2, pady=5)

        self.email = StringVar()  # primer entrada correo electrónico
        labelemail = Label(frame1, text="Email: ").grid(row=2, column=1, columnspan=1)
        entryemail = Entry(frame1, textvariable=self.email).grid(row=2,
                         column=2, columnspan=2, padx=10)

        self.name = StringVar()  # segunda entrada nombre
        labelname = Label(frame1, text="Nombre: ").grid(row=3, column=1, columnspan=1)
        entryname = Entry(frame1, textvariable=self.name).grid(row=3,
                         column=2, columnspan=2, padx=10)

        self.commit = StringVar()  # tercera entrada comentario
        labelcommit = Label(frame1, text="Comentario: ").grid(row=5, column=1, columnspan=1)
        entrycommit = Entry(frame1, textvariable=self.commit).grid(row=5,
                         column=2, columnspan=2, padx=10)

        frame2= Frame(window)  # cuadro 2
        frame2.pack()

        #  botón para clonar
        Btclone = Button(frame2, text="Clonar",
                         command=self.CloneButton).grid(row=6, column=1, padx=15, pady=10)

        # botón borrar el anterior origin creado
        Btclear = Button(frame2, text="Limpiar",
                         command=self.clearData).grid(row=6, column=2, padx=15, pady=10)

        # botón para crear origin y agregar archivos
        Btprepare = Button(frame2, text="Preparar",
                           command=self.prepareButton).grid(row=6, column=3, padx=15, pady=10)

        # botón para subir los archivos
        Btbegin = Button(frame2, text="Subir",
                         command=self.BeginButton).grid(row=6, column=4, padx=15, pady=10)

        window.mainloop()

    def CloneButton(self):
        print subprocess.check_output('git init', shell=True)
        print subprocess.check_output('git clone https://github.com/Clasedeprogramacion/Memorias-de-clase.git', shell=True)

    def prepareButton(self):
        print subprocess.check_output('git init', shell=True)
        name = "git config --global user.name " + self.name.get()
        email = "git config --global user.email " + self.email.get()
        print subprocess.check_output(name, shell=True)  # configura para el uso de git
        print subprocess.check_output(email, shell=True)  # configura para el uso de git
        print subprocess.check_output('git add .', shell=True)  # agrega los archivos
        print subprocess.check_output('git remote add origin https://github.com/Clasedeprogramacion/Memorias-de-clase.git', shell=True)

    def BeginButton(self):
        commit = "git commit -m " + self.commit.get()
        print subprocess.check_output(commit, shell=True)  # agrega comentario
        print subprocess.check_output('git push -f origin master', shell=True)  # sube los archivos a github

    def clearData(self):
        print subprocess.check_output('git init', shell=True)
        print subprocess.check_output('git remote rm origin', shell=True)


Widgets()
