# <span style="color:salmon">tuna ⚓</span>

The Universal News Anchor ⚓

## Stack
Dockerized:<br>
- PostgreSQL (BaaS: Supabase / Appwrite)
- Fastify (or Express ...tbd)
- Vite build: React - typescript
- Node.js


# Todo
- DB setup
- frontend design
- Backend setup


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


# To Run
## Download Docker Desktop
in tuna folder, run
```
docker compose up --watch
```
--watch flag to automatically rebuild the files while you are developing <br>

- frontend should serve in http://localhost:3000
  - The default graphic is provided by vite build tool
- backend should serve in http://localhost:8080


# Functionality Clarification
Switch time zone per region? <br>
Curr date updates every hour? <br>