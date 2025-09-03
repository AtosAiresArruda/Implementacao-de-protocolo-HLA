
try:
    with open('federation.txt', 'r') as arq:
        texto    = arq.read()
        palavras = texto.split()
except FileNotFoundError:
    print(f"Erro ao abrir Arquivo.")
except Exception as e:
    print(f"Erro = {e}")

print(palavras)
'''

[[[cog	
	import cog
	try:
		with open("federation.txt", "r") as arq:
			texto = arq.read()
			palavras = texto.split()
	except FileNotFoundError:
		print(f"Erro ao abrir arquivo")
	except Exception as e:
		print(f"Erro = {e}")

	print(palavras)
	def buildHeader():
		#Monta Cabecalho da federacao
		cog.outl("<?xml version='1.0' encoding='UTF-8'?>")
		cog.outl("<federation>")
		#Fim da montagem

	def buildFederation(federationName, typeFederetion):

		#Monta nome da federacao
		cog.out("	<federationName>")
		cog.out(federationName)
		cog.outl("</federationName>")
		#Fim da montagem

		#Monta tipo da federacao
		cog.out("	<federateType>")
		cog.out(typeFederetion)
		cog.outl("</federateType>")	
		#Fim da montagem

	def startBuildObject(nameObjectClass, typeSharing, typeDimensions, typeIsAbstract):
		#Monta Objeto
		cog.outl("	<objects>")

	def startBuildClass(nameObjectClass, typeSharing, typeDimensions, typeIsAbstract):
		#Monta Classe
		cog.outl("		<objectClass")

		#Monta Name
		cog.out("			name='")
		cog.out(nameObjectClass)
		cog.outl("'")
		#Fim da montagem nome
		
		#Monta sharing
		cog.out("			sharing='")
		cog.out(typeSharing)
		cog.outl("'")
		#Fim da montagem sharing

		#Monta dimensions
		cog.out("			dimensions='")
		cog.out(typeDimensions)
		cog.outl("'")
		#Fim da montagem dimensions

		#Monta dimensions
		cog.out("			isAbstract='")
		cog.out(typeIsAbstract)
		cog.outl("'")
		#Fim da montagem isAbstract

		#Inserindo Atributo
		cog.outl("		>")

		#Fim da montagem Classe

	def enterAttribute(nameAttribute, typeDataType, typeOwnership, typeUpdateRate, typeTransportation):

		#Monta Atributos
		cog.outl("			<attribute")
		cog.out("				name='")
		cog.out(nameAttribute)
		cog.outl("'")

		cog.out("				dataType='")
		cog.out(typeDataType)
		cog.outl("'")

		cog.out("				ownership='")
		cog.out(typeOwnership)
		cog.outl("'")

		cog.out("				updateRate='")
		cog.out(typeUpdateRate)
		cog.outl("'")

		cog.out("				transportation='")
		cog.out(typeTransportation)
		cog.outl("'")

		#Sinaliza fim da montagem dos atributos
		cog.outl("			/>")

	def finishBuildClass():
		cog.outl("		</objectClass>")
		cog.outl("	</objects>")
		#Fim da montagem Objeto

	def startBuildInterations():
		cog.outl("	<interactions>")

	def BuildInteractions(nameInteraction, typeSharing, typeDimensions, typeTransportation):
		cog.outl("		<interactionClass")

		#Monta Name
		cog.out("			name='")
		cog.out(nameInteraction)
		cog.outl("'")
		#Fim da montagem nome
		
		#Monta sharing
		cog.out("			sharing='")
		cog.out(typeSharing)
		cog.outl("'")
		#Fim da montagem sharing

		#Monta dimensions
		cog.out("			dimensions='")
		cog.out(typeDimensions)
		cog.outl("'")
		#Fim da montagem dimensions

		#Monta transportations
		cog.out("			transportation='")
		cog.out(typeTransportation)
		cog.outl("'")
		#Fim da montagem transportation

		#Inserindo parametros
		cog.outl("		>")

		#Fim da montagem da interação

	def enterParameter(nameParameter, typeDataType):

		cog.outl("			<parameter")

		#Monta Name
		cog.out("			name='")
		cog.out(nameParameter)
		cog.outl("'")
		#Fim da montagem nome

		#Monta dataType
		cog.out("			dataType='")
		cog.out(typeDataType)
		cog.outl("'")
		#Fim da montagem dataType

		cog.outl("			/>")

	def finishBuildInteractions():
		cog.outl("		</interactionClass>")
		#Fim da insersão de interações

	







	#buildHeader()
	#buildFederation(federationName, typeFederetion)
	#startBuildObject(nameObjectClass, typeSharing, typeDimensions, typeIsAbstract)	
	#startBuildClass(nameObjectClass, typeSharing, typeDimensions, typeIsAbstract)

	
	#buildAttribute(nameAttribute, typeDataType, typeOwnership, typeUpdateRate, typeTransportation) #Insira quantos quiser
	#finishBuildClass()

	#startBuildInterations()
	#BuildInteractions(nameInteraction, typeSharing, typeDimensions, typeTransportation)
	
	#enterParameter(nameParameter, typeDataType) #Insira quantas quiser
	#finishBuildInteractions()

	buildHeader()
	for palavras in palavras:
		
    
	

]]]
[[[end]]]
'''