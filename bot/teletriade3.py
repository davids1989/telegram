import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
import logging
import httpx

logging.basicConfig(level=logging.INFO)

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
almoxarifado_group = {}
administrativo_group = {}
ti_group = {}

async def check_group_role(user_id: int, group_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Verifica se o usuário tem permissão para executar a ação."""
    try:
        # Obter informações do usuário
        user_info = await context.bot.get_chat_member(chat_id=group_id, user_id=user_id)

        # Verificar se o usuário tem permissão para executar a ação
        if user_info.status in ['administrator', 'creator']:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao acessar a API de usuários: {e}")
        return False


async def mencionar_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    
   # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://api:3002/api/usuarios/')

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
        response = await client.get('http://api:3002/api/usuarios/')

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
        response = await client.get('http://api:3002/api/usuarios/')

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
        response = await client.get('http://api:3002/api/usuarios/')

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
        response = await client.get('http://api:3002/api/usuarios/')

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

async def mencionar_almoxarifado(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    
   # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://api:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'suporte_group'
        almoxarifado_users = [user['username'] for user in usuarios if user['grupo'] == 'almoxarifado_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in almoxarifado_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")

async def mencionar_administrativo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    
   # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://api:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'suporte_group'
        administrativo_users = [user['username'] for user in usuarios if user['grupo'] == 'administrativo_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in administrativo_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")

async def mencionar_ti(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    
   # Fazer uma solicitação HTTP para a API
    async with httpx.AsyncClient() as client:
        response = await client.get('http://api:3002/api/usuarios/')

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        usuarios = response.json()
        
        # Filtrar os usuários que têm 'grupo' igual a 'suporte_group'
        ti_users = [user['username'] for user in usuarios if user['grupo'] == 'ti_group']
        
        # Formatar a lista de usuários mencionando-os
        mentioned_users = " ".join([f"@{user}" for user in ti_users])
        
        # Enviar a lista de usuários mencionados como resposta
        await update.message.reply_text(mentioned_users)
    else:
        # Tratar erros, se necessário
        await update.message.reply_text("Ocorreu um erro ao acessar a API de usuários.")


async def adicionar_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            suporte_group[user_id] = username  # Store the username in the support group dictionary
            print("Suporte Group:", suporte_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo de suporte
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "suporte_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo de suporte.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo de suporte.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo de suporte.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo de suporte.")

async def adicionar_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            financeiro_group[user_id] = username  # Store the username in the support group dictionary
            print("financeiro Group:", financeiro_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo do financeiro
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "financeiro_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo do financeiro.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo do financeiro.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo do financeiro.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo do financeiro.")

async def adicionar_tecnicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            tecnicos_group[user_id] = username  # Store the username in the support group dictionary
            print("tecnicos Group:", tecnicos_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo do financeiro
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "tecnicos_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo dos técnicos.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo dos técnicos.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo dos técnicos.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo dos técnicos.")

async def adicionar_fusao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            fusao_group[user_id] = username  # Store the username in the support group dictionary
            print("fusao Group:", fusao_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo do financeiro
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "fusao_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo da fusão.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo da fusão.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo da fusão.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo da fusão.")

async def adicionar_comercial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            comercial_group[user_id] = username  # Store the username in the support group dictionary
            print("comercial Group:", comercial_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo do financeiro
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "comercial_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo do comercial.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo do comercial.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo do comercial.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo do comercial.")

async def adicionar_almoxarifado(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            almoxarifado_group[user_id] = username  # Store the username in the support group dictionary
            print("almoxarifado Group:", almoxarifado_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo do financeiro
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "almoxarifado_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo do almoxarifado.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo do almoxarifado.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo do almoxarifado.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo do almoxarifado.")

async def adicionar_administrativo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            administrativo_group[user_id] = username  # Store the username in the support group dictionary
            print("administrativo Group:", administrativo_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo do financeiro
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "administrativo_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo do administrativo.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo do administrativo.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo do administrativo.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo do administrativo.")

async def adicionar_ti(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    if update.message.reply_to_message:
        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            client = httpx.AsyncClient()  # Create the client without using async with
            mentioned_user = update.message.reply_to_message.from_user
            user_id = mentioned_user.id  # Get the user ID
            username = mentioned_user.username
            print("Username:", username)  # Print the username for debugging purposes
            ti_group[user_id] = username  # Store the username in the support group dictionary
            print("ti Group:", ti_group)  # Print the updated support group for debugging purposes

            # Faça a chamada de API para adicionar o usuário ao grupo do financeiro
            api_url = "http://api:3002/api/usuarios/"
            data = { "username": username, "grupo": "ti_group", "telegram_id": user_id }

            try:
                response = await client.post(api_url, json=data)

                if response.status_code == 200:
                    await update.message.reply_text(f"Adicionado {username} ao grupo do Ti.")
                else:
                    await update.message.reply_text("Erro ao adicionar o usuário ao grupo do Ti.")
            except Exception as e:
                print("Erro ao fazer a chamada de API:", str(e))
                await update.message.reply_text("Erro ao adicionar o usuário ao grupo do Ti.")
            finally:
                await client.aclose()  # Close the client manually
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa mencionar um usuário para adicionar ao grupo do Ti.")

async def remover_suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo do suporte."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/suporte_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo do suporte.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo do suporte.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo do suporte.")


async def remover_financeiro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo do financeiro."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/financeiro_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo do financeiro.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo do financeiro.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo do financeiro.")


async def remover_tecnicos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo dos técnicos."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/tecnicos_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo dos técnicos.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo dos técnicos.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo dos técnicos.")

                        

async def remover_fusao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo dos técnicos."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/fusao_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo da fusão.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo da fusão.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo da fusão.")


async def remover_comercial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo de suporte."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/comercial_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo do comercial.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo do comercial.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo do comercial.")

async def remover_almoxarifado(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo de suporte."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/almoxarifado_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo do almoxarifado.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo do almoxarifado.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo do almoxarifado.")

async def remover_administrativo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo de suporte."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/administrativo_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo do administrativo.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo do administrativo.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo do administrativo.")

async def remover_ti(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove um usuário do grupo de suporte."""

    # Obter o ID do grupo a partir da mensagem
    group_id = update.message.chat_id

    # Verificar se a mensagem contém uma menção a um usuário
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        mentioned_user = update.message.reply_to_message.from_user
        user_id = mentioned_user.id

        # Verificar se o usuário que está executando a ação tem permissão para executar a ação
        if await check_group_role(update.message.from_user.id, group_id, context):
            async with httpx.AsyncClient() as client:
                delete_response = await client.delete(f'http://api:3002/api/usuarios/{user_id}/ti_group')

                if delete_response.status_code == 200:
                    await update.message.reply_text(f"Removido {mentioned_user.username} do grupo do Ti.")
                else:
                    await update.message.reply_text(f"Erro ao remover {mentioned_user.username} do grupo do Ti.")
        else:
            await update.message.reply_text("Você não tem permissão para executar esta ação.")
    else:
        await update.message.reply_text("Você precisa responder a uma mensagem mencionando o usuário para remover do grupo do Ti.")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start para testar este bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7906537668:AAG-cwINseV48YaXIfgklJUUyF6lqTPHR3s").build()

    application.add_handler(CommandHandler("mencionar_suporte", mencionar_suporte))
    application.add_handler(CommandHandler("mencionar_financeiro", mencionar_financeiro))
    application.add_handler(CommandHandler("mencionar_tecnicos", mencionar_tecnicos))
    application.add_handler(CommandHandler("mencionar_fusao", mencionar_fusao))
    application.add_handler(CommandHandler("mencionar_comercial", mencionar_comercial))
    application.add_handler(CommandHandler("mencionar_almoxarifado", mencionar_almoxarifado))
    application.add_handler(CommandHandler("mencionar_administrativo", mencionar_administrativo))
    application.add_handler(CommandHandler("mencionar_ti", mencionar_ti))
    application.add_handler(CommandHandler("adicionar_suporte", adicionar_suporte))
    application.add_handler(CommandHandler("adicionar_financeiro", adicionar_financeiro))
    application.add_handler(CommandHandler("adicionar_tecnicos", adicionar_tecnicos))
    application.add_handler(CommandHandler("adicionar_fusao", adicionar_fusao))
    application.add_handler(CommandHandler("adicionar_comercial", adicionar_comercial))
    application.add_handler(CommandHandler("adicionar_almoxarifado", adicionar_almoxarifado))
    application.add_handler(CommandHandler("adicionar_administrativo", adicionar_administrativo))
    application.add_handler(CommandHandler("adicionar_ti", adicionar_ti))
    application.add_handler(CommandHandler("remover_suporte", remover_suporte))
    application.add_handler(CommandHandler("remover_financeiro", remover_financeiro))
    application.add_handler(CommandHandler("remover_tecnicos", remover_tecnicos))
    application.add_handler(CommandHandler("remover_fusao", remover_fusao))
    application.add_handler(CommandHandler("remover_comercial", remover_comercial))
    application.add_handler(CommandHandler("remover_almoxarifado", remover_almoxarifado))
    application.add_handler(CommandHandler("remover_administrativo", remover_administrativo))
    application.add_handler(CommandHandler("remover_ti", remover_ti))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
