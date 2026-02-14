# Timezone Finder API

A lightweight REST API to find timezone, current local time, and GMT offset from geographic coordinates (latitude & longitude). Built with **FastAPI** and **timezonefinder**.

## Endpoints

### `GET /`

Health check endpoint.

```json
{
  "message": "Timezone Finder API is running!"
}
```

### `GET /timezone?lat={latitude}&lon={longitude}`

Returns timezone info for the given coordinates.

**Parameters:**

| Parameter | Type  | Range        | Description |
|-----------|-------|--------------|-------------|
| `lat`     | float | -90 to 90    | Latitude    |
| `lon`     | float | -180 to 180  | Longitude   |

**Example:**

```
GET /timezone?lat=40.7128&lon=-74.0060
```

```json
{
  "timezone": "America/New_York",
  "current_time": "2026-02-14 10:30:00",
  "gmt_offset": -5.0
}
```

**Error:**

```
GET /timezone?lat=0&lon=500
```

```json
{
  "detail": [
    {
      "msg": "Input should be less than or equal to 180",
      "type": "less_than_equal"
    }
  ]
}
```

## Quick Start

### Local

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open http://127.0.0.1:8000/docs for interactive API docs.

### Docker

```bash
docker build -t timezone-finder-api .
docker run -d -p 8000:8000 timezone-finder-api
```

### Heroku / Railway

The project includes a `Procfile` for cloud deployment:

```bash
# Heroku
heroku create your-app-name
git push heroku main

# Railway
# Connect your GitHub repo — Railway auto-detects the Procfile.
```

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework
- [timezonefinder](https://github.com/jannikmi/timezonefinder) — Timezone lookup from coordinates
- [pytz](https://pypi.org/project/pytz/) — Timezone database
- [Uvicorn](https://www.uvicorn.org/) — ASGI server

## License

MIT
