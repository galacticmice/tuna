# <span style="color:salmon">tuna ⚓</span>
Current trends around the world, canned.

### Stack
- Appwrite
- Python FastAPI
- React TypeScript
- Docker


### Todo
- ~~initialize db schema (done)~~
  - ~~typesafe objects using pydantic~~
- ~~db operations (done)~~
  - ~~get~~
  - ~~update~~
  - ~~create~~
  - ~~delete~~
- ~~populate db (done)~~
- get trends API (partial)
  - ~~organize into class~~
  - ~~prep for interval update~~
  - assign weight to categories (optional)
- trends refresh interval (planned)
- llm integration (planned)
  - get trends from db
  - feed to llm
  - use scraper for misc data (optional)
- routes setup (WIP)
- frontend design (planned)

## Build
### Download [Docker Desktop](https://www.docker.com/get-started/)
in tuna folder, run
```
docker compose up --watch
```
_--watch_ flag to automatically rebuild the files as you are developing <br>

- frontend should serve in http://localhost:5173
  - placeholder page
- backend should serve in http://localhost:8080
  - doesn't have any routes yet --> WIP


## Functionality Clarification
Switch time zone per region? <br>
Curr date updates every hour? <br>