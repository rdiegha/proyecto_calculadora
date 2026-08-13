##Logica de la calculadora

#Titulo 
print("======INGRESE NOTAS Y PONDERACIONES======\n")

#Lista de diciconarios para almacenar las notas y ponderaciones
evaluaciones = []

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


#Pedir al usuario nota y ponderacion
continuar = True
i = 0
aporte_total = 0
porcentaje_evaluado = 0

while continuar:
    evaluacion = input("Ingrese nombre de la evaluacion: ")
    nota = int(input("Ingrese la nota: "))
    ponderacion = int(input("Ingrese la ponderacion (%): "))
    evaluaciones.append({
        "nombre": evaluacion,
        "nota": nota,
        "ponderacion": ponderacion
    })
    #Sumar aportes de todas las evaluaciones
    nota = evaluaciones[i]["nota"]
    ponderacion = evaluaciones[i]["ponderacion"]
    porcentaje_evaluado += ponderacion
    continuar = False
    resultado = calcular_aporte(nota, ponderacion)
    aporte_total += resultado
    i += 1
    continuar = input("¿Desea ingresar otra evaluacion? (s/n): ")
    if continuar != "s":
        continuar = False

#Mostrar lista de evaluaciones con sus notas y ponderaciones
print("======LISTA DE EVALUACIONES======\n")
for evaluacion in evaluaciones:
    print("Evaluacion:", evaluacion["nombre"], "\nNota:", evaluacion["nota"], "\nPonderacion:", str(evaluacion["ponderacion"]) + "%\n")

#Mostrar aporte total y porcentaje evaluado
print("======APORTE TOTAL======\n")
print("Aporte total:", aporte_total)
print("Porcentaje evaluado:", str(porcentaje_evaluado) + "%\n")

#Mostrar nota necesaria para aprobar
print("======NOTA NECESARIA PARA APROBAR======\n")
#Interpretar el resultado de la funcion calcular_nota_necesaria
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