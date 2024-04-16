from tkinter import *
from tkinter import ttk
import customtkinter

root = Tk()

class App():
    def __init__(self, root):
        self.root = root
        self.Window()
        self.Frames()
        self.Buttons()
        root.mainloop()
        
    def Window(self):
        self.root.title('ToDo List')
        self.root.configure(background='#09112e')
        self.root.geometry('900x600')
        self.root.resizable(True, True)
        
    def Frames(self):
        self.frame_1 = Frame(self.root, bg='white', bd=4, highlightbackground='#007A78', highlightthickness=8)
        self.frame_1.place(relx=0.1, rely=0.25, relheight=0.5, relwidth=0.8)

        self.frame_2 = Frame(self.root, bg='#007A78', bd=4, highlightbackground='#007A78', highlightthickness=4)
        self.frame_2.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)  # Alterado o rely para posicionar abaixo do frame_1
        
        # Campo de texto
        self.text_entry = Entry(self.frame_2, bg='#eeedf2', fg='black', font=('Helvetica', 12))
        self.text_entry.pack(fill='both', expand=True)
        
    def Buttons(self):
        
        self.button_add = customtkinter.CTkButton(self.root, text="Adicionar Tarefa", fg_color='#09ff00', text_color='black')
        self.button_add.place(relx=0.74, rely=0.04)

        self.button_remove = customtkinter.CTkButton(self.root, text="Remover tarefa",text_color='black', fg_color='red')
        self.button_remove.place(relx=0.55, rely=0.041)
        
    

App(root)
