from desafioadl.models import Tarea, SubTarea

# a. recupera_tareas_y_sub_tareas OK
# b. crear_nueva_tarea OK
# c. crear_sub_tarea OK
# d. elimina_tarea OK
# e. elimina_sub_tarea OK
# f. imprimir_en_pantalla 

def crear_nueva_tarea(texto:str):
    tarea = Tarea(descripcion=texto)
    tarea.save()
    imprimir_en_pantalla()


def crear_sub_tarea(texto:str, idtarea:int):
    tarea_encontrada = Tarea.objects.get(id=idtarea)
    subtarea = SubTarea(descripcion=texto, tarea=tarea_encontrada)
    subtarea.save()
    imprimir_en_pantalla()

def elimina_tarea(idtarea:int):
    t = Tarea.objects.get(id=idtarea) 
    t.eliminada = True
    t.save()

def elimina_sub_tarea(idsubtarea:int):
    st = SubTarea.objects.get(id=idsubtarea) 
    st.eliminada = True
    st.save()

def matar_tarea(idtarea:int):
    t = Tarea.objects.get(id=idtarea) 
    t.delete()


def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    return tareas

def imprimir_en_pantalla():
    tareas = recupera_tareas_y_sub_tareas()
    for t in tareas:
        print (f'[{t.id}] {t.descripcion}')
        for sub_tarea in t.subtareas.filter(eliminada=False):
            print (f'       [{sub_tarea.id}] {sub_tarea.descripcion}')