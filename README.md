# <span style="color:salmon">tuna ⚓</span>

The Universal News Anchor ⚓

## Stack
Dockerized:<br>
- PostgreSQL (BaaS: Supabase / Appwrite)
- Fastify (or Express ...tbd)
- Vite build: React - typescript
- Node.js


# Todo
- DB setup eta 03/23
- Backend setup
- frontend design


# Relational DB Schemas
- Option 1:
  - Tables by country: DATE as primary key
  - Country (DATE*, category, trend)
- Option 2: // not good practice
  - Tables by DATE (a new table each day), country as primary key
  - DATE (country*, category, trend)
- Option 3:
  - ~~Tables by YEAR: many columns~~
  - YEAR (DAY*, <lots of columns>)


## Build
download docker desktop!

### **RUN THIS FOR NOW** ONLY FRONTEND WORKING
docker build -t tuna-front .
docker run -p 5050:5050 -v "$(pwd):/app" -v /app/node_modules tuna-front

### as whole package (tbd -- backend not connected yet)
docker compose up --watch


# Functionality Clarification
Switch time zone per region? <br>
Curr date updates every hour? <br>