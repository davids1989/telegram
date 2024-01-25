import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
import logging
import httpx

# Configure httpcore logging to suppress INFO messages
httpx_logger = logging.getLogger('httpx')
httpx_logger.setLevel(logging.WARNING)  # Define o nível de log que você deseja (e.g., WARNING, ERROR)


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
   # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'suporte_group'
        suporte_users = [user['username'] for user in usuarios if user['grupo'] == 'suporte_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in suporte_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")


async def mencionar_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'financeiro_group'
        financeiro_users = [user['username'] for user in usuarios if user['grupo'] == 'financeiro_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in financeiro_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")


async def mencionar_tecnicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'tecnicos_group'
        tecnicos_users = [user['username'] for user in usuarios if user['grupo'] == 'tecnicos_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in tecnicos_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")


async def mencionar_fusao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'fusao_group'
        fusao_users = [user['username'] for user in usuarios if user['grupo'] == 'fusao_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in fusao_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")


async def mencionar_comercial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'comercial_group'
        comercial_users = [user['username'] for user in usuarios if user['grupo'] == 'comercial_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in comercial_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")


async def adicionar_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        suporte_group[username] = True
        print("Suporte Group:", suporte_group)  # Print the updated support group for debugging purposes

        # Faça a chamada de API para adicionar o usuário ao grupo de suporte
        api_url = "http://localhost:3002/api/usuarios/"
        data = { "username": username, "grupo": "suporte_group" }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                await update.message.reply_text(f"Adicionado {username} ao grupo de suporte.")
            else:
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo de suporte.")
        except Exception as e:
            print("Erro ao fazer a chamada de API:", str(e))
            await update.message.reply_text("Erro ao adicionar o usuário ao grupo de suporte.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo de suporte.")

async def adicionar_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        financeiro_group[username] = True
        print("Financeiro Group:", financeiro_group)  # Print the updated financeiro group for debugging purposes
        
        # Faça a chamada de API para adicionar o usuário ao grupo de financeiro
        api_url = "http://localhost:3002/api/usuarios/"
        data = { "username": username, "grupo": "financeiro_group" }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                await update.message.reply_text(f"Adicionado {username} ao grupo do financeiro.")
            else:
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo do financeiro.")
        except Exception as e:
            print("Erro ao fazer a chamada de API:", str(e))
            await update.message.reply_text("Erro ao adicionar o usuário ao grupo do financeiro.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo financeiro.")


async def adicionar_tecnicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        tecnicos_group[username] = True
        print("Tecnicos Group:", tecnicos_group)  # Print the updated tecnicos group for debugging purposes
        
        # Faça a chamada de API para adicionar o usuário ao grupo dos técnicos
        api_url = "http://localhost:3002/api/usuarios/"
        data = { "username": username, "grupo": "tecnicos_group" }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                await update.message.reply_text(f"Adicionado {username} ao grupo dos tecnicos.")
            else:
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo dos tecnicos.")
        except Exception as e:
            print("Erro ao fazer a chamada de API:", str(e))
            await update.message.reply_text("Erro ao adicionar o usuário ao grupo dos tecnicos.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo dos técnicos.")


async def adicionar_fusao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        fusao_group[username] = True
        print("Fusao Group:", fusao_group)  # Print the updated fusao group for debugging purposes
        
        # Faça a chamada de API para adicionar o usuário ao grupo dos técnicos
        api_url = "http://localhost:3002/api/usuarios/"
        data = { "username": username, "grupo": "fusao_group" }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                await update.message.reply_text(f"Adicionado {username} ao grupo de fusão.")
            else:
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo de fusão.")
        except Exception as e:
            print("Erro ao fazer a chamada de API:", str(e))
            await update.message.reply_text("Erro ao adicionar o usuário ao grupo de fusão.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo de fusão.")


async def adicionar_comercial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        mentioned_user = update.message.reply_to_message.from_user
        username = mentioned_user.username
        print("Username:", username)  # Print the username for debugging purposes
        comercial_group[username] = True
        print("Comercial Group:", comercial_group)  # Print the updated comercial group for debugging purposes
        
        # Faça a chamada de API para adicionar o usuário ao grupo comercial
        api_url = "http://localhost:3002/api/usuarios/"
        data = { "username": username, "grupo": "comercial_group" }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                await update.message.reply_text(f"Adicionado {username} ao grupo comercial.")
            else:
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo comercial.")
        except Exception as e:
            print("Erro ao fazer a chamada de API:", str(e))
            await update.message.reply_text("Erro ao adicionar o usuário ao grupo comercial.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo comercial.")


async def remover_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Verifica se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_username = update.message.reply_to_message.from_user.username

        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:3002/api/usuarios/')

            if response.status_code == 200:
                usuarios = response.json()

                for usuario in usuarios:
                    print("Username:", usuario['username'])
                    if usuario['username'] == mentioned_username and usuario['grupo'] == 'suporte_group':
                        user_id = usuario['id']

                        delete_response = await client.delete(f'http://localhost:3002/api/usuarios/{user_id}')

                        if delete_response.status_code == 204:
                            await update.message.reply_text(f"Removido {mentioned_username} do grupo de suporte.")
                        else:
                            await update.message.reply_text(f"Erro ao remover {mentioned_username} do grupo de suporte.")
                        break  # Parar a iteração após a exclusão

                else:
                    await update.message.reply_text(f"{mentioned_username} não está no grupo de suporte.")
            else:
                await update.message.reply_text("Erro ao acessar a API de usuários.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo de suporte.")




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
    main()
