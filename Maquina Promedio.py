# -*- coding: utf-8 -*-

print "Hola, ¿Qué quieres hacer?"

cursos = {'com': 18, 'eng': 19, 'mate': 20, 'chem': 18, 'phy': 18, 'glo': 18, 
'eso': 18, 'filo': 18, 'rel': 17, 'ctv': 20, 'efi': 17, 'deu': 17}


#Preguntar qué hacer
def comienzo():
	opc = raw_input("¿Quieres cambiar o ver algun promedio? ").lower()
	if opc == "cambiar" or opc == "c":
		cambio()
	elif opc == "promedio" or opc =="p" or opc == "ver" or opc =="v":
		ver_que()
	else:
		print "Escribe 'ver' o 'cambiar' por favor"
		comienzo()

#cambia una nota
def cambio():
	curso = raw_input("Qué curso quieres cambiar? (3-4 letras): ").lower()
	if cursos.has_key(curso):
		def input_nota():
			nota = raw_input("Cuál es la nueva nota? ").lower()
			if nota.isdigit():
				nota = int(nota)
				cursos[curso] = nota
				denuevo()
			else:
				print "Por favor escribe un número"
				input_nota()
		input_nota()
	else:
		print "Ese curso no existe"
		cambio()

# ver que? promedio o curso
def ver_que():
  ver = raw_input("Quieres ver un curso o tu promedio en general? ").lower()
  if ver == 'curso' or ver == 'c':
    curso()
  elif ver == 'promedio' or ver == 'p':
    promedio()
  else:
    print "Por favor escribe 'curso' o 'promedio'"
    ver_que()

#ver promedio
def promedio():
	notas = list(cursos.values())
	while 0 in notas: notas.remove(0)
	promedio = float(sum(notas)) / max(len(notas), 1)
	promedio = round(promedio, 2)
	print "Tu promedio es: ", promedio
	denuevo()

#repetir
def denuevo():
	denuevo = raw_input("Quieres hacer algo más? ").lower()
	if denuevo == "si"  or denuevo == "s":
		comienzo()
	else:
		print "Chau!"

#ver un curso
def curso():
	c = raw_input("Qué curso quieres ver? ").lower()
	if c in cursos:
	  print "Tu promedio en " + str(c.upper()) + " es: " + str(cursos[c])
	  denuevo()
	else: 
	  print "Ese curso no existe, intentalo de nuevo"
	  curso()
	  
comienzo()