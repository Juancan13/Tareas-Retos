print("SISTEMA PARA CALCULAR PROMEDIO")

name = input("Para empezar, ¿cual es su nombre? ")
matematicas = float(input(name + ", ¿Cuál fue tu calificación en matemásticas?: "))
etica = float(input("¿En ética?: "))
sociales = float(input("¿Y en sociales: "))
ciencias = float(input("¿En ciencias?: "))
español = float(input("¿En español?: "))
ingles = float(input("¿Y en inglés?: "))
artistica = float(input("¿En artistica?: "))
tecnologia = float(input("¿En tecnología?: "))
religion = float(input("¿En religión?: "))
fisica = float(input("¿Y en educación física?: "))

promedio = (matematicas + etica + sociales + ciencias + español + ingles + artistica + tecnologia + religion + fisica) /10
promedio = int(promedio)
if promedio >=3 :
    print("Felicidades " + name + ", aprobaste con un promedio de: " + str(promedio))
