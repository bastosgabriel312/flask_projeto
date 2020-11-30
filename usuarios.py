class Usuario():
	def __init__(self,id, login, senha, nome, email, nivel):
		self.__id = id
		self.__login = login
		self.__senha = senha
		self.__nome = nome
		self.__email = email
		self.__nivel = str(nivel)

	#id SETs and GETs
	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id

	#login SETs and GETs
	def get_login(self):
		return self.__login

	def set_login(self, login):
		self.__login = login

	#senha SETs and GETs
	def get_senha(self):
		return self.__senha

	def set_senha(self, senha):
		self.__senha = senha

	#nome SETs and GETs
	def get_nome(self):
		return self.__nome

	def set_nome(self, nome):
		self.__nome = nome

	#email SETs and GETs
	def get_email(self):
		return self.__email

	def set_email(self, email):
		self.__email = email

	#nivel_usuario SETs and GETs
	def get_nivel(self):
		return self.__nivel

	def set_nivel(self, nivel):
		self.__nivel = nivel

	###### PRINT ALL (PARA TESTES) ###########
	def print_all(self):
		print("ID: ",self.__id)
		print("LOGIN: ",self.__login)
		print("SENHA: ",self.__senha)
		print("NOME:", self.__nome)
		print("E-MAIL: ",self.__email)
		print("NIVEL: ",self.__nivel)

