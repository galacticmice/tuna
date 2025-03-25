# <span style="color:salmon">tuna ⚓</span>

The Universal News Anchor ⚓

### Stack
Dockerized:<br>
- PostgreSQL (BaaS: Supabase / Appwrite)
- Fastify - Typescript
- Vite build: React - Typescript
- Node.js


### Todo
- DB setup (important!)
- frontend design
- Backend setup


### Relational DB Schemas
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
### Download [Docker Desktop](https://www.docker.com/get-started/)
in tuna folder, run
```
docker compose up --watch
```
_--watch_ flag to automatically rebuild the files as you are developing <br>

- frontend should serve in http://localhost:3000
  - The default graphic is provided by vite build tool
- backend should serve in http://localhost:8080
  - They are not connected yet, I still haven't learned how...


## Functionality Clarification
Switch time zone per region? <br>
Curr date updates every hour? <br>