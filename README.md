# <span style="color:salmon">tuna ⚓</span>
Current trends around the world, canned.

### Stack
Routes and API are built using FastAPI. 

The frontend is built using SvelteKit, with Tailwind CSS for styling. 

Map uses D3-geo for rendering. 

The LLM integration is done using the Gemini Flash API.

Uses session storage for compute efficiency.

### Todo
- ~~initialize db schema~~ (done but not in use)
  - ~~typesafe objects using pydantic~~
- ~~db operations~~ (done but not in use)
  - ~~get~~
  - ~~update~~
  - ~~create~~
  - ~~delete~~
- ~~populate db (done)~~
- ~~get trends API~~ (MVP done)
  - ~~organize into class~~
  - ~~prep for interval update~~
  - assign categorical weights (optional)
- ~~LLM integration~~ (done)
  - ~~Gemini Flash (test pass)~~
  - ~~get trends from db~~
  - ~~feed to llm~~
  - use scraper for misc data (optional)
- ~~routes setup~~ (done)
  - ~~parellelize requests~~
- ~~frontend design~~ (done)
  - ~~interactive map~~
  - ~~LLM result display~~
- ~~session storage~~ (done)
- ~~dockerize~~ (done)
  - ~~docker compose~~
  - ~~dockerfile for frontend~~
  - ~~dockerfile for backend~~
- redis / mongo for db (planned)
  - trends refresh interval
- misc frontend details
  - header and footer.. 
  - more navigation stuff

## Build
```
docker compose up --build --watch
```
_--watch_ flag to automatically rebuild the files as you are developing <br>

- frontend should serve in http://localhost:5173
- backend should serve in http://localhost:8080
