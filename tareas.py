def agregar_tarea(lista, tarea):
 lista.append(tarea)
 return lista


def listar_tareas(lista):
 for i, tarea in enumerate(lista, 1):
  print(f"{i}. {tarea}")