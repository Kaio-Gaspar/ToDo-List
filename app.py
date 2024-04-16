from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter
from workbook import *

root = Tk()

class App():
    def __init__(self, root):
        self.root = root
        self.get_log()
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
        self.text_entry.insert(0, 'Insira sua tarefa aqui') 
        self.text_entry.bind("<FocusIn>", self.on_entry_click)  # Vincula evento FocusIn
        self.text_entry.bind("<FocusOut>", self.on_focus_out)
        self.text_entry.pack(fill='both', expand=True)

        


        
    def Buttons(self):
        
        self.button_add = customtkinter.CTkButton(self.root, text="Adicionar Tarefa", fg_color='#09ff00', text_color='black')
        self.button_add.place(relx=0.74, rely=0.04)

        self.button_remove = customtkinter.CTkButton(self.root, text="Remover tarefa",text_color='black', fg_color='red')
        self.button_remove.place(relx=0.74, rely=0.76)

        self.button_select_all = customtkinter.CTkButton(self.root, text="Selecionar tudo",text_color='black', fg_color='yellow')
        self.button_select_all.place(relx=0.55, rely=0.758)

        self.button_plot_graph = customtkinter.CTkButton(self.root, text="Gerar gráfico",text_color='black', fg_color='blue')
        self.button_plot_graph.place(relx=0.1, rely=0.753)

        self.button_log = customtkinter.CTkButton(self.root, text="Gerar log",text_color='black', fg_color='orange', command=self.get_log())
        self.button_log.place(relx=0.35, rely=0.755)

    def on_entry_click(self, event):
        if self.text_entry.get() == 'Insira sua tarefa aqui':
            self.text_entry.delete(0, tk.END)
            self.text_entry.config(fg='black')  

    # Função para restaurar o texto placeholder se a entrada estiver vazia quando perder o foco
    def on_focus_out(self, event):
        if not self.text_entry.get():
            self.text_entry.insert(0, 'Insira sua tarefa aqui')
            self.text_entry.config(fg='grey')  
    
    def get_log(self):
        wb.create_sheet("Mysheet")
        
        
    

App(root)
