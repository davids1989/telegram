# Usar uma imagem base oficial do Node.js
FROM node:18.18.0 AS node_base

# Criar e definir permissões no diretório de trabalho
RUN mkdir -p /app/telegram && chown -R node:node /app/telegram

# Definir o diretório de trabalho
WORKDIR /app/telegram

# Copiar arquivos de dependências e instalar
RUN npm install express mysql

COPY package*.json ./api


# Copiar o código da API
COPY --chown=node:node . .

# Expor a porta da API
EXPOSE 3002


# Usar uma imagem base oficial do Python
FROM python:3.9-slim AS python_base

WORKDIR /app/telegram/bot

# Copiar arquivos de dependências do bot
COPY requirements.txt .

# Instalar dependências do bot
RUN pip install -r requirements.txt

# Copiar o código do bot
COPY . .

# Final stage
FROM node:18.18.0

WORKDIR /app/telegram

# Copiar a construção da API
COPY --from=node_base /app/telegram/api /app/telegram/api

# Copiar a construção do bot
COPY --from=python_base /app/telegram/bot /app/telegram/bot

# Comando para rodar a API e o bot
CMD ["node", "teletriade.js", "&", "python", "teletriade.py"]