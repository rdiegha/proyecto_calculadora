##Logica de la calculadora

#Titulo 
print("======INGRESE NOTAS Y PONDERACIONES======\n")

#Lista de diciconarios para almacenar las notas y ponderaciones
evaluaciones = []

#Variables necesarias
continuar = True
aporte_total = 0
porcentaje_evaluado = 0

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
while continuar:
    evaluacion = input("Ingrese nombre de la evaluacion: ")
    #Validar la nota
    while True:
        try:
            nota = int(input("Ingrese la nota: "))
            if nota < 0 or nota > 100:
                print("La nota debe estar entre 0 y 100.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

    #Validar la ponderacion
    while True:
        try:
            ponderacion = int(input("Ingrese la ponderacion (%): "))
            if ponderacion < 0 or ponderacion > 100:
                print("La ponderacion debe estar entre 0 y 100.")
                continue
            if porcentaje_evaluado + ponderacion > 100:
                print("El porcentaje evaluado no puede superar el 100%.")
                continue
            porcentaje_evaluado += ponderacion
            break
        except ValueError:
            print("Por favor, ingrese un numero valido.")

    evaluaciones.append({
        "nombre": evaluacion,
        "nota": nota,
        "ponderacion": ponderacion,
    })
    seguir = input("¿Desea ingresar otra evaluacion? (s/n): ")
    if seguir != "s":
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