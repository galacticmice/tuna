# <span style="color:salmon">tuna ⚓</span>
Current trends around the world, canned.

### Stack
- MariaDB --> might switch to NoSQL if we drop weighting
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
  - assign categorical weights (optional)
- trends refresh interval (planned)
- LLM integration (WIP)
  - Gemini Flash / Llama Maverick
  - get trends from db
  - feed to llm
  - use scraper for misc data (optional)
- routes setup (WIP)
- frontend design (planned)
  - interactive map
  - LLM result display

## Build
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