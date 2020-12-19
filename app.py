from flask import Flask, render_template, make_response, request, session, Blueprint
from mysql import *
from time import sleep

################ FLASK PARAMETROS ################
app = Flask(__name__)
host="192.168.16.49"


################ INSTANCIA CLASSE DE CONEXAO MYSQL PARA COMANDOS (UPDATE, DELETE READ E CREATE) ################
executar = ConexaoMysql()
################ SENHA PARA CRIPTOGEAFIA DE SESSION ################
app.secret_key = "asd78767asd5!(a$"





################ DEFINIR SESSION E VALIDA LOGIN ################
log_in = Blueprint("log_in",__name__)
@app.route("/validacao", methods = ['POST', 'GET'])
def session_login():
        pad = "<a href='/'>Retornar para a pagina de login</a>"
        if request.method == 'POST':
                        resp = make_response(render_template('login_invalido.html'))
                        user = request.form['usuario']
                        password = request.form['senha']
                        usuario = executar.temp_user(user)
                        if usuario != None:
                                login = usuario.get_login()
                                if user == login:
                                        senha = usuario.get_senha()
                                        if password != "" and password == senha:
                                                id = usuario.get_id()
                                                login = usuario.get_login()
                                                nome = usuario.get_nome()
                                                email = usuario.get_email()
                                                nivel = usuario.get_nivel()
                                                resp = make_response(render_template('return.html'))
                                                session['id'] = id
                                                session['login'] = login
                                                session['senha'] = senha
                                                session['nome'] = nome
                                                session['email'] = email
                                                session['nivel'] = nivel
                                                
                        return resp
        return pad


################ PAGINA DE LOGOUT ################
@app.route('/logout', methods = ['POST','GET'])
def logout():
        session.clear()
        return render_template("return_login.html")


################ PAGINA DE LOGIN (FORMULÁRIO) ################
@app.route('/', methods = ['POST', 'GET'])
def index():
        session.clear()
        return render_template('login.html')


################ PAGINA HOME - ACESSIVEL APÓS LOGIN ################
@app.route('/home', methods = ['POST', 'GET'])
def home():
        if 'login' in session:
            artigos = executar.read_allartigos()
            if request.form.get('idartigo',None) != None:
                executar.delete_artigo(request.form['idartigo'])
            if request.method == 'POST':
                if request.form.get('titulo',None) != None and request.form.get('conteudo',None) :
                    executar.create_artigo(request.form['titulo'],request.form['conteudo'],request.form['autor'])
            return render_template('home.html',title = 'Home',icon = 'icon-home.svg', id = session["id"], usuario = session['login'], nome = session['nome'], email = session['email'], artigos = artigos)
        return "Você não está logado <a href='/'>Clique aqui para ir para pagina de login</a>"



################ PAGINA DE CADASTRO (FORMULÁRIO) - ACESSIVEL APÓS LOGIN ################
@app.route('/cadastro', methods = ['POST','GET'])
def cadastro():
            if request.method == 'POST':
                    user = request.form['user']
                    password = request.form['password']
                    email = request.form['email']
                    nome = request.form['nome']
                    nivel = request.form['nivel']
                    usuario = executar.temp_user(user)
                    if user != "" and password != "" and email != "" and nome != "" and nivel != "":
                            if usuario == None:
                                    executar.create_user(user,password,nome,email,nivel)
            return render_template('cadastro.html')



################ PAGINA DE USUARIOS - ACESSIVEL APÓS LOGIN ################
@app.route('/usuarios', methods = ['POST', 'GET'])
def usuarios():
        if 'login' in session:
                usuarios = executar.read_alllogin()
                    

                if request.method == 'POST':
                    if request.form.get('delete_usuario', None) =='True':
                        executar.delete_user(request.form['option_user'])
                    else:
                        if request.form.get('update_nome', None) =='True':
                            executar.update_nome(request.form['option_user'],request.form['nome_atual'])
                        if request.form.get('update_email', None) == 'True':
                            executar.update_email(request.form['option_user'],request.form['email_atual'])
                        if request.form.get('update_usuario', None) == 'True':
                            executar.update_usuario(request.form['option_user'],request.form['usuario_atual'])
                        if request.form.get('update_senha', None) == 'True':
                            executar.update_senha(request.form['option_user'],request.form['senha_atual'])


                return render_template('usuarios.html',title ='Usuários' ,icon = 'icon-lista.svg',id = session["id"], usuarios = usuarios, usuario = session['login'], nome = session['nome'], email = session['email'])
        return "Você não está logado <a href='/'>Clique aqui para ir para pagina de login</a>"


################ PAGINA DE CONFIGURACAO - ACESSIVEL APÓS LOGIN ################
@app.route('/configuracao', methods = ['POST', 'GET'])
def perfil():
        if 'login' in session:
            if request.method == 'POST':
                id = session['id']
                temp_user = executar.temp_user(session['login'])
                nome_atual = request.form['nome_atual']
                email_atual = request.form['email_atual']
                senha_atual = request.form['senha_atual']
                executar.update_nome(id,nome_atual)
                executar.update_email(id,email_atual)
                if request.form['check_senha'] == 'True':
                    if request.form['senha_antiga'] == temp_user.get_senha():
                        executar.update_senha(id,senha_atual)

            return render_template('editar_usuario.html',title = "Meu perfil",icon = 'icon-user.svg', id = session["id"], usuario = session['login'], nome = session['nome'], email = session['email'])
        return "Você não está logado <a href='/'>Clique aqui para ir para pagina de login</a>"

################ PAGINA DE QUEM SOMOS - ACESSIVEL APÓS LOGIN ################
@app.route('/quem_somos', methods = ['POST', 'GET'])
def quem_somos():
        if 'login' in session:
            return render_template('quem_somos.html',title = "Sobre nós", id = session["id"], usuario = session['login'], nome = session['nome'], email = session['email'])
        return "Você não está logado <a href='/'>Clique aqui para ir para pagina de login</a>"






if __name__ == '__main__':
    app.run(debug=True, port=5000, host="192.168.16.49")
    


