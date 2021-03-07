print('¡Hola a ´"todas\"´y "´todos!"".')            #Ejercicio No.1
name = input('Ingresa tu Nombre: ')                 #Ejercicio No.2
print('Hola', name)
A = int(input('Ingresa "A":  '))                    #Ejercicio No.4
B = int(input('Ingresa "B":  '))
if A == 0 and B == 0:
    print ('"Q = 0"')
if A == 0 and B == 1:
    print ('"Q = 1"')
if A == 1 and B == 0:
    print ('"Q = 1"')
if A == 1 and B == 1:
    print ('"Q = 1"')
if A > 1 or B > 1:
    print ('DATOS INVALIDOS')
name = input('Estudiante ingresa tu Nombre: ')      #Ejercicio No.5
print('Hola', name , 'ingresa el número de horas que llevas estudiadas del curso')
Horas = int(input('No. de Horas:'  ))
print(name , 'ingresa el número de horas que estudias el curso por día')
HXD = int(input('No. de Horas:'  )) #HXD = Horas por día
print ('BIENVENIDO')                                #Ejercicio No.7
peso = int(input('Ingresa Tu Peso  '))                    
altura = int(input('Ingresa Tu Altura:  '))
imc = float(input(peso/altura))
n = round(imc, 2)
print(n)
