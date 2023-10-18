<h1>Installation</h1>

<h3>Clone repository</h3>

```bash
$ git clone "https://github.com/simonari/bewise.ai-contest.git" "/dir/to/save"
```

<h3>Set up environment variables</h3>
``.env file``
```dotenv
DOCKER_NETWORK="bewise.ai"

POSTGRES_CONTAINER_NAME="bewise.ai.db"

POSTGRES_USER="postgres"
POSTGRES_PASSWORD="postgres"
POSTGRES_DB="bewise.ai"

POSTGRES_DOCKER_VOLUME="./db-pg"
```

More detailed explanation of values available in file.

<h3>Compose</h3>

```bash
$ docker compose up
```

<h3>Set up python dependencies</h3>

```bash
$ pip install -r requirements.txt
```

<h3>Start web-app</h3>

```bash
$ uvicorn app.main:app --reload
```

<h3>Example of POST request</h3>

Request:
```
POST /1 HTTP/1.1
```

Response:
```json
{"question": "I've done good work. haven't I?"}
```