import pymysql
from usuarios import Usuario
from artigos import Artigo

############ CONEXAO MYSQL HEROKU #########################
'''
username: b7b2178122d9f2
password:21659ddc
host:us-cdbr-east-02.cleardb.com
port:3306
DB = heroku_38b8825dfc725a7
'''
class ConexaoMysql():
        def __init__(self):
                self.host = 'localhost'
                self.db = 'DB_TESTE'
                self.user = "root"
                self.password = 'Gabriele!0'
                '''
                host = 'us-cdbr-east-02.cleardb.com'
                db = 'heroku_38b8825dfc725a7'
                user = 'b7b2178122d9f2'
                password = '21659ddc'
                '''

        ############ CRIAR USUÁRIO ########################
        def create_user(self,login,senha,nome,email,nivel):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"INSERT INTO TB_USUARIOS (LOGIN,SENHA,NOME,EMAIL, NIVEL_USUARIO) VALUES (%s,%s,%s,%s,%s);"
                tuple_login = (login,senha,nome,email,nivel)
                cursor.execute(query,tuple_login)
                conexao.commit()
                conexao.close()

        ############ LER USUÁRIO ########################
        def read_login(self,login):
	        conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
	        cursor = conexao.cursor()
	        query = f"SELECT * FROM TB_USUARIOS WHERE LOGIN = %s"
	        tuple_login = (login)
	        cursor.execute(query, tuple_login)
	        for row in cursor:
	        	usuario = row
	        	break
	        conexao.commit()
	        conexao.close()
	        return usuario

        ############ USUÁRIO TEMPORÁRIO ########################
        def temp_user(self,login):
                try:
                        mysql_return = self.read_login(login)
                        user_temp = Usuario(mysql_return[0],mysql_return[3],mysql_return[4],mysql_return[1],mysql_return[2],mysql_return[5])
                except:
                        user_temp = None
                return user_temp




        ############ UPDATES ########################
        def update_nome(self,id,novo_nome):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"UPDATE TB_USUARIOS SET NOME = %s WHERE ID = %s;"
                tuple_update = (novo_nome,id)
                cursor.execute(query,tuple_update)
                conexao.commit()
                conexao.close()
                return

        def update_usuario(self,id,novo_usuario):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"UPDATE TB_USUARIOS SET LOGIN = %s WHERE ID = %s;"
                tuple_update = (novo_usuario,id)
                cursor.execute(query,tuple_update)
                conexao.commit()
                conexao.close()
                return

        def update_email(self,id,novo_email):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"UPDATE TB_USUARIOS SET EMAIL = %s WHERE ID = %s;"
                tuple_update = (novo_email, id)
                cursor.execute(query,tuple_update)
                conexao.commit()
                conexao.close()
                return

        def update_senha(self,id,nova_senha):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"UPDATE TB_USUARIOS SET SENHA = %s WHERE ID = %s;"
                tuple_update = (nova_senha, id)
                cursor.execute(query,tuple_update)
                conexao.commit()
                conexao.close()
                return


        ############ DELETAR USUÁRIO ########################
        def delete_user(self, id):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"DELETE FROM TB_USUARIOS WHERE ID = %s;"
                tuple_delete = (id)
                cursor.execute(query,id)
                conexao.commit()
                conexao.close()

        ############ LER TODOS USUÁRIOS ########################
        def read_alllogin(self):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"SELECT * FROM TB_USUARIOS"
                cursor.execute(query)
                usuario = []
                for row in cursor:
                        usuario.append(row)
                conexao.commit()
                conexao.close()
                return usuario


        ############ LER TODOS ARTIGOS ########################
        def read_allartigos(self):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"SELECT * FROM TB_ARTIGO"
                cursor.execute(query)
                artigos = []
                for artigo in cursor:
                        artigos.append([artigo[0],artigo[1], artigo[2], artigo[3]])
                return artigos
                conexao.commit()
                conexao.close()
                
        ############ CREATE ARTIGO ########################

        def create_artigo(self, titulo, conteudo, autor):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"INSERT INTO TB_ARTIGO (TITULO, CONTEUDO, AUTOR) VALUES (%s,%s,%s)"
                tupla_artigo = (titulo, conteudo, autor)
                cursor.execute(query,tupla_artigo)
                conexao.commit()
                conexao.close()

        ############ DELETAR ARTIGO ########################
        def delete_artigo(self, id):
                conexao = pymysql.connect(host=self.host ,db=self.db, user=self.user, passwd=self.password)
                cursor = conexao.cursor()
                query = f"DELETE FROM TB_ARTIGO WHERE ID = %s;"
                tuple_delete = (id)
                cursor.execute(query,id)
                conexao.commit()
                conexao.close()

               
