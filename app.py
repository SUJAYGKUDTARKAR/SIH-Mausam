from flask import Flask, jsonify, request

from weather_service import ALLOWED_PERSONAS, WeatherServiceError, get_personalized_homepage

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"success": True, "message": "Mausam backend is running"}), 200


@app.post("/api/homepage")
def personalized_homepage():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(
            {
                "success": False,
                "error": "Request body must be valid JSON.",
            }
        ), 400

    city = data.get("city")
    persona = data.get("persona")

    if not isinstance(city, str) or not city.strip():
        return jsonify(
            {
                "success": False,
                "error": "Field 'city' must be a non-empty string.",
            }
        ), 400

    if not isinstance(persona, str) or persona.strip().lower() not in ALLOWED_PERSONAS:
        return jsonify(
            {
                "success": False,
                "error": "Field 'persona' must be commuter, farmer, or fitness.",
            }
        ), 400

    try:
        result = get_personalized_homepage(city, persona)
        return jsonify(result), 200

    except WeatherServiceError as error:
        return jsonify(
            {
                "success": False,
                "error": str(error),
            }
        ), 502

    except Exception:
        # Keep implementation details out of the API response.
        return jsonify(
            {
                "success": False,
                "error": "Unexpected server error.",
            }
        ), 500


if __name__ == "__main__":
    app.run(debug=True)