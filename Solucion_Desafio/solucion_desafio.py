# Defino las variables a ingresar
# score_1 = float(input("Ingrese nota 1: "))
# score_2 = float(input("Ingrese nota 2: "))
# score_3 = float(input("Ingrese nota 3: "))
# score_4 = float(input("Ingrese nota 4: "))
# score_5 = float(input("Ingrese nota 5: "))

#Opción 2, solución más versatil
n = int( input("Ingrese la cantidad de notas a promediar: "))
sum = 0
i = 1
while (i <= n):
    print("Ingrese la nota número: ",i)
    score = float(input())
    sum= sum + score
    i+=1

# Defino los procedimientos aritmeticos a ejecutar
#sum = (score_1 + score_2 + score_3 + score_4 + score_5)
Avg = sum / n
Avg_percent = Avg / n * 100
print ("El promedio de notas es: ", Avg)

# Defino la estructura de control para determinar si el estudiante ha aprobado o no basado en el promedio de sus calificaciones
if Avg_percent >= 60:
    print ("Aprobado")
elif Avg_percent < 40:
    print ("Reprobado")
else:
    print ("En recuperación")
