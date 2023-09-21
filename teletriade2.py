import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask, request, jsonify
import pymysql
import requests

app = Flask(__name__)

# Configuração do MySQL
connection = pymysql.connect(
    host='38.156.3.8',
    port=3306,
    user='david',
    password='Tri@#102030',
    database='telegram'
)

# Rota para listar usuários
@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    return jsonify(usuarios)

# Rota para criar um usuário
@app.route('/api/usuarios', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    username = data['username']
    cursor = connection.cursor()
    cursor.execute('INSERT INTO usuarios (username) VALUES (%s)', (username,))
    connection.commit()
    cursor.close()
    return 'Usuario Salvo!'

# Rota para atualizar um usuário
@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.get_json()
    username = data['username']
    cursor = connection.cursor()
    cursor.execute('UPDATE usuarios SET username = %s WHERE id = %s', (username, id))
    connection.commit()
    cursor.close()
    return 'Usuario atualizado!'

# Rota para excluir um usuário
@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = %s', (id,))
    connection.commit()
    cursor.close()
    return 'Usuario Excluído!'

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

suporte_group = {}


async def adicionar_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        suporte_group[username] = True
        print("Suporte Group:", suporte_group)  # Print the updated support group for debugging purposes
        
        # Agora, faça uma solicitação POST para criar o usuário no servidor
        url = 'http://localhost:3002/api/usuarios'  # Substitua pelo URL correto do seu servidor
        data = {'username': username}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            await update.message.reply_text(f"Adicionado {username} ao grupo de suporte e criado no servidor.")
        else:
            await update.message.reply_text("Ocorreu um erro ao criar o usuário no servidor.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo de suporte.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start para testar este bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6473614239:AAHtG7dot5Zr5njx48eIL1YrewkkjyRn3to").build()

    application.add_handler(CommandHandler("adicionar_suporte", adicionar_suporte))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
   def main(): pass
   app = Flask(__name__)
   app.run(host='localhost', port=3002)