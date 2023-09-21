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

# Rota para listar grupos
@app.route('/api/grupos', methods=['GET'])
def listar_grupos():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM grupos')
    grupos = cursor.fetchall()
    cursor.close()
    return jsonify(grupos)

# Rota para criar um grupo
@app.route('/api/grupos', methods=['POST'])
def criar_grupo():
    data = request.get_json()
    nome = data['nome']
    cursor = connection.cursor()
    cursor.execute('INSERT INTO grupos (nome) VALUES (%s)', (nome,))
    connection.commit()
    cursor.close()
    return 'Grupo Salvo!'

# Rota para atualizar um grupo
@app.route('/api/grupos/<int:id>', methods=['PUT'])
def atualizar_grupo(id):
    data = request.get_json()
    nome = data['nome']
    cursor = connection.cursor()
    cursor.execute('UPDATE grupos SET nome = %s WHERE id = %s', (nome, id))
    connection.commit()
    cursor.close()
    return 'Grupo atualizado!'

# Rota para excluir um grupo
@app.route('/api/grupos/<int:id>', methods=['DELETE'])
def excluir_grupo(id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM grupos WHERE id = %s', (id,))
    connection.commit()
    cursor.close()
    return 'Grupo Excluído!'

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
financeiro_group = {}
tecnicos_group = {}
fusao_group = {}
comercial_group = {}


async def mencionar_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    members = " ".join([f"@{member}" for member in suporte_group.keys()])
    await update.message.reply_text(members)


async def mencionar_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    members = " ".join([f"@{member}" for member in financeiro_group.keys()])
    await update.message.reply_text(members)


async def mencionar_tecnicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    members = " ".join([f"@{member}" for member in tecnicos_group.keys()])
    await update.message.reply_text(members)


async def mencionar_fusao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    members = " ".join([f"@{member}" for member in fusao_group.keys()])
    await update.message.reply_text(members)


async def mencionar_comercial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    members = " ".join([f"@{member}" for member in comercial_group.keys()])
    await update.message.reply_text(members)


async def adicionar_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        suporte_group[username] = True
        print("Suporte Group:", suporte_group)  # Print the updated support group for debugging purposes
        
        # Agora, faça uma solicitação POST para criar o usuário no servidor
        url = 'http://localhost:3001/api/usuarios'  # Substitua pelo URL correto do seu servidor
        data = {'username': username}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            await update.message.reply_text(f"Adicionado {username} ao grupo de suporte e criado no servidor.")
        else:
            await update.message.reply_text("Ocorreu um erro ao criar o usuário no servidor.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo de suporte.")


async def adicionar_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        financeiro_group[username] = True
        print("Financeiro Group:", financeiro_group)  # Print the updated financeiro group for debugging purposes
        await update.message.reply_text(f"Adicionado {username} ao grupo financeiro.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo financeiro.")


async def adicionar_tecnicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        tecnicos_group[username] = True
        print("Tecnicos Group:", tecnicos_group)  # Print the updated tecnicos group for debugging purposes
        await update.message.reply_text(f"Adicionado {username} ao grupo de técnicos.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo de técnicos.")


async def adicionar_fusao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        fusao_group[username] = True
        print("Fusao Group:", fusao_group)  # Print the updated fusao group for debugging purposes
        await update.message.reply_text(f"Adicionado {username} ao grupo de fusão.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo de fusão.")


async def adicionar_comercial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        comercial_group[username] = True
        print("Comercial Group:", comercial_group)  # Print the updated comercial group for debugging purposes
        await update.message.reply_text(f"Adicionado {username} ao grupo comercial.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo comercial.")


async def remover_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.chat.username
    if username in suporte_group:
        del suporte_group[username]
        await update.message.reply_text(f"Removido {username} do grupo de suporte.")
    else:
        await update.message.reply_text("Você não está no grupo de suporte.")


async def remover_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.chat.username
    if username in financeiro_group:
        del financeiro_group[username]
        await update.message.reply_text(f"Removido {username} do grupo financeiro.")
    else:
        await update.message.reply_text("Você não está no grupo financeiro.")


async def remover_tecnicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.chat.username
    if username in tecnicos_group:
        del tecnicos_group[username]
        await update.message.reply_text(f"Removido {username} do grupo de técnicos.")
    else:
        await update.message.reply_text("Você não está no grupo de técnicos.")


async def remover_fusao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.chat.username
    if username in fusao_group:
        del fusao_group[username]
        await update.message.reply_text(f"Removido {username} do grupo de fusão.")
    else:
        await update.message.reply_text("Você não está no grupo de fusão.")


async def remover_comercial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.chat.username
    if username in comercial_group:
        del comercial_group[username]
        await update.message.reply_text(f"Removido {username} do grupo comercial.")
    else:
        await update.message.reply_text("Você não está no grupo comercial.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start para testar este bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6473614239:AAHtG7dot5Zr5njx48eIL1YrewkkjyRn3to").build()

    application.add_handler(CommandHandler("mencionar_suporte", mencionar_suporte))
    application.add_handler(CommandHandler("mencionar_financeiro", mencionar_financeiro))
    application.add_handler(CommandHandler("mencionar_tecnicos", mencionar_tecnicos))
    application.add_handler(CommandHandler("mencionar_fusao", mencionar_fusao))
    application.add_handler(CommandHandler("mencionar_comercial", mencionar_comercial))
    application.add_handler(CommandHandler("adicionar_suporte", adicionar_suporte))
    application.add_handler(CommandHandler("adicionar_financeiro", adicionar_financeiro))
    application.add_handler(CommandHandler("adicionar_tecnicos", adicionar_tecnicos))
    application.add_handler(CommandHandler("adicionar_fusao", adicionar_fusao))
    application.add_handler(CommandHandler("adicionar_comercial", adicionar_comercial))
    application.add_handler(CommandHandler("remover_suporte", remover_suporte))
    application.add_handler(CommandHandler("remover_financeiro", remover_financeiro))
    application.add_handler(CommandHandler("remover_tecnicos", remover_tecnicos))
    application.add_handler(CommandHandler("remover_fusao", remover_fusao))
    application.add_handler(CommandHandler("remover_comercial", remover_comercial))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
   def main(): pass
   app = Flask(__name__)
   app.run(host='0.0.0.0', port=3001)