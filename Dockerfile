# Usar uma imagem base oficial do Node.js
FROM node:18.18.0 AS node_base

# Criar e definir permissões no diretório de trabalho
RUN mkdir -p /app/telegram/api && chown -R node:node /app/telegram/api

# Definir o diretório de trabalho
WORKDIR /app/telegram/api

# Copiar arquivos de dependências e instalar
COPY ./api/package*.json ./
RUN npm install express mysql

# Copiar o código da API
COPY ./api .

# Expor a porta da API
EXPOSE 3002

# Comando para rodar a API
CMD ["node", "teletriade.js"]

# Usar uma imagem base oficial do Python
FROM python:3.9-slim AS python_base

WORKDIR /app/telegram/bot

# Copiar arquivos de dependências do bot
COPY ./bot/requirements.txt ./

# Instalar dependências do bot
RUN pip install -r requirements.txt

# Copiar o código do bot
COPY ./bot .

# Comando para rodar o bot
CMD ["python", "teletriade.py"]

# Multi-stage build para juntar ambas as partes
FROM node:18.18.0

# Copiar a construção da API
COPY --from=node_base /app/telegram/api /app/telegram/api

# Copiar a construção do bot
COPY --from=python_base /app/telegram/bot /app/telegram/bot
