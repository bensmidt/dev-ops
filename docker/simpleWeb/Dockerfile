# Specify a base image
FROM node:14-alpine

# Specify working directory
WORKDIR /usr/app

# Install dependencies
COPY ./package.json ./
RUN npm install 
COPY ./ ./

# Default command
CMD ["npm", "start"]