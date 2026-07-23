# curryculum

CV builder: keep the content in one place and generate the document from it.

## Stack

FastAPI · MongoDB · SvelteKit · Skeleton · Nginx · Docker Compose

## Run

```bash
cp env.sample .env   # MongoDB credentials
make up              # -> http://localhost
make down
```

## Configuration

| File | What goes in it |
|---|---|
| `.env` | MongoDB root credentials |
| `backend/.env` | `MONGO_URI`, `MONGO_DB`, backend name and version |
| `ui/.env` | `VITE_API_URL` — backend base URL |
