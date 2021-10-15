#Tarea de Introducción a ingeniería en Sistemas

print("Valor de las tareas medidas en escala del 1-10: ")
tareas = {
    "Programa en python":       8 ,
    "Suma de fuerzas":          3 ,
    "Seminario 2":              10,
    "Pentagrama":               1 ,
    "Cuerpos en el espacio":    10,
    "Álgebra booleana":         7 ,
    "Ciclos indeterminados":    7 ,
    "Ficha de lectura":         5 ,
    "Monografía":               6 ,
    "Trabajo en clase":         3 ,
}

tareas["Evaluación 2 parcial"] = 10
del(tareas["Pentagrama"])

print("\n\t--Tarea--\t\t    --Valor--")
for valor in tareas:
    print(valor, "\t\t\t", str(tareas[valor]))


