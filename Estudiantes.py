listaEstudiantes=[]

class Estudiantes(object):
	def __init__(self, cedula, nombre, apellido, edad, nota1, nota2, nota3):
		self.cedula=cedula
		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
		self.nota1=nota1
		self.nota2=nota2
		self.nota3=nota3
		self.notaFinal=(nota1+nota2+nota3) / 3
		self.historial=[]
	def entregarDatos(self):
		print("No. Cedula: {} - {} {} - Nota Final: {}".format(self.cedula, self.nombre, self.apellido, self.notaFinal))
	def editarNotas(self, nota1, nota2, nota3):
		self.nota1=nota1
		self.nota2=nota2
		self.nota3=nota3
		self.notaFinal=(nota1+nota2+nota3) / 3
		print("Registro Exitoso!")
	def incluirEvento(self, nota1, nota2, nota3):
		return("Modificar: Nota_1: {} Nota_2: {} Nota_3: {}".format(nota1, nota2, nota3))
	def entregarHistorial(self):
		print("No. Cedula: {} - {} {}".format(self.cedula, self.nombre, self.apellido))



def registrarEstudiante():
	print("Registrar de Estudiantes\n")
	cedula=int(input("Ingrese El Numero De Cedula: "))
	nombre=input("Ingrese El Nombre: ")
	apellido=input("Ingrese El Apellido: ")
	edad=int(input("Ingrese La Edad: "))
	nota1=int(input("Ingrese La Nota 1: "))
	nota2=int(input("Ingrese La Nota 2: "))
	nota3=int(input("Ingrese La Nota 3: "))
	objAlumno=Estudiantes(cedula, nombre, apellido, edad, nota1, nota2, nota3)
	listaEstudiantes.append(objAlumno)

def listadoEstudiantes():
	print("Listado de Estudiantes\n")
	for objAlumno in listaEstudiantes:
		objAlumno.entregarDatos()

def buscarEstudiantes():
	print("Buscar Estudiante\n")
	cedula=int(input("Ingrese el numero de Cedula: "))
	for objAlumno in listaEstudiantes:
		if cedula==objAlumno.cedula:
			objAlumno.entregarDatos()

def modificarNotas():
	print("Modificar Notas\n")
	cedula=int(input("Ingrese el numero de Cedula: "))
	for objAlumno in listaEstudiantes:
		if cedula==objAlumno.cedula:
			nota1=float(input("Ingrese nota 1: "))
			nota2=float(input("Ingrese nota 2: "))
			nota3=float(input("Ingrese nota 3: "))
			objAlumno.editarNotas(nota1, nota2, nota3)
			objAlumno.entregarDatos()
			recepcionMensaje=objAlumno.incluirEvento(nota1, nota2, nota3)
			objAlumno.historial.append(recepcionMensaje)

def consultarHistorial():
	print("Consulta de Historial\n")
	cedula=int(input("Ingrese el numero de Cedula: "))
	for objAlumno in listaEstudiantes:
		if cedula==objAlumno.cedula:
			for recepcionMensaje in objAlumno.historial:
				print("Evento: {}".format(recepcionMensaje))

def salir():
	print("Salir inminente....!")
	exit()

def main():
	while True:
		print("\n")
		print("|***********************************|")
		print("|**|		Bienvenido	 |**|")
		print("|**|		   Menu	         |**|")
		print("|***********************************|")
		print("")
		print("Selecione una de las siguientes opciones:")
		print("1.- Registrar Estudiante")
		print("2.- Mostrar Estudiante")
		print("3.- Buscar Estudiante")
		print("4.- Modificar Notas")
		print("5.- Consultar Historial")
		print("6.- Salir\n")

		opcion=int(input("Opcion: "))

		if opcion==1:
			registrarEstudiante()
		elif opcion==2:
			listadoEstudiantes()
		elif opcion==3:
			buscarEstudiantes()
		elif opcion==4:
			modificarNotas()
		elif opcion==5:
			consultarHistorial()
		elif opcion==6:
			salir()

if __name__=='__main__':
	main();