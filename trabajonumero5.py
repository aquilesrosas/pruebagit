# 1) Hacer un programa que gestiones datos para una escuela.
# El programa tiene que ser capaz de:
# a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, 
# Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las 
# notas, cantidad de faltas, cantidad de amonestaciones recibidas.
# Recomendación: Para llevar un registro de estos dato se puede 
# utilizar un diccionario estructurado de la siguiente manera:
# {
# “Alumnos” : [alumno1,alumno2,alumno3 ]
# }
# Donde cada alumno es otro diccionario estructurado de la 
# siguiente forma:
# {
# “Nombre”: nombre de alumno,
# “Apellido” : apellido de alumno,
# “DNI” : DNI de alumno
# “Fecha de nacimiento”, fecha de nacimiento de alumno,
# “Tutor” : nombre y apellido de tutor,
# “Notas” : todas las notas del alumno,
# “Faltas” : cantidad de faltas,
# “amonestaciones” : cantidad de amonestaciones
# }
# En esta estructura:
# Datos = {
# “Alumnos” : [alumno1,alumno2,alumno3 ]
# }
# Para acceder por ejemplo al numero de DNI del tercer alumno 
# podríamos hacer algo así:
# Datos[“Alumnos”][2][“DNI”]
# Este es un ejemplo de estructura, se puede cambiar 
# completamente o hacer algunos cambios sobre el para mejorar el 
# orden (si lo consideran necesario)
# b) Mostrar los datos de cada alumno
# c) Modificar los datos de los alumnos
# d) Agregar alumnos
# e) Expulsar alumnos
# RECOMEDACIONN GENERAL:
# El programa es extenso, hacer por partes.
# Llevará mucho tiempo, la paciencia es importante.
# Internet es una gran ayuda.
# La prolijidad es fundamental
# Las funciones tendrán que recibir como parámetros los diccionarios que 
# representan a los alumnos.