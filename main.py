# site com os scripts: https://cdnjs.com
# pegar o socket.io e colocar o script no html, pegar o jquery e colocar no html
# instalar os websockets pelo comando abaixo
# pip install python-socketio flask-socketio simple-websocket



#estrutura base para rodar código javascript no html
# <script type="text/javascript">
#    $(document).ready(function(){
#        
#    })
#</script>

#criamos o ambiente virtual venv, CTRL + SHIFT + P pesquisa por create enviroment

# passo 1 importar o Flask
# pass2 2 abrir o código com:  app = Flask (__name__)

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

#tunel para troca/visualização de mensagens pelos usuários do site
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagens
@socketio.on("message") #o @ tem o nome de decorator no python
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

#Criar a  nossa 1a página = 1a rota

@app.route("/") #o @ tem o nome de decorator no python
def homepage():
    return render_template("index.html")

# rodar nosso aplicativo com o código: app.run()

#app.run(debug=True) #trocou para o socketio

socketio.run(app, host="localhost") #alterar isso para apontar o servidor


#websocket
