def adicionar_tarefa(text_entry, lista_tarefas_lb, lista_tarefas):
    tarefa = text_entry.get()
    if tarefa.strip():
        text_entry.delete(0, 'end')  
        lista_tarefas.append(tarefa) 
        atualizar_lista_tarefas(lista_tarefas_lb, lista_tarefas)

def remover_tarefa(lista_tarefas_lb, lista_tarefas):
    selecoes = lista_tarefas_lb.curselection()
    if selecoes:
        for indice in selecoes[::-1]:  
            del lista_tarefas[indice]
        atualizar_lista_tarefas(lista_tarefas_lb, lista_tarefas)

def selecionar_todas_tarefas(lista_tarefas_lb):
    lista_tarefas_lb.select_set(0, 'end') 

def atualizar_lista_tarefas(lista_tarefas_lb, lista_tarefas):
    lista_tarefas_lb.delete(0, 'end')
    for tarefa in lista_tarefas:
        lista_tarefas_lb.insert('end', tarefa)

def marcar_como_concluida():
    selecoes = app.lista_tarefas_lb.curselection()
    if selecoes:
        for indice in selecoes:
            tarefa = app.lista_tarefas[indice]
            tarefa_concluida = f'[Concluída] {tarefa}'
            app.lista_tarefas[indice] = tarefa_concluida
        app.atualizar_lista_tarefas()