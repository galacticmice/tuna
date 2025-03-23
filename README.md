# <span style="color:salmon">tuna ⚓</span>

The Universal News Anchor ⚓

## Stack
Dockerized:<br>
- PostgreSQL (BaaS: Supabase / Appwrite)
- Fastify (or Express ...tbd)
- Vite build: React - typescript
- Node.js


### docker tba 03/23
download docker desktop!

### backend setup eta 03/23

### frontend is not intialized yet, eta 03/25


### Relational DB Schemas
- Option 1:
  - Country (DATE*, category, trend)
- Option 2: // not good practice
  - DATE (country*, category, trend)
- Option 3:
  - YEAR (DAY*, )

## Functionality
Switch time zone per region? <br>
Curr date updates every hour? <br>


## Build
### for individual front/backend
docker build -t tuna-front .
docker run -p 5050:5050 -v "$(pwd):/app" -v /app/node_modules tuna-front

### as whole package (tbd -- backend not connected yet)
docker compose up --watch