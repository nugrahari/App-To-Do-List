# Base image: using Node.js 18
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install all dependencies including devDependencies using npm ci
RUN npm install --include=dev

# Copy the rest of the Vite project files
COPY . .

# Expose Vite.js default port (5173)
EXPOSE 5173

# Run Vite in developer mode
# CMD ["npm", "run", "dev"]
