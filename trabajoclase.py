# -*- coding: utf-8 -*-

from Tkinter import *
import subprocess  # permite usar la terminal del sistema operativo desde python


class Widgets:
    def __init__(self):
        window = Tk()
        window.title("Suba aquí su repositorio :D")
        window.resizable(0,0)

        frame1 = Frame(window)
        frame1.pack()
        M1 = Message(frame1, text="Por favor ingrese los siguientes datos",
                     width=200)
        M1.grid(row=1, column=2)

        self.email = StringVar()
        labelemail = Label(frame1, text="Email: ").grid(row=2, column=1)
        entryemail = Entry(frame1, textvariable=self.email).grid(row=2,
                         column=2)

        self.name = StringVar()
        labelname = Label(frame1, text="Nombre: ").grid(row=3, column=1)
        entryname = Entry(frame1, textvariable=self.name).grid(row=3,
                         column=2)

        self.commit = StringVar()
        labelcommit = Label(frame1, text="Comentario: ").grid(row=5, column=1)
        entrycommit = Entry(frame1, textvariable=self.commit).grid(row=5,
                         column=2)

        Btprepare = Button(frame1, text="Preparar",
                           command=self.prepareButton).grid(row=7, column=2)

        Btbegin = Button(frame1, text="Subir",
                         command=self.BeginButton).grid(row=8, column=2)

        Btclear = Button(frame1, text="Limpiar",
                         comman=self.clearData).grid(row=6, column=2)

        window.mainloop()

    def prepareButton(self):
        print subprocess.check_output('git init', shell=True)
        print subprocess.check_output('git remote add origin https://github.com/Clasedeprogramacion/prueba.git', shell=True)
        name = "git config --global user.name " + self.name.get()
        email = "git config --global user.email " + self.email.get()
        print subprocess.check_output(name, shell=True)  # configura para el uso de git
        print subprocess.check_output(email, shell=True)  # configura para el uso de git

    def BeginButton(self):
        commit = "git commit -m " + self.commit.get()
        print subprocess.check_output('git add .', shell=True)  # agrega los archivos
        print subprocess.check_output(commit, shell=True)  # agrega comentario
        print subprocess.check_output('git push -f origin master', shell=True)  # sube los archivos a github

    def clearData(self):
        print subprocess.check_output('git remote rm origin', shell=True)


Widgets()
