# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:20:45 2019

@author: estefani
"""

# Lo primero que hacemos es definir las variables que vamos a usar para resolver el problema planteado

"""
r = cuota (renta)
p = prestamo adquirido
i = tasa de interes
n = numero de periodos

tambien definimos la formula para hallar la cuota 

r = p * [(i * ( 1 + i )**n / (( 1 + i )**n ) - 1 )]

"""

#Le pedimos a la persona que nos de los datos necesarios para poder hallar la cuota, los intereses, el abono al capital y 
#el saldo final en cada periodo

x =1
p = int(input("¿De cuanto es el prestamo?"))
i = int(input("¿Cual es la tasa de interes?")) # Solo acepta valores numericos, no con el signo % , es decir si es 4% se debe poner 0.04
n = int(input("¿Por cuantos periodos se efecturara el prestamo?"))

def cuota_prestamo(p,i,n):
    a = (i*( 1 + i )**n)
    b = (( 1 + i )**n ) - 1
    c = (a/b)
    r = p *c
    return r

r = cuota_prestamo(p,i,n)
print("La cuota del prestamo es:",r)

def intereses (p,i):
    q = p * i
    return q

q = intereses(p,i)
print("Los intereses pagados sobre el prestamo en el periodo",x,"son:",q)

def abono_capital(r,q):
    ac = r - q
    return ac

ac = abono_capital(r,q)
print ("El abono al capital es:",ac)

def saldo_final (p,ac):
    sf = p - ac
    return sf

sf = saldo_final (p ,ac)
print ("El saldo final en la cuota", x, "es:",sf)

q2 = intereses (sf,i)
print("Los intereses pagados sobre el prestamo en el periodo",x+1,"son:",q2)

sf2 = saldo_final(sf,ac)
print("El saldo final en la cuota", x+1, "es:",sf2)

#Con los valores p = 150000 , i = 0.04 , n = 8 , para los primeros 2 periodos la respuestas serian...
#La cuota del prestamo es: 20476.469870064386
#Los intereses pagados sobre el prestamo en el periodo 1 son: 3000.0
#El abono al capital es: 17476.469870064386
#El saldo final en la cuota 1 es: 132523.53012993562
#Los intereses pagados sobre el prestamo en el periodo 2 son: 2650.4706025987125
#El saldo final en la cuota 2 es: 115047.06025987124


#EL CODIGO NO ESTA FINALIZADO PARA TODOS LOS PERIODOS YA QUE AHORA DEBEMOS ENCONTRAR LA MANERA DE QUE LA COMPUTADORA 
#REALICE ESTE PROCESO SIMULTANEAMENTE, ES DECIR SI HAY 30 PERIODOS, DEBEMOS MIRAR COMO HACER PARA QUE SE REALICE EN UNA SOLA
#FORMULA. :)
