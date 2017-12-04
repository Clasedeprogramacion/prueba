
# coding: utf-8

# In[56]:


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
                     width=400)
        M1.grid(row=1, column=1, columnspan=2, pady=5)

        self.email = StringVar()
        labelemail = Label(frame1, text="Email: ").grid(row=2, column=1, columnspan=1)
        entryemail = Entry(frame1, textvariable=self.email).grid(row=2,
                         column=2, columnspan=2, padx=10)

        self.name = StringVar()
        labelname = Label(frame1, text="Nombre: ").grid(row=3, column=1, columnspan=1)
        entryname = Entry(frame1, textvariable=self.name).grid(row=3,
                         column=2, columnspan=2, padx=10)

        self.commit = StringVar()
        labelcommit = Label(frame1, text="Comentario: ").grid(row=5, column=1, columnspan=1)
        entrycommit = Entry(frame1, textvariable=self.commit).grid(row=5,
                         column=2, columnspan=2, padx=10)

        frame2= Frame(window)
        frame2.pack()
        Btprepare = Button(frame2, text="Preparar",
                           command=self.prepareButton).grid(row=6, column=1, padx=15, pady=10)

        Btbegin = Button(frame2, text="Subir",
                         command=self.BeginButton).grid(row=6, column=2, padx=15, pady=10)

        Btclear = Button(frame2, text="Limpiar",
                         command=self.clearData).grid(row=6, column=3, padx=15, pady=10)

        window.mainloop()

    def prepareButton(self):
        print subprocess.check_output('git init', shell=True)
        name = "git config --global user.name " + self.name.get()
        email = "git config --global user.email " + self.email.get()
        print subprocess.check_output(name, shell=True)  # configura para el uso de git
        print subprocess.check_output(email, shell=True)  # configura para el uso de git
        print subprocess.check_output('git remote add origin https://github.com/Clasedeprogramacion/prueba.git', shell=True)
        print subprocess.check_output('git add .', shell=True)  # agrega los archivos

    def BeginButton(self):
        commit = "git commit -m " + self.commit.get()
        print subprocess.check_output(commit, shell=True)  # agrega comentario
        print subprocess.check_output('git push -f origin master', shell=True)  # sube los archivos a github

    def clearData(self):
        print subprocess.check_output('git init', shell=True)
        print subprocess.check_output('git remote rm origin', shell=True)


Widgets()

