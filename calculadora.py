##Logica de la calculadora

#Titulo 
print("======INGRESE NOTAS Y PONDERACIONES======\n")

import json

#Funcion para calcular el aporte 
def calcular_aporte(nota, ponderacion):
    ponderacion /= 100
    resultado = round((nota * ponderacion), 2)
    return resultado

#Funcion para calcular la nota minima necesaria para aprobar
def calcular_nota_necesaria(aporte_total, porcentaje_evaluado):
    porcentaje_restante = (100 - porcentaje_evaluado) / 100
    nota_necesaria = round((55 - aporte_total) / porcentaje_restante, 2)
    return nota_necesaria

#Funcion apra guardar las evaluaciones en un archivo .JSON
def guardar_evaluaciones(evaluaciones):
    with open("datos.json", "w") as archivo:
        json.dump(evaluaciones, archivo, indent=4)

#Funcion para cargar las evaluaciones desde un archivo .JSON
def cargar_evaluaciones():
    try:
        with open("datos.json", "r") as archivo:
            evaluaciones = json.load(archivo)
            return evaluaciones
    except FileNotFoundError:
        return []

#Validacion de notas
def validar_nota(nota):
    try:
        nota = int(nota)
    except ValueError:
        return False
    if nota < 0 or nota > 100:
        return False
    return True

#Validacion de ponderaciones
def validar_ponderacion(ponderacion, porcentaje_evaluado):
    try:
        ponderacion = int(ponderacion)
    except ValueError:
        return False
    if ponderacion <= 0 or ponderacion > 100:
        return False
    if porcentaje_evaluado + ponderacion > 100:
        return False

    return True

#Lista de diciconarios para almacenar las notas y ponderaciones
evaluaciones = cargar_evaluaciones()

#Variables necesarias
continuar = True
aporte_total = 0
porcentaje_evaluado = 0

#Recuperar el porcentaje evaluado de las evaluaciones cargadas
for evaluacion in evaluaciones:
    porcentaje_evaluado += evaluacion["ponderacion"]

#Pedir al usuario nota y ponderacion
while continuar:
    evaluacion = input("Ingrese nombre de la evaluacion: ")
    #Validar la nota
    while True:
        nota = input("Ingrese la nota: ")
        if validar_nota(nota):
            nota = int(nota)
            break
        
        print("Ingrese una nota valida.")

    #Validar la ponderacion
    while True:
            ponderacion = input("Ingrese la ponderacion (%): ")                
            if validar_ponderacion(ponderacion, porcentaje_evaluado):
                ponderacion = int(ponderacion)
                break
            else:
                print("Ingrese una ponderacion valida.")

    evaluaciones.append({
        "nombre": evaluacion,
        "nota": nota,
        "ponderacion": ponderacion,
    })
    seguir = input("¿Desea ingresar otra evaluacion? (s/n): ")
    if seguir != "s":
        guardar_evaluaciones(evaluaciones)
        continuar = False

#Sumar aportes de todas las evaluaciones
for evaluacion in evaluaciones:
    nota = evaluacion["nota"]
    ponderacion = evaluacion["ponderacion"]
    resultado = calcular_aporte(nota, ponderacion)
    aporte_total += resultado
    

#Mostrar lista de evaluaciones con sus notas y ponderaciones
print("======LISTA DE EVALUACIONES======\n")
for evaluacion in evaluaciones:
    print("Evaluacion:", evaluacion["nombre"], "\nNota:", evaluacion["nota"], "\nPonderacion:", str(evaluacion["ponderacion"]) + "%\n")

#Mostrar aporte total y porcentaje evaluado
print("======APORTE TOTAL======\n")
print("Aporte total:", round(aporte_total))
print("Porcentaje evaluado:", str(porcentaje_evaluado) + "%\n")

#Mostrar nota necesaria para aprobar
print("======NOTA NECESARIA PARA APROBAR======\n")
##Interpretar el resultado de la funcion calcular_nota_necesaria
#Arreglo en caso de que el porcentaje evaluado sea 100
if porcentaje_evaluado == 100:
    if aporte_total >= 55:
        print("Ya has aprobado con las evaluaciones ingresadas.")
    else:
        print("No es posible aprobar con las evaluaciones ingresadas.")
else:
    nota_necesaria = calcular_nota_necesaria(aporte_total, porcentaje_evaluado)
    if aporte_total >= 55:
        print("Ya has aprobado con las evaluaciones ingresadas.")
    elif nota_necesaria > 100:
        print("No es posible aprobar con las evaluaciones ingresadas.")
    elif nota_necesaria <= 100:
        print("La nota necesaria para aprobar es:", nota_necesaria)