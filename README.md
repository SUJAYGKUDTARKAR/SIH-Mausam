# SIH Mausam – Personalized Weather Homepage

Backend module for the SIH26076 Mausam personalized homepage prototype.

## Features

- City name → latitude and longitude using Open-Meteo geocoding
- Current, hourly, and daily weather forecast
- Clean normalized JSON response
- Personas:
  - commuter
  - farmer
  - traveller
  - runner
- Error handling for invalid city names and personas

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the backend

```powershell
python app.py
```

The backend runs at:

```text
http://127.0.0.1:5000
```

## Test the API

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/homepage" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"city":"Davangere","persona":"commuter"}' |
  ConvertTo-Json -Depth 10
```

## Request JSON

```json
{
  "city": "Davangere",
  "persona": "commuter"
}
```

Allowed personas: `commuter`, `farmer`, `traveller`, `runner`.

## Main endpoint

```text
POST /api/homepage
```