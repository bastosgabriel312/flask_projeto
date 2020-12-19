class Artigo():
	"""docstring for Artigos"""
	def __init__(self,id, titulo, conteudo, autor):
		self.__id = id
		self.__titulo = titulo
		self.__conteudo = conteudo
		self.__autor = autor


	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id

	def get_titulo(self):
		return self.__titulo

	def set_conteudo(self, conteudo):
		self.__conteudo = conteudo

	def get_autor(self):
		return self.__autor

	def set_autor(self, autor):
		self.__autor = autor

