FROM node:18.18.0 AS node_base
FROM python:3.9-slim AS python_base

# Etapa para construir e rodar a API
FROM node_base AS api_builder

RUN mkdir -p /app/telegram/api/node_modules && chown -R node:node /app/telegram/api

# Definir o diretório de trabalho
WORKDIR /app/telegram/api

# Instalar as dependências
RUN npm install express mysql

COPY package*.json ./

COPY --chown=node:node . .

# Expor a porta 3002
EXPOSE 3002

# Definir o comando para executar o aplicativo
CMD ["node", "teletriade.js"]

# Etapa para construir e rodar o bot
FROM python_base AS bot_builder

WORKDIR /app/telegram/bot

# Copiar arquivos do bot
COPY ./app/telegram/requirements.txt ./

# Instalar dependências do bot
RUN pip install -r requirements.txt

# Copiar código do bot
COPY ./app/telegram/bot .

# Comando para rodar o bot
CMD ["python", "teletriade.py"]

# Multi-stage build para juntar ambas as partes
FROM node_base

# Copiar a construção da API
COPY --from=api_builder /app/telegram/api /app/telegram/api

# Copiar a construção do bot
COPY --from=bot_builder /app/telegram/bot /app/telegram/bot

# Expor a porta da API
EXPOSE 3002

# Comando para rodar ambos: API e bot
CMD ["sh", "-c", "npm start --prefix /app/telegram/api & python /app/telegram/bot/teletriade3.py"]