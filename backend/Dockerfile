FROM node:23-alpine3.21

WORKDIR /app
COPY package*.json ./

RUN npm install

COPY . .

ENV PORT=3000
EXPOSE 3000

CMD npm run dev