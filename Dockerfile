# Use an official Node.js image as the base
FROM node:18.18.0 AS base

# Create and set permissions for the working directory
RUN mkdir -p /app/telegram/api/node_modules && chown -R node:node /app/telegram/api
RUN mkdir -p /app/telegram/bot && chown -R node:node /app/telegram/bot

# Set the working directory
WORKDIR /app/telegram

# Copy package.json and install dependencies for the API
COPY api/package*.json api/
RUN npm install express mysql

# Copy the API code
COPY api/. api/

# Copy requirements.txt and install dependencies for the bot
COPY bot/requirements.txt bot/
RUN pip install -r bot/requirements.txt

# Copy the bot code
COPY bot/. bot/

# Expose the API port
EXPOSE 3002

# Command to run both the API and bot
CMD ["bash", "-c", "node api/teletriade.js & python bot/teletriade.py"]