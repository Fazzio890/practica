'Clase de Variable'
nombre = 'Tony Soprano'
edad = 51
print(nombre, edad)

nombre1 = 'Julia '
apellido = 'Roberts'
nombrecompleto = (nombre1 + apellido)
print('Tu nombre es ' + nombrecompleto)

curso = 'Python'
print('Estas tomando un curso para ello ' + curso)

'Clase de Nombre de Variables'
'1_ Legible: nombre de la variable es relevante según su contenido'
'2_ Unidad: no existen espacios (puedes incorporar guiones bajos)'
'3_ Hispanismos: omitir signos específicos del idioma español, como tildes o la letra ñ'
'4_ Números: los nombres de las variables no deben empezar por números (aunque pueden contenerlos al final)'
'5_ Signos/símbolos: no se deben incluir : " , < > / ? | \ ( ) ! @ # $ % ^ & * ~ - +'
'6_ Palabras clave: no utilizamos palabras reservadas por Python'

'Clase de Integers & Floats'
num_entero = 10
print(num_entero)
print(type(num_entero))

num_decimal = 5.9
print(num_decimal)
print(type(num_decimal))

num1 = 7.5
num2 = 2.3
print(num1 + num2)
print(type(num1 + num2))

'Clase de Conversiones'
num1 = 7.5
print(int(num1))
print(type(int(num1)))

num2 = 10
print(float(num2))
print(type(float(num2)))

print(num1+num2)
print(type(num1+num2))

'Clase de Formatear Cadenas'
nombre_asociado = 'Jesse Pinkman'
numero_asociado = 399058
print(f'Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}')
print('Estimado/a {}, su número de asociado es: {}'.format(nombre_asociado, numero_asociado))

puntos_nuevos = 350
puntos_totales = 1225
print(f'Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos')
print('Has ganado {} puntos! En total, acumulas {} puntos'.format(puntos_nuevos, puntos_totales))

puntos_nuevos1 = 350
puntos_anteriores = 875
print(f'Has ganado {puntos_nuevos1} puntos! En total, acumulas {puntos_nuevos + puntos_anteriores} puntos')
print('Has ganado {} puntos! En total, acumulas {} puntos'.format(puntos_nuevos1 + puntos_anteriores))

'Clase de Operadores Matematicos'
a = 874
b = 27
print(f'{a} divido al piso de {b} es igual {a//b}')

c = 456
d = 33
print(f'{c} modulo de {d} es igual {c%d}')

e = 783
print(f'la raiz cuadra de {e} es igual {e**0.5}')

'Clase de Redondeo'
num1 = 10/3
print(round(num1, 2))

num2 = 10.676767
print(round(num2))

num3 = 5
print(round(5**0.5, 4))

'Proyecto'
