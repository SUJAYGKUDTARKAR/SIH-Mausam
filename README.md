
# Mausam — Personalized Weather Homepage

**SIH 2026 | Problem Statement: SIH26076**

Mausam is a personalized weather application designed to provide relevant weather information based on the user's activity and needs. It supports Farmers, Runners, Commuters, and Travellers with weather details and tailored recommendations.

## Features

- **Personalized weather:** Recommendations based on the selected persona.
- **Weather information:** Temperature, humidity, rainfall, wind speed, visibility, and other available weather metrics.
- **Farmer mode:** Weather insights to support irrigation and farming decisions.
- **Runner mode:** Weather information to help plan outdoor runs.
- **Commuter mode:** Weather information for daily travel.
- **Traveller mode:** Destination weather and travel-related recommendations.
- **REST API:** Flask backend endpoints for health checks and personalized weather data.
- **Frontend:** React, TypeScript, and Vite-based user interface.
- **Database:** SQLite support for backend data storage.

## Technology Stack

### Frontend
- React
- TypeScript
- Vite
- Tailwind CSS

### Backend
- Python
- Flask
- Flask-CORS
- Requests
- SQLite

### Weather Data
- Open-Meteo API integration, as configured in the backend.

## Project Structure

```text
SIH-Mausam/
├── app.py
├── database.py
├── weather_service.py
├── test_api.py
├── check_database.py
├── start_mausam.bat
├── requirements.txt
├── BACKEND_SETUP.md
├── README.md
└── mausam-persona-builder-main/
    └── mausam-persona-builder-main/
        ├── package.json
        ├── src/
        └── ...
```

*The frontend folder structure may vary depending on the current repository version.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SUJAYGKUDTARKAR/SIH-Mausam.git
cd SIH-Mausam
```

### 2. Set up the Python backend

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### 3. Run the backend

```bash
python app.py
```

Keep the backend terminal running. The Flask server should display its local address in the terminal.

### 4. Test the backend

In another terminal, activate the virtual environment and run:

```bash
python test_api.py
```

The test script checks the supported persona endpoints or requests configured in the project.

## API Endpoints

### Health Check

**Method:** `GET`

```text
/health
```

Use this endpoint to check whether the backend is running.

### Personalized Weather

**Method:** `POST`

```text
/api/personalize
```

The endpoint accepts a JSON request containing the selected persona and any other required fields defined by the current backend implementation.

Example request format:

```json
{
  "city": "Bengaluru",
  "persona": "commuter"
}
```

Supported personas:

- `farmer`
- `runner`
- `commuter`
- `traveller`

**Note:** Confirm the exact endpoint path, request fields, and response format in `app.py` and `weather_service.py`, as these can change between versions.

## Running the Frontend

1. Open the frontend directory containing `package.json`.
2. Install the frontend dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

4. Open the local URL printed in the terminal.

Ensure the Flask backend is running and that the frontend API configuration points to the correct backend URL.

## Team Contributions

The project is developed collaboratively for Smart India Hackathon 2026.

- **Backend development:** Flask APIs, weather-service integration, persona-based recommendations, and SQLite support.
- **Frontend development:** User interface, dashboard, persona selection, and API integration.
- **UI/UX:** Interface design and user experience.
- **Research and documentation:** Requirements, research, and project documentation.
- **Testing and integration:** API testing, frontend-backend integration, and validation.

## Future Improvements

- Improve personalized weather recommendations.
- Add stronger validation and error handling.
- Improve destination weather support for travellers.
- Expand automated testing.
- Enhance frontend-backend integration and deployment.
- Improve database management and data persistence.

## Contributors

Developed by the SIH 2026 Mausam team.

## License

Add the appropriate license if the project is intended for public distribution.
