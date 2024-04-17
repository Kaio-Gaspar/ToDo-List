from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter
from time import strftime
from functions import *

root = Tk()

class App():
    def __init__(self, root):
        self.root = root    
        self.Window()
        self.Frames()
        self.Buttons()
        self.Add_clock()
        self.lista_tarefas = [] 
        root.mainloop()

    def Window(self):
        self.root.title('ToDo List')
        self.root.configure(background='#09112e')
        self.root.geometry('900x600')
        self.root.resizable(True, True)

    def Frames(self):
        self.lista_tarefas_lb = Listbox(self.root, bg='white', bd=4, highlightbackground='#007A78', highlightthickness=8)
        self.lista_tarefas_lb.place(relx=0.1, rely=0.25, relheight=0.5, relwidth=0.8)

        self.frame_2 = Frame(self.root, bg='#007A78', bd=4, highlightbackground='#007A78', highlightthickness=4)
        self.frame_2.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)  # Alterado o rely para posicionar abaixo do frame_1
        
        # Campo de texto
        self.text_entry = Entry(self.frame_2, bg='#eeedf2', fg='black', font=('Helvetica', 12))
        self.text_entry.insert(0, 'Insira sua tarefa aqui') 
        self.text_entry.bind("<FocusIn>", self.on_entry_click)  # Vincula evento FocusIn
        self.text_entry.bind("<FocusOut>", self.on_focus_out)
        self.text_entry.pack(fill='both', expand=True)

    def Buttons(self):
        self.button_add = customtkinter.CTkButton(self.root, text="Adicionar Tarefa", fg_color='#09ff00', text_color='black', command=lambda: adicionar_tarefa(self.text_entry, self.lista_tarefas_lb, self.lista_tarefas))
        self.button_add.place(relx=0.74, rely=0.04)

        self.button_remove = customtkinter.CTkButton(self.root, text="Remover tarefa", text_color='black', fg_color='red', command=lambda: remover_tarefa(self.lista_tarefas_lb, self.lista_tarefas))
        self.button_remove.place(relx=0.74, rely=0.76)

        self.button_select_all = customtkinter.CTkButton(self.root, text="Selecionar tudo", text_color='black', fg_color='yellow', command=lambda: selecionar_todas_tarefas(self.lista_tarefas_lb))
        self.button_select_all.place(relx=0.55, rely=0.758)

        self.button_marcar_concluida = customtkinter.CTkButton(self.root, text="Marcar como concluída", text_color='black', fg_color='green', command=self.marcar_como_concluida)
        self.button_marcar_concluida.place(relx=0.3, rely=0.758)

        self.button_plot_graph = customtkinter.CTkButton(self.root, text="Gerar gráfico", text_color='black', fg_color='blue')
        self.button_plot_graph.place(relx=0.1, rely=0.753)

        self.button_log = customtkinter.CTkButton(self.root, text="Gerar log", text_color='black', fg_color='orange')
        self.button_log.place(relx=0.1, rely=0.82)

    def on_entry_click(self, event):
        if self.text_entry.get() == 'Insira sua tarefa aqui':
            self.text_entry.delete(0, tk.END)
            self.text_entry.config(fg='black')  

    def on_focus_out(self, event):
        if not self.text_entry.get():
            self.text_entry.insert(0, 'Insira sua tarefa aqui')
            self.text_entry.config(fg='grey')  
    
    def Add_clock(self):
        # Cria um rótulo para exibir o relógio no canto da janela
        self.clock_label = Label(self.root, font=('calibri', 20, 'bold'), background='#09112e', foreground='white')
        self.clock_label.place(relx=0.001, rely=0)  # Posiciona o rótulo no canto sudeste da janela

        # Atualiza o relógio a cada segundo
        self.update_clock()

    def update_clock(self):
        # Obtém a hora atual
        hora_atual = strftime('%H:%M:%S %p')
        # Atualiza o texto do rótulo do relógio
        self.clock_label.config(text=hora_atual)
        # Chama novamente após 1 segundo
        self.clock_label.after(1000, self.update_clock)

    def marcar_como_concluida(self):
        selecoes = self.lista_tarefas_lb.curselection()
        if selecoes:
            for indice in selecoes:
                tarefa = self.lista_tarefas[indice]
                if '[Concluída]' not in tarefa: 
                    tarefa_concluida = f'[Concluída] {tarefa}'
                    self.lista_tarefas[indice] = tarefa_concluida
                else:
                    self.text_entry.config(fg='red')
                    self.text_entry.delete(0, 'end') 
                    self.text_entry.insert(0, 'Tarefas selecionadas ja foram conluidas') 
            self.atualizar_lista_tarefas()

    def atualizar_lista_tarefas(self):
        # Limpa a Listbox
        self.lista_tarefas_lb.delete(0, END)
        # Adiciona as tarefas atualizadas
        for tarefa in self.lista_tarefas:
            self.lista_tarefas_lb.insert(END, tarefa)

App(root)
